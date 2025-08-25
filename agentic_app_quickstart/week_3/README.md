# 🐳 Week 3 Assignment: Containerization & Model Context Protocol (MCP)

## 📋 Mission Overview

Welcome to your third agentic systems challenge! It's time to transform your monitored agent from a local development tool into a production-ready, containerized service with secure external tool capabilities through the Model Context Protocol (MCP).

### 🎪 The Challenge

Your task is to containerize your agent and extend its capabilities using MCP:
- 🐳 **Docker Containerization** - Package your agent for consistent, secure deployment
- 🔗 **Model Context Protocol (MCP)** - Connect to external tools and data sources
- 🛡️ **Security Best Practices** - Implement container security and MCP safety measures
- 🌐 **HTTP API Exposure** - Make your agent accessible via web endpoints

**Real-world scenario**: Imagine you're deploying your agent to a corporate environment where it needs to access various internal systems (databases, APIs, file systems) while maintaining strict security boundaries - just like how Slack bots access multiple services or how GitHub Actions runners execute in isolated containers!

---

## 🏗️ Why Containerization & MCP Matter

### The Deployment Problem 📦
Without containers, deploying agents is a nightmare:
- ❓ "It works on my machine" syndrome
- 🔧 Complex dependency management
- 🚫 Inconsistent environments across dev/staging/prod
- 🐛 Security vulnerabilities from host system access

### The Tool Integration Challenge 🔌
Agents need to interact with external systems:
- 📊 Databases and data warehouses
- 📁 File systems and cloud storage
- 🌐 REST APIs and microservices
- 🔍 Search engines and knowledge bases

For enterprises who envision multiple agents consuming and reusing multiple different internal tools, MCP provides a good foundation to improve standardisation and discoverability.

---

## 🧰 Required Features (Core Assignment)

### 1. **Docker Containerization** 🐳
Transform your Week 2 agent into a secure container:
- Create a `Dockerfile` following security best practices
- Use **distroless** or minimal base images (Alpine Linux)
- Run as **non-root user** with minimal privileges

### 2. **MCP Server Integration (stdio)** 🔗
Leverage your first MCP server using stdio transport:
- Create or download an **MCP server** that has at least 2 tools
- Package both your agentic app and your MCP server in the same container
- Use **stdio transport** for local communication within the container

### 3. **Container Security** 🛡️
Apply security best practices for container deployment:
- **Minimal attack surface** - Achieved through using minimal Docker images (distroless/Alpine) with only essential dependencies
- **Non-root user execution** - Configure container to run as unprivileged user to prevent privilege escalation attacks

### 4. **HTTP API Endpoints** 🌐
Expose your agent via RESTful API:
- `/chat` endpoint for conversations
- `/health` endpoint for monitoring
- Proper error handling and response formatting

### **Recap: All-in-One Container Setup** 📦
Create a single, self-contained containerized application:
- Agent application with REST API endpoints
- Sample CSV files baked into the container for testing
- MCP Server with stdio transport running in the same container (can be any MCP server: you can create a simple one which tells your agent the current time - or one which helps your agent navigate the Pandas documentation)
- All dependencies and configurations included in one deployable unit

---

## 🌟 Bonus Challenges (Extra Credit)

### 🥉 Bronze Level: Function Tool Migration to MCP Server
Extract and migrate your existing agent functionality into a proper MCP architecture:

**🔄 Tool Migration Strategy**
- **Extract existing function tools**: Move all CSV analysis functions from your agent code into a dedicated MCP server (still running locally via stdio)
- **Implement MCP protocol**: Convert your Week 1 function tools (`calculate_column_average`, `count_rows_with_value`, etc.) into proper MCP tools with standardized input/output schemas
- **Decouple agent logic**: Your agent container now communicates with tools via MCP protocol rather than direct function calls, creating a separation of concerns between reasoning (agent) and execution (MCP tools)

**🚨 Robust Error Handling**
```python
# Your MCP tools should handle errors gracefully:
@mcp_tool("calculate_column_average")
async def calc_avg(filepath: str, column_name: str) -> str:
    try:
        # Validate file exists and column is present
        if not validate_csv_column(filepath, column_name):
            return "Error: Column not found in dataset"
        
        # Execute with proper error handling
        result = await compute_average(filepath, column_name)
        return f"Average of {column_name}: {result}"
        
    except FileNotFoundError:
        return "Error: CSV file not found"
    except ValueError as e:
        logger.error(f"Data processing error: {e}")
        return "Error: Unable to calculate average - check data types"
```

### 🥈 Silver Level: Multi-Container Architecture with Streamable HTTP
Implement production-ready MCP with network security using multiple containers:

**🌐 Multi-Container Setup with Docker Compose**
- Agent container with REST API
- Separate MCP server container accessible via network
- Proper service dependencies and inter-container networking

**🌐 Streamable HTTP Transport**
- Migrate from stdio to **Streamable HTTP** for network-based MCP

**🔐 Optional: Mutual TLS (mTLS) Authentication**
Following the security patterns from [this example repo](https://github.com/weet-ai/agentic-app-openai-agents-sdk-mcp-example):
```bash
# Generate certificates for secure MCP communication
docker build -t cert-generator ./certs-generator
docker run --rm -v $(pwd)/certs:/certs cert-generator

# Deploy with mTLS-enabled NGINX proxy
docker-compose up --build
```

**🛡️ Zero Trust Network Architecture**
- All MCP traffic encrypted and mutually authenticated
- Certificate-based client/server validation  
- Audit logging for all MCP interactions

### 🥇 Gold Level: Agentic ETL & Advanced Container Orchestration
Build enterprise-grade data processing capabilities:

**🔄 Intelligent ETL Pipeline**
Your agent becomes a data engineer that can:
```python
# Example of agentic ETL capabilities
User: "Process all CSV files in /data, clean the data, and create a summary report"

Agent: 
1. 📁 Discovers files using MCP file tools
2. 🔍 Analyzes data structure and quality
3. 🧹 Applies intelligent cleaning rules
4. 📊 Generates statistical summaries
5. 📈 Creates visualizations
```

**Multi-File Intelligence:**
- **Schema detection**: Automatically understand data structures
- **Data validation**: Detect and handle inconsistencies
- **Smart joins**: Automatically correlate related datasets
- **Advanced MCP toolchain**: Build sophisticated MCP servers that can handle complex data workflows beyond simple analysis

---

## 🚀 Getting Started

### Step 1: Study the Security Reference
Review the [sample repo architecture](https://github.com/weet-ai/agentic-app-openai-agents-sdk-mcp-example):
- Container security best practices
- MCP protocol implementation patterns
- mTLS certificate generation and management
- Docker Compose orchestration patterns

### Step 2: Containerize Your Week 2 Agent
**Migration Checklist:**
- ✅ Create secure Dockerfile with minimal base image
- ✅ Configure non-root user and proper permissions
- ✅ Set up environment variable management
- ✅ Test container locally with your monitoring setup

### Step 3: Build Your First MCP Server (stdio, local)
Start with stdio transport within your container:
1. Create a simple MCP server with 2 basic tools ✅
2. Connect your containerized agent to the MCP server via stdio ✅
3. Test tool discovery and execution within the container ✅
4. Implement proper error handling ✅
5. **Then** advance to multi-container setup with HTTP transport and mTLS (Silver)! 🚀

### Step 4: Implement Advanced Features (Bonus)
**For Bronze Level (Function Tool Migration):**
1. Extract your existing CSV analysis functions
2. Implement proper MCP tool schemas and protocols
3. Test the separation between agent reasoning and tool execution
4. Validate error handling and edge cases

**For Silver Level (Multi-Container + mTLS):**
1. Split your application into multiple containers
2. Generate certificates using the provided tooling
3. Migrate MCP connections to HTTP transport
4. Implement mutual authentication

**For Gold Level (Agentic ETL):**
1. Design intelligent data processing workflows
2. Build multi-file analysis capabilities

---

## 📊 Sample MCP Tools to Implement

### Essential Tools (Required)
```python
# File operations
@mcp_tool("read_file")
async def read_file(filepath: str) -> str:
    """Safely read a file with proper validation"""
    
@mcp_tool("list_directory") 
async def list_dir(path: str) -> List[str]:
    """List directory contents with permissions check"""

# Data analysis
@mcp_tool("analyze_csv")
async def analyze_csv(filepath: str) -> dict:
    """Analyze CSV structure and provide summary statistics"""

@mcp_tool("query_data")
async def query_data(filepath: str, query: str) -> str:
    """Execute natural language queries on data files"""
```

### Migrated Tools (Bronze+)
```python
# Your existing Week 1 functions converted to MCP tools
@mcp_tool("calculate_column_average")
async def calculate_column_average(filepath: str, column_name: str) -> str:
    """Calculate average value for a numeric column"""

@mcp_tool("count_rows_with_value")
async def count_rows_with_value(filepath: str, column_name: str, value: str) -> str:
    """Count rows containing specific value in column"""

@mcp_tool("get_column_names")
async def get_column_names(filepath: str) -> str:
    """List all column names in the CSV file"""
```

### Advanced Tools (Silver+)
```python
# Database operations
@mcp_tool("execute_sql")
async def execute_sql(connection_string: str, query: str) -> str:
    """Execute SQL queries with safety checks"""

# Computation tools
@mcp_tool("calculate_statistics")
async def calc_stats(data: List[float]) -> dict:
    """Compute statistical measures with error handling"""
```

---

## 📝 Submission Requirements

### Documentation Requirements
1. **README.md** in your solution folder explaining:
   - Container architecture and security measures
   - MCP server design and tool implementations
   - Deployment instructions and prerequisites
   - Security considerations and threat mitigation

2. **Security Assessment**: Document your container security posture

3. **API Documentation**: OpenAPI/Swagger specs for your HTTP endpoints

4. **Demo**: Deploy your containerized agent and share screenshots/video on Slack

---

## 🎯 Assessment Criteria

| Criteria | Weight | What We're Looking For |
|----------|--------|----------------------|
| **Container Security** | 30% | Proper security practices, minimal attack surface, non-root execution |
| **MCP Implementation** | 25% | Well-designed tools, proper protocol handling, error management |  
| **Architecture Quality** | 25% | Clean separation of concerns, scalable design, maintainable code |
| **Documentation & Deploy** | 20% | Clear instructions, security documentation, working deployment |

**Bonus points are added on top of the base score!**

---

## 🔒 Security Checklist

### Container Security
- [ ] **Minimal base image** (distroless/Alpine)
- [ ] **Non-root user** with minimal privileges
- [ ] **No secrets in image layers** - use environment variables
- [ ] **Health checks** implemented
- [ ] **Multi-stage build** for smaller attack surface

### MCP Security
- [ ] **Input validation** for all tool parameters
- [ ] **Path traversal protection** for file operations
- [ ] **SQL injection prevention** for database tools
- [ ] **Certificate validation** (Silver/Gold levels)

### Network Security
- [ ] **Least privilege networking** - minimal port exposure
- [ ] **TLS encryption** for all external communication (Silver+)

---

## 💡 Learning Objectives

By completing this assignment, you will:
- ✅ Master containerization best practices for AI applications
- ✅ Understand MCP protocol and secure tool integration patterns
- ✅ Implement production-grade security measures
- ✅ Experience container orchestration and deployment strategies
- ✅ Learn to balance functionality with security constraints
- ✅ Develop skills in enterprise-grade agent architecture

---

## 🛡️ Security Deep Dive

### Why These Security Measures Matter

**Real Attack Scenarios:**
- **Container Breakout**: Malicious code escaping container to host system
- **MCP Tool Poisoning**: Malicious MCP servers injecting harmful instructions
- **Data Exfiltration**: Agents accessing unauthorized data sources
- **Privilege Escalation**: Agents gaining higher system permissions than intended

**Our Mitigation Strategy:**
1. **Defense in Depth**: Multiple security layers (container + network + application)
2. **Zero Trust**: Never trust, always verify (especially with mTLS)
3. **Principle of Least Privilege**: Minimal permissions and access
4. **Audit Everything**: Comprehensive logging and monitoring

---

## 🤝 Getting Help

**Stuck? Here's your support system:**

1. **Security Reference Repo** - [Study the mTLS implementation patterns](https://github.com/weet-ai/agentic-app-openai-agents-sdk-mcp-example)
2. **Office hours & 1x1 Sessions**
3. **#help channel** - Container and MCP specific questions
4. **Docker Documentation** - Security best practices
5. **[MCP Specification](https://modelcontextprotocol.io/docs/getting-started/intro)** - Protocol details and examples

**Pro Tips:**
- Start with basic Docker containerization before adding MCP
- Test stdio MCP locally within your container before attempting multi-container setup
- Use the provided certificate generation tools for mTLS (Silver level)
- Always test security measures - try to break your own container!

---

## 📅 Important Dates

- **Assignment Release**: August 25, 2025
- **Submission Deadline**: September 1, 2025, 11:59 PM  

---

## ⚠️ Important Security Note

This assignment involves implementing security-critical features. While we provide guidance and examples, always:
- **Review your security implementation** with experienced developers
- **Test thoroughly** in isolated environments
- **Never deploy to production** without proper security audits
- **Keep certificates and keys secure** - never commit them to version control

Remember: Security is not a feature you add at the end - it must be designed in from the beginning! 🔐
