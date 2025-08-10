# 🎯 Week 1 Assignment: CSV Data Analysis Agent

## 📋 Mission Overview

Welcome to your first hands-on agentic system challenge! You'll be building an AI-powered CSV data analyst that can answer natural language questions about datasets.

### 🎪 The Challenge

Your task is to create an intelligent system that can:
- 📊 Load and analyze CSV files 
- 🗣️ Understand natural language questions from users
- 🔍 Extract insights and answer questions about the data
- 💬 Communicate findings in a clear, human-friendly way

**Real-world scenario**: Imagine you're building a data analysis assistant for a small business owner who wants to understand their data but doesn't know SQL or Python!

---

## 🏗️ Architecture Choices

You have **two paths** to choose from:

### Path A: Single Agent Approach 🤖
- One intelligent agent that handles everything
- Simpler to implement and debug
- Perfect for getting started quickly

### Path B: Multi-Agent System 🤖🤖🤖
- Specialized agents for different tasks
- More complex but more powerful
- **Bonus points available!** 🌟

---

## 🧰 Required Features (Core Assignment)

### 1. **CSV File Loading** 📁
Create a function that can load CSV files and make them accessible to your agent(s).

### 2. **Function Calling Implementation** ⚙️
Implement **at least 3 function tools** that your agent can use. Here are some starter ideas to get your creativity flowing:

**Basic Statistics Functions:**
- `calculate_column_average(column_name)` - Get the mean value of a numeric column
- `count_rows_with_value(column_name, value)` - Count how many rows contain a specific value
- `get_column_names()` - List all available columns in the dataset

**Think beyond the basics! 🚀**
- What about finding the maximum/minimum values?
- Calculating percentages or ratios?
- Finding correlations between columns?
- Detecting outliers or unusual patterns?

### 3. **Natural Language Interface** 🗣️
Your system should handle questions like:
- "What's the average price in the dataset?"
- "How many customers are from California?"
- "What are the column names in this file?"
- "Show me the highest revenue month"

### 4. **Error Handling** 🛡️
Make your system robust:
- Handle missing columns gracefully
- Deal with non-numeric data appropriately  
- Provide helpful error messages to users

---

## 🌟 Bonus Challenges (Extra Credit)

### 🥉 Bronze Level: Multi-Agent Architecture
Instead of one agent doing everything, create specialized agents:
- **Data Loader Agent**: Handles file operations and data preparation
- **Analytics Agent**: Performs calculations and statistical analysis
- **Communication Agent**: Formats responses in user-friendly language

**Teaching Moment**: Multi-agent systems mirror real-world teams where specialists collaborate!

### 🥈 Silver Level: Short-Term Memory
Implement conversation memory so your system can:
- Remember previous questions and answers
- Allow follow-up questions like "What about the median?" after asking about averages
- Build context over multiple interactions

**Example conversation:**
```
User: "What's the average sales amount?"
Agent: "The average sales amount is $1,247.50"
User: "What about the median for the same column?"
Agent: "The median sales amount is $1,100.25" ← Remembers we're talking about sales!
```

### 🥇 Gold Level: Advanced Analytics
Choose one or more advanced features:

**📈 Data Visualization**
- Generate simple plots or charts
- Create summary visualizations
- Export charts as images

**🧠 Smart Data Insights**
- Automatically detect interesting patterns
- Suggest relevant questions users might want to ask
- Provide data quality assessments

**🔄 Multiple File Handling**
- Compare data across multiple CSV files
- Join/merge datasets intelligently
- Handle different file formats (JSON, Excel)

**🎯 Query Optimization**
- Cache frequently requested calculations
- Optimize performance for large datasets
- Implement smart data sampling for huge files

---

## 🚀 Getting Started

### Step 1: Explore the Examples
Before you start coding, study these example files:
- `examples/code/01_hello_world.py` - Basic agent setup
- `examples/code/02_function_calling.py` - How to add tools to agents  
- `examples/code/03_simple_memory.py` - Implementing conversation memory
- `examples/code/05_handoffs.py` - Multi-agent coordination

### Step 2: Plan Your Architecture
**Reflection Questions** (Udacity-style):
- Will you use a single agent or multiple agents? Why?
- What functions does your agent need to analyze CSV data?
- How will you handle edge cases (empty files, missing columns)?
- What makes a good user experience for data questions?

### Step 3: Start Small, Think Big
Begin with the simplest possible version:
1. Load a CSV file ✅
2. Create one basic function (like column average) ✅
3. Make your agent use that function ✅
4. Test with simple questions ✅
5. **Then** expand with more features! 🚀

---

## 📊 Sample Data

We've provided some sample CSV files to test with:

**`sample_sales.csv`** - E-commerce sales data
- Columns: date, product, price, quantity, customer_state
- Perfect for testing averages, counts, and filtering

**`employee_data.csv`** - HR dataset  
- Columns: name, department, salary, hire_date, performance_score
- Great for grouping and statistical analysis

**`weather_data.csv`** - Weather measurements
- Columns: date, temperature, humidity, precipitation, city
- Ideal for time-series and geographical analysis

---

## 📝 Submission Requirements

### Code Structure
```
week_1/
├── README.md                    # This file
├── solution/
    ├── main.py                  # Your main application
    ├── agents.py                # Agent definitions
    ├── tools.py                 # Function tool implementations  
    └── data/
        ├── sample_sales.csv
        ├── employee_data.csv
        └── weather_data.csv

```

### Documentation Nice-to-haves
1. **README.md** in your solution folder explaining:
   - Your architecture choice and reasoning
   - How to run your system
   - Example questions users can ask
   - Challenges you overcame

2. **Code Comments**: Follow the style from the examples with clear explanations

3. **Demo**: Post a short video or some screenshots in #week1 channel on Slack

---

## 🎯 Assessment Criteria

| Criteria | Weight | What We're Looking For |
|----------|--------|----------------------|
| **Functionality** | 40% | Does your system work as described? Can it answer basic questions about CSV data? |
| **Code Quality** | 25% | Clean, well-commented code following examples' style |  
| **User Experience** | 20% | How intuitive and helpful is your system for non-technical users? |
| **Creativity** | 15% | What unique features or approaches did you implement? |

**Bonus points are added on top of the base score!**

---

## 💡 Learning Objectives

By completing this assignment, you will:
- ✅ Understand how to create practical AI agents for real-world tasks
- ✅ Master function calling to extend agent capabilities  
- ✅ Experience the trade-offs between single vs multi-agent architectures
- ✅ Learn to handle user input gracefully and provide good error messages
- ✅ Practice translating business requirements into technical solutions

---

## 🤝 Getting Help

**Stuck? Here's your support system:**

1. **Start with the examples** - They contain 90% of what you need to know!
2. **Office hours** - Every Tuesday, 2-4 PM
3. **#help channel** - Help your classmates and get help back
4. **Documentation** - Check the openai-agents package docs

**Remember**: The goal isn't to build the perfect system on the first try. It's to learn by doing, make mistakes, and iterate! 🔄


---

## 📅 Important Dates

- **Assignment Release**: August 10, 2025
- **Submission Deadline**: August 15, 2025, 11:59 PM
- **Peer Review**: August 22, 2025 (optional but encouraged!)

---
