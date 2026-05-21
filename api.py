from flask import Flask, jsonify
from flask_cors import CORS
import google.generativeai as genai
import json
import os
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load static question banks
STATIC_QUESTIONS = {}
for topic in ["matrix", "vectors", "identity-matrix", "dot-product", "vector-magnitude", "vector-addition", "cross-product",
              "matrix-transpose", "matrix-determinant", "matrix-inverse", "eigenvalues-eigenvectors", 
              "vector-projection", "linear-independence", "basis-vectors", "linear-transformations",
              "orthogonality", "matrix-rank", "null-space",
              "systems-linear-equations", "gaussian-elimination", "row-echelon-form", "matrix-trace",
              "gram-schmidt", "diagonalization", "column-row-space", "lu-decomposition",
              "least-squares", "change-of-basis"]:
    try:
        with open(f"questions/{topic}.json", 'r', encoding='utf-8') as f:
            STATIC_QUESTIONS[topic] = json.load(f)
        print(f"Loaded {len(STATIC_QUESTIONS[topic])} static questions for {topic}")
    except FileNotFoundError:
        print(f"Warning: Static questions file not found for {topic}")
        STATIC_QUESTIONS[topic] = []

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Gemini Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_ENABLED = False  # Set to False to use fallback hardcoded questions

# Initialize Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    GEMINI_ENABLED = False

# Prompt templates for each topic
PROMPT_TEMPLATES = {
    "matrix": """Generate 5 linear algebra quiz questions about Matrix Multiplication.

Requirements:
- Mix of 3 MCQ (Multiple Choice) and 2 FIB (Fill in the Blank)
- Use LaTeX notation with \\( \\) delimiters for math
- Include 2×2 and 3×3 matrix examples
- Return ONLY a valid JSON array, no additional text

Format:
[
  {"type": "MCQ", "question": "What is \\(A \\times B\\) where...", "options": ["option1", "option2", "option3", "option4"], "answer": "correct option"},
  {"type": "FIB", "question": "Calculate...", "answer": "correct answer"}
]""",
    
    "identity-matrix": """Generate 5 quiz questions about Identity Matrix.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Focus on properties: AI = IA = A, diagonal of 1s
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "vectors": """Generate 5 quiz questions about Vectors.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Cover magnitude, dot product, addition
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "dot-product": """Generate 5 quiz questions about Dot Product.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include perpendicular vectors (dot product = 0)
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "vector-magnitude": """Generate 5 quiz questions about Vector Magnitude.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include unit vector questions
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "vector-addition": """Generate 5 quiz questions about Vector Addition.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include subtraction questions too
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "cross-product": """Generate 5 quiz questions about Cross Product.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include i×j=k relationships
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
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

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "systems-linear-equations": """Generate 5 quiz questions about Systems of Linear Equations.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 and 3×3 systems
- Cover solutions types: unique, infinite, no solution
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "gaussian-elimination": """Generate 5 quiz questions about Gaussian Elimination.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include row operations
- Cover reducing to row echelon form
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "row-echelon-form": """Generate 5 quiz questions about Row Echelon Form (REF/RREF).

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include identifying REF vs RREF
- Cover pivot positions
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "matrix-trace": """Generate 5 quiz questions about Matrix Trace.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 and 3×3 matrices
- Cover properties: tr(A+B) = tr(A)+tr(B), tr(AB) = tr(BA)
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "gram-schmidt": """Generate 5 quiz questions about Gram-Schmidt Process.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2D and 3D vector examples
- Cover orthogonalization steps
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "diagonalization": """Generate 5 quiz questions about Matrix Diagonalization.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 matrix examples
- Cover A = PDP^(-1) form
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "column-row-space": """Generate 5 quiz questions about Column Space and Row Space.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include finding basis for column/row space
- Cover dimension and rank relationship
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "lu-decomposition": """Generate 5 quiz questions about LU Decomposition.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2×2 and 3×3 examples
- Cover A = LU factorization
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "least-squares": """Generate 5 quiz questions about Least Squares Approximation.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include normal equation: A^T Ax = A^T b
- Cover linear regression applications
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]""",
    
    "change-of-basis": """Generate 5 quiz questions about Change of Basis.

Requirements:
- Mix of 3 MCQ and 2 FIB
- Use LaTeX notation with \\( \\) delimiters
- Include 2D coordinate transformations
- Cover change of basis matrix P
- Return ONLY valid JSON array

Format: [{"type": "MCQ", "question": "...", "options": [...], "answer": "..."}, ...]"""
}

def generate_questions(topic):
    """Generate quiz questions using Gemini API"""
    if not GEMINI_ENABLED:
        # Return fallback hardcoded questions if Gemini is disabled
        return get_fallback_questions(topic)
    
    try:
        prompt = PROMPT_TEMPLATES.get(topic, PROMPT_TEMPLATES["matrix"])
        
        # Generate content using Gemini
        response = model.generate_content(
            f"You are a math education expert. Generate quiz questions in valid JSON format only.\n\n{prompt}",
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=2000,
            )
        )
        
        content = response.text.strip()
        
        # Try to extract JSON from the response
        # Sometimes LLMs wrap JSON in markdown code blocks
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
        
        questions = json.loads(content)
        return questions
        
    except Exception as e:
        print(f"Error generating questions with Gemini API: {e}")
        print("Falling back to hardcoded questions...")
        return get_fallback_questions(topic)

def get_fallback_questions(topic):
    """Return randomly selected questions from static question banks"""
    # Use new static question banks if available
    if topic in STATIC_QUESTIONS and len(STATIC_QUESTIONS[topic]) > 0:
        # Ensure unique question text within the quiz (no duplicate questions)
        selected = []
        seen_questions = set()
        available = STATIC_QUESTIONS[topic].copy()
        random.shuffle(available)
        
        # Select up to 5 questions with unique question text
        for q in available:
            if q['question'] not in seen_questions and len(selected) < 5:
                selected.append(q)
                seen_questions.add(q['question'])
            
            if len(selected) >= 5:
                break
        
        # If we couldn't find 5 unique questions, fill with any remaining
        if len(selected) < 5:
            for q in available:
                if len(selected) < 5 and q not in selected:
                    selected.append(q)
        
        return selected
    
    # Fallback to original hardcoded questions if static files not found
    fallback_map = {
        "matrix": "MATRIX_QUESTIONS",
        "vectors": "VECTORS_QUESTIONS",
        "identity-matrix": "IDENTITY_MATRIX_QUESTIONS",
        "dot-product": "DOT_PRODUCT_QUESTIONS",
        "vector-magnitude": "VECTOR_MAGNITUDE_QUESTIONS",
        "vector-addition": "VECTOR_ADDITION_QUESTIONS",
        "cross-product": "CROSS_PRODUCT_QUESTIONS"
    }
    
    var_name = fallback_map.get(topic, "MATRIX_QUESTIONS")
    return globals().get(var_name, [])

# Matrix quiz questions (5 questions with mix of MCQ and FIB)
MATRIX_QUESTIONS = [
    {
        "type": "MCQ",
        "question": "What is \\(A \\times B\\) where \\(A = \\begin{bmatrix}1 & 2\\\\\\\\3 & 4\\end{bmatrix}\\) and \\(B = \\begin{bmatrix}5 & 6\\\\\\\\7 & 8\\end{bmatrix}\\)?",
        "options": [
            "\\(\\begin{bmatrix}19 & 22\\\\\\\\43 & 50\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}17 & 20\\\\\\\\41 & 48\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}19 & 23\\\\\\\\42 & 50\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}18 & 22\\\\\\\\43 & 49\\end{bmatrix}\\)"
        ],
        "answer": "\\(\\begin{bmatrix}19 & 22\\\\\\\\43 & 50\\end{bmatrix}\\)"
    },
    {
        "type": "FIB",
        "question": "What is \\(A \\times B\\) where \\(A = \\begin{bmatrix}1 & 0 & 2\\\\\\\\0 & 1 & 3\\\\\\\\2 & 1 & 0\\end{bmatrix}\\) and \\(B = \\begin{bmatrix}3 & 1 & 0\\\\\\\\0 & 2 & 1\\\\\\\\1 & 0 & 2\\end{bmatrix}\\)?",
        "answer": "\\(\\begin{bmatrix}5 & 1 & 4\\\\\\\\3 & 2 & 7\\\\\\\\6 & 4 & 1\\end{bmatrix}\\)"
    },
    {
        "type": "MCQ",
        "question": "What is \\(A \\times B\\) where \\(A = \\begin{bmatrix}2 & 0\\\\\\\\1 & 3\\end{bmatrix}\\) and \\(B = \\begin{bmatrix}4 & 1\\\\\\\\2 & 5\\end{bmatrix}\\)?",
        "options": [
            "\\(\\begin{bmatrix}8 & 2\\\\\\\\10 & 16\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}8 & 3\\\\\\\\10 & 15\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}7 & 2\\\\\\\\11 & 16\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}8 & 2\\\\\\\\9 & 16\\end{bmatrix}\\)"
        ],
        "answer": "\\(\\begin{bmatrix}8 & 2\\\\\\\\10 & 16\\end{bmatrix}\\)"
    },
    {
        "type": "FIB",
        "question": "What is \\(A \\times B\\) where \\(A = \\begin{bmatrix}1 & 2 & 3\\\\\\\\4 & 5 & 6\\\\\\\\7 & 8 & 9\\end{bmatrix}\\) and \\(B = \\begin{bmatrix}1 & 0 & 0\\\\\\\\0 & 1 & 0\\\\\\\\0 & 0 & 1\\end{bmatrix}\\)?",
        "answer": "\\(\\begin{bmatrix}1 & 2 & 3\\\\\\\\4 & 5 & 6\\\\\\\\7 & 8 & 9\\end{bmatrix}\\)"
    },
    {
        "type": "MCQ",
        "question": "What is \\(A \\times B\\) where \\(A = \\begin{bmatrix}2 & 1\\\\\\\\4 & 3\\end{bmatrix}\\) and \\(B = \\begin{bmatrix}1 & 2\\\\\\\\3 & 4\\end{bmatrix}\\)?",
        "options": [
            "\\(\\begin{bmatrix}5 & 8\\\\\\\\13 & 20\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}5 & 7\\\\\\\\13 & 19\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}6 & 8\\\\\\\\13 & 20\\end{bmatrix}\\)",
            "\\(\\begin{bmatrix}5 & 8\\\\\\\\12 & 20\\end{bmatrix}\\)"
        ],
        "answer": "\\(\\begin{bmatrix}5 & 8\\\\\\\\13 & 20\\end{bmatrix}\\)"
    }
]

# Vectors quiz questions (5 questions with mix of MCQ and FIB)
VECTORS_QUESTIONS = [
    {
        "type": "MCQ",
        "question": "What is the dot product of vectors \\(\\vec{u} = (2, 3)\\) and \\(\\vec{v} = (4, 5)\\)?",
        "options": ["\\(23\\)", "\\(26\\)", "\\(27\\)", "\\(28\\)"],
        "answer": "\\(23\\)"
    },
    {
        "type": "FIB",
        "question": "The magnitude of vector \\(\\vec{v} = (3, 4)\\) is ____.",
        "answer": "5"
    },
    {
        "type": "MCQ",
        "question": "Which of the following is the cross product of \\(\\vec{i}\\) and \\(\\vec{j}\\)?",
        "options": ["\\(\\vec{k}\\)", "\\(-\\vec{k}\\)", "\\(0\\)", "\\(\\vec{i} + \\vec{j}\\)"],
        "answer": "\\(\\vec{k}\\)"
    },
    {
        "type": "FIB",
        "question": "What is the angle (in degrees) between vectors \\(\\vec{u} = (1, 0)\\) and \\(\\vec{v} = (0, 1)\\)?",
        "answer": "90"
    },
    {
        "type": "MCQ",
        "question": "What is the result of \\((3, 4) + (1, 2)\\)?",
        "options": ["\\((4, 6)\\)", "\\((4, 8)\\)", "\\((2, 2)\\)", "\\((3, 6)\\)"],
        "answer": "\\((4, 6)\\)"
    }
]

# Identity Matrix quiz questions
IDENTITY_MATRIX_QUESTIONS = [
    {
        "type": "MCQ",
        "question": "What is the result of multiplying any matrix \\(A\\) by the identity matrix \\(I\\)?",
        "options": ["\\(0\\)", "\\(A\\)", "\\(I\\)", "\\(2A\\)"],
        "answer": "\\(A\\)"
    },
    {
        "type": "FIB",
        "question": "What is the 3×3 identity matrix \\(I_3\\)?",
        "answer": "\\(\\begin{bmatrix}1 & 0 & 0\\\\\\\\0 & 1 & 0\\\\\\\\0 & 0 & 1\\end{bmatrix}\\)"
    },
    {
        "type": "MCQ",
        "question": "What are the values on the main diagonal of an identity matrix?",
        "options": ["\\(0\\)", "\\(1\\)", "\\(-1\\)", "\\(n\\)"],
        "answer": "\\(1\\)"
    },
    {
        "type": "FIB",
        "question": "What is \\(\\begin{bmatrix}2 & 3\\\\\\\\4 & 5\\end{bmatrix} \\times \\begin{bmatrix}1 & 0\\\\\\\\0 & 1\\end{bmatrix}\\)?",
        "answer": "\\(\\begin{bmatrix}2 & 3\\\\\\\\4 & 5\\end{bmatrix}\\)"
    },
    {
        "type": "MCQ",
        "question": "Which property does the identity matrix have?",
        "options": ["\\(AI = IA = A\\)", "\\(AI = 0\\)", "\\(AI \\neq IA\\)", "\\(AI = I\\)"],
        "answer": "\\(AI = IA = A\\)"
    }
]

# Dot Product quiz questions
DOT_PRODUCT_QUESTIONS = [
    {
        "type": "MCQ",
        "question": "What is the dot product of \\(\\vec{u} = (2, 3)\\) and \\(\\vec{v} = (4, 5)\\)?",
        "options": ["\\(23\\)", "\\(26\\)", "\\(20\\)", "\\(15\\)"],
        "answer": "\\(23\\)"
    },
    {
        "type": "FIB",
        "question": "What is \\((1, 2, 3) \\cdot (4, 5, 6)\\)?",
        "answer": "32"
    },
    {
        "type": "MCQ",
        "question": "If \\(\\vec{u} \\cdot \\vec{v} = 0\\), what can we conclude about the vectors?",
        "options": ["They are perpendicular", "They are parallel", "They are equal", "They are zero vectors"],
        "answer": "They are perpendicular"
    },
    {
        "type": "FIB",
        "question": "What is \\((3, 0) \\cdot (0, 4)\\)?",
        "answer": "0"
    },
    {
        "type": "MCQ",
        "question": "What is \\(\\vec{v} \\cdot \\vec{v}\\) equal to?",
        "options": ["\\(|\\vec{v}|^2\\)", "\\(0\\)", "\\(1\\)", "\\(|\\vec{v}|\\)"],
        "answer": "\\(|\\vec{v}|^2\\)"
    }
]

# Vector Magnitude quiz questions
VECTOR_MAGNITUDE_QUESTIONS = [
    {
        "type": "MCQ",
        "question": "What is the magnitude of \\(\\vec{v} = (3, 4)\\)?",
        "options": ["\\(5\\)", "\\(7\\)", "\\(12\\)", "\\(25\\)"],
        "answer": "\\(5\\)"
    },
    {
        "type": "FIB",
        "question": "What is the magnitude of \\(\\vec{u} = (1, 2, 2)\\)?",
        "answer": "3"
    },
    {
        "type": "MCQ",
        "question": "What is a unit vector?",
        "options": ["A vector with magnitude 1", "A vector with magnitude 0", "A vector along the x-axis", "A zero vector"],
        "answer": "A vector with magnitude 1"
    },
    {
        "type": "FIB",
        "question": "What is the magnitude of \\(\\vec{w} = (0, 5)\\)?",
        "answer": "5"
    },
    {
        "type": "MCQ",
        "question": "If \\(|\\vec{v}| = 0\\), what is \\(\\vec{v}\\)?",
        "options": ["\\(\\vec{0}\\) (zero vector)", "\\((1, 0)\\)", "\\((0, 1)\\)", "\\((1, 1)\\)"],
        "answer": "\\(\\vec{0}\\) (zero vector)"
    }
]

# Vector Addition quiz questions
VECTOR_ADDITION_QUESTIONS = [
    {
        "type": "MCQ",
        "question": "What is \\((3, 4) + (1, 2)\\)?",
        "options": ["\\((4, 6)\\)", "\\((4, 8)\\)", "\\((2, 2)\\)", "\\((3, 6)\\)"],
        "answer": "\\((4, 6)\\)"
    },
    {
        "type": "FIB",
        "question": "What is \\((1, 2, 3) + (4, 5, 6)\\)?",
        "answer": "(5, 7, 9)"
    },
    {
        "type": "MCQ",
        "question": "What is \\((5, 8) - (2, 3)\\)?",
        "options": ["\\((3, 5)\\)", "\\((7, 11)\\)", "\\((3, 4)\\)", "\\((2, 5)\\)"],
        "answer": "\\((3, 5)\\)"
    },
    {
        "type": "FIB",
        "question": "What is \\((2, 0) + (0, 3)\\)?",
        "answer": "(2, 3)"
    },
    {
        "type": "MCQ",
        "question": "Which property does vector addition satisfy?",
        "options": ["Commutative: \\(\\vec{u} + \\vec{v} = \\vec{v} + \\vec{u}\\)", "\\(\\vec{u} + \\vec{v} = \\vec{u} - \\vec{v}\\)", "\\(\\vec{u} + \\vec{v} = 0\\)", "\\(\\vec{u} + \\vec{v} = \\vec{u} \\cdot \\vec{v}\\)"],
        "answer": "Commutative: \\(\\vec{u} + \\vec{v} = \\vec{v} + \\vec{u}\\)"
    }
]

# Cross Product quiz questions
CROSS_PRODUCT_QUESTIONS = [
    {
        "type": "MCQ",
        "question": "What is \\(\\vec{i} \\times \\vec{j}\\)?",
        "options": ["\\(\\vec{k}\\)", "\\(-\\vec{k}\\)", "\\(\\vec{i}\\)", "\\(0\\)"],
        "answer": "\\(\\vec{k}\\)"
    },
    {
        "type": "FIB",
        "question": "What is \\(\\vec{j} \\times \\vec{i}\\)?",
        "answer": "\\(-\\vec{k}\\)"
    },
    {
        "type": "MCQ",
        "question": "The cross product of two vectors produces:",
        "options": ["A vector perpendicular to both", "A scalar", "A parallel vector", "The zero vector always"],
        "answer": "A vector perpendicular to both"
    },
    {
        "type": "FIB",
        "question": "What is \\(\\vec{u} \\times \\vec{u}\\)?",
        "answer": "\\(\\vec{0}\\)"
    },
    {
        "type": "MCQ",
        "question": "Which property does the cross product have?",
        "options": ["Anti-commutative: \\(\\vec{u} \\times \\vec{v} = -(\\vec{v} \\times \\vec{u})\\)", "Commutative", "\\(\\vec{u} \\times \\vec{v} = \\vec{u} \\cdot \\vec{v}\\)", "Always zero"],
        "answer": "Anti-commutative: \\(\\vec{u} \\times \\vec{v} = -(\\vec{v} \\times \\vec{u})\\)"
    }
]

@app.route('/api/quiz/matrix', methods=['GET'])
def get_matrix_quiz():
    """Return matrix multiplication quiz questions"""
    questions = generate_questions("matrix")
    return jsonify({"questions": questions})

@app.route('/api/quiz/vectors', methods=['GET'])
def get_vectors_quiz():
    """Return vector operations quiz questions"""
    questions = generate_questions("vectors")
    return jsonify({"questions": questions})

@app.route('/api/quiz/identity-matrix', methods=['GET'])
def get_identity_matrix_quiz():
    """Return identity matrix quiz questions"""
    questions = generate_questions("identity-matrix")
    return jsonify({"questions": questions})

@app.route('/api/quiz/dot-product', methods=['GET'])
def get_dot_product_quiz():
    """Return dot product quiz questions"""
    questions = generate_questions("dot-product")
    return jsonify({"questions": questions})

@app.route('/api/quiz/vector-magnitude', methods=['GET'])
def get_vector_magnitude_quiz():
    """Return vector magnitude quiz questions"""
    questions = generate_questions("vector-magnitude")
    return jsonify({"questions": questions})

@app.route('/api/quiz/vector-addition', methods=['GET'])
def get_vector_addition_quiz():
    """Return vector addition quiz questions"""
    questions = generate_questions("vector-addition")
    return jsonify({"questions": questions})

@app.route('/api/quiz/cross-product', methods=['GET'])
def get_cross_product_quiz():
    """Return cross product quiz questions"""
    questions = generate_questions("cross-product")
    return jsonify({"questions": questions})

@app.route('/api/quiz/matrix-transpose', methods=['GET'])
def get_matrix_transpose_quiz():
    """Return matrix transpose quiz questions"""
    questions = generate_questions("matrix-transpose")
    return jsonify({"questions": questions})

@app.route('/api/quiz/matrix-determinant', methods=['GET'])
def get_matrix_determinant_quiz():
    """Return matrix determinant quiz questions"""
    questions = generate_questions("matrix-determinant")
    return jsonify({"questions": questions})

@app.route('/api/quiz/matrix-inverse', methods=['GET'])
def get_matrix_inverse_quiz():
    """Return matrix inverse quiz questions"""
    questions = generate_questions("matrix-inverse")
    return jsonify({"questions": questions})

@app.route('/api/quiz/eigenvalues-eigenvectors', methods=['GET'])
def get_eigenvalues_eigenvectors_quiz():
    """Return eigenvalues and eigenvectors quiz questions"""
    questions = generate_questions("eigenvalues-eigenvectors")
    return jsonify({"questions": questions})

@app.route('/api/quiz/vector-projection', methods=['GET'])
def get_vector_projection_quiz():
    """Return vector projection quiz questions"""
    questions = generate_questions("vector-projection")
    return jsonify({"questions": questions})

@app.route('/api/quiz/linear-independence', methods=['GET'])
def get_linear_independence_quiz():
    """Return linear independence quiz questions"""
    questions = generate_questions("linear-independence")
    return jsonify({"questions": questions})

@app.route('/api/quiz/basis-vectors', methods=['GET'])
def get_basis_vectors_quiz():
    """Return basis vectors quiz questions"""
    questions = generate_questions("basis-vectors")
    return jsonify({"questions": questions})

@app.route('/api/quiz/linear-transformations', methods=['GET'])
def get_linear_transformations_quiz():
    """Return linear transformations quiz questions"""
    questions = generate_questions("linear-transformations")
    return jsonify({"questions": questions})

@app.route('/api/quiz/orthogonality', methods=['GET'])
def get_orthogonality_quiz():
    """Return orthogonality quiz questions"""
    questions = generate_questions("orthogonality")
    return jsonify({"questions": questions})

@app.route('/api/quiz/matrix-rank', methods=['GET'])
def get_matrix_rank_quiz():
    """Return matrix rank quiz questions"""
    questions = generate_questions("matrix-rank")
    return jsonify({"questions": questions})

@app.route('/api/quiz/null-space', methods=['GET'])
def get_null_space_quiz():
    """Return null space quiz questions"""
    questions = generate_questions("null-space")
    return jsonify({"questions": questions})

@app.route('/api/quiz/systems-linear-equations', methods=['GET'])
def get_systems_linear_equations_quiz():
    """Return systems of linear equations quiz questions"""
    questions = generate_questions("systems-linear-equations")
    return jsonify({"questions": questions})

@app.route('/api/quiz/gaussian-elimination', methods=['GET'])
def get_gaussian_elimination_quiz():
    """Return Gaussian elimination quiz questions"""
    questions = generate_questions("gaussian-elimination")
    return jsonify({"questions": questions})

@app.route('/api/quiz/row-echelon-form', methods=['GET'])
def get_row_echelon_form_quiz():
    """Return row echelon form quiz questions"""
    questions = generate_questions("row-echelon-form")
    return jsonify({"questions": questions})

@app.route('/api/quiz/matrix-trace', methods=['GET'])
def get_matrix_trace_quiz():
    """Return matrix trace quiz questions"""
    questions = generate_questions("matrix-trace")
    return jsonify({"questions": questions})

@app.route('/api/quiz/gram-schmidt', methods=['GET'])
def get_gram_schmidt_quiz():
    """Return Gram-Schmidt process quiz questions"""
    questions = generate_questions("gram-schmidt")
    return jsonify({"questions": questions})

@app.route('/api/quiz/diagonalization', methods=['GET'])
def get_diagonalization_quiz():
    """Return diagonalization quiz questions"""
    questions = generate_questions("diagonalization")
    return jsonify({"questions": questions})

@app.route('/api/quiz/column-row-space', methods=['GET'])
def get_column_row_space_quiz():
    """Return column and row space quiz questions"""
    questions = generate_questions("column-row-space")
    return jsonify({"questions": questions})

@app.route('/api/quiz/lu-decomposition', methods=['GET'])
def get_lu_decomposition_quiz():
    """Return LU decomposition quiz questions"""
    questions = generate_questions("lu-decomposition")
    return jsonify({"questions": questions})

@app.route('/api/quiz/least-squares', methods=['GET'])
def get_least_squares_quiz():
    """Return least squares approximation quiz questions"""
    questions = generate_questions("least-squares")
    return jsonify({"questions": questions})

@app.route('/api/quiz/change-of-basis', methods=['GET'])
def get_change_of_basis_quiz():
    """Return change of basis quiz questions"""
    questions = generate_questions("change-of-basis")
    return jsonify({"questions": questions})


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("LinearLeap API Server starting...")
    print(f"Gemini API: {'Enabled' if GEMINI_ENABLED else 'Disabled (using fallback questions)'}")
    print("\nAvailable Quiz Endpoints:")
    print("  • Matrix Multiplication: http://localhost:5000/api/quiz/matrix")
    print("  • Vectors: http://localhost:5000/api/quiz/vectors")
    print("  • Identity Matrix: http://localhost:5000/api/quiz/identity-matrix")
    print("  • Dot Product: http://localhost:5000/api/quiz/dot-product")
    print("  • Vector Magnitude: http://localhost:5000/api/quiz/vector-magnitude")
    print("  • Vector Addition: http://localhost:5000/api/quiz/vector-addition")
    print("  • Cross Product: http://localhost:5000/api/quiz/cross-product")
    print("  • Matrix Transpose: http://localhost:5000/api/quiz/matrix-transpose")
    print("  • Matrix Determinant: http://localhost:5000/api/quiz/matrix-determinant")
    print("  • Matrix Inverse: http://localhost:5000/api/quiz/matrix-inverse")
    print("  • Eigenvalues & Eigenvectors: http://localhost:5000/api/quiz/eigenvalues-eigenvectors")
    print("  • Vector Projection: http://localhost:5000/api/quiz/vector-projection")
    print("  • Linear Independence: http://localhost:5000/api/quiz/linear-independence")
    print("  • Basis Vectors: http://localhost:5000/api/quiz/basis-vectors")
    print("  • Linear Transformations: http://localhost:5000/api/quiz/linear-transformations")
    print("  • Orthogonality: http://localhost:5000/api/quiz/orthogonality")
    print("  • Matrix Rank: http://localhost:5000/api/quiz/matrix-rank")
    print("  • Null Space: http://localhost:5000/api/quiz/null-space")
    print("  • Systems of Linear Equations: http://localhost:5000/api/quiz/systems-linear-equations")
    print("  • Gaussian Elimination: http://localhost:5000/api/quiz/gaussian-elimination")
    print("  • Row Echelon Form: http://localhost:5000/api/quiz/row-echelon-form")
    print("  • Matrix Trace: http://localhost:5000/api/quiz/matrix-trace")
    print("  • Gram-Schmidt Process: http://localhost:5000/api/quiz/gram-schmidt")
    print("  • Diagonalization: http://localhost:5000/api/quiz/diagonalization")
    print("  • Column & Row Space: http://localhost:5000/api/quiz/column-row-space")
    print("  • LU Decomposition: http://localhost:5000/api/quiz/lu-decomposition")
    print("  • Least Squares: http://localhost:5000/api/quiz/least-squares")
    print("  • Change of Basis: http://localhost:5000/api/quiz/change-of-basis")
    app.run(debug=True, port=5000)

