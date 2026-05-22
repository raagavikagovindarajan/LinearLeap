import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# New topics to generate
NEW_TOPICS = {
    "matrix-transpose": "Matrix Transpose",
    "matrix-determinant": "Matrix Determinant",  
    "matrix-inverse": "Matrix Inverse",
    "eigenvalues-eigenvectors": "Eigenvalues and Eigenvectors",
    "vector-projection": "Vector Projection",
    "linear-independence": "Linear Independence",
    "basis-vectors": "Basis Vectors",
    "linear-transformations": "Linear Transformations",
    "orthogonality": "Orthogonality",
    "matrix-rank": "Rank of a Matrix",
    "null-space": "Null Space"
}

def generate_questions_for_topic(topic_id, topic_name, num_batches=200):
    """Generate 1000 questions (5 per batch × 200 batches) for a given topic"""
    print(f"\n{'='*60}")
    print(f"Generating questions for: {topic_name}")
    print(f"{'='*60}")
    
    all_questions = []
    
    # Prompts for each topic
    prompts = {
        "matrix-transpose": """Generate 5 quiz questions about Matrix Transpose.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters  
- Include 2×2 and 3×3 examples
- Cover properties: (A^T)^T = A, (AB)^T = B^T A^T
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "matrix-determinant": """Generate 5 quiz questions about Matrix Determinant.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 and 3×3 determinant calculations
- Cover properties: det(AB) = det(A)det(B)
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "matrix-inverse": """Generate 5 quiz questions about Matrix Inverse.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 inverse calculations
- Cover properties: AA^(-1) = I
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "eigenvalues-eigenvectors": """Generate 5 quiz questions about Eigenvalues and Eigenvectors.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 matrix examples
- Cover definition: Av = λv
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "vector-projection": """Generate 5 quiz questions about Vector Projection.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include proj_v(u) formula
- Cover 2D and 3D examples
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "linear-independence": """Generate 5 quiz questions about Linear Independence.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2-3 vector examples
- Cover definition and testing
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "basis-vectors": """Generate 5 quiz questions about Basis Vectors.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include standard basis examples
- Cover span and linear independence
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "linear-transformations": """Generate 5 quiz questions about Linear Transformations.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2D transformation matrices
- Cover rotation, scaling, reflection
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "orthogonality": """Generate 5 quiz questions about Orthogonality.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include orthogonal vectors and matrices
- Cover dot product = 0 condition
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "matrix-rank": """Generate 5 quiz questions about Rank of a Matrix.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 and 3×3 examples
- Cover row echelon form
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",

        "null-space": """Generate 5 quiz questions about Null Space.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include solving Ax = 0
- Cover 2×2 and 3×3 examples
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]"""
    }
    
    prompt = prompts[topic_id]
    
    for batch in range(num_batches):
        try:
            print(f"  Batch {batch+1}/{num_batches}...", end=" ", flush=True)
            
            response = model.generate_content(
                f"You are a math education expert. Generate quiz questions in valid JSON format only.\n\n{prompt}",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.9,  # Higher temperature for more variety
                    max_output_tokens=2000,
                )
            )
            
            content = response.text.strip()
            
            # Extract JSON from potential markdown code blocks
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
            questions = json.loads(content)
            
            # Validate that we got 5 questions
            if len(questions) == 5:
                all_questions.extend(questions)
                print("✓")
            else:
                print(f"⚠ Got {len(questions)} questions, expected 5")
            
            # Rate limiting to avoid API quota issues
            time.sleep(1)
            
        except Exception as e:
            print(f"✗ Error: {str(e)[:50]}")
            continue
    
    print(f"\n  Total questions generated: {len(all_questions)}")
    
    # Save to file
    os.makedirs("questions", exist_ok=True)
    filename = f"questions/{topic_id}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, indent=2, ensure_ascii=False)
    
    print(f"  ✓ Saved to {filename}")
    return len(all_questions)

# Main execution
if __name__ == "__main__":
    print("\n" + "="*60)
    print("GENERATING STATIC QUESTIONS FOR NEW TOPICS")
    print("="*60)
    
    total_generated = 0
    
    for topic_id, topic_name in NEW_TOPICS.items():
        count = generate_questions_for_topic(topic_id, topic_name)
        total_generated += count
    
    print("\n" + "="*60)
    print(f"GENERATION COMPLETE!")
    print(f"Total questions generated: {total_generated}")
    print("="*60)
