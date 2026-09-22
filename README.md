# AI Software Requirement Analyzer using LangGraph

An AI-powered software requirement analysis system built using **Python, LangChain, LangGraph, and OpenAI GPT-4o-mini**.

The project takes an unstructured software requirement from the user and processes it through a sequential workflow to generate:

* Requirement Analysis
* Functional Requirements
* Non-Functional Requirements
* User Stories
* Test Cases
* Final Software Requirement Report

The project demonstrates how **LangGraph StateGraph, nodes, shared state, and sequential edges** can be used to build an LLM-powered workflow.

---

## Problem Statement

In real-world software development, requirements are often provided as unstructured text by clients or stakeholders.

For example:

> "I want to build an online doctor appointment system where patients can register, search for doctors, book appointments, and cancel appointments."

Before development begins, this requirement needs to be analyzed and converted into structured software requirements.

Manually performing this analysis can take time and may lead to missing requirements.

This project uses an LLM-powered LangGraph workflow to automate the initial requirement-analysis process.

---

## Project Objective

The main objective of this project is to convert a user's natural-language software requirement into a structured software requirement document.

The workflow performs the following tasks:

1. Analyze the software requirement.
2. Identify functional requirements.
3. Identify non-functional requirements.
4. Generate user stories.
5. Generate test cases.
6. Generate a final consolidated report.

---

## Workflow

The application follows a fixed sequential workflow:

```text
                    User Requirement
                           |
                           v
                Requirement Analyzer
                           |
                           v
             Functional Requirements
                           |
                           v
          Non-Functional Requirements
                           |
                           v
                  User Stories
                           |
                           v
                   Test Cases
                           |
                           v
                  Final Report
```

### LangGraph Workflow

```text
START
  |
  v
Requirement Analyzer
  |
  v
Functional Requirement Generator
  |
  v
Non-Functional Requirement Generator
  |
  v
User Story Generator
  |
  v
Test Case Generator
  |
  v
Final Report Generator
  |
  v
END
```

---

## How the Workflow Works

### 1. Requirement Analyzer

The first node receives the user's software requirement and analyzes it.

It identifies:

* Main objective
* Target users
* User needs
* Main features
* Important business requirements
* Constraints

Example:

```text
Input:
I want to build an online doctor appointment system...

Output:
- Objective
- Users
- Main features
- Business requirements
```

---

### 2. Functional Requirement Generator

The second node uses the requirement analysis to generate functional requirements.

Functional requirements describe **what the system should do**.

Example:

```text
FR-01: The system shall allow patients to register.
FR-02: The system shall allow patients to log in.
FR-03: The system shall allow patients to search for doctors.
FR-04: The system shall allow patients to book appointments.
FR-05: The system shall allow patients to cancel appointments.
```

---

### 3. Non-Functional Requirement Generator

The third node identifies important non-functional requirements.

Non-functional requirements describe **how the system should perform** or the qualities/constraints of the system.

The workflow considers:

* Security
* Performance
* Reliability
* Availability
* Scalability

Example:

```text
NFR-01: The system should protect user information.
NFR-02: The system should provide acceptable response times.
NFR-03: The system should be reliable.
NFR-04: The system should be available when required.
NFR-05: The system should support increasing numbers of users.
```

---

### 4. User Story Generator

The fourth node converts functional requirements into user stories.

The project uses the standard format:

```text
As a [user],
I want to [action],
so that [benefit].
```

Example:

```text
As a patient,
I want to search for doctors by specialization,
so that I can find a suitable doctor.
```

---

### 5. Test Case Generator

The fifth node generates test cases based on the functional requirements and user stories.

Example:

```text
TC-01: Verify that a patient can register with valid information.

TC-02: Verify that registration fails when required information is missing.

TC-03: Verify that a patient can search for doctors.

TC-04: Verify that a patient can book an available appointment.

TC-05: Verify that a patient can cancel an appointment.
```

---

### 6. Final Report Generator

The final node combines all generated information into a consolidated software requirement report.

The report contains:

```text
Requirement Analysis
        +
Functional Requirements
        +
Non-Functional Requirements
        +
User Stories
        +
Test Cases
        ↓
Final Report
```

---

# Technologies Used

| Technology         | Purpose                         |
| ------------------ | ------------------------------- |
| Python             | Programming language            |
| LangChain          | LLM application framework       |
| LangGraph          | Workflow orchestration          |
| OpenAI GPT-4o-mini | Language model                  |
| python-dotenv      | Environment variable management |
| TypedDict          | Defining the workflow state     |

---

# LangGraph Concepts Demonstrated

This project demonstrates several important LangGraph concepts.

### State

A shared state is defined using `TypedDict`.

```python
class RequirementState(TypedDict):

    requirement: str
    requirement_analysis: str
    functional_requirement: str
    non_functional_requirement: str
    user_story: str
    test_cases: str
    final_report: str
```

The state allows different nodes to read previously generated information and add their own results.

---

### Nodes

Each processing step is implemented as a node.

```text
Requirement Analyzer
Functional Requirement Generator
Non-Functional Requirement Generator
User Story Generator
Test Case Generator
Final Report Generator
```

Each node receives the current state, performs an LLM operation, and returns an update to the state.

---

### Edges

Edges define the execution order between nodes.

For example:

```python
graph.add_edge(
    "requirementanalyser",
    "functionalrequirementgenerator"
)
```

This means:

```text
Requirement Analyzer
        |
        v
Functional Requirement Generator
```

---

### START and END

The workflow begins with:

```python
graph.add_edge(START, "requirementanalyser")
```

and finishes with:

```python
graph.add_edge("finalreportgenerator", END)
```

---

### StateGraph

The complete workflow is created using:

```python
graph = StateGraph(RequirementState)
```

The graph is then compiled:

```python
requirementAgent = graph.compile()
```

---

# Project Structure

```text
AI-Software-Requirement-Analyzer/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### File Description

| File               | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `main.py`          | Main Python application containing the LangGraph workflow |
| `.env`             | Stores the OpenAI API key locally                         |
| `.gitignore`       | Prevents sensitive/unnecessary files from being uploaded  |
| `requirements.txt` | Contains Python dependencies                              |
| `README.md`        | Project documentation                                     |

---

# Installation

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd AI-Software-Requirement-Analyzer
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install langchain langgraph langchain-openai python-dotenv
```

Alternatively, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file in the project root directory.

```text
OPENAI_API_KEY=your_openai_api_key
```

The application loads the environment variable using:

```python
from dotenv import load_dotenv

load_dotenv()
```

### Important

Do **not** hard-code your API key inside `main.py`.

Do **not** upload `.env` to GitHub.

---

# .gitignore

The `.gitignore` file should contain at least:

```text
.env
venv/
__pycache__/
*.pyc
```

This prevents sensitive credentials and unnecessary Python files from being committed.

---

# Running the Application

Run:

```bash
python main.py
```

The application will ask:

```text
Enter the software requirement:
```

Enter a software requirement.

---

# Example Input

```text
I want to build an online doctor appointment system. Patients should be able to register and log in, search for doctors by specialization, view available appointment slots, book appointments, and cancel appointments. Doctors should be able to manage their profiles and availability. The system should send appointment confirmation and cancellation notifications to patients.
```

---

# Example Output

The application generates a final report containing sections such as:

```text
1. Requirement Analysis

2. Functional Requirements

FR-01: The system shall allow patients to register.
FR-02: The system shall allow patients to log in.
FR-03: The system shall allow patients to search for doctors.
FR-04: The system shall allow patients to view available slots.
FR-05: The system shall allow patients to book appointments.
FR-06: The system shall allow patients to cancel appointments.

3. Non-Functional Requirements

NFR-01: Security
NFR-02: Performance
NFR-03: Reliability
NFR-04: Availability
NFR-05: Scalability

4. User Stories

As a patient, I want to search for doctors by specialization,
so that I can find a suitable doctor.

5. Test Cases

TC-01: Verify that a patient can register with valid information.
TC-02: Verify that a patient can log in with valid credentials.
TC-03: Verify that a patient can book an available appointment.

6. Final Report

A consolidated report containing the analyzed requirements,
functional requirements, non-functional requirements,
user stories, and test cases.
```

> The exact output may vary because the application uses an LLM to generate the content.

---

# Example Use Cases

This workflow can be used as an initial requirement-analysis assistant for different software projects, such as:

### E-Commerce System

```text
Online shopping platform where customers can browse products,
add products to a cart, make payments, and track orders.
```

### Banking System

```text
Online banking application where users can view balances,
transfer money, and download transaction statements.
```

### Hospital Management System

```text
Hospital system for managing patients, doctors,
appointments, and medical records.
```

### Library Management System

```text
System where students can search for books,
borrow books, return books, and check availability.
```

---

# Project Architecture

The project uses an LLM at each processing stage.

```text
                         OpenAI GPT-4o-mini
                                |
                                |
User Requirement ───────────────┤
        |                       |
        v                       |
Requirement Analyzer <──────────┘
        |
        v
Functional Requirement Generator
        |
        v
Non-Functional Requirement Generator
        |
        v
User Story Generator
        |
        v
Test Case Generator
        |
        v
Final Report Generator
        |
        v
    Final Report
```

---

# Why LangGraph?

A simple Python program could call an LLM multiple times sequentially.

However, LangGraph provides a structured way to represent the workflow as a graph.

Instead of manually managing the sequence:

```text
LLM Call → LLM Call → LLM Call → LLM Call
```

the project explicitly defines:

```text
Node → Node → Node → Node
```

This makes the workflow easier to extend with concepts such as:

* Conditional edges
* Branching
* Parallel execution
* Validation
* Retry logic
* Human approval
* Tool integration
* More complex agentic workflows

---

# Current Limitations

This project is intentionally kept simple for learning purposes.

### 1. Fixed Sequential Workflow

The execution order is predefined.

The system does not dynamically decide which node to execute next.

### 2. No External Tools

The workflow does not currently connect to:

* Databases
* APIs
* Jira
* GitHub
* Web search
* External business systems

### 3. No Validation Layer

The generated requirements and test cases are not automatically validated.

### 4. LLM-Generated Results

The generated content may contain incorrect, incomplete, or overly general requirements.

Human review is therefore recommended before using the generated output for actual software development.

### 5. Command-Line Interface

The project currently uses a simple command-line input rather than a graphical user interface or web application.

### 6. Multiple LLM Calls

Each workflow node makes an LLM call, which can increase processing time and API usage.

---

# Future Enhancements

The project can be extended step-by-step.

## Phase 1 — Structured Output

Convert free-form LLM responses into structured data such as:

```text
JSON
Typed objects
Pydantic models
```

---

## Phase 2 — Validation

Add a validation node:

```text
Generate Requirements
        |
        v
Validate Requirements
        |
   ┌────┴────┐
   |         |
 Valid     Invalid
   |         |
   v         v
 Next      Retry
```

---

## Phase 3 — Conditional Routing

Instead of always following the same path, the graph can make decisions based on the generated results.

```text
Requirement
     |
     v
Analyze
     |
     v
Validate
   /   \
Valid  Invalid
 |       |
 v       └──→ Retry
Next
```

---

## Phase 4 — Tool Integration

The workflow could eventually connect to external tools such as:

```text
Jira
GitHub
Database
Web Search
Documentation Systems
```

For example:

```text
Requirement
     ↓
Analyze
     ↓
Generate User Stories
     ↓
Create Jira Tickets
```

---

## Phase 5 — Human Approval

A human approval step could be introduced before creating development tasks:

```text
Generate Requirements
        ↓
Generate User Stories
        ↓
Human Review
     /       \
Approve     Reject
   |           |
   v           v
Create       Revise
Tasks
```

---

## Phase 6 — Advanced Agentic Workflow

A future version could allow an agent to dynamically decide:

```text
What information is needed?
        ↓
Which tool should be used?
        ↓
Should another analysis be performed?
        ↓
Is human approval required?
        ↓
What action should be performed next?
```

This would move the project from a **fixed workflow** toward a more **agentic workflow**.

---

# Learning Outcomes

By building this project, you learn how to:

* Build an LLM-powered application using LangChain.
* Create workflows using LangGraph.
* Define a shared state using `TypedDict`.
* Create LangGraph nodes.
* Connect nodes using edges.
* Use `START` and `END`.
* Pass information between nodes through state.
* Build a sequential LLM workflow.
* Use multiple LLM calls for different processing stages.
* Generate software engineering artifacts using an LLM.
* Design a workflow that can later be extended into a more advanced agentic system.

---

# Key Concepts

### LangChain

A framework/ecosystem for building applications around language models and related components.

### LangGraph

A framework for building stateful workflows and agentic applications using graph-based execution.

### Node

A function that performs a particular operation within the graph.

### State

Shared information that flows between nodes.

### Edge

Defines the relationship and execution path between nodes.

### StateGraph

The graph structure used to define the workflow and its state.

### LLM

The language model used to analyze requirements and generate outputs.

---

# Workflow vs AI Agent

This project is a **fixed workflow**, not a fully autonomous AI agent.

The workflow follows a predefined sequence:

```text
Analyzer
   ↓
Functional Requirements
   ↓
Non-Functional Requirements
   ↓
User Stories
   ↓
Test Cases
   ↓
Final Report
```

A more advanced AI agent could dynamically decide which action or tool to use based on the current situation.

This distinction is important when describing the project in interviews.

---

# Security

Never expose API keys in source code or public repositories.

Use environment variables:

```text
OPENAI_API_KEY=your_api_key
```

and keep `.env` in `.gitignore`.

If an API key is accidentally exposed, revoke/rotate it before publishing the repository.

---

## 👨‍💻 Author

Snehal Vhasure | Full Stack Developer | AI & Machine Learning Enthusiast | Master's Aspirant in Information Technology

This project was built as part of my Deep Learning and Computer Vision learning journey to understand how CNNs improve upon traditional ANN architectures for image-based applications.
