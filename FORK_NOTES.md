
🎯 Overview
This fork serves as a technical portfolio for my work in AI Model Evaluation and Prompt Engineering. While the original deepeval framework provides the tooling, this repository contains custom implementation logic designed to solve high-stakes alignment and hallucination issues in production LLM systems.

🛠️ Key Contributions
I have extended this repository with a dedicated test suite located in /tests/muthoni_ai_evals/. My focus areas include:

1. Hallucination Detection Framework
Leveraging my experience in high-volume data quality (Google/Rex.zone), I implemented custom HallucinationMetric configurations to validate model outputs against a "Ground Truth" retrieval context.

Use Case: Preventing "Policy Drifting" in customer support chatbots.

Technical Approach: Implementing a dual-metric check that balances Factual Consistency with Instruction Adherence.

2. G-Eval Implementation (LLM-as-a-Judge)
I designed custom GEval criteria to measure qualitative metrics that standard NLP benchmarks often miss:

Tone Alignment: Ensuring the model maintains a professional, helpful persona across multi-turn dialogues.

Reasoning Efficiency: Evaluating if the model achieves the user's goal in the minimum number of steps.

📈 Impact on AI Quality
By applying these structured evaluation frameworks, I demonstrate the ability to:

Reduce Hallucination Rates: Quantifiably identifying when a model ignores retrieval context.

Standardize Quality: Moving away from "vibe-based" testing toward programmatic, reproducible unit tests for AI.

Optimize Prompts: Using evaluation results to iterate on system instructions, ensuring higher adherence to complex constraints.