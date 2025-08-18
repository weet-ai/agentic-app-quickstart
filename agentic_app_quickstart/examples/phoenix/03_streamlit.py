"""
Streamlit Data Analyzer Application

This application provides a web interface for analyzing CSV files using an AI agent.
Users can upload CSV files and ask questions about unique values in specific columns.
The agent uses Polars for data processing and SQL queries for analysis.

Dependencies:
    - agents: AI agent framework for function calling and chat
    - polars: Fast DataFrame library for data processing
    - streamlit: Web framework for the user interface
    - asyncio: For asynchronous execution of agent operations
"""

from agents import Agent, Runner, function_tool
from agentic_app_quickstart.examples.helpers import get_model, get_tracing_provider
from textwrap import dedent
import polars as pl
import streamlit as st
import asyncio
import tempfile
import os


# Initialize tracing provider for monitoring agent interactions
tracing_provider = get_tracing_provider()


### AGENTIC FUNCTIONALITY
# This section defines the AI agent and its tools for data analysis

@function_tool
def get_headers(file_path: str) -> list[str]:
    """
    Get the column headers from a CSV file.
    
    This function reads the CSV file and returns the column names,
    which helps the agent understand what columns are available for analysis.
    
    Args:
        file_path (str): Absolute path to the CSV file
    
    Returns:
        list[str]: List of column names in the CSV file
        
    Raises:
        Exception: If file reading fails
        
    Example:
        >>> get_headers("/path/to/data.csv")
        ['id', 'name', 'department', 'salary']
    """
    try:
        # Read just the schema to get column names efficiently
        df = pl.read_csv(file_path, n_rows=0)
        return df.columns
    except Exception as e:
        print(f"Error occurred while reading headers from file {file_path}: {e}")
        raise e


@function_tool
def count_unique(file_path: str, target_column: str, extension: str = "csv") -> int:
    """
    Count the number of unique values in a specified column of a CSV file.
    
    This function uses Polars to read the CSV file and SQL to count unique values
    in the specified column. It handles file reading, SQL context creation, and
    query execution with error handling.
    
    Args:
        file_path (str): Absolute path to the CSV file to analyze
        target_column (str): Name of the column to count unique values for
        extension (str, optional): File extension, defaults to "csv"
    
    Returns:
        int: Number of unique values in the specified column
        
    Raises:
        Exception: If file reading or SQL execution fails
        
    Example:
        >>> count_unique("/path/to/data.csv", "customer_id")
        1250
    """
    try:
        # Read CSV file into Polars DataFrame
        df = pl.read_csv(file_path)
        
        # Create SQL context for querying
        sql_context = pl.SQLContext()
        
        # Generate a simple table name for SQL context
        # Use a generic name since the actual file path doesn't matter for the table name
        table_name = "data_table"
        
        # Register DataFrame as a table in SQL context
        sql_context.register(table_name, df)
        
        # Execute SQL query to count unique values in target column
        result = sql_context.execute(
            f"SELECT COUNT(DISTINCT {target_column}) FROM {table_name}"
        ).collect()
        
        # Extract the actual count value from the result
        # The result is a DataFrame with one row and one column
        num_unique = result[0, 0]
        
    except Exception as e:
        print(f"Error occurred while processing file {file_path}: {e}")
        raise e

    return num_unique


# Define instructions for the AI agent's behavior and capabilities
instructions = dedent("""
    You are a data analyst agent specialized in CSV file analysis.
    
    Your primary task is to help users count unique values for columns in CSV files.
    You will receive a file path to a CSV file and a question from the user about
    unique value counts in specific columns.

    Follow this step-by-step process:
        1. Analyze the user's question to identify the target column for analysis
        2. Use the `get_headers` function to retrieve available column headers from the CSV file
        3. Execute the appropriate function to calculate unique values in the specified column
        4. Provide a clear, informative response to the user

    Always use the provided tools to gather information and perform calculations.
    Be helpful and provide context about your findings when possible.
""")    

# Create the data analyzer agent with specified instructions, model, and tools
data_analyzer_agent = Agent(
    name="DataAnalyzerAgent",
    instructions=instructions,
    model=get_model(),  # Get the configured language model
    tools=[get_headers, count_unique]  # Available tools for the agent to use
)

### STREAMLIT INTERFACE
# This section contains the web application interface and user interaction logic

async def main():
    """
    Main application function that handles the Streamlit interface.
    
    This async function manages:
    - File upload functionality in the sidebar
    - Chat history management using session state
    - User input processing and agent interaction
    - Display of chat messages and responses
    
    The function runs continuously to handle user interactions and maintain
    the chat interface state across sessions.
    """
    
    # === FILE UPLOAD SECTION ===
    # Create sidebar file uploader that accepts any file type
    uploaded_file = st.sidebar.file_uploader("Upload a file", type=None)
    
    if uploaded_file is not None:
        # Display success message with filename
        st.sidebar.success(f"Uploaded: {uploaded_file.name}")

        # Save uploaded file to temporary location for processing
        # This allows the agent to access the file via file path
        # Preserve the original filename by using a temporary directory
        import os
        
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        
        # Create the full path with the original filename
        tmp_file_path = os.path.join(temp_dir, uploaded_file.name)
        
        # Write the file content to the temporary file with original name
        with open(tmp_file_path, 'wb') as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            
        # Store file path in session state for persistence across interactions
        st.session_state.tmp_file_path = tmp_file_path

    # === CHAT HISTORY MANAGEMENT ===
    # Initialize chat history in session state if it doesn't exist
    # This maintains conversation history across user interactions
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # === MAIN INTERFACE ===
    # Set the main title for the application
    st.title("Agentic Unique Values Analyzer")

    # Display all previous chat messages from session state
    # This creates a persistent chat interface
    for message in st.session_state.chat_history:
        st.chat_message(message["role"]).write(message["content"])

    # === USER INPUT PROCESSING ===
    # Create chat input field for user questions
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Check if a file has been uploaded
        if 'tmp_file_path' not in st.session_state:
            # If no file uploaded, inform the user
            error_message = "Please upload a CSV file first before asking questions about the data."
            st.session_state.chat_history.append({
                "role": "assistant", 
                "content": error_message
            })
            st.rerun()
            return
        
        # Create formatted prompt for the AI agent
        # Include both file path and user question for context
        prompt_template = dedent("""
            File path: {file_path}
            User question: {user_question}
        """).format(
            file_path=st.session_state.tmp_file_path, 
            user_question=user_input
        )

        # Execute the agent with the formatted prompt
        # This runs asynchronously to handle the AI processing
        result = await Runner.run(
            starting_agent=data_analyzer_agent, 
            input=prompt_template
        )
        
        # Add agent response to chat history
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": result.final_output
        })
        
        # Rerun the app to display the new messages
        # This refreshes the interface to show the latest conversation
        st.rerun()

# === APPLICATION ENTRY POINT ===
if __name__ == "__main__":
    """
    Welcome to the Data Analyst Agent App!
    """
    asyncio.run(main())