def build_prompt(topic, num_questions, level):
    level_descriptions = {
        "Easy": "basic concepts, definitions, and straightforward applications",
        "Medium": "applied knowledge, analysis, and moderate problem-solving",
        "Hard": "complex analysis, synthesis, evaluation, and advanced problem-solving"
    }
    
    level_desc = level_descriptions.get(level, "appropriate for the selected level")
    
    return f"""
You are an expert educator and assessment designer. Create EXACTLY {num_questions} high-quality multiple-choice questions about "{topic}".

REQUIREMENTS:
- Difficulty Level: {level} ({level_desc})
- Each question must have exactly 4 options (A, B, C, D)
- Only ONE correct answer per question
- Include a clear, educational explanation for each correct answer
- Questions should be well-structured, clear, and unambiguous
- Avoid trick questions or overly complex language
- Cover different aspects of the topic when possible

FORMATTING RULES:
- Use consistent numbering (1., 2., 3., etc.)
- Label options as A), B), C), D)
- Start explanations with "Explanation:"
- Keep explanations concise but informative

EXAMPLE FORMAT:
1. What is the primary function of mitochondria in cells?
A) Protein synthesis
B) Energy production
C) DNA storage
D) Waste removal

Answer: B
Explanation: Mitochondria are known as the "powerhouses" of the cell because they produce ATP through cellular respiration, providing energy for cellular processes.

NOW GENERATE {num_questions} QUESTIONS ABOUT: {topic}

Remember: Focus on educational value, accuracy, and clarity. Each question should test genuine understanding of the topic.
"""