"""
Generate all missing topic learn pages for LinearLeap.
"""
import os

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - LinearLeap</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{
        delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '\\\\[', right: '\\\\]', display: true}},
            {{left: '$', right: '$', display: false}},
            {{left: '\\\\(', right: '\\\\)', display: false}}
        ]
    }});"></script>
</head>

<body>
    <div class="theme-toggle" onclick="toggleTheme()">
        <span id="theme-icon">🌙</span>
    </div>

    <div class="container">
        <div class="topic-content">
            <h1 style="color: var(--text-primary); text-align: center; margin-bottom: 2rem;">{icon} {title}</h1>

{body}

            <div class="navigation-buttons">
                <button class="btn btn-primary" onclick="location.href='../quiz.html?type={quiz_type}'">📝 Take the Quiz</button>
                <button class="btn btn-secondary" onclick="location.href='../index.html'">⬅ Back to Home</button>
            </div>
        </div>
    </div>

    <script src="../js/theme.js"></script>
</body>

</html>'''

TOPICS = {
    "matrix-transpose": {
        "title": "Matrix Transpose",
        "icon": "🔄",
        "body": """            <h2>What is a Matrix Transpose?</h2>
            <p>The <strong>transpose</strong> of a matrix $A$, written $A^T$, is formed by flipping the matrix over its main diagonal — swapping rows and columns.</p>

            <div class="example-box">
                <h4>Definition</h4>
                <p>If $A$ is an $m \\times n$ matrix, then $A^T$ is an $n \\times m$ matrix where $(A^T)_{ij} = A_{ji}$.</p>
            </div>

            <h2>Example</h2>
            <div class="example-box">
                <p style="text-align:center; font-size:1.2rem; margin:1.5rem 0;">
                    $$A = \\begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{bmatrix} \\quad\\Rightarrow\\quad A^T = \\begin{bmatrix} 1 & 4 \\\\ 2 & 5 \\\\ 3 & 6 \\end{bmatrix}$$
                </p>
            </div>

            <h2>Properties</h2>
            <div class="example-box">
                <p><strong>1. Double transpose:</strong> $(A^T)^T = A$</p>
                <p><strong>2. Sum:</strong> $(A + B)^T = A^T + B^T$</p>
                <p><strong>3. Product:</strong> $(AB)^T = B^T A^T$</p>
                <p><strong>4. Scalar:</strong> $(cA)^T = cA^T$</p>
            </div>"""
    },
    "matrix-determinant": {
        "title": "Matrix Determinant",
        "icon": "🔢",
        "body": """            <h2>What is a Determinant?</h2>
            <p>The <strong>determinant</strong> is a scalar value that summarizes key properties of a square matrix — whether it has an inverse, and how it scales space.</p>

            <h2>2×2 Determinant</h2>
            <div class="example-box">
                <p style="text-align:center; font-size:1.2rem; margin:1.5rem 0;">
                    $$\\det\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} = ad - bc$$
                </p>
                <p><strong>Example:</strong> $\\det\\begin{bmatrix} 3 & 1 \\\\ 2 & 4 \\end{bmatrix} = 3 \\cdot 4 - 1 \\cdot 2 = 10$</p>
            </div>

            <h2>Properties</h2>
            <div class="example-box">
                <p><strong>1.</strong> $\\det(AB) = \\det(A)\\det(B)$</p>
                <p><strong>2.</strong> $\\det(A^T) = \\det(A)$</p>
                <p><strong>3.</strong> If $\\det(A) = 0$, the matrix is singular (no inverse).</p>
                <p><strong>4.</strong> $\\det(A^{-1}) = 1/\\det(A)$</p>
            </div>"""
    },
    "matrix-inverse": {
        "title": "Matrix Inverse",
        "icon": "↩️",
        "body": """            <h2>What is a Matrix Inverse?</h2>
            <p>The <strong>inverse</strong> of a matrix $A$, written $A^{-1}$, satisfies $A \\cdot A^{-1} = A^{-1} \\cdot A = I$, where $I$ is the identity matrix.</p>

            <h2>2×2 Inverse Formula</h2>
            <div class="example-box">
                <p style="text-align:center; font-size:1.2rem; margin:1.5rem 0;">
                    $$A = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\quad\\Rightarrow\\quad A^{-1} = \\frac{1}{ad-bc}\\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix}$$
                </p>
            </div>

            <h2>When Does an Inverse Exist?</h2>
            <div class="example-box">
                <p>A matrix is <strong>invertible</strong> (non-singular) if and only if $\\det(A) \\neq 0$.</p>
            </div>

            <h2>Properties</h2>
            <div class="example-box">
                <p><strong>1.</strong> $(A^{-1})^{-1} = A$</p>
                <p><strong>2.</strong> $(AB)^{-1} = B^{-1}A^{-1}$</p>
                <p><strong>3.</strong> $(A^T)^{-1} = (A^{-1})^T$</p>
            </div>"""
    },
    "eigenvalues-eigenvectors": {
        "title": "Eigenvalues & Eigenvectors",
        "icon": "λ",
        "body": """            <h2>What are Eigenvalues and Eigenvectors?</h2>
            <p>For a square matrix $A$, a non-zero vector $\\vec{v}$ is an <strong>eigenvector</strong> if multiplying it by $A$ only scales it:</p>
            <p style="text-align:center; font-size:1.3rem; margin:1.5rem 0;">$$A\\vec{v} = \\lambda\\vec{v}$$</p>
            <p>The scalar $\\lambda$ is the corresponding <strong>eigenvalue</strong>.</p>

            <h2>Finding Eigenvalues</h2>
            <div class="example-box">
                <p>Solve the <strong>characteristic equation</strong>:</p>
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$\\det(A - \\lambda I) = 0$$</p>
            </div>

            <h2>Applications</h2>
            <ul style="color: var(--text-secondary); line-height: 2; margin-left: 2rem;">
                <li><strong>PCA:</strong> Dimensionality reduction in machine learning</li>
                <li><strong>Vibration Analysis:</strong> Natural frequencies of structures</li>
                <li><strong>Google PageRank:</strong> Ranking web pages</li>
            </ul>"""
    },
    "vector-projection": {
        "title": "Vector Projection",
        "icon": "📊",
        "body": """            <h2>What is Vector Projection?</h2>
            <p>The <strong>projection</strong> of vector $\\vec{u}$ onto vector $\\vec{v}$ gives the component of $\\vec{u}$ in the direction of $\\vec{v}$.</p>

            <h2>Formula</h2>
            <div class="example-box">
                <p style="text-align:center; font-size:1.2rem; margin:1.5rem 0;">
                    $$\\text{proj}_{\\vec{v}}\\vec{u} = \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|^2}\\vec{v}$$
                </p>
            </div>

            <h2>Scalar Projection</h2>
            <div class="example-box">
                <p>The scalar projection (length of the shadow) is:</p>
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$\\text{comp}_{\\vec{v}}\\vec{u} = \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{v}|}$$</p>
            </div>

            <h2>Applications</h2>
            <ul style="color: var(--text-secondary); line-height: 2; margin-left: 2rem;">
                <li><strong>Physics:</strong> Work done by a force</li>
                <li><strong>Gram-Schmidt:</strong> Orthogonalization process</li>
                <li><strong>Least Squares:</strong> Best-fit approximations</li>
            </ul>"""
    },
    "linear-independence": {
        "title": "Linear Independence",
        "icon": "🎯",
        "body": """            <h2>What is Linear Independence?</h2>
            <p>A set of vectors is <strong>linearly independent</strong> if no vector in the set can be written as a linear combination of the others.</p>

            <h2>Test for Independence</h2>
            <div class="example-box">
                <p>Vectors $\\vec{v}_1, \\vec{v}_2, \\ldots, \\vec{v}_n$ are linearly independent if the only solution to:</p>
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$c_1\\vec{v}_1 + c_2\\vec{v}_2 + \\cdots + c_n\\vec{v}_n = \\vec{0}$$</p>
                <p>is $c_1 = c_2 = \\cdots = c_n = 0$.</p>
            </div>

            <h2>Quick Check</h2>
            <div class="example-box">
                <p>For 2D vectors: two vectors are linearly dependent if they are parallel (one is a scalar multiple of the other).</p>
                <p>For a matrix: columns are linearly independent iff $\\det(A) \\neq 0$.</p>
            </div>"""
    },
    "basis-vectors": {
        "title": "Basis Vectors",
        "icon": "🏗️",
        "body": """            <h2>What is a Basis?</h2>
            <p>A <strong>basis</strong> for a vector space is a set of vectors that are linearly independent and span the entire space.</p>

            <h2>Standard Basis</h2>
            <div class="example-box">
                <p>For $\\mathbb{R}^2$: $\\{\\vec{e}_1, \\vec{e}_2\\} = \\{(1,0), (0,1)\\}$</p>
                <p>For $\\mathbb{R}^3$: $\\{\\vec{e}_1, \\vec{e}_2, \\vec{e}_3\\} = \\{(1,0,0), (0,1,0), (0,0,1)\\}$</p>
            </div>

            <h2>Key Properties</h2>
            <div class="example-box">
                <p><strong>1.</strong> Every vector in the space has a unique representation as a linear combination of basis vectors.</p>
                <p><strong>2.</strong> The number of basis vectors = the <strong>dimension</strong> of the space.</p>
                <p><strong>3.</strong> A basis must be linearly independent and span the space.</p>
            </div>"""
    },
    "linear-transformations": {
        "title": "Linear Transformations",
        "icon": "🔀",
        "body": """            <h2>What is a Linear Transformation?</h2>
            <p>A <strong>linear transformation</strong> $T: \\mathbb{R}^n \\to \\mathbb{R}^m$ satisfies:</p>
            <div class="example-box">
                <p>$T(\\vec{u} + \\vec{v}) = T(\\vec{u}) + T(\\vec{v})$ &nbsp; (additivity)</p>
                <p>$T(c\\vec{u}) = cT(\\vec{u})$ &nbsp; (homogeneity)</p>
            </div>

            <h2>Matrix Representation</h2>
            <p>Every linear transformation can be represented as matrix multiplication: $T(\\vec{x}) = A\\vec{x}$</p>

            <h2>Common 2D Transformations</h2>
            <div class="example-box">
                <p><strong>Rotation by $\\theta$:</strong> $\\begin{bmatrix}\\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta\\end{bmatrix}$</p>
                <p><strong>Reflection over x-axis:</strong> $\\begin{bmatrix}1 & 0 \\\\ 0 & -1\\end{bmatrix}$</p>
                <p><strong>Scaling by $k$:</strong> $\\begin{bmatrix}k & 0 \\\\ 0 & k\\end{bmatrix}$</p>
            </div>"""
    },
    "orthogonality": {
        "title": "Orthogonality",
        "icon": "⊥",
        "body": """            <h2>What is Orthogonality?</h2>
            <p>Two vectors are <strong>orthogonal</strong> (perpendicular) if their dot product is zero: $\\vec{u} \\cdot \\vec{v} = 0$.</p>

            <h2>Orthogonal Matrices</h2>
            <div class="example-box">
                <p>A square matrix $Q$ is <strong>orthogonal</strong> if its columns form an orthonormal set:</p>
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$Q^T Q = QQ^T = I, \\text{ so } Q^{-1} = Q^T$$</p>
            </div>

            <h2>Orthonormal Sets</h2>
            <div class="example-box">
                <p>A set of vectors is <strong>orthonormal</strong> if every pair is orthogonal AND each vector has magnitude 1.</p>
                <p>$\\vec{u}_i \\cdot \\vec{u}_j = \\begin{cases} 1 & i = j \\\\ 0 & i \\neq j \\end{cases}$</p>
            </div>"""
    },
    "matrix-rank": {
        "title": "Matrix Rank",
        "icon": "🏅",
        "body": """            <h2>What is the Rank of a Matrix?</h2>
            <p>The <strong>rank</strong> of a matrix is the number of linearly independent rows (or columns) — equivalently, the dimension of the column space.</p>

            <h2>How to Find Rank</h2>
            <div class="example-box">
                <p>Row-reduce the matrix to row echelon form. The number of <strong>non-zero rows</strong> is the rank.</p>
            </div>

            <h2>Rank-Nullity Theorem</h2>
            <div class="example-box">
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$\\text{rank}(A) + \\text{nullity}(A) = n$$</p>
                <p>where $n$ is the number of columns.</p>
            </div>

            <h2>Key Facts</h2>
            <div class="example-box">
                <p>$\\text{rank}(A) = \\text{rank}(A^T)$ — row rank equals column rank.</p>
                <p>A square $n\\times n$ matrix is invertible iff $\\text{rank}(A) = n$.</p>
            </div>"""
    },
    "null-space": {
        "title": "Null Space",
        "icon": "∅",
        "body": """            <h2>What is the Null Space?</h2>
            <p>The <strong>null space</strong> (or kernel) of a matrix $A$ is the set of all vectors $\\vec{x}$ such that $A\\vec{x} = \\vec{0}$.</p>
            <p style="text-align:center; font-size:1.2rem; margin:1.5rem 0;">$$\\text{Null}(A) = \\{\\vec{x} : A\\vec{x} = \\vec{0}\\}$$</p>

            <h2>Finding the Null Space</h2>
            <div class="example-box">
                <p>1. Write the augmented matrix $[A | \\vec{0}]$</p>
                <p>2. Row-reduce to RREF</p>
                <p>3. Express free variables as parameters</p>
                <p>4. Write the general solution</p>
            </div>

            <h2>Nullity</h2>
            <div class="example-box">
                <p>The <strong>nullity</strong> = dimension of the null space = number of free variables.</p>
                <p>By the Rank-Nullity Theorem: $\\text{rank}(A) + \\text{nullity}(A) = n$</p>
            </div>"""
    },
    "systems-linear-equations": {
        "title": "Systems of Linear Equations",
        "icon": "⚡",
        "body": """            <h2>What is a System of Linear Equations?</h2>
            <p>A collection of linear equations involving the same variables. In matrix form: $A\\vec{x} = \\vec{b}$</p>

            <h2>Types of Solutions</h2>
            <div class="example-box">
                <p><strong>Unique solution:</strong> Lines/planes intersect at exactly one point. ($\\det(A) \\neq 0$)</p>
                <p><strong>Infinite solutions:</strong> Equations are dependent (one is a multiple of another).</p>
                <p><strong>No solution:</strong> Equations are inconsistent (parallel lines).</p>
            </div>

            <h2>Solution Methods</h2>
            <div class="example-box">
                <p><strong>1. Substitution</strong> — solve one equation, substitute into others.</p>
                <p><strong>2. Elimination (Gaussian)</strong> — row-reduce via elementary operations.</p>
                <p><strong>3. Cramer's Rule</strong> — use determinants for small systems.</p>
                <p><strong>4. Matrix Inverse</strong> — $\\vec{x} = A^{-1}\\vec{b}$ (when $A$ is invertible).</p>
            </div>"""
    },
    "gaussian-elimination": {
        "title": "Gaussian Elimination",
        "icon": "🔄",
        "body": """            <h2>What is Gaussian Elimination?</h2>
            <p><strong>Gaussian elimination</strong> is a systematic method to solve systems of linear equations by row-reducing the augmented matrix to row echelon form.</p>

            <h2>Elementary Row Operations</h2>
            <div class="example-box">
                <p><strong>R1:</strong> Swap two rows</p>
                <p><strong>R2:</strong> Multiply a row by a non-zero scalar</p>
                <p><strong>R3:</strong> Add a multiple of one row to another</p>
            </div>

            <h2>Steps</h2>
            <div class="example-box">
                <p><strong>1.</strong> Write the augmented matrix $[A|\\vec{b}]$</p>
                <p><strong>2.</strong> Forward elimination: create zeros below each pivot</p>
                <p><strong>3.</strong> Back substitution: solve from the bottom row upward</p>
            </div>"""
    },
    "row-echelon-form": {
        "title": "Row Echelon Form",
        "icon": "📊",
        "body": """            <h2>Row Echelon Form (REF)</h2>
            <p>A matrix is in <strong>REF</strong> when:</p>
            <div class="example-box">
                <p>1. All zero rows are at the bottom.</p>
                <p>2. Each leading entry (pivot) is to the right of the pivot above it.</p>
                <p>3. All entries below a pivot are zero.</p>
            </div>

            <h2>Reduced Row Echelon Form (RREF)</h2>
            <p>RREF adds two more conditions:</p>
            <div class="example-box">
                <p>4. Each pivot is 1.</p>
                <p>5. All entries <em>above</em> a pivot are also zero.</p>
            </div>

            <h2>Example</h2>
            <div class="example-box">
                <p style="text-align:center; font-size:1.1rem; margin:1rem 0;">
                    $$\\text{RREF: }\\begin{bmatrix} 1 & 0 & 2 \\\\ 0 & 1 & -1 \\\\ 0 & 0 & 0 \\end{bmatrix}$$
                </p>
            </div>"""
    },
    "matrix-trace": {
        "title": "Matrix Trace",
        "icon": "✨",
        "body": """            <h2>What is the Trace?</h2>
            <p>The <strong>trace</strong> of a square matrix $A$ is the sum of its main diagonal elements:</p>
            <p style="text-align:center; font-size:1.3rem; margin:1.5rem 0;">$$\\text{tr}(A) = \\sum_{i=1}^n a_{ii} = a_{11} + a_{22} + \\cdots + a_{nn}$$</p>

            <h2>Example</h2>
            <div class="example-box">
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">
                    $$\\text{tr}\\begin{bmatrix} 3 & 1 \\\\ 2 & 7 \\end{bmatrix} = 3 + 7 = 10$$
                </p>
            </div>

            <h2>Properties</h2>
            <div class="example-box">
                <p><strong>1.</strong> $\\text{tr}(A+B) = \\text{tr}(A) + \\text{tr}(B)$</p>
                <p><strong>2.</strong> $\\text{tr}(cA) = c\\,\\text{tr}(A)$</p>
                <p><strong>3.</strong> $\\text{tr}(AB) = \\text{tr}(BA)$</p>
                <p><strong>4.</strong> $\\text{tr}(A) = \\sum \\lambda_i$ (sum of eigenvalues)</p>
            </div>"""
    },
    "gram-schmidt": {
        "title": "Gram-Schmidt Process",
        "icon": "🎯",
        "body": """            <h2>What is the Gram-Schmidt Process?</h2>
            <p>The <strong>Gram-Schmidt process</strong> converts a set of linearly independent vectors into an orthonormal set spanning the same space.</p>

            <h2>Algorithm</h2>
            <div class="example-box">
                <p>Given vectors $\\{\\vec{v}_1, \\vec{v}_2, \\ldots, \\vec{v}_n\\}$:</p>
                <p><strong>Step 1:</strong> $\\vec{u}_1 = \\vec{v}_1$</p>
                <p><strong>Step 2:</strong> $\\vec{u}_2 = \\vec{v}_2 - \\text{proj}_{\\vec{u}_1}\\vec{v}_2$</p>
                <p><strong>Step k:</strong> $\\vec{u}_k = \\vec{v}_k - \\sum_{j=1}^{k-1}\\text{proj}_{\\vec{u}_j}\\vec{v}_k$</p>
                <p><strong>Normalize:</strong> $\\vec{e}_k = \\dfrac{\\vec{u}_k}{|\\vec{u}_k|}$</p>
            </div>

            <h2>Application: QR Decomposition</h2>
            <div class="example-box">
                <p>Gram-Schmidt produces the $Q$ factor in $A = QR$, where $Q$ is orthogonal and $R$ is upper triangular.</p>
            </div>"""
    },
    "diagonalization": {
        "title": "Diagonalization",
        "icon": "🔢",
        "body": """            <h2>What is Diagonalization?</h2>
            <p>A matrix $A$ is <strong>diagonalizable</strong> if it can be written as $A = PDP^{-1}$, where $D$ is diagonal (containing eigenvalues) and $P$ contains the corresponding eigenvectors.</p>

            <h2>Steps to Diagonalize</h2>
            <div class="example-box">
                <p><strong>1.</strong> Find all eigenvalues $\\lambda_i$ by solving $\\det(A - \\lambda I) = 0$</p>
                <p><strong>2.</strong> Find eigenvectors for each eigenvalue</p>
                <p><strong>3.</strong> Form $P$ (columns = eigenvectors) and $D$ (diagonal = eigenvalues)</p>
                <p><strong>4.</strong> Verify: $A = PDP^{-1}$</p>
            </div>

            <h2>When is a Matrix Diagonalizable?</h2>
            <div class="example-box">
                <p>An $n\\times n$ matrix is diagonalizable iff it has $n$ linearly independent eigenvectors.</p>
                <p>Matrices with $n$ distinct eigenvalues are always diagonalizable.</p>
            </div>"""
    },
    "column-row-space": {
        "title": "Column & Row Space",
        "icon": "📐",
        "body": """            <h2>Column Space</h2>
            <p>The <strong>column space</strong> (range) of $A$ is the set of all linear combinations of the columns of $A$:</p>
            <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$\\text{Col}(A) = \\{A\\vec{x} : \\vec{x} \\in \\mathbb{R}^n\\}$$</p>

            <h2>Row Space</h2>
            <p>The <strong>row space</strong> of $A$ is the set of all linear combinations of the rows of $A$ = $\\text{Col}(A^T)$.</p>

            <h2>Key Facts</h2>
            <div class="example-box">
                <p><strong>dim(Col(A)) = rank(A)</strong> — the column rank.</p>
                <p><strong>dim(Row(A)) = rank(A)</strong> — row rank always equals column rank.</p>
                <p>The column space tells you which $\\vec{b}$ values make $A\\vec{x} = \\vec{b}$ consistent.</p>
            </div>"""
    },
    "lu-decomposition": {
        "title": "LU Decomposition",
        "icon": "🧮",
        "body": """            <h2>What is LU Decomposition?</h2>
            <p><strong>LU decomposition</strong> factors a matrix $A$ into a lower triangular matrix $L$ and an upper triangular matrix $U$: $A = LU$.</p>

            <h2>Structure</h2>
            <div class="example-box">
                <p>$L$ has 1s on the diagonal and zeros above.</p>
                <p>$U$ is upper triangular (zeros below the diagonal).</p>
                <p style="text-align:center; font-size:1.1rem; margin:1rem 0;">
                    $$A = LU = \\begin{bmatrix} 1 & 0 \\\\ l_{21} & 1 \\end{bmatrix}\\begin{bmatrix} u_{11} & u_{12} \\\\ 0 & u_{22} \\end{bmatrix}$$
                </p>
            </div>

            <h2>Why Use LU?</h2>
            <div class="example-box">
                <p>Solving $A\\vec{x} = \\vec{b}$ becomes two easy triangular solves:</p>
                <p><strong>1.</strong> Solve $L\\vec{y} = \\vec{b}$ (forward substitution)</p>
                <p><strong>2.</strong> Solve $U\\vec{x} = \\vec{y}$ (back substitution)</p>
            </div>"""
    },
    "least-squares": {
        "title": "Least Squares",
        "icon": "📈",
        "body": """            <h2>What is Least Squares?</h2>
            <p>When $A\\vec{x} = \\vec{b}$ has no exact solution, the <strong>least squares</strong> solution $\\hat{x}$ minimizes $|A\\hat{x} - \\vec{b}|^2$.</p>

            <h2>Normal Equation</h2>
            <div class="example-box">
                <p>The least squares solution satisfies the <strong>normal equation</strong>:</p>
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$A^T A\\hat{x} = A^T\\vec{b}$$</p>
                <p>So: $\\hat{x} = (A^T A)^{-1} A^T\\vec{b}$</p>
            </div>

            <h2>Geometric Meaning</h2>
            <div class="example-box">
                <p>$A\\hat{x}$ is the projection of $\\vec{b}$ onto the column space of $A$.</p>
                <p>The residual $\\vec{b} - A\\hat{x}$ is perpendicular to the column space.</p>
            </div>"""
    },
    "change-of-basis": {
        "title": "Change of Basis",
        "icon": "🔀",
        "body": """            <h2>What is Change of Basis?</h2>
            <p>Coordinates of a vector depend on the basis. A <strong>change of basis</strong> re-expresses the same vector using a different basis.</p>

            <h2>Change of Basis Matrix</h2>
            <div class="example-box">
                <p>If $B = \\{\\vec{b}_1, \\vec{b}_2\\}$ is a new basis, the <strong>change of basis matrix</strong> $P$ has the new basis vectors as its columns:</p>
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$P = [\\vec{b}_1 \\mid \\vec{b}_2]$$</p>
                <p>Convert from $B$-coordinates to standard: $\\vec{x} = P\\vec{x}_B$</p>
                <p>Convert from standard to $B$: $\\vec{x}_B = P^{-1}\\vec{x}$</p>
            </div>

            <h2>Transformation in a New Basis</h2>
            <div class="example-box">
                <p>If $A$ represents a transformation in standard coordinates, then in the $B$ basis it becomes:</p>
                <p style="text-align:center; font-size:1.2rem; margin:1rem 0;">$$A_B = P^{-1}AP$$</p>
            </div>"""
    },
}


def generate_pages():
    topics_dir = os.path.join("frontend", "topics")
    os.makedirs(topics_dir, exist_ok=True)

    for quiz_type, info in TOPICS.items():
        filepath = os.path.join(topics_dir, f"{quiz_type}.html")
        content = TEMPLATE.format(
            title=info["title"],
            icon=info["icon"],
            quiz_type=quiz_type,
            body=info["body"]
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated: {filepath}")

    print(f"Done! Generated {len(TOPICS)} topic pages.")


if __name__ == "__main__":
    generate_pages()
