import json
import random
import os

def generate_matrix_questions(count=1000):
    """Generate matrix multiplication questions"""
    questions = []
    
    for i in range(count):
        if i % 2 == 0:  # MCQ
            # Generate random 2x2 matrices
            if i < 400:  # 2x2 matrices
                a11, a12 = random.randint(1, 9), random.randint(1, 9)
                a21, a22 = random.randint(1, 9), random.randint(1, 9)
                b11, b12 = random.randint(1, 9), random.randint(1, 9)
                b21, b22 = random.randint(1, 9), random.randint(1, 9)
                
                # Calculate correct answer
                c11 = a11 * b11 + a12 * b21
                c12 = a11 * b12 + a12 * b22
                c21 = a21 * b11 + a22 * b21
                c22 = a21 * b12 + a22 * b22
                
                correct = f"\\\\(\\\\begin{{bmatrix}}{c11} & {c12}\\{c21} & {c22}\\\\end{{bmatrix}}\\\\)"
                
                # Generate wrong options
                options = [correct]
                for _ in range(3):
                    w11 = c11 + random.randint(-3, 3)
                    w12 = c12 + random.randint(-3, 3)
                    w21 = c21 + random.randint(-3, 3)
                    w22 = c22 + random.randint(-3, 3)
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{w11} & {w12}\\{w21} & {w22}\\\\end{{bmatrix}}\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                while len(options) < 4:
                    w11 = c11 + random.randint(-5, 5)
                    w12 = c12 + random.randint(-5, 5)
                    w21 = c21 + random.randint(-5, 5)
                    w22 = c22 + random.randint(-5, 5)
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{w11} & {w12}\\{w21} & {w22}\\\\end{{bmatrix}}\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is \\\\(A \\\\times B\\\\) where \\\\(A = \\\\begin{{bmatrix}}{a11} & {a12}\\{a21} & {a22}\\\\end{{bmatrix}}\\\\) and \\\\(B = \\\\begin{{bmatrix}}{b11} & {b12}\\{b21} & {b22}\\\\end{{bmatrix}}\\\\)?",
                    "options": options,
                    "answer": correct
                })
            else:  # 3x3 matrices
                # Generate random 3x3 matrices
                A = [[random.randint(0, 5) for _ in range(3)] for _ in range(3)]
                B = [[random.randint(0, 5) for _ in range(3)] for _ in range(3)]
                
                # Calculate product
                C = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
                
                a_str = f"\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\end{{bmatrix}}"
                b_str = f"\\\\begin{{bmatrix}}{B[0][0]} & {B[0][1]} & {B[0][2]}\\{B[1][0]} & {B[1][1]} & {B[1][2]}\\{B[2][0]} & {B[2][1]} & {B[2][2]}\\\\end{{bmatrix}}"
                correct = f"\\\\(\\\\begin{{bmatrix}}{C[0][0]} & {C[0][1]} & {C[0][2]}\\{C[1][0]} & {C[1][1]} & {C[1][2]}\\{C[2][0]} & {C[2][1]} & {C[2][2]}\\\\end{{bmatrix}}\\\\)"
                
                # Generate wrong options
                options = [correct]
                for _ in range(3):
                    W = [[C[i][j] + random.randint(-3, 3) for j in range(3)] for i in range(3)]
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]} & {W[0][2]}\\{W[1][0]} & {W[1][1]} & {W[1][2]}\\{W[2][0]} & {W[2][1]} & {W[2][2]}\\\\end{{bmatrix}}\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                while len(options) < 4:
                    W = [[C[i][j] + random.randint(-5, 5) for j in range(3)] for i in range(3)]
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]} & {W[0][2]}\\{W[1][0]} & {W[1][1]} & {W[1][2]}\\{W[2][0]} & {W[2][1]} & {W[2][2]}\\\\end{{bmatrix}}\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is \\\\(A \\\\times B\\\\) where \\\\(A = {a_str}\\\\) and \\\\(B = {b_str}\\\\)?",
                    "options": options,
                    "answer": correct
                })
        else:  # FIB
            if i < 500:
                # 2x2 matrix multiplication FIB
                a11, a12 = random.randint(1, 9), random.randint(0, 9)
                a21, a22 = random.randint(0, 9), random.randint(1, 9)
                b11, b12 = random.randint(1, 9), random.randint(0, 9)
                b21, b22 = random.randint(0, 9), random.randint(1, 9)
                
                c11 = a11 * b11 + a12 * b21
                c12 = a11 * b12 + a12 * b22
                c21 = a21 * b11 + a22 * b21
                c22 = a21 * b12 + a22 * b22
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is \\\\(A \\\\times B\\\\) where \\\\(A = \\\\begin{{bmatrix}}{a11} & {a12}\\{a21} & {a22}\\\\end{{bmatrix}}\\\\) and \\\\(B = \\\\begin{{bmatrix}}{b11} & {b12}\\{b21} & {b22}\\\\end{{bmatrix}}\\\\)?",
                    "answer": f"\\\\(\\\\begin{{bmatrix}}{c11} & {c12}\\{c21} & {c22}\\\\end{{bmatrix}}\\\\)"
                })
            else:
                # 3x3 matrix multiplication FIB
                A = [[random.randint(0, 4) for _ in range(3)] for _ in range(3)]
                B = [[random.randint(0, 4) for _ in range(3)] for _ in range(3)]
                
                C = [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
                
                a_str = f"\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\end{{bmatrix}}"
                b_str = f"\\\\begin{{bmatrix}}{B[0][0]} & {B[0][1]} & {B[0][2]}\\{B[1][0]} & {B[1][1]} & {B[1][2]}\\{B[2][0]} & {B[2][1]} & {B[2][2]}\\\\end{{bmatrix}}"
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is \\\\(A \\\\times B\\\\) where \\\\(A = {a_str}\\\\) and \\\\(B = {b_str}\\\\)?",
                    "answer": f"\\\\(\\\\begin{{bmatrix}}{C[0][0]} & {C[0][1]} & {C[0][2]}\\{C[1][0]} & {C[1][1]} & {C[1][2]}\\{C[2][0]} & {C[2][1]} & {C[2][2]}\\\\end{{bmatrix}}\\\\)"
                })
    
    return questions

def generate_vector_questions(count=1000):
    """Generate general vector questions"""
    questions = []
    
    for i in range(count):
        topic_choice = i % 4
        
        if i % 2 == 0:  # MCQ
            if topic_choice == 0:  # Dot product
                x1, y1 = random.randint(1, 10), random.randint(1, 10)
                x2, y2 = random.randint(1, 10), random.randint(1, 10)
                correct_ans = x1 * x2 + y1 * y2
                
                options = [f"\\\\({correct_ans}\\\\)"]
                for _ in range(3):
                    wrong = correct_ans + random.randint(-10, 10)
                    if wrong != correct_ans and f"\\\\({wrong}\\\\)" not in options:
                        options.append(f"\\\\({wrong}\\\\)")
                
                while len(options) < 4:
                    wrong = correct_ans + random.randint(-15, 15)
                    if f"\\\\({wrong}\\\\)" not in options:
                        options.append(f"\\\\({wrong}\\\\)")
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the dot product of vectors \\\\(\\\\vec{{u}} = ({x1}, {y1})\\\\) and \\\\(\\\\vec{{v}} = ({x2}, {y2})\\\\)?",
                    "options": options,
                    "answer": f"\\\\({correct_ans}\\\\)"
                })
            elif topic_choice == 1:  # Vector magnitude
                import math
                x, y = random.randint(1, 12), random.randint(1, 12)
                mag = math.sqrt(x**2 + y**2)
                is_int = mag == int(mag)
                
                if is_int:
                    correct_ans = int(mag)
                    options = [f"\\\\({correct_ans}\\\\)"]
                    for off in [-2, -1, 1, 2]:
                        if correct_ans + off > 0:
                            options.append(f"\\\\({correct_ans + off}\\\\)")
                    options = options[:4]
                else:
                    correct_ans = round(mag, 2)
                    options = [f"\\\\({correct_ans:.2f}\\\\)"]
                    for _ in range(3):
                        wrong = correct_ans + random.uniform(-2, 2)
                        options.append(f"\\\\({wrong:.2f}\\\\)")
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the magnitude of vector \\\\(\\\\vec{{v}} = ({x}, {y})\\\\)?",
                    "options": options,
                    "answer": options[0] if is_int else f"\\\\({correct_ans:.2f}\\\\)"
                })
            elif topic_choice == 2:  # Vector addition
                x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
                x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
                rx, ry = x1 + x2, y1 + y2
                
                correct = f"\\\\(({rx}, {ry})\\\\)"
                options = [correct]
                
                for _ in range(3):
                    wx = rx + random.randint(-5, 5)
                    wy = ry + random.randint(-5, 5)
                    wrong = f"\\\\(({wx}, {wy})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                while len(options) < 4:
                    wx = rx + random.randint(-8, 8)
                    wy = ry + random.randint(-8, 8)
                    wrong = f"\\\\(({wx}, {wy})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is \\\\(({x1}, {y1}) + ({x2}, {y2})\\\\)?",
                    "options": options,
                    "answer": correct
                })
            else:  # Cross product concept
                questions.append({
                    "type": "MCQ",
                    "question": "Which of the following is \\\\(\\\\vec{i} \\\\times \\\\vec{j}\\\\)?",
                    "options": ["\\\\(\\\\vec{k}\\\\)", "\\\\(-\\\\vec{k}\\\\)", "\\\\(0\\\\)", "\\\\(\\\\vec{i} + \\\\vec{j}\\\\)"],
                    "answer": "\\\\(\\\\vec{k}\\\\)"
                })
        else:  # FIB
            if topic_choice == 0:  # Dot product FIB
                x1, y1, z1 = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
                x2, y2, z2 = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
                result = x1*x2 + y1*y2 + z1*z2
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is \\\\(({x1}, {y1}, {z1}) \\\\cdot ({x2}, {y2}, {z2})\\\\)?",
                    "answer": str(result)
                })
            elif topic_choice == 1:  # Magnitude FIB
                import math
                x, y = random.randint(0, 5), random.randint(0, 12)
                mag = math.sqrt(x**2 + y**2)
                
                if mag == int(mag):
                    questions.append({
                        "type": "FIB",
                        "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({x}, {y})\\\\)?",
                        "answer": str(int(mag))
                    })
                else:
                    questions.append({
                        "type": "FIB",
                        "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({x}, {y})\\\\)? (Round to 2 decimal places)",
                        "answer": f"{mag:.2f}"
                    })
            elif topic_choice == 2:  # Addition FIB
                x1, y1, z1 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
                x2, y2, z2 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is \\\\(({x1}, {y1}, {z1}) + ({x2}, {y2}, {z2})\\\\)?",
                    "answer": f"({x1+x2}, {y1+y2}, {z1+z2})"
                })
            else:  # Perpendicularity
                questions.append({
                    "type": "FIB",
                    "question": "What is the angle (in degrees) between vectors \\\\(\\\\vec{u} = (1, 0)\\\\) and \\\\(\\\\vec{v} = (0, 1)\\\\)?",
                    "answer": "90"
                })
    
    return questions

def generate_identity_matrix_questions(count=1000):
    """Generate identity matrix questions"""
    questions = []
    
    conceptual_mcqs = [
        {
            "question": "What is the result of multiplying any matrix \\\\(A\\\\) by the identity matrix \\\\(I\\\\)?",
            "options": ["\\\\(0\\\\)", "\\\\(A\\\\)", "\\\\(I\\\\)", "\\\\(2A\\\\)"],
            "answer": "\\\\(A\\\\)"
        },
        {
            "question": "What are the values on the main diagonal of an identity matrix?",
            "options": ["\\\\(0\\\\)", "\\\\(1\\\\)", "\\\\(-1\\\\)", "\\\\(n\\\\)"],
            "answer": "\\\\(1\\\\)"
        },
        {
            "question": "Which property does the identity matrix have?",
            "options": ["\\\\(AI = IA = A\\\\)", "\\\\(AI = 0\\\\)", "\\\\(AI \\\\neq IA\\\\)", "\\\\(AI = I\\\\)"],
            "answer": "\\\\(AI = IA = A\\\\)"
        },
        {
            "question": "What are all off-diagonal elements in an identity matrix?",
            "options": ["\\\\(0\\\\)", "\\\\(1\\\\)", "\\\\(-1\\\\)", "Variable"],
            "answer": "\\\\(0\\\\)"
        }
    ]
    
    for i in range(count):
        if i % 3 == 0:  # Conceptual MCQ
            q = random.choice(conceptual_mcqs)
            questions.append({
                "type": "MCQ",
                "question": q["question"],
                "options": q["options"],
                "answer": q["answer"]
            })
        elif i % 3 == 1:  # Computational MCQ
            size = random.choice([2, 3])
            A = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]
            
            if size == 2:
                a_str = f"\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]}\\{A[1][0]} & {A[1][1]}\\\\end{{bmatrix}}"
                correct = f"\\\\(\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]}\\{A[1][0]} & {A[1][1]}\\\\end{{bmatrix}}\\\\)"
            else:
                a_str = f"\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\end{{bmatrix}}"
                correct = f"\\\\(\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\end{{bmatrix}}\\\\)"
            
            options = [correct]
            for _ in range(3):
                if size == 2:
                    W = [[A[i][j] + random.randint(-3, 3) for j in range(size)] for i in range(size)]
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]}\\{W[1][0]} & {W[1][1]}\\\\end{{bmatrix}}\\\\)"
                else:
                    W = [[A[i][j] + random.randint(-3, 3) for j in range(size)] for i in range(size)]
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]} & {W[0][2]}\\{W[1][0]} & {W[1][1]} & {W[1][2]}\\{W[2][0]} & {W[2][1]} & {W[2][2]}\\\\end{{bmatrix}}\\\\)"
                
                if wrong not in options:
                    options.append(wrong)
            
            while len(options) < 4:
                if size == 2:
                    W = [[A[i][j] + random.randint(-5, 5) for j in range(size)] for i in range(size)]
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]}\\{W[1][0]} & {W[1][1]}\\\\end{{bmatrix}}\\\\)"
                else:
                    W = [[A[i][j] + random.randint(-5, 5) for j in range(size)] for i in range(size)]
                    wrong = f"\\\\(\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]} & {W[0][2]}\\{W[1][0]} & {W[1][1]} & {W[1][2]}\\{W[2][0]} & {W[2][1]} & {W[2][2]}\\\\end{{bmatrix}}\\\\)"
                
                if wrong not in options:
                    options.append(wrong)
            
            random.shuffle(options)
            
            i_str = "\\\\begin{bmatrix}1 & 0\\0 & 1\\\\end{bmatrix}" if size == 2 else "\\\\begin{bmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\\\\end{bmatrix}"
            
            questions.append({
                "type": "MCQ",
                "question": f"What is \\\\({a_str} \\\\times {i_str}\\\\)?",
                "options": options,
                "answer": correct
            })
        else:  # FIB
            size = random.choice([2, 3])
            
            if size == 2:
                answer = "\\\\(\\\\begin{bmatrix}1 & 0\\0 & 1\\\\end{bmatrix}\\\\)"
                questions.append({
                    "type": "FIB",
                    "question": "What is the 2×2 identity matrix \\\\(I_2\\\\)?",
                    "answer": answer
                })
            else:
                answer = "\\\\(\\\\begin{bmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\\\\end{bmatrix}\\\\)"
                questions.append({
                    "type": "FIB",
                    "question": "What is the 3×3 identity matrix \\\\(I_3\\\\)?",
                    "answer": answer
                })
    
    return questions

def generate_dot_product_questions(count=1000):
    """Generate dot product questions"""
    questions = []
    
    for i in range(count):
        if i % 2 == 0:  # MCQ
            dim = 2 if i < 500 else 3
            
            if dim == 2:
                x1, y1 = random.randint(1, 10), random.randint(1, 10)
                x2, y2 = random.randint(1, 10), random.randint(1, 10)
                correct_ans = x1 * x2 + y1 * y2
                
                options = [f"\\\\({correct_ans}\\\\)"]
                for _ in range(3):
                    wrong = correct_ans + random.randint(-10, 10)
                    if wrong != correct_ans and f"\\\\({wrong}\\\\)" not in options:
                        options.append(f"\\\\({wrong}\\\\)")
                
                while len(options) < 4:
                    wrong = correct_ans + random.randint(-15, 15)
                    if f"\\\\({wrong}\\\\)" not in options:
                        options.append(f"\\\\({wrong}\\\\)")
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the dot product of \\\\(\\\\vec{{u}} = ({x1}, {y1})\\\\) and \\\\(\\\\vec{{v}} = ({x2}, {y2})\\\\)?",
                    "options": options,
                    "answer": f"\\\\({correct_ans}\\\\)"
                })
            else:
                x1, y1, z1 = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
                x2, y2, z2 = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
                correct_ans = x1 * x2 + y1 * y2 + z1 * z2
                
                options = [f"\\\\({correct_ans}\\\\)"]
                for _ in range(3):
                    wrong = correct_ans + random.randint(-10, 10)
                    if wrong != correct_ans and f"\\\\({wrong}\\\\)" not in options:
                        options.append(f"\\\\({wrong}\\\\)")
                
                while len(options) < 4:
                    wrong = correct_ans + random.randint(-15, 15)
                    if f"\\\\({wrong}\\\\)" not in options:
                        options.append(f"\\\\({wrong}\\\\)")
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is \\\\(({x1}, {y1}, {z1}) \\\\cdot ({x2}, {y2}, {z2})\\\\)?",
                    "options": options,
                    "answer": f"\\\\({correct_ans}\\\\)"
                })
        else:  # FIB
            if i % 4 == 1:  # Perpendicular vectors (dot product = 0)
                if random.random() < 0.5:
                    questions.append({
                        "type": "FIB",
                        "question": "What is \\\\((1, 0) \\\\cdot (0, 1)\\\\)?",
                        "answer": "0"
                    })
                else:
                    a = random.randint(1, 9)
                    b = random.randint(1, 9)
                    questions.append({
                        "type": "FIB",
                        "question": f"What is \\\\(({a}, 0) \\\\cdot (0, {b})\\\\)?",
                        "answer": "0"
                    })
            else:  # Regular computation
                dim = 2 if i < 500 else 3
                
                if dim == 2:
                    x1, y1 = random.randint(1, 10), random.randint(1, 10)
                    x2, y2 = random.randint(1, 10), random.randint(1, 10)
                    result = x1 * x2 + y1 * y2
                    
                    questions.append({
                        "type": "FIB",
                        "question": f"What is \\\\(({x1}, {y1}) \\\\cdot ({x2}, {y2})\\\\)?",
                        "answer": str(result)
                    })
                else:
                    x1, y1, z1 = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
                    x2, y2, z2 = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
                    result = x1 * x2 + y1 * y2 + z1 * z2
                    
                    questions.append({
                        "type": "FIB",
                        "question": f"What is \\\\(({x1}, {y1}, {z1}) \\\\cdot ({x2}, {y2}, {z2})\\\\)?",
                        "answer": str(result)
                    })
    
    return questions

def generate_vector_magnitude_questions(count=1000):
    """Generate vector magnitude questions"""
    import math
    questions = []
    
    # Pythagorean triples for exact answers
    triples_2d = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10)]
    triples_3d = [(2, 3, 4), (1, 2, 2), (2, 6, 9)]
    
    for i in range(count):
        if i % 2 == 0:  # MCQ
            if i < 400:  # Use Pythagorean triples for clean answers
                triple = random.choice(triples_2d)
                x, y, mag = triple[0], triple[1], triple[2]
                
                options = [f"\\\\({mag}\\\\)"]
                for off in [-2, -1, 1, 2, 3]:
                    if mag + off > 0 and f"\\\\({mag + off}\\\\)" not in options:
                        options.append(f"\\\\({mag + off}\\\\)")
                
                options = options[:4]
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({x}, {y})\\\\)?",
                    "options": options,
                    "answer": f"\\\\({mag}\\\\)"
                })
            else:  # General cases
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                mag = math.sqrt(x**2 + y**2)
                
                if mag == int(mag):
                    correct = int(mag)
                    options = [f"\\\\({correct}\\\\)"]
                    for off in [- 2, -1, 1, 2]:
                        if correct + off > 0:
                            options.append(f"\\\\({correct + off}\\\\)")
                    options = options[:4]
                else:
                    correct = round(mag, 2)
                    options = [f"\\\\({correct:.2f}\\\\)"]
                    for _ in range(3):
                        wrong = round(correct + random.uniform(-2, 2), 2)
                        if wrong > 0:
                            options.append(f"\\\\({wrong:.2f}\\\\)")
                    options = options[:4]
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({x}, {y})\\\\)?",
                    "options": options,
                    "answer": options[0]
                })
        else:  # FIB
            if i % 4 == 1:  # Pythagorean triple
                triple = random.choice(triples_2d)
                questions.append({
                    "type": "FIB",
                    "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({triple[0]}, {triple[1]})\\\\)?",
                    "answer": str(triple[2])
                })
            elif i % 4 == 3:  # 3D vector
                if i < 500:
                    triple = random.choice(triples_3d)
                    mag = math.sqrt(triple[0]**2 + triple[1]**2 + triple[2]**2)
                    if mag == int(mag):
                        questions.append({
                            "type": "FIB",
                            "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({triple[0]}, {triple[1]}, {triple[2]})\\\\)?",
                            "answer": str(int(mag))
                        })
                    else:
                        questions.append({
                            "type": "FIB",
                            "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({triple[0]}, {triple[1]}, {triple[2]})\\\\)? (Round to 2 decimal places)",
                            "answer": f"{mag:.2f}"
                        })
                else:
                    x, y, z = random.randint(1, 8), random.randint(1, 8), random.randint(1, 8)
                    mag = math.sqrt(x**2 + y**2 + z**2)
                    questions.append({
                        "type": "FIB",
                        "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({x}, {y}, {z})\\\\)? (Round to 2 decimal places)",
                        "answer": f"{mag:.2f}"
                    })
            else:  # Simple cases
                if random.random() < 0.3:
                    val = random.randint(1, 12)
                    if random.random() < 0.5:
                        questions.append({
                            "type": "FIB",
                            "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({val}, 0)\\\\)?",
                            "answer": str(val)
                        })
                    else:
                        questions.append({
                            "type": "FIB",
                            "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = (0, {val})\\\\)?",
                            "answer": str(val)
                        })
                else:
                    x, y = random.randint(1, 9), random.randint(1, 9)
                    mag = math.sqrt(x**2 + y**2)
                    if mag == int(mag):
                        questions.append({
                            "type": "FIB",
                            "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({x}, {y})\\\\)?",
                            "answer": str(int(mag))
                        })
                    else:
                        questions.append({
                            "type": "FIB",
                            "question": f"What is the magnitude of \\\\(\\\\vec{{v}} = ({x}, {y})\\\\)? (Round to 2 decimal places)",
                            "answer": f"{mag:.2f}"
                        })
    
    return questions

def generate_vector_addition_questions(count=1000):
    """Generate vector addition and subtraction questions"""
    questions = []
    
    for i in range(count):
        operation = "addition" if i < 500 else "subtraction"
        dim = 2 if i % 3 != 0 else 3
        
        if i % 2 == 0:  # MCQ
            if dim == 2:
                x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
                x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
                
                if operation == "addition":
                    rx, ry = x1 + x2, y1 + y2
                    op_symbol = "+"
                else:
                    rx, ry = x1 - x2, y1 - y2
                    op_symbol = "-"
                
                correct = f"\\\\(({rx}, {ry})\\\\)"
                options = [correct]
                
                for _ in range(3):
                    wx = rx + random.randint(-5, 5)
                    wy = ry + random.randint(-5, 5)
                    wrong = f"\\\\(({wx}, {wy})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                while len(options) < 4:
                    wx = rx + random.randint(-8, 8)
                    wy = ry + random.randint(-8, 8)
                    wrong = f"\\\\(({wx}, {wy})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is \\\\(({x1}, {y1}) {op_symbol} ({x2}, {y2})\\\\)?",
                    "options": options,
                    "answer": correct
                })
            else:  # 3D
                x1, y1, z1 = random.randint(-8, 8), random.randint(-8, 8), random.randint(-8, 8)
                x2, y2, z2 = random.randint(-8, 8), random.randint(-8, 8), random.randint(-8, 8)
                
                if operation == "addition":
                    rx, ry, rz = x1 + x2, y1 + y2, z1 + z2
                    op_symbol = "+"
                else:
                    rx, ry, rz = x1 - x2, y1 - y2, z1 - z2
                    op_symbol = "-"
                
                correct = f"\\\\(({rx}, {ry}, {rz})\\\\)"
                options = [correct]
                
                for _ in range(3):
                    wx = rx + random.randint(-4, 4)
                    wy = ry + random.randint(-4, 4)
                    wz = rz + random.randint(-4, 4)
                    wrong = f"\\\\(({wx}, {wy}, {wz})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                while len(options) < 4:
                    wx = rx + random.randint(-6, 6)
                    wy = ry + random.randint(-6, 6)
                    wz = rz + random.randint(-6, 6)
                    wrong = f"\\\\(({wx}, {wy}, {wz})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is \\\\(({x1}, {y1}, {z1}) {op_symbol} ({x2}, {y2}, {z2})\\\\)?",
                    "options": options,
                    "answer": correct
                })
        else:  # FIB
            if dim == 2:
                x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
                x2, y2 = random.randint(-10, 10), random.randint(-10, 10)
                
                if operation == "addition":
                    result = f"({x1 + x2}, {y1 + y2})"
                    op_symbol = "+"
                else:
                    result = f"({x1 - x2}, {y1 - y2})"
                    op_symbol = "-"
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is \\\\(({x1}, {y1}) {op_symbol} ({x2}, {y2})\\\\)?",
                    "answer": result
                })
            else:  # 3D
                x1, y1, z1 = random.randint(-8, 8), random.randint(-8, 8), random.randint(-8, 8)
                x2, y2, z2 = random.randint(-8, 8), random.randint(-8, 8), random.randint(-8, 8)
                
                if operation == "addition":
                    result = f"({x1 + x2}, {y1 + y2}, {z1 + z2})"
                    op_symbol = "+"
                else:
                    result = f"({x1 - x2}, {y1 - y2}, {z1 - z2})"
                    op_symbol = "-"
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is \\\\(({x1}, {y1}, {z1}) {op_symbol} ({x2}, {y2}, {z2})\\\\)?",
                    "answer": result
                })
    
    return questions

def generate_cross_product_questions(count=1000):
    """Generate cross product questions"""
    questions = []
    
    conceptual_questions = [
        {
            "type": "MCQ",
            "question": "What is \\\\(\\\\vec{i} \\\\times \\\\vec{j}\\\\)?",
            "options": ["\\\\(\\\\vec{k}\\\\)", "\\\\(-\\\\vec{k}\\\\)", "\\\\(\\\\vec{i}\\\\)", "\\\\(0\\\\)"],
            "answer": "\\\\(\\\\vec{k}\\\\)"
        },
        {
            "type": "MCQ",
            "question": "What is \\\\(\\\\vec{j} \\\\times \\\\vec{k}\\\\)?",
            "options": ["\\\\(\\\\vec{i}\\\\)", "\\\\(-\\\\vec{i}\\\\)", "\\\\(\\\\vec{j}\\\\)", "\\\\(0\\\\)"],
            "answer": "\\\\(\\\\vec{i}\\\\)"
        },
        {
            "type": "MCQ",
            "question": "What is \\\\(\\\\vec{k} \\\\times \\\\vec{i}\\\\)?",
            "options": ["\\\\(\\\\vec{j}\\\\)", "\\\\(-\\\\vec{j}\\\\)", "\\\\(\\\\vec{k}\\\\)", "\\\\(0\\\\)"],
            "answer": "\\\\(\\\\vec{j}\\\\)"
        },
        {
            "type": "MCQ",
            "question": "The cross product of two vectors produces:",
            "options": ["A vector perpendicular to both", "A scalar", "A parallel vector", "The zero vector always"],
            "answer": "A vector perpendicular to both"
        },
        {
            "type": "MCQ",
            "question": "Which property does the cross product have?",
            "options": ["Anti-commutative: \\\\(\\\\vec{u} \\\\times \\\\vec{v} = -(\\\\vec{v} \\\\times \\\\vec{u})\\\\)", "Commutative", "\\\\(\\\\vec{u} \\\\times \\\\vec{v} = \\\\vec{u} \\\\cdot \\\\vec{v}\\\\)", "Always zero"],
            "answer": "Anti-commutative: \\\\(\\\\vec{u} \\\\times \\\\vec{v} = -(\\\\vec{v} \\\\times \\\\vec{u})\\\\)"
        }
    ]
    
    for i in range(count):
        if i % 3 == 0:  # Conceptual question
            q = random.choice(conceptual_questions)
            questions.append(q)
        elif i % 3 == 1:  # Unit vector cross products
            unit_pairs = [
                ("\\\\vec{i}", "\\\\vec{j}", "\\\\vec{k}"),
                ("\\\\vec{j}", "\\\\vec{i}", "-\\\\vec{k}"),
                ("\\\\vec{j}", "\\\\vec{k}", "\\\\vec{i}"),
                ("\\\\vec{k}", "\\\\vec{j}", "-\\\\vec{i}"),
                ("\\\\vec{k}", "\\\\vec{i}", "\\\\vec{j}"),
                ("\\\\vec{i}", "\\\\vec{k}", "-\\\\vec{j}")
            ]
            
            pair = random.choice(unit_pairs)
            questions.append({
                "type": "FIB",
                "question": f"What is \\\\({pair[0]} \\\\times {pair[1]}\\\\)?",
                "answer": f"\\\\({pair[2]}\\\\)"
            })
        else:  # Computational cross product
            # For 3D vectors (a1, a2, a3) × (b1, b2, b3) = (a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)
            a1, a2, a3 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
            b1, b2, b3 = random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)
            
            c1 = a2 * b3 - a3 * b2
            c2 = a3 * b1 - a1 * b3
            c3 = a1 * b2 - a2 * b1
            
            if i % 2 == 0:  # MCQ
                correct = f"\\\\(({c1}, {c2}, {c3})\\\\)"
                options = [correct]
                
                for _ in range(3):
                    w1 = c1 + random.randint(-5, 5)
                    w2 = c2 + random.randint(-5, 5)
                    w3 = c3 + random.randint(-5, 5)
                    wrong = f"\\\\(({w1}, {w2}, {w3})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                while len(options) < 4:
                    w1 = c1 + random.randint(-8, 8)
                    w2 = c2 + random.randint(-8, 8)
                    w3 = c3 + random.randint(-8, 8)
                    wrong = f"\\\\(({w1}, {w2}, {w3})\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is \\\\(({a1}, {a2}, {a3}) \\\\times ({b1}, {b2}, {b3})\\\\)?",
                    "options": options,
                    "answer": correct
                })
            else:  # FIB
                questions.append({
                    "type": "FIB",
                    "question": f"What is \\\\(({a1}, {a2}, {a3}) \\\\times ({b1}, {b2}, {b3})\\\\)?",
                    "answer": f"({c1}, {c2}, {c3})"
                })
    
    return questions

def generate_matrix_transpose_questions(count=1000):
    """Generate matrix transpose questions"""
    questions = []
    
    for i in range(count):
        if i % 2 == 0:  # MCQ
            size = 2 if i < 500 else 3
            
            if size == 2:
                a11, a12 = random.randint(1, 9), random.randint(1, 9)
                a21, a22 = random.randint(1, 9), random.randint(1, 9)
                
                a_str = f"\\\\\\\\begin{{bmatrix}}{a11} & {a12}\\\\{a21} & {a22}\\\\\\\\end{{bmatrix}}"
                correct = f"\\\\\\\\(\\\\\\\\begin{{bmatrix}}{a11} & {a21}\\\\{a12} & {a22}\\\\\\\\end{{bmatrix}}\\\\\\\\)"
                
                options = [correct]
                W = [[a11, a12], [a21, a22]]
                for _ in range(3):
                    random.shuffle(W)
                    wrong = f"\\\\\\\\(\\\\\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]}\\\\{W[1][0]} & {W[1][1]}\\\\\\\\end{{bmatrix}}\\\\\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                while len(options) < 4:
                    w11 = random.randint(1, 9)
                    w12 = random.randint(1, 9)
                    w21 = random.randint(1, 9)
                    w22 = random.randint(1, 9)
                    wrong = f"\\\\\\\\(\\\\\\\\begin{{bmatrix}}{w11} & {w21}\\\\{w12} & {w22}\\\\\\\\end{{bmatrix}}\\\\\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the transpose of \\\\\\\\({a_str}\\\\\\\\)?",
                    "options": options,
                    "answer": correct
                })
            else:
                A = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
                a_str = f"\\\\\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\\\\\end{{bmatrix}}"
                correct = f"\\\\\\\\(\\\\\\\\begin{{bmatrix}}{A[0][0]} & {A[1][0]} & {A[2][0]}\\\\{A[0][1]} & {A[1][1]} & {A[2][1]}\\\\{A[0][2]} & {A[1][2]} & {A[2][2]}\\\\\\\\end{{bmatrix}}\\\\\\\\)"
                
                options = [correct]
                for _ in range(3):
                    W = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
                    wrong = f"\\\\\\\\(\\\\\\\\begin{{bmatrix}}{W[0][0]} & {W[0][1]} & {W[0][2]}\\\\{W[1][0]} & {W[1][1]} & {W[1][2]}\\\\{W[2][0]} & {W[2][1]} & {W[2][2]}\\\\\\\\end{{bmatrix}}\\\\\\\\)"
                    if wrong not in options:
                        options.append(wrong)
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the transpose of \\\\\\\\({a_str}\\\\\\\\)?",
                    "options": options,
                    "answer": correct
                })
        else:  # FIB
            size = 2 if i < 500 else 3
            
            if size == 2:
                a11, a12 = random.randint(1, 9), random.randint(1, 9)
                a21, a22 = random.randint(1, 9), random.randint(1, 9)
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is the transpose of \\\\\\\\(\\\\\\\\begin{{bmatrix}}{a11} & {a12}\\\\{a21} & {a22}\\\\\\\\end{{bmatrix}}\\\\\\\\)?",
                    "answer": f"\\\\\\\\(\\\\\\\\begin{{bmatrix}}{a11} & {a21}\\\\{a12} & {a22}\\\\\\\\end{{bmatrix}}\\\\\\\\)"
                })
            else:
                A = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
                
                questions.append({
                    "type": "FIB",
                    "question": f"What is the transpose of \\\\\\\\(\\\\\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\\\\\end{{bmatrix}}\\\\\\\\)?",
                    "answer": f"\\\\\\\\(\\\\\\\\begin{{bmatrix}}{A[0][0]} & {A[1][0]} & {A[2][0]}\\\\{A[0][1]} & {A[1][1]} & {A[2][1]}\\\\{A[0][2]} & {A[1][2]} & {A[2][2]}\\\\\\\\end{{bmatrix}}\\\\\\\\)"
                })
    
    return questions

def generate_matrix_determinant_questions(count=1000):
    """Generate matrix determinant questions"""
    questions = []
    
    for i in range(count):
        if i < 600:  # 2x2 determinants
            a, b = random.randint(1, 9), random.randint(1, 9)
            c, d = random.randint(1, 9), random.randint(1, 9)
            det = a * d - b * c
            
            if i % 2 == 0:  # MCQ
                correct = f"\\\\\\\\({det}\\\\\\\\)"
                options = [correct]
                for _ in range(3):
                    wrong = det + random.randint(-10, 10)
                    if f"\\\\\\\\({wrong}\\\\\\\\)" not in options:
                        options.append(f"\\\\\\\\({wrong}\\\\\\\\)")
                
                while len(options) < 4:
                    wrong = det + random.randint(-15, 15)
                    if f"\\\\\\\\({wrong}\\\\\\\\)" not in options:
                        options.append(f"\\\\\\\\({wrong}\\\\\\\\)")
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the determinant of \\\\\\\\(\\\\\\\\begin{{bmatrix}}{a} & {b}\\\\{c} & {d}\\\\\\\\end{{bmatrix}}\\\\\\\\)?",
                    "options": options,
                    "answer": correct
                })
            else:  # FIB
                questions.append({
                    "type": "FIB",
                    "question": f"What is the determinant of \\\\\\\\(\\\\\\\\begin{{bmatrix}}{a} & {b}\\\\{c} & {d}\\\\\\\\end{{bmatrix}}\\\\\\\\)?",
                    "answer": str(det)
                })
        else:  # 3x3 determinants
            A = [[random.randint(0, 5) for _ in range(3)] for _ in range(3)]
            det = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) -
                   A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0]) +
                   A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
            
            if i % 2 == 0:  # MCQ
                correct = f"\\\\\\\\({det}\\\\\\\\)"
                options = [correct]
                for _ in range(3):
                    wrong = det + random.randint(-10, 10)
                    if f"\\\\\\\\({wrong}\\\\\\\\)" not in options:
                        options.append(f"\\\\\\\\({wrong}\\\\\\\\)")
                
                while len(options) < 4:
                    wrong = det + random.randint(-15, 15)
                    if f"\\\\\\\\({wrong}\\\\\\\\)" not in options:
                        options.append(f"\\\\\\\\({wrong}\\\\\\\\)")
                
                random.shuffle(options)
                
                questions.append({
                    "type": "MCQ",
                    "question": f"What is the determinant of \\\\\\\\(\\\\\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\\\\\end{{bmatrix}}\\\\\\\\)?",
                    "options": options,
                    "answer": correct
                })
            else:  # FIB
                questions.append({
                    "type": "FIB",
                    "question": f"What is the determinant of \\\\\\\\(\\\\\\\\begin{{bmatrix}}{A[0][0]} & {A[0][1]} & {A[0][2]}\\\\{A[1][0]} & {A[1][1]} & {A[1][2]}\\\\{A[2][0]} & {A[2][1]} & {A[2][2]}\\\\\\\\end{{bmatrix}}\\\\\\\\)?",
                    "answer": str(det)
                })
    
    return questions

def generate_lu_decomposition_questions(count=1000):
    """Generate LU decomposition questions with variety"""
    questions = []
    
    conceptual = [
        {"type": "MCQ", "question": "LU decomposition expresses A as:", "options": ["\\(A = LU\\)", "\\(A = L + U\\)", "\\(A = L - U\\)", "\\(A = UL\\)"], "answer": "\\(A = LU\\)"},
        {"type": "MCQ", "question": "In LU decomposition, L is:", "options": ["Lower triangular", "Upper triangular", "Diagonal", "Symmetric"], "answer": "Lower triangular"},
        {"type": "MCQ", "question": "In LU decomposition, what are the diagonal elements of L typically?", "options": ["All 1s", "All 0s", "Variables", "Same as A"], "answer": "All 1s"},
        {"type": "FIB", "question": "If \\(A = LU\\), what type of matrix is U?", "answer": "Upper triangular"},
        {"type": "MCQ", "question": "LU decomposition is useful for:", "options": ["Solving systems efficiently", "Finding eigenvalues", "Matrix addition", "Vector cross products"], "answer": "Solving systems efficiently"}
    ]
    
    for i in range(count):
        if i % 5 < 2:  # 40% conceptual
            q = random.choice(conceptual)
            questions.append(q.copy())
        elif i % 3 == 0:  
            a, b, c = random.randint(2, 6), random.randint(1, 5), random.randint(1, 5)
            d = a * random.randint(2, 4) + b
            
            questions.append({
                "type": "MCQ" if i % 2 == 0 else "FIB",
                "question": f"For matrix \\(\\begin{{bmatrix}}{a} & {b}\\\\{c} & {d}\\end{{bmatrix}}\\), what is the (2,1) element of L?",
                "options": [f"\\({c}/{a}\\)", f"\\({c}\\)", f"\\({a}/{c}\\)", "\\(1\\)"] if i % 2 == 0 else None,
                "answer": f"\\({c}/{a}\\)"
            })
        else:
            props = [
                ("Can every matrix be LU decomposed?", "No", ["No", "Yes", "Only square", "Only symmetric"]),
                ("What does the U matrix represent?", "Upper triangular form", ["Upper triangular form", "Lower form", "Diagonal", "Identity"]),
                ("LU decomposition requires:", "Gaussian elimination", ["Gaussian elimination", "Eigenvalues", "Determinants only", "Transpose"]),
                ("The product LU gives:", "Original matrix A", ["Original matrix A", "Identity", "Zero matrix", "Transpose"])
            ]
            q_text, ans, opts = random.choice(props)
            
            if i % 2 == 0:
                random.shuffle(opts)
                questions.append({"type": "MCQ", "question": q_text, "options": opts, "answer": ans})
            else:
                questions.append({"type": "FIB", "question": q_text, "answer": ans})
    
    return questions

def generate_least_squares_questions(count=1000):
    """Generate least squares questions with variety"""
    questions = []
    
    conceptual = [
        {"type": "MCQ", "question": "The least squares solution minimizes:", "options": ["\\(||Ax - b||\\)", "\\(||x||\\)", "\\(||A||\\)", "\\(det(A)\\)"], "answer": "\\(||Ax - b||\\)"},
        {"type": "MCQ", "question": "The normal equation for least squares is:", "options": ["\\(A^T A x = A^T b\\)", "\\(Ax = b\\)", "\\(A^T x = b\\)", "\\(Ax = A^T b\\)"], "answer": "\\(A^T A x = A^T b\\)"},
        {"type": "MCQ", "question": "Least squares is used when:", "options": ["System has no exact solution", "System is underdetermined", "A is singular", "b = 0"], "answer": "System has no exact solution"},
        {"type": "FIB", "question": "In least squares, we minimize the norm of the _____.", "answer": "residual"},
        {"type": "MCQ", "question": "The least squares solution is the:", "options": ["Best approximation", "Exact solution", "Null space", "Eigenvalue"], "answer": "Best approximation"}
    ]
    
    for i in range(count):
        if i % 4 < 2:  # 50% conceptual
            q = random.choice(conceptual)
            questions.append(q.copy())
        elif i % 3 == 0:
            apps = [
                ("Least squares is commonly used in:", "Linear regression", ["Linear regression", "Matrix multiplication", "Cross products", "Determinants"]),
                ("The residual vector r is:", "\\(b - Ax\\)", ["\\(b - Ax\\)", "\\(Ax\\)", "\\(A^T b\\)", "\\(x - b\\)"]),
                ("For overdetermined systems, least squares finds:", "Closest solution", ["Closest solution", "Exact solution", "No solution", "Infinite solutions"]),
                ("The matrix \\(A^T A\\) is:", "Symmetric", ["Symmetric", "Skew-symmetric", "Upper triangular", "Lower triangular"])
            ]
            q_text, ans, opts = random.choice(apps)
            
            if i % 2 == 0:
                random.shuffle(opts)
                questions.append({"type": "MCQ", "question": q_text, "options": opts, "answer": ans})
            else:
                questions.append({"type": "FIB", "question": q_text, "answer": ans})
        else:
            a1, a2, a3 = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
            result = a1**2 + a2**2 + a3**2
            
            questions.append({
                "type": "MCQ",
                "question": f"For A = \\(\\begin{{bmatrix}}{a1}\\\\{a2}\\\\{a3}\\end{{bmatrix}}\\), what is \\(A^T A\\)?",
                "options": [f"\\({result}\\)", f"\\({a1 + a2 + a3}\\)", f"\\({a1 * a2 * a3}\\)", "\\(0\\)"],
                "answer": f"\\({result}\\)"
            })
    
    return questions

def generate_column_row_space_questions(count=1000):
    """Generate column and row space questions with variety"""
    questions = []
    
    conceptual = [
        {"type": "MCQ", "question": "The column space of A is spanned by:", "options": ["Columns of A", "Rows of A", "Diagonals of A", "Eigenvalues"], "answer": "Columns of A"},
        {"type": "MCQ", "question": "The row space of A is spanned by:", "options": ["Rows of A", "Columns of A", "Eigenvectors", "Null space"], "answer": "Rows of A"},
        {"type": "MCQ", "question": "The dimension of the column space equals:", "options": ["Rank of A", "Number of columns", "Number of rows", "Determinant"], "answer": "Rank of A"},
        {"type": "FIB", "question": "The row space and column space have the same _____.", "answer": "dimension"},
        {"type": "MCQ", "question": "If A is m×n with rank r, what is dim(col space)?", "options": ["r", "m", "n", "m+n"], "answer": "r"}
    ]
    
    for i in range(count):
        if i % 5 < 2:  # 40% conceptual
            q = random.choice(conceptual)
            questions.append(q.copy())
        elif i % 3 == 0:
            m, n, r = random.randint(3, 7), random.randint(3, 7), random.randint(2, 5)
            r = min(r, m, n)
            
            questions.append({
                "type": "MCQ" if i % 2 == 0 else "FIB",
                "question": f"If A is {m}×{n} with rank {r}, what is the dimension of the column space?",
                "options": [f"{r}", f"{m}", f"{n}", f"{m-r}"] if i % 2 == 0 else None,
                "answer": f"{r}"
            })
        else:
            rels = [
                ("Column space is also called:", "Range of A", ["Range of A", "Null space", "Domain", "Kernel"]),
                ("Row space equals column space of:", "\\(A^T\\)", ["\\(A^T\\)", "\\(A\\)", "\\(A^{-1}\\)", "\\(I\\)"]),
                ("dim(col space) + dim(null space) =", "n (number of columns)", ["n (number of columns)", "m (number of rows)", "rank", "0"]),
                ("The null space is _____ to the row space", "orthogonal", ["orthogonal", "parallel", "equal", "similar"])
            ]
            q_text, ans, opts = random.choice(rels)
            
            if i % 2 == 0:
                random.shuffle(opts)
                questions.append({"type": "MCQ", "question": q_text, "options": opts, "answer": ans})
            else:
                questions.append({"type": "FIB", "question": q_text, "answer": ans})
    
    return questions

def generate_change_of_basis_questions(count=1000):
    """Generate change of basis questions with variety"""
    questions = []
    
    conceptual = [
        {"type": "MCQ", "question": "Change of basis transforms:", "options": ["Coordinates between different bases", "Matrices to diagonals", "Vectors to scalars", "Bases to vectors"], "answer": "Coordinates between different bases"},
        {"type": "MCQ", "question": "The change of basis matrix P transforms:", "options": ["Old coordinates to new", "Vectors to basis", "Basis to origin", "Scalars to vectors"], "answer": "Old coordinates to new"},
        {"type": "MCQ", "question": "If P is change of basis matrix, then \\(P^{-1}\\) transforms:", "options": ["New coordinates to old", "Old to new", "Basis to itself", "Nothing"], "answer": "New coordinates to old"},
        {"type": "FIB", "question": "Change of basis preserves the _____ itself.", "answer": "vector"},
        {"type": "MCQ", "question": "In 2D, how many vectors define a new basis?", "options": ["2 linearly independent", "1", "3", "Infinite"], "answer": "2 linearly independent"}
    ]
    
    for i in range(count):
        if i % 5 < 2:  # 40% conceptual
            q = random.choice(conceptual)
            questions.append(q.copy())
        elif i % 3 == 0:
            n = random.randint(2, 5)
            
            questions.append({
                "type": "MCQ" if i % 2 == 0 else "FIB",
                "question": f"How many components does a vector in \\(R^{n}\\) have?",
                "options": [f"{n}", f"{n-1}", f"{n+1}", f"{2*n}"] if i % 2 == 0 else None,
                "answer": f"{n}"
            })
        else:
            props = [
                ("Change of basis matrix must be:", "Invertible", ["Invertible", "Singular", "Diagonal", "Zero"]),
                ("The standard basis in \\(R^2\\) is:", "\\(\\{(1,0), (0,1)\\}\\)", ["\\(\\{(1,0), (0,1)\\}\\)", "\\(\\{(1,1), (0,0)\\}\\)", "\\(\\{(2,0), (0,2)\\}\\)", "\\(\\{(0,0)\\}\\)"]),
                ("Coordinates depend on:", "Choice of basis", ["Choice of basis", "Vector magnitude", "Dot product", "Cross product"]),
                ("A diagonal matrix in the eigenbasis is:", "Easy to work with", ["Easy to work with", "Complex", "Undefined", "Singular"])
            ]
            q_text, ans, opts = random.choice(props)
            
            if i % 2 == 0:
                random.shuffle(opts)
                questions.append({"type": "MCQ", "question": q_text, "options": opts, "answer": ans})
            else:
                questions.append({"type": "FIB", "question": q_text, "answer": ans})
    
    return questions

def generate_diagonalization_questions(count=1000):
    """Generate diagonalization questions with variety"""
    questions = []
    
    conceptual = [
        {"type": "MCQ", "question": "A matrix A is diagonalizable if:", "options": ["It has n linearly independent eigenvectors", "det(A) = 0", "A is singular", "A is zero"], "answer": "It has n linearly independent eigenvectors"},
        {"type": "MCQ", "question": "If A is diagonalizable, then \\(A = PDP^{-1}\\) where D is:", "options": ["Diagonal matrix of eigenvalues", "Identity matrix", "Zero matrix", "Transpose of A"], "answer": "Diagonal matrix of eigenvalues"},
        {"type": "MCQ", "question": "The columns of P in \\(A = PDP^{-1}\\) are:", "options": ["Eigenvectors of A", "Eigenvalues of A", "Rows of A", "Diagonal elements"], "answer": "Eigenvectors of A"},
        {"type": "FIB", "question": "A diagonal matrix has all _____ elements equal to zero.", "answer": "off-diagonal"},
        {"type": "MCQ", "question": "Not all matrices are:", "options": ["Diagonalizable", "Square", "Real", "Non-zero"], "answer": "Diagonalizable"}
    ]
    
    for i in range(count):
        if i % 5 < 2:  # 40% conceptual
            q = random.choice(conceptual)
            questions.append(q.copy())
        elif i % 3 == 0:
            props = [
                ("If A has n distinct eigenvalues, then A is:", "Diagonalizable", ["Diagonalizable", "Not diagonalizable", "Singular", "Zero"]),
                ("Diagonalization simplifies:", "Matrix powers", ["Matrix powers", "Addition", "Subtraction", "Nothing"]),
                ("Similar matrices have the same:", "Eigenvalues", ["Eigenvalues", "Eigenvectors", "Entries", "Dimensions"]),
                ("The matrix D in \\(A = PDP^{-1}\\) contains:", "Eigenvalues on diagonal", ["Eigenvalues on diagonal", "Eigenvectors", "Determinant", "Trace"])
            ]
            q_text, ans, opts = random.choice(props)
            
            if i % 2 == 0:
                random.shuffle(opts)
                questions.append({"type": "MCQ", "question": q_text, "options": opts, "answer": ans})
            else:
                questions.append({"type": "FIB", "question": q_text, "answer": ans})
        else:
            # Dimension questions
            n = random.randint(2, 5)
            questions.append({
                "type": "MCQ" if i % 2 == 0 else "FIB",
                "question": f"An {n}×{n} matrix needs how many linearly independent eigenvectors to be diagonalizable?",
                "options": [f"{n}", f"{n-1}", f"{n+1}", f"{2*n}"] if i % 2 == 0 else None,
                "answer": f"{n}"
            })
    
    return questions

def generate_gram_schmidt_questions(count=1000):
    """Generate Gram-Schmidt process questions with variety"""
    questions = []
    
    conceptual = [
        {"type": "MCQ", "question": "Gram-Schmidt process creates:", "options": ["Orthogonal vectors", "Parallel vectors", "Zero vectors", "Identical vectors"], "answer": "Orthogonal vectors"},
        {"type": "MCQ", "question": "Gram-Schmidt is used to create:", "options": ["Orthonormal basis", "Any basis", "Eigenvectors", "Determinants"], "answer": "Orthonormal basis"},
        {"type": "MCQ", "question": "The first step in Gram-Schmidt is:", "options": ["Normalize the first vector", "Take the cross product", "Find determinant", "Square the matrix"], "answer": "Normalize the first vector"},
        {"type": "FIB", "question": "Gram-Schmidt produces vectors that are _____ to each other.", "answer": "orthogonal"},
        {"type": "MCQ", "question": "After Gram-Schmidt, the vectors are:", "options": ["Orthonormal", "Parallel", "Zero", "Unchanged"], "answer": "Orthonormal"}
    ]
    
    for i in range(count):
        if i % 5 < 2:  # 40% conceptual
            q = random.choice(conceptual)
            questions.append(q.copy())
        elif i % 3 == 0:
            props = [
                ("Orthogonal vectors have dot product:", "0", ["0", "1", "-1", "Undefined"]),
                ("Gram-Schmidt starts with:", "Linearly independent vectors", ["Linearly independent vectors", "Any vectors", "Zero vectors", "Orthogonal vectors"]),
                ("The output of Gram-Schmidt is:", "Orthonormal set", ["Orthonormal set", "Linearly dependent set", "Parallel vectors", "Zero vectors"]),
                ("Gram-Schmidt is used in:", "QR decomposition", ["QR decomposition", "LU decomposition", "Matrix addition", "Cross products"])
            ]
            q_text, ans, opts = random.choice(props)
            
            if i % 2 == 0:
                random.shuffle(opts)
                questions.append({"type": "MCQ", "question": q_text, "options": opts, "answer": ans})
            else:
                questions.append({"type": "FIB", "question": q_text, "answer": ans})
        else:
            # Normalization questions
            if i % 4 == 0:
                a = random.randint(3, 5)
                questions.append({
                    "type": "MCQ",
                    "question": f"To normalize vector \\(({a}, 0)\\), divide by:",
                    "options": [f"{a}", f"{a**2}", "1", "0"],
                    "answer": f"{a}"
                })
            else:
                questions.append({
                    "type": "FIB",
                    "question": "A unit vector has magnitude:",
                    "answer": "1"
                })
    
    return questions

def generate_matrix_trace_questions(count=1000):
    """Generate matrix trace questions with variety"""
    questions = []
    
    conceptual = [
        {"type": "MCQ", "question": "The trace of a matrix is:", "options": ["Sum of diagonal elements", "Product of diagonal elements", "Determinant", "Rank"], "answer": "Sum of diagonal elements"},
        {"type": "MCQ", "question": "Trace is only defined for:", "options": ["Square matrices", "All matrices", "Invertible matrices", "Diagonal matrices"], "answer": "Square matrices"},
        {"type": "MCQ", "question": "\\(\\text{tr}(A + B) = \\):", "options": ["\\(\\text{tr}(A) + \\text{tr}(B)\\)", "\\(\\text{tr}(A) \\cdot \\text{tr}(B)\\)", "\\(\\text{tr}(AB)\\)", "0"], "answer": "\\(\\text{tr}(A) + \\text{tr}(B)\\)"},
        {"type": "FIB", "question": "The trace is the _____ of the diagonal elements.", "answer": "sum"},
        {"type": "MCQ", "question": "For similar matrices A and B:", "options": ["\\(\\text{tr}(A) = \\text{tr}(B)\\)", "\\(\\text{tr}(A) \\neq \\text{tr}(B)\\)", "A = B", "\\(\\text{tr}(A) = 0\\)"], "answer": "\\(\\text{tr}(A) = \\text{tr}(B)\\)"}
    ]
    
    for i in range(count):
        if i % 5 < 2:  # 40% conceptual
            q = random.choice(conceptual)
            questions.append(q.copy())
        elif i % 3 == 0:
            # Computational questions with specific values
            a, b, c, d = random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)
            trace = a + d
            
            questions.append({
                "type": "MCQ" if i % 2 == 0 else "FIB",
                "question": f"What is the trace of \\(\\begin{{bmatrix}}{a} & {b}\\\\{c} & {d}\\end{{bmatrix}}\\)?",
                "options": [f"{trace}", f"{a*d}", f"{a*d - b*c}", f"{a + b + c + d}"] if i % 2 == 0 else None,
                "answer": f"{trace}"
            })
        else:
            props = [
                ("\\(\\text{tr}(cA) = \\) (where c is a scalar):", "\\(c \\cdot \\text{tr}(A)\\)", ["\\(c \\cdot \\text{tr}(A)\\)", "\\(\\text{tr}(A)\\)", "\\(c + \\text{tr}(A)\\)", "0"]),
                ("The trace of the identity matrix \\(I_n\\) is:", "n", ["n", "1", "0", "n²"]),
                ("Trace and eigenvalues are related by:", "tr(A) = sum of eigenvalues", ["tr(A) = sum of eigenvalues", "tr(A) = product of eigenvalues", "tr(A) = det(A)", "No relation"]),
                ("\\(\\text{tr}(AB) = \\):", "\\(\\text{tr}(BA)\\)", ["\\(\\text{tr}(BA)\\)", "\\(\\text{tr}(A) \\cdot \\text{tr}(B)\\)", "\\(\\text{tr}(A) + \\text{tr}(B)\\)", "0"])
            ]
            q_text, ans, opts = random.choice(props)
            
            if i % 2 == 0:
                random.shuffle(opts)
                questions.append({"type": "MCQ", "question": q_text, "options": opts, "answer": ans})
            else:
                questions.append({"type": "FIB", "question": q_text, "answer": ans})
    
    return questions

def generate_simple_topic_questions(topic_name, count=1000):
    """Generate simple conceptual questions for advanced topics"""
    # Placeholder generator for topics that need basic conceptual questions
    questions = []
    
    conceptual_templates = {
        "matrix-inverse": [
            {"q": "What is \\\\\\\\\\\\\\\\(A \\\\\\\\\\\\\\\\times A^{{-1}}\\\\\\\\\\\\\\\\)?", "a": "\\\\\\\\\\\\\\\\(I\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(I\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(2A\\\\\\\\\\\\\\\\)"]},
            {"q": "If det(A) = 0, does A have an inverse?", "a": "No", "opts": [" No", "Yes", "Sometimes", "Always"]},
            {"q": "A matrix is invertible if and only if:", "a": "det(A) ≠ 0", "opts": ["det(A) ≠ 0", "det(A) = 0", "A = I", "A is square"]},
            {"q": "\\\\\\\\\\\\\\\\((AB)^{{-1}} = \\\\\\\\\\\\\\\\)?", "a": "\\\\\\\\\\\\\\\\(B^{{-1}}A^{{-1}}\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(B^{{-1}}A^{{-1}}\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A^{{-1}}B^{{-1}}\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(AB\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\((BA)^{{-1}}\\\\\\\\\\\\\\\\)"]},
            {"q": "\\\\\\\\\\\\\\\\((A^{{-1}})^{{-1}} = \\\\\\\\\\\\\\\\)?", "a": "\\\\\\\\\\\\\\\\(A\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(A\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(I\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A^{{-1}}\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)"]},
            {"q": "The inverse of \\\\\\\\\\\\\\\\(A^T\\\\\\\\\\\\\\\\) is:", "a": "\\\\\\\\\\\\\\\\((A^{{-1}})^T\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\((A^{{-1}})^T\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\((A^T)^{{-1}}\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A^{{-1}}\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A^T\\\\\\\\\\\\\\\\)"]},
            {"q": "If A is invertible, then \\\\\\\\\\\\\\\\(A^{{-1}}\\\\\\\\\\\\\\\\) is:", "a": "Unique", "opts": ["Unique", "Not unique", "Zero", "Undefined"]},
            {"q": "\\\\\\\\\\\\\\\\(A^{{-1}}A = \\\\\\\\\\\\\\\\)?", "a": "\\\\\\\\\\\\\\\\(I\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(I\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A^2\\\\\\\\\\\\\\\\)"]},
            {"q": "If A is invertible, \\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{det}}(A^{{-1}})\\\\\\\\\\\\\\\\) =", "a": "\\\\\\\\\\\\\\\\(1/\\\\\\\\\\\\\\\\text{{det}}(A)\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(1/\\\\\\\\\\\\\\\\text{{det}}(A)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{det}}(A)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(1\\\\\\\\\\\\\\\\)"]},
            {"q": "Which matrices are always invertible?", "a": "Orthogonal matrices", "opts": ["Orthogonal matrices", "Singular matrices", "Zero matrices", "Rectangular matrices"]},
        ],
        "eigenvalues-eigenvectors": [
            {"q": "If \\\\\\\\\\\\\\\\(Av = \\\\\\\\\\\\\\\\lambda v\\\\\\\\\\\\\\\\), what is \\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\lambda\\\\\\\\\\\\\\\\)?", "a": "Eigenvalue", "opts": ["Eigenvalue", "Eigenvector", "Determinant", "Trace"]},
            {"q": "What does the eigenvector represent?", "a": "Direction unchanged by transformation", "opts": ["Direction unchanged by transformation", "Magnitude", "Determinant", "Rank"]},
            {"q": "Eigenvalues are found from:", "a": "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{det}}(A - \\\\\\\\\\\\\\\\lambda I) = 0\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{det}}(A - \\\\\\\\\\\\\\\\lambda I) = 0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(Av = 0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A + \\\\\\\\\\\\\\\\lambda I = 0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{tr}}(A) = \\\\\\\\\\\\\\\\lambda\\\\\\\\\\\\\\\\)"]},
            {"q": "The trace of A equals:", "a": "Sum of eigenvalues", "opts": ["Sum of eigenvalues", "Product of eigenvalues", "Largest eigenvalue", "Number of eigenvalues"]},
            {"q": "The determinant of A equals:", "a": "Product of eigenvalues", "opts": ["Product of eigenvalues", "Sum of eigenvalues", "Largest eigenvalue", "Trace"]},
            {"q": "If 0 is an eigenvalue of A, then A is:", "a": "Singular", "opts": ["Singular", "Invertible", "Orthogonal", "Identity"]},
            {"q": "Eigenvectors for different eigenvalues are:", "a": "Linearly independent", "opts": ["Linearly independent", "Linearly dependent", "Parallel", "Zero"]},
            {"q": "Eigenvalues of \\\\\\\\\\\\\\\\(A^T\\\\\\\\\\\\\\\\) are:", "a": "Same as A", "opts": ["Same as A", "Negatives of A", "Inverses of A", "Different from A"]},
            {"q": "Real symmetric matrices have:", "a": "Real eigenvalues", "opts": ["Real eigenvalues", "Complex eigenvalues", "No eigenvalues", "Zero eigenvalues"]},
            {"q": "An n×n matrix has at most how many eigenvalues?", "a": "n", "opts": ["n", "n-1", "n+1", "2n"]},
        ],
        "vector-projection": [
            {"q": "The projection of vector u onto v is:", "a": "Parallel to v", "opts": ["Parallel to v", "Perpendicular to v", "Equal to u", "Zero"]},
            {"q": "The formula for projection is:", "a": "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\frac{{u \\\\\\\\\\\\\\\\cdot v}}{{v \\\\\\\\\\\\\\\\cdot v}}v\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\frac{{u \\\\\\\\\\\\\\\\cdot v}}{{v \\\\\\\\\\\\\\\\cdot v}}v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u \\\\\\\\\\\\\\\\cdot v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u - v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u \\\\\\\\\\\\\\\\times v\\\\\\\\\\\\\\\\)"]},
            {"q": "Projection magnitude is:", "a": "\\\\\\\\\\\\\\\\(|u|\\\\\\\\\\\\\\\\cos\\\\\\\\\\\\\\\\theta\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(|u|\\\\\\\\\\\\\\\\cos\\\\\\\\\\\\\\\\theta\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(|u|\\\\\\\\\\\\\\\\sin\\\\\\\\\\\\\\\\theta\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(|v|\\\\\\\\\\\\\\\\cos\\\\\\\\\\\\\\\\theta\\\\\\\\\\\\\\\\)", "|u||v|"]},
            {"q": "Component of u perpendicular to v is:", "a": "\\\\\\\\\\\\\\\\(u - \\\\\\\\\\\\\\\\text{{proj}}_v(u)\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(u - \\\\\\\\\\\\\\\\text{{proj}}_v(u)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u + \\\\\\\\\\\\\\\\text{{proj}}_v(u)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{proj}}_v(u)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(v\\\\\\\\\\\\\\\\)"]},
            {"q": "If u and v are perpendicular, projection is:", "a": "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u + v\\\\\\\\\\\\\\\\)"]},
            {"q": "If u = v, then projection is:", "a": "\\\\\\\\\\\\\\\\(v\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(2v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(v/2\\\\\\\\\\\\\\\\)"]},
            {"q": "Projection satisfies:", "a": "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{proj}}_v(u) \\\\\\\\\\\\\\\\cdot (u - \\\\\\\\\\\\\\\\text{{proj}}_v(u)) = 0\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{proj}}_v(u) \\\\\\\\\\\\\\\\cdot (u - \\\\\\\\\\\\\\\\text{{proj}}_v(u)) = 0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{proj}}_v(u) = u\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{proj}}_v(u) > u\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(\\\\\\\\\\\\\\\\text{{proj}}_v(u) < 0\\\\\\\\\\\\\\\\)"]},
            {"q": "Projecting onto unit vector v gives:", "a": "\\\\\\\\\\\\\\\\((u \\\\\\\\\\\\\\\\cdot v)v\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\((u \\\\\\\\\\\\\\\\cdot v)v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u \\\\\\\\\\\\\\\\cdot v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(u - v\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(uv\\\\\\\\\\\\\\\\)"]},
            {"q": "Vector projection is used in:", "a": "Finding shortest distance", "opts": ["Finding shortest distance", "Cross products", "Determinants", "Matrix multiplication"]},
            {"q": "The projection of u onto itself is:", "a": "u", "opts": ["u", "0", "2u", "u/2"]},
        ],
        "linear-independence": [
            {"q": "Vectors are linearly independent if:", "a": "No vector is a linear combination of others", "opts": ["No vector is a linear combination of others", "All vectors are parallel", "All vectors are zero", "Determinant is zero"]},
            {"q": "If vectors are linearly dependent:", "a": " One is a combination of others", "opts": ["One is a combination of others", "They are orthogonal", "They span R^n", "Determinant ≠ 0"]},
            {"q": "Standard basis vectors in R^n are:", "a": "Linearly independent", "opts": ["Linearly independent", "Linearly dependent", "Parallel", "Zero"]},
            {"q": "n vectors in R^n are independent if:", "a": "det(A) ≠ 0", "opts": ["det(A) ≠ 0", "det(A) = 0", "They are orthogonal", "They are normalized"]},
            {"q": "If c₁v₁ + c₂v₂ + ... = 0 only when all cᵢ = 0, vectors are:", "a": "Linearly independent", "opts": ["Linearly independent", "Linearly dependent", "Parallel", "Orthogonal"]},
            {"q": "More than n vectors in R^n are:", "a": "Linearly dependent", "opts": ["Linearly dependent", "Linearly independent", "A basis", "Orthonormal"]},
            {"q": "If one vector is zero, the set is:", "a": "Linearly dependent", "opts": ["Linearly dependent", "Linearly independent", "A basis", "Orthogonal"]},
            {"q": "Two parallel vectors are:", "a": "Linearly dependent", "opts": ["Linearly dependent", "Linearly independent", "Orthogonal", "A basis"]},
            {"q": "The rank of a matrix equals:", "a": "Number of linearly independent columns", "opts": ["Number of linearly independent columns", "Number of columns", "Determinant", "Trace"]},
            {"q": "If columns of A are independent:", "a": "Ax = 0 has only trivial solution", "opts": ["Ax = 0 has only trivial solution", "Ax = b has no solution", "det(A) = 0", "A is singular"]},
        ],
        "basis-vectors": [
            {"q": "A basis for R^n contains how many vectors?", "a": "n", "opts": ["n", "n-1", "n+1", "2n"]},
            {"q": "A basis must be:", "a": "Linearly independent and span the space", "opts": ["Linearly independent and span the space", "Orthogonal", "Normalized", "Infinite"]},
            {"q": "The dimension of R^n is:", "a": "n", "opts": ["n", "n-1", "n+1", "Infinite"]},
            {"q": "Standard basis for R^3 is:", "a": "{(1,0,0), (0,1,0), (0,0,1)}", "opts": ["{(1,0,0), (0,1,0), (0,0,1)}", "{(1,1,0), (0,1,1), (1,0,1)}", "{(1,1,1)}", "{(0,0,0)}"]},
            {"q": "Every vector can be written as a _____ combination of basis vectors", "a": "Linear", "opts": ["Linear", "Nonlinear", "Zero", "Infinite"]},
            {"q": "If vectors span R^n but are not independent:", "a": "Remove vectors to get basis", "opts": ["Remove vectors to get basis", "Add vectors to get basis", "They form a basis", "No basis exists"]},
            {"q": "Coordinates of a vector depend on:", "a": "Choice of basis", "opts": ["Choice of basis", "Vector magnitude", "Dot product", "Cross product"]},
            {"q": "An orthonormal basis has vectors that are:", "a": "Orthogonal and unit length", "opts": ["Orthogonal and unit length", "Parallel", "Long", "Zero"]},
            {"q": "A basis provides:", "a": "Unique representation for each vector", "opts": ["Unique representation for each vector", "Multiple representations", "No representation", "Infinite representations"]},
            {"q": "Changing basis:", "a": "Changes coordinates but not the vector", "opts": ["Changes coordinates but not the vector", "Changes the vector", "Changes dimension", "Changes the space"]},
        ],
        "linear-transformations": [
            {"q": "A linear transformation satisfies \\\\\\\\\\\\\\\\(T(u+v) = \\\\\\\\\\\\\\\\)?", "a": "\\\\\\\\\\\\\\\\(T(u) + T(v)\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(T(u) + T(v)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(T(u) \\\\\\\\\\\\\\\\cdot T(v)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(T(u) - T(v)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)"]},
            {"q": "A linear transformation satisfies \\\\\\\\\\\\\\\\(T(cv) = \\\\\\\\\\\\\\\\)?", "a": "\\\\\\\\\\\\\\\\(cT(v)\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(cT(v)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(T(c) + T(v)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(T(v)\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(T(c)T(v)\\\\\\\\\\\\\\\\)"]},
            {"q": "T(0) = ?", "a": "0", "opts": ["0", "I", "T", "Undefined"]},
            {"q": "Every linear transformation T: R^n → R^m is represented by:", "a": "An m×n matrix", "opts": ["An m×n matrix", "An n×m matrix", "A scalar", "A vector"]},
            {"q": "The kernel (null space) of T contains vectors where T(v) = ?", "a": "0", "opts": ["0", "I", "v", "T"]},
            {"q": "The range of T is:", "a": "All possible outputs", "opts": ["All possible outputs", "All inputs", "Kernel", "Null space"]},
            {"q": "Composition of linear transformations is:", "a": "Linear", "opts": ["Linear", "Not linear", "Undefined", "Zero"]},
            {"q": "A rotation in R^2 is:", "a": "A linear transformation", "opts": ["A linear transformation", "Not linear", "A translation", "Non-invertible"]},
            {"q": "Which is NOT linear?", "a": "Translation", "opts": ["Translation", "Rotation", "Scaling", "Reflection"]},
            {"q": "A linear transformation preserves:", "a": "Linear combinations", "opts": ["Linear combinations", "Distances always", "Angles always", "Volume always"]},
        ],
        "orthogonality": [
            {"q": "Two vectors are orthogonal if their dot product is:", "a": "\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(1\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(-1\\\\\\\\\\\\\\\\)", "Undefined"]},
            {"q": "Orthogonal vectors are:", "a": "Perpendicular", "opts": ["Perpendicular", "Parallel", "Equal", "Zero"]},
            {"q": "If u and v are orthogonal, ||u + v||² = ?", "a": "||u||² + ||v||²", "opts": ["||u||² + ||v||²", "||u||² - ||v||²", "||u|| · ||v||", "0"]},
            {"q": "An orthonormal set has vectors that are:", "a": "Orthogonal and unit length", "opts": ["Orthogonal and unit length", "Parallel and unit length", "Orthogonal only", "Unit length only"]},
            {"q": "Standard basis vectors are:", "a": "Orthonormal", "opts": ["Orthonormal", "Parallel", "Dependent", "Zero"]},
            {"q": "An orthogonal matrix Q satisfies:", "a": "Q^T Q = I", "opts": ["Q^T Q = I", "Q² = I", "Q = I", "Q = 0"]},
            {"q": "If Q is orthogonal, Q^(-1) = ?", "a": "Q^T", "opts": ["Q^T", "Q", "-Q", "I"]},
            {"q": "Orthogonal matrices preserve:", "a": "Lengths and angles", "opts": ["Lengths and angles", "Only lengths", "Only angles", "Nothing"]},
            {"q": "(1, 0) and (0, 1) in R^2 are:", "a": "Orthogonal", "opts": ["Orthogonal", "Parallel", "Dependent", "None"]},
            {"q": "The angle between orthogonal vectors is:", "a": "90°", "opts": ["90°", "0°", "180°", "45°"]},
        ],
        "matrix-rank": [
            {"q": "The rank of a matrix is:", "a": "Number of linearly independent rows/columns", "opts": ["Number of linearly independent rows/columns", "Number of zeros", "Determinant", "Trace"]},
            {"q": "Row rank equals:", "a": "Column rank", "opts": ["Column rank", "Number of rows", "Determinant", "Trace"]},
            {"q": "Rank of m×n matrix is at most:", "a": "min(m, n)", "opts": ["min(m, n)", "max(m, n)", "m + n", "mn"]},
            {"q": "Full rank means:", "a": "rank = min(m, n)", "opts": ["rank = min(m, n)", "rank = 0", "rank = 1", "rank = max(m, n)"]},
            {"q": "Rank is the number of _____ in RREF", "a": "Pivots", "opts": ["Pivots", "Zeros", "Ones", "Columns"]},
            {"q": "If rank(A) < n for n×n matrix A:", "a": "A is singular", "opts": ["A is singular", "A is invertible", "det(A) ≠ 0", "A = I"]},
            {"q": "rank(A) + dim(null space) =", "a": "Number of columns", "opts": ["Number of columns", "Number of rows", "0", "Determinant"]},
            {"q": "Zero matrix has rank:", "a": "0", "opts": ["0", "1", "n", "Undefined"]},
            {"q": "rank(A) = rank(A^T)?", "a": " True", "opts": ["True", "False", "Sometimes", "Never"]},
            {"q": "If A is invertible, rank(A) =", "a": "n (size of A)", "opts": ["n (size of A)", "0", "1", "n-1"]},
        ],
        "null-space": [
            {"q": "The null space of A contains all vectors x where:", "a": "\\\\\\\\\\\\\\\\(Ax = 0\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(Ax = 0\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(Ax = I\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(Ax = A\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(Ax = x\\\\\\\\\\\\\\\\)"]},
            {"q": "The null space is also called:", "a": "Kernel", "opts": ["Kernel", "Range", "Image", "Codomain"]},
            {"q": "The null space is always a:", "a": "Subspace", "opts": ["Subspace", "Basis", "Single vector", "Empty set"]},
            {"q": "If A is invertible, null space is:", "a": "{0}", "opts": ["{0}", "R^n", "Empty", "Infinite"]},
            {"q": "Dimension of null space is called:", "a": "Nullity", "opts": ["Nullity", "Rank", "Determinant", "Trace"]},
            {"q": "rank(A) + nullity(A) =", "a": "Number of columns", "opts": ["Number of columns", "Number of rows", "0", "Determinant"]},
            {"q": "To find null space, solve:", "a": "Ax = 0", "opts": ["Ax = 0", "Ax = b", "A = 0", "x = 0"]},
            {"q": "Null space is:", "a": "A vector space", "opts": ["A vector space", "A single vector", "A scalar", "Empty always"]},
            {"q": "If null space = {0}, columns are:", "a": "Linearly independent", "opts": ["Linearly independent", "Linearly dependent", "Parallel", "Zero"]},
            {"q": "Null space of identity matrix is:", "a": "{0}", "opts": ["{0}", "R^n", "Undefined", "Empty"]},
        ],
        "systems-linear-equations": [
            {"q": "A system Ax = b has a unique solution if:", "a": "A is invertible", "opts": ["A is invertible", "det(A) = 0", "A is singular", "b = 0"]},
            {"q": "System has no solution if:", "a": "b not in column space of A", "opts": ["b not in column space of A", "b = 0", "A is invertible", "det(A) ≠ 0"]},
            {"q": "System has infinitely many solutions if:", "a": "rank(A) < number of unknowns and consistent", "opts": ["rank(A) < number of unknowns and consistent", "A is invertible", "b ≠ 0", "det(A) ≠ 0"]},
            {"q": "Homogeneous system Ax = 0 always has:", "a": "At least the zero solution", "opts": ["At least the zero solution", "No solution", "Unique non-zero solution", "Infinite solutions always"]},
            {"q": "Cramer's rule applies when:", "a": "A is square and invertible", "opts": ["A is square and invertible", "A is rectangular", "b = 0", "A is singular"]},
            {"q": "If det(A) = 0, the system:", "a": "Has no unique solution", "opts": ["Has no unique solution", "Has unique solution", "Has no solution always", "Has infinite solutions always"]},
            {"q": "For consistent system, solution is:", "a": "Particular + homogeneous solutions", "opts": ["Particular + homogeneous solutions", "Only particular", "Only homogeneous", "Zero"]},
            {"q": "n×n system with det(A) ≠ 0 has:", "a": "Unique solution", "opts": ["Unique solution", "No solution", "Infinite solutions", "Two solutions"]},
            {"q": "Augmented matrix [A|b] is used in:", "a": "Gaussian elimination", "opts": ["Gaussian elimination", "Cramer's rule", "Determinant", "Eigenvalues"]},
            {"q": "System is consistent if:", "a": "It has at least one solution", "opts": ["It has at least one solution", "It has no solution", "A is singular", "b = 0"]},
        ],
        "gaussian-elimination": [
            {"q": "Gaussian elimination uses which operations?", "a": "Elementary row operations", "opts": ["Elementary row operations", "Column operations only", "Matrix multiplication", "Determinants"]},
            {"q": "Three elementary row operations are:", "a": "Swap, scale, add multiple of row", "opts": ["Swap, scale, add multiple of row", "Only swap", "Only scale", "Multiply rows"]},
            {"q": "Gaussian elimination transforms A to:", "a": "Row echelon form", "opts": ["Row echelon form", "Diagonal form", "Identity", "Zero"]},
            {"q": "Gauss-Jordan elimination transforms A to:", "a": "Reduced row echelon form", "opts": ["Reduced row echelon form", "Row echelon form only", "Diagonal form always", "Identity always"]},
            {"q": "Eliminating variables is called:", "a": "Forward elimination", "opts": ["Forward elimination", "Back substitution", "Reduction", "Expansion"]},
            {"q": "Back substitution is used:", "a": "After forward elimination", "opts": ["After forward elimination", "Before elimination", "Instead of elimination", "Never"]},
            {"q": "Pivots are:", "a": "First non-zero entries in rows", "opts": ["First non-zero entries in rows", "Any entries", "Zero entries", "Last entries"]},
            {"q": "Row operations:", "a": "Don't change solutions", "opts": ["Don't change solutions", "Change solutions", "Make system inconsistent", "Always fail"]},
            {"q": "Swapping two rows:", "a": "Changes sign of determinant", "opts": ["Changes sign of determinant", "Doesn't change determinant", "Makes det = 0", "Makes det = 1"]},
            {"q": "Gaussian elimination can find:", "a": "Rank of A", "opts": ["Rank of A", "Eigenvalues", "Eigenvectors", "Trace"]},
        ],
        "row-echelon-form": [
            {"q": "In REF, what is below each pivot?", "a": "Zeros", "opts": ["Zeros", "Ones", "Pivots", "Any value"]},
            {"q": "In RREF, what is above each pivot?", "a": "Zeros", "opts": ["Zeros", "Ones", "Pivots", "Any value"]},
            {"q": "In RREF, each pivot is:", "a": "1", "opts": ["1", "0", "Any value", "The determinant"]},
            {"q": "REF stands for:", "a": "Row Echelon Form", "opts": ["Row Echelon Form", "Reduced Excel Form", "Row Elimination Form", "Rank Echelon Format"]},
            {"q": "RREF stands for:", "a": "Reduced Row Echelon Form", "opts": ["Reduced Row Echelon Form", "Row Reduced Excel Form", "Rank REF", "Real REF"]},
            {"q": "Number of pivots in RREF equals:", "a": "Rank of A", "opts": ["Rank of A", "Number of rows", "Number of columns", "Determinant"]},
            {"q": "Each pivot column in RREF:", "a": "Has one 1 and rest 0s", "opts": ["Has one 1 and rest 0s", "Has all 1s", "Has all 0s", "Has random values"]},
            {"q": "RREF is:", "a": "Unique for each matrix", "opts": ["Unique for each matrix", "Not unique", "Random", "Undefined"]},
            {"q": "Columns without pivots correspond to:", "a": "Free variables", "opts": ["Free variables", "Basic variables", "No variables", "Determinant"]},
            {"q": "Zero rows in REF are:", "a": "At the bottom", "opts": ["At the bottom", "At the top", "Anywhere", "Not allowed"]},
        ],
        "matrix-trace": [
            {"q": "The trace of a matrix is:", "a": "Sum of diagonal elements", "opts": ["Sum of diagonal elements", "Product of diagonal elements", "Determinant", "Rank"]},
        ],
        "gram-schmidt": [
            {"q": "Gram-Schmidt process creates:", "a": "Orthogonal vectors", "opts": ["Orthogonal vectors", "Parallel vectors", "Zero vectors", "Identical vectors"]},
        ],
        "diagonalization": [
            {"q": "A matrix A is diagonalizable if:", "a": "It has n linearly independent eigenvectors", "opts": ["It has n linearly independent eigenvectors", "det(A) = 0", "A is singular", "A is zero"]},
        ],
        "column-row-space": [
            {"q": "The column space of A is spanned by:", "a": "Columns of A", "opts": ["Columns of A", "Rows of A", "Diagonals of A", "Eigenvalues"]},
        ],
        "lu-decomposition": [
            {"q": "LU decomposition expresses A as:", "a": "\\\\\\\\\\\\\\\\(A = LU\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(A = LU\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A = L + U\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A = L - U\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(A = UL\\\\\\\\\\\\\\\\)"]},
        ],
        "least-squares": [
            {"q": "The least squares solution minimizes:", "a": "\\\\\\\\\\\\\\\\(||Ax - b||\\\\\\\\\\\\\\\\)", "opts": ["\\\\\\\\\\\\\\\\(||Ax - b||\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(||x||\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(||A||\\\\\\\\\\\\\\\\)", "\\\\\\\\\\\\\\\\(det(A)\\\\\\\\\\\\\\\\)"]},
        ],
        "change-of-basis": [
            {"q": "Change of basis transforms:", "a": "Coordinates between different bases", "opts": ["Coordinates between different bases", "Matrix to diagonal", "Vectors to scalars", "Bases to vectors"]},
        ]
    }
    
    templates = conceptual_templates.get(topic_name, conceptual_templates["matrix-inverse"])
    
    for i in range(count):
        template = random.choice(templates)
        
        if i % 2 == 0:  # MCQ
            options = template["opts"].copy()
            random.shuffle(options)
            
            questions.append({
                "type": "MCQ",
                "question": template["q"],
                "options": options,
                "answer": template["a"]
            })
        else:  # FIB
            questions.append({
                "type": "FIB",
                "question": template["q"],
                "answer": template["a"]
            })
    
    return questions

def main():
    """Generate all question files"""
    print("Generating static questions for all topics...")
    
    # Create questions directory if it doesn't exist
    os.makedirs("questions", exist_ok=True)
    
    topics = {
        "matrix": generate_matrix_questions,
        "vectors": generate_vector_questions,
        "identity-matrix": generate_identity_matrix_questions,
        "dot-product": generate_dot_product_questions,
        "vector-magnitude": generate_vector_magnitude_questions,
        "vector-addition": generate_vector_addition_questions,
        "cross-product": generate_cross_product_questions,
        "matrix-transpose": generate_matrix_transpose_questions,
        "matrix-determinant": generate_matrix_determinant_questions,
        "matrix-inverse": lambda c: generate_simple_topic_questions("matrix-inverse", c),
        "eigenvalues-eigenvectors": lambda c: generate_simple_topic_questions("eigenvalues-eigenvectors", c),
        "vector-projection": lambda c: generate_simple_topic_questions("vector-projection", c),
        "linear-independence": lambda c: generate_simple_topic_questions("linear-independence", c),
        "basis-vectors": lambda c: generate_simple_topic_questions("basis-vectors", c),
        "linear-transformations": lambda c: generate_simple_topic_questions("linear-transformations", c),
        "orthogonality": lambda c: generate_simple_topic_questions("orthogonality", c),
        "matrix-rank": lambda c: generate_simple_topic_questions("matrix-rank", c),
        "null-space": lambda c: generate_simple_topic_questions("null-space", c),
        "systems-linear-equations": lambda c: generate_simple_topic_questions("systems-linear-equations", c),
        "gaussian-elimination": lambda c: generate_simple_topic_questions("gaussian-elimination", c),
        "row-echelon-form": lambda c: generate_simple_topic_questions("row-echelon-form", c),
        "matrix-trace": generate_matrix_trace_questions,
        "gram-schmidt": generate_gram_schmidt_questions,
        "diagonalization": generate_diagonalization_questions,
        "column-row-space": generate_column_row_space_questions,
        "lu-decomposition": generate_lu_decomposition_questions,
        "least-squares": generate_least_squares_questions,
        "change-of-basis": generate_change_of_basis_questions
    }
    
    for topic_name, generator_func in topics.items():
        print(f"\nGenerating {topic_name} questions...")
        questions = generator_func(1000)
        
        filename = f"questions/{topic_name}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
        
        print(f"[OK] Generated {len(questions)} questions for {topic_name}")
        print(f"  Saved to: {filename}")
    
    print("\n[SUCCESS] All static question files generated successfully!")
    print(f"Total topics: {len(topics)}")
    print("Location: ./questions/")

if __name__ == "__main__":
    main()
