import pytest
from deepeval import assert_test
from deepeval.metrics import HallucinationMetric, GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

# 1. Setup a custom G-Eval metric for 'Instruction Adherence'
# This proves you can define complex evaluation criteria beyond simple facts.
instruction_adherence_metric = GEval(
    name="Instruction Adherence",
    criteria="Determine if the 'actual output' follows the specific formatting constraints (e.g., bullet points, no preamble) provided in the 'input'.",
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
    threshold=0.7
)

# 2. Setup the standard Hallucination Metric
# This measures how much of the output is factually grounded in the retrieval context.
hallucination_metric = HallucinationMetric(threshold=0.5)

def test_customer_support_hallucination():
    """
    Scenario: A customer asks about a specific refund policy.
    The goal is to ensure the model doesn't 'hallucinate' a 60-day window 
    when the context says 30 days.
    """
    
    # This data mimics the 'Multi-turn conversational datasets' mentioned in your CV
    input_query = "I bought my shoes 45 days ago. Can I still get a refund?"
    
    # The 'Context' is what the AI is told to read
    context = [
        "Our official policy allows for a full refund within 30 days of purchase.",
        "Store credit is available for returns between 31 and 60 days.",
        "Proof of purchase is required for all transactions."
    ]
    
    # The 'Actual Output' is what the AI actually said (simulated here)
    # NOTE: This response is a 'Partial Hallucination' because it ignores the 30-day limit.
    actual_ai_response = "Yes, you can get a full refund because we have a 60-day return window."

    test_case = LLMTestCase(
        input=input_query,
        actual_output=actual_ai_response,
        retrieval_context=context
    )

    # We run both metrics: one for factual grounding, one for following instructions
    assert_test(test_case, [hallucination_metric, instruction_adherence_metric])

if __name__ == "__main__":
    # This allows you to run the test directly via 'python test_hallucination_logic.py'
    # though 'deepeval test run' is the preferred method.
    print("Running Hallucination Logic Test...")