"""
Test script to verify static question bank functionality
Tests random selection and question variety
"""

import json
import random

# Load one topic's questions
with open('questions/matrix.json', 'r', encoding='utf-8') as f:
    matrix_questions = json.load(f)

print(f"Total matrix questions loaded: {len(matrix_questions)}")
print(f"\nQuestion types breakdown:")

mcq_count = sum(1 for q in matrix_questions if q['type'] == 'MCQ')
fib_count = sum(1 for q in matrix_questions if q['type'] == 'FIB')

print(f"  - MCQ: {mcq_count}")
print(f"  - FIB: {fib_count}")

# Test random selection (simulate 5 quizzes)
print(f"\n{'='*60}")
print("Testing Random Selection - Simulating 5 Different Quizzes")
print(f"{'='*60}\n")

for quiz_num in range(1, 6):
    selected = random.sample(matrix_questions, 5)
    print(f"Quiz #{quiz_num}:")
    
    for i, q in enumerate(selected, 1):
        # Extract first 60 chars of question for display
        question_preview = q['question'][:60] + "..." if len(q['question']) > 60 else q['question']
        print(f"  {i}. [{q['type']}] {question_preview}")
    
    print()

# Verify all topics have questions
print(f"{'='*60}")
print("Verifying All Topics")
print(f"{'='*60}\n")

topics = ["matrix", "vectors", "identity-matrix", "dot-product", 
          "vector-magnitude", "vector-addition", "cross-product"]

for topic in topics:
    try:
        with open(f'questions/{topic}.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
            mcq = sum(1 for q in questions if q['type'] == 'MCQ')
            fib = sum(1 for q in questions if q['type'] == 'FIB')
            print(f"[OK] {topic:20s}: {len(questions):4d} questions (MCQ: {mcq}, FIB: {fib})")
    except FileNotFoundError:
        print(f"[X] {topic:20s}: FILE NOT FOUND")

print(f"\n{'='*60}")
print("Test Complete!")
print(f"{'='*60}")
