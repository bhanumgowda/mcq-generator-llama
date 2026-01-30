def build_prompt(topic, num_questions, level):
    return f"""
Generate EXACTLY {num_questions} multiple-choice questions.

Topic: {topic}
Difficulty Level: {level}

Rules:
- Each question must have 4 options (A, B, C, D)
- Only ONE correct answer
- Provide a short explanation for the correct answer
- No extra text outside the format

Format:
Q1. Question text
A. Option
B. Option
C. Option
D. Option
Answer: A
Explanation: Short explanation
"""
