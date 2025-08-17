# 🔍 Week 2 Assignment: Agent Observability & Monitoring

## 📋 Mission Overview

Welcome to your second agentic systems challenge! Now that you've built your first intelligent agent, it's time to peek under the hood and understand what's really happening when your agent thinks, acts, and responds.

### 🎪 The Challenge

Your task is to implement comprehensive monitoring and observability for your agentic system using industry-standard tools:
- 📊 **OpenTelemetry** for distributed tracing 
- 🌟 **Phoenix Arize** for visualization and analysis
- 🤖 **LLM-as-a-Judge** for automated evaluation (bonus!)

**Real-world scenario**: Imagine you're deploying your agent to production and need to monitor its performance, debug issues, and ensure quality - just like how Netflix monitors their recommendation algorithms or how Uber tracks their routing systems!

---

## 🏗️ Why Observability Matters

### The Black Box Problem 🕳️
Without proper monitoring, your agent is a black box:
- ❓ Why did it choose that tool?
- ⏱️ How long did each step take?
- 💸 How much did that conversation cost?
- 🐛 Where exactly did it go wrong?

### Production-Ready Agents 🚀
Real agentic systems need:
- **Performance monitoring** - Track latency and throughput
- **Cost tracking** - Monitor API usage and expenses
- **Quality assurance** - Detect hallucinations and poor responses
- **Debugging capabilities** - Trace complex multi-step workflows

---

## 🧰 Required Features (Core Assignment)

### 1. **Phoenix Arize Setup** 🌟
- Create a free Phoenix Arize account
- Set up a new project for your agent
- Generate and configure your API key
- Establish secure connection from your local environment

### 2. **OpenTelemetry Integration** 📡
Implement distributed tracing to capture:
- **LLM calls** - Every interaction with your language model
- **Tool executions** - When and how your agent uses functions
- **Agent handoffs** - Communication between multiple agents (if applicable)
- **User interactions** - Input/output flows

### 3. **Auto-Instrumentation** ⚙️
Add automatic instrumentation to monitor:
```python
# Example of what you'll be tracking:
- Function call latencies
- Token usage and costs  
- Error rates and types
- Agent decision points
- Tool success/failure rates
```

### 4. **Trace Visualization** 📊
Your Phoenix dashboard should show:
- Complete conversation flows
- Timing breakdowns for each operation
- Token consumption patterns

### 5. **Performance Analysis** 📈
Analyze your agent's behavior:
- Identify bottlenecks in your workflows
- Track token usage across conversations
- Monitor tool usage patterns
- Document insights from your traces

---

## 🌟 Bonus Challenges (Extra Credit)

### 🥉 Bronze Level: Enhanced Auto-Instrumentation
Implement comprehensive auto-instrumentation with rich metadata:
- **Enhanced configuration**: Add custom project names and endpoints
- **Performance benchmarks**: Set up alerts for slow responses
- **Cost optimization**: Track and optimize token usage
- **User experience metrics**: Monitor response quality indicators

```python
# Bronze level uses auto-instrumentation
tracing_provider = register(
    endpoint=os.getenv("PHOENIX_ENDPOINT"),
    project_name="agentic_app_quickstart",
    protocol="http/protobuf",
    auto_instrument=True
)
```

### 🥈 Silver Level: LLM-as-a-Judge Implementation
Build an automated evaluation system using LLM-as-a-Judge to detect:

**🚨 Hallucination Detection**
```python
# Your evaluator should catch responses like this: (just a silly example :D)
User: "How many sales we had for product type XYZ?"
Agent: "1 million"
Judge: "🚨 HALLUCINATION DETECTED - There is no product XYZ in the dataset"
```

**Note**: for some cases, it can be that you don't necessarily need an LLM Judge to catch this! If you have guardrails that are strong enough or function tools which are decoupled and properly catch exceptions, you will probably mitigate cases like this :)

**🎯 Relevance Scoring**
- Ensure responses address the actual question
- Detect when agents go off-topic
- Score response quality automatically

### 🥇 Gold Level: Custom Tracing & Trajectory Evaluation
Implement advanced monitoring techniques:

**🛤️ Trajectory Evaluation**
- Evaluate entire conversation flows, not just individual responses
- Assess whether the agent followed logical reasoning paths
- Detect when agents get "stuck" in loops or inefficient patterns
- Score the overall problem-solving approach


**🔧 Custom Tracing Implementation**

Examples:

- Write your own custom spans and attributes beyond auto-instrumentation - you can add tags and create [separate sessions](https://arize.com/docs/phoenix/tracing/features-tracing/sessions) for distinct conversations
- Implement business-specific tracing logic
- Create detailed timing breakdowns for complex operations
- Add rich metadata for debugging and analysis

---

## 🚀 Getting Started

### Step 1: Review Phoenix Arize Documentation
Familiarize yourself with:
- Phoenix Arize platform capabilities
- Best practices for agent monitoring

### Step 2: Set Up Your Environment
**Preparation Checklist:**
- ✅ Create Phoenix Arize account and project
- ✅ Install required monitoring packages
- ✅ Configure environment variables and API keys
- ✅ Test basic connectivity

### Step 3: Instrument Your Existing Agent
Start with your Week 1 CSV agent using auto-instrumentation:
1. Set up basic auto-instrumentation with Phoenix ✅
2. Configure your project endpoint and credentials ✅
3. Test with simple conversations ✅
4. Verify traces appear in Phoenix dashboard ✅
5. **Then** add LLM-as-a-Judge evaluation (Silver) or custom tracing (Gold)! 🚀

### Step 4: Implement Advanced Features (Bonus)
**For Silver Level (LLM-as-a-Judge):**
1. Design evaluation criteria for your use case
2. Create judge prompts for quality assessment
3. Implement automated evaluation pipeline
4. Integrate results into your monitoring dashboard

**For Gold Level (Custom Tracing & Trajectory Evaluation):**
1. Implement custom spans beyond auto-instrumentation
2. Design trajectory evaluation criteria
3. Build conversation flow analysis
4. Create efficiency and reasoning path assessments

---

## 📊 Sample Scenarios

Test your monitoring with these scenarios:

**🧪 Happy Path Testing**
- Normal CSV questions with successful responses
- Multi-turn conversations with context
- Complex queries requiring multiple tool calls

**🚨 Error Scenario Testing**
- Invalid CSV file uploads
- Requests for non-existent columns
- Network timeouts and API failures
- Malformed user inputs

**⚡ Performance Testing**
- Large dataset processing
- Rapid-fire question sequences
- Memory-intensive operations
- Concurrent user simulations

---

## 📝 Submission Requirements

### Code Structure
```
week_2/
├── README.md                    # This file
├── solution/
    ├── main.py                  # Your instrumented application
    ├── monitoring/
        ├── tracing.py          # OpenTelemetry configuration
        ├── evaluators.py       # LLM-as-a-Judge implementations
        └── metrics.py          # Custom metrics and spans
    ├── config/
        └── phoenix_config.py   # Phoenix Arize setup
    └── examples/
        ├── trace_examples.py   # Sample traces for testing
        └── evaluation_examples.py # LLM judge examples
```

### Documentation Requirements
1. **README.md** in your solution folder explaining:
   - Your monitoring setup and configuration
   - Key insights discovered from your traces
   - LLM-as-a-Judge implementation (if applicable)
   - Screenshots of your Phoenix dashboard

2. **Configuration Guide**: Step-by-step setup instructions

3. **Performance Report**: Analysis of your agent's behavior based on traces

4. **Demo**: Share screenshots or a short video of your Phoenix dashboard in the #week2 channel

---

## 🎯 Assessment Criteria

| Criteria | Weight | What We're Looking For |
|----------|--------|----------------------|
| **Monitoring Setup** | 30% | Proper OpenTelemetry and Phoenix integration with comprehensive trace coverage |
| **Trace Quality** | 25% | Rich, informative traces that provide actionable insights |  
| **Analysis & Insights** | 25% | Meaningful performance analysis and optimization recommendations |
| **Code Quality** | 20% | Clean, well-documented monitoring code following best practices |

**Bonus points are added on top of the base score!**

---

## 💡 Learning Objectives

By completing this assignment, you will:
- ✅ Master production-grade monitoring for AI systems
- ✅ Understand distributed tracing concepts and implementation
- ✅ Learn to identify and optimize performance bottlenecks
- ✅ Experience automated quality evaluation techniques
- ✅ Develop debugging skills for complex agentic workflows
- ✅ Gain hands-on experience with industry-standard observability tools

---

## 🔧 Technical Deep Dive

### Technical Deep Dive

### Auto-Instrumentation Setup (Bronze & Silver)
```python
from phoenix.trace import register

# Simple auto-instrumentation setup
tracing_provider = register(
    endpoint=os.getenv("PHOENIX_ENDPOINT"),
    project_name="agentic_app_quickstart", 
    protocol="http/protobuf",
    auto_instrument=True
)

# This automatically captures:
# - LLM calls and responses
# - Function/tool executions  
# - Agent reasoning steps
# - Token usage and costs
```

### Custom Tracing (Gold Level Only)
```python
# Advanced custom spans for Gold level
with tracer.start_as_current_span("agent_reasoning") as span:
    span.set_attribute("user_query", user_input)
    span.set_attribute("agent_decision", chosen_action)

# Tool execution span  
with tracer.start_as_current_span("tool_execution") as span:
    span.set_attribute("tool_name", tool_name)
    span.set_attribute("tool_input", tool_params)
    span.set_attribute("tool_success", success)

# LLM call span
with tracer.start_as_current_span("llm_call") as span:
    span.set_attribute("model", model_name)
    span.set_attribute("prompt_tokens", prompt_tokens)
    span.set_attribute("completion_tokens", completion_tokens)
    span.set_attribute("total_cost", calculated_cost)
```

### Key Metrics to Track
- **Latency**: Response time from user input to final answer
- **Throughput**: Conversations per minute/hour
- **Token Usage**: Input/output tokens per conversation
- **Cost**: Dollar cost per conversation/day/month
- **Agent Handoffs**: which agents transferred to which, when and why
- **Tool Usage**: Which tools are used most frequently
- **Error Rates**: Types and frequency of errors

---

## 🤝 Getting Help

**Stuck? Here's your support system:**

1. **Phoenix Arize Documentation** - Comprehensive guides and tutorials
2. **Office hours** - Every Thursday, 7 PM GMT+2
3. **#help channel** - General questions and peer assistance

**Pro Tips:**
- Start with basic auto-instrumentation before adding custom spans
- Use Phoenix's built-in examples to understand trace structure
- Test your setup with simple conversations before complex scenarios
- Document interesting patterns you discover in your traces

---

## 📅 Important Dates

- **Assignment Release**: August 18, 2025
- **Submission Deadline**: August 25, 2025, 11:59 PM
- **Office Hours**: August 19, 2025 (optional but recommended!)

---

## 🏆 Success Stories

Previous customers of mine have discovered amazing insights:
- "I found my agent was making 3x more API calls than necessary due to inefficient tool selection"
- "LLM-as-a-Judge caught hallucinations I never would have noticed manually"
- "Cost tracking revealed that 80% of my expenses came from just 20% of conversations"

**Your turn to uncover what's really happening in your agent! 🕵️‍♂️**