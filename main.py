import os
import langchain
import langgraph
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI 
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# llm_model
llm_model = ChatOpenAI(model ="gpt-4o-mini")

# State 
class RequirementState(TypedDict):
    requirement: str
    requirement_analysis: str
    functional_requirement: str
    non_functional_requirement : str
    user_story : str
    test_cases : str
    final_report : str

# Node1: Requirement Analyser
def requirementAnalyser(state : RequirementState):
    """Understand the requirement privided by the user"""

    requirement = state["requirement"]
    prompt = f"""Analyze the following software requirement: 
                 {requirement}
                    1. Objective: Understand the requirement and provide a detailed analysis.
                    2. Users: Identify the target users and their needs.
                    3. Main features: List the main features and functionalities of the software.
                    4. Important business requirements: Highlight any critical business requirements or constraints.
                 """

    result = llm_model.invoke(prompt).content
    return {"requirement_analysis" : result}

# Node2: Functional Requirement Generator

# This node takes the analysis from Node 1.
# Requirement Analysis
#        ↓
# Functional Requirements
#Example output:
# FR-01: User can register.
# FR-02: User can log in.
# FR-03: User can search for products.
# FR-04: User can place an order.
# FR-05: User can cancel an order.
def functionalRequirementGenerator(state : RequirementState):
    """Generate the functional requirements based on the analysis provided by the user."""

    generator = state["requirement_analysis"]
    prompt2 = f"""On the bases of requirement analysis provided below, generate a list of functional requirements for the software.
                {generator}
                Please provide the functional requirements in the following format:
                FR-01: [Functional Requirement 1]
                FR-02: [Functional Requirement 2]
                FR-03: [Functional Requirement 3]
    """

    result = llm_model.invoke(prompt2).content
    return {"functional_requirement" : result}


# Node 3: Non-Functional Requirement Generator

# Requirement Analysis
#         ↓
# Non-Functional Requirements
# For example:
# - Security
# - Performance
# - Availability
# - Scalability
# - Reliability

def nonFunctionalRequirements(state : RequirementState):
    """This node identifies requirements related to qualities and constraints of the system."""
    analysis = state["requirement_analysis"]
    prompt3 = f"""Based on the requirement analysis provided, identify the important non-functional requirements for the software.
                {analysis}
                    Consider: 
                    1. Security
                    2. Performance
                    3. Reliability
                    4. Availability
                    5. Scalability
                    Please provide the non-functional requirements in a clear and concise manner.
"""

    result = llm_model.invoke(prompt3).content
    return {"non_functional_requirement" : result}

# Node 4: User Story Generator

def userStoryGenerator(state: RequirementState):
    """Generate user stories based on the functional and non-functional requirements provided by the user."""

    user_story = state["functional_requirement"]
    prompt4 = f"""Convert the functional requirements into user stories: {user_story}
                    Use the format: 
                    As a [user], I want to [action], so that [benefit]."""

    result = llm_model.invoke(prompt4).content
    return {"user_story" : result}

# Node 5: Test Case Generator
# Functional Requirements
#         +
# User Stories
#         ↓
#    Test Cases
# example: 
# TC-01:
# Verify that a user can register with valid information.
# TC-02:
# Verify that registration fails when the email is already registered.
# TC-03:
# Verify that a user can search for a product.

def testCaseGenerator(state: RequirementState):
    """ Generate the test cases based on the functional requirements and user stories provided by the user."""

    case_generator = state["functional_requirement"]
    user_story = state["user_story"]
    prompt5 = f"""Generate test cases on the basis of functional requirements.
                Functional Requirements: {case_generator}
                User Stories: {user_story}
                    Please provide the test cases in the following format:
                    TC-01: [Test Case 1]
                    TC-02: [Test Case 2]
                    TC-03: [Test Case 3]
    """

    result = llm_model.invoke(prompt5).content
    return {"test_cases" : result}

# Node 6: Final Report

# Requirement Analysis
#         +
# Functional Requirements
#         +
# Non-Functional Requirements
#         +
# User Stories
#         +
# Test Cases
#      ↓
#   Final Report

def generateFinalReport(state: RequirementState):
    """Generate a final report based on the functional requirements, non-functional requirements, user stories, and test cases provided by the user."""

    final_report = state["requirement_analysis"]
    functional_requirement = state["functional_requirement"]
    non_functional_requirement = state["non_functional_requirement"]
    user_story = state["user_story"]
    test_cases = state["test_cases"]

    result = llm_model.invoke(f"""Generate a final report based on the following information:
                                    Requirement Analysis: {final_report}
                                    Functional Requirements: {functional_requirement}
                                    Non-Functional Requirements: {non_functional_requirement}
                                    User Stories: {user_story}
                                    Test Cases: {test_cases}
                                    """).content
    return {"final_report": result}

# LANGGRAPH 
graph = StateGraph(RequirementState)

# Add Nodes
graph.add_node("requirementanalyser", requirementAnalyser)
graph.add_node("nonfunctionalrequirementgenerator", nonFunctionalRequirements)
graph.add_node("functionalrequirementgenerator", functionalRequirementGenerator)
graph.add_node("userstorygenerator", userStoryGenerator)
graph.add_node("testcasegenerator", testCaseGenerator)
graph.add_node("finalreportgenerator", generateFinalReport)

# Add Edges
graph.add_edge(START, "requirementanalyser")
graph.add_edge("requirementanalyser", "functionalrequirementgenerator")
graph.add_edge("functionalrequirementgenerator", "nonfunctionalrequirementgenerator")
graph.add_edge("nonfunctionalrequirementgenerator", "userstorygenerator")
graph.add_edge("userstorygenerator", "testcasegenerator")
graph.add_edge("testcasegenerator", "finalreportgenerator")
graph.add_edge("finalreportgenerator", END)

# Compile Graph
requirementAgent = graph.compile()

# Input requirement from the user
input_requirement = input("Enter the software requirement: ")
result = requirementAgent.invoke({"requirement" : input_requirement})

print(result["final_report"])