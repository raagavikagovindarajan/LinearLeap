// Quiz state
let questions = [];
let currentQuestionIndex = 0;
let userAnswers = [];
let quizType = '';

/**
 * Normalize an answer string for comparison.
 * Strips LaTeX delimiters \\(...\\) and \\[...\\], extra whitespace,
 * and collapses internal spaces so user input like "5" matches stored "\\(5\\)".
 */
function normalizeAnswer(str) {
    if (!str) return '';
    let s = str.trim();
    // Remove LaTeX inline delimiters \( ... \)
    s = s.replace(/\\\(|\\\)/g, '');
    // Remove LaTeX display delimiters \[ ... \]
    s = s.replace(/\\\[|\\\]/g, '');
    // Remove double-escaped delimiters \\( \\)
    s = s.replace(/\\\\\(|\\\\\)/g, '');
    s = s.replace(/\\\\\[|\\\\\]/g, '');
    // Collapse whitespace
    s = s.replace(/\s+/g, ' ').trim();
    return s.toLowerCase();
}

// ============================================================
// DEPLOYMENT CONFIG — update this after deploying to Render:
// 1. Go to render.com, deploy the API, copy the service URL
// 2. Paste it below as RENDER_API_URL (keep the https://)
// ============================================================
const RENDER_API_URL = 'https://linearleap-1.onrender.com';

const API_URL = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
    ? 'http://localhost:5000'
    : RENDER_API_URL;

// Load quiz on page load
document.addEventListener('DOMContentLoaded', () => {
    loadQuiz();
});

// Load quiz from API
async function loadQuiz() {
    try {
        const response = await fetch(`${API_URL}/api/quiz/${quizType}`);
        const data = await response.json();
        questions = data.questions;
        userAnswers = new Array(questions.length).fill('');

        document.getElementById('loading').style.display = 'none';
        document.getElementById('quiz-content').style.display = 'block';

        showQuestion();
    } catch (error) {
        document.getElementById('loading').innerHTML = `
            <p style="color: #ef4444;">❌ Failed to load quiz. Make sure the API server is running:</p>
            <p style="margin-top: 1rem;"><code>python api.py</code></p>
        `;
        console.error('Error loading quiz:', error);
    }
}

// Render LaTeX in element using KaTeX auto-render
function renderMath(text) {
    const temp = document.createElement('div');

    // The JSON strings have two escaping problems when they reach JS:
    //   1. LaTeX commands/delimiters are double-escaped: \\( \\begin \\times → need \( \begin \times
    //   2. Matrix row separators are single-backslash-digit: \3  → need \\ before the digit
    //
    // Fix step 1: replace every \\ (double backslash) with \ (single backslash)
    // Fix step 2: after step 1, lone \<digit> still exists — add the missing backslash
    const step1 = text.replace(/\\\\/g, '\\');
    // Now fix row separators: a single \ immediately before a digit (matrix row break)
    // Replace \<digit> with \\<digit>  so KaTeX sees the proper \\ row separator
    const fixed = step1.replace(/\\(\d)/g, '\\\\$1');

    // Use textContent (not innerHTML) so LaTeX is not further HTML-escaped
    temp.textContent = fixed;

    try {
        // Use KaTeX auto-render to process \(...\) delimiters
        renderMathInElement(temp, {
            delimiters: [
                { left: "\\(", right: "\\)", display: false },
                { left: "\\[", right: "\\]", display: true }
            ],
            throwOnError: false
        });
    } catch (e) {
        console.error('KaTeX rendering error:', e);
        temp.textContent = fixed;
    }

    return temp.innerHTML;
}

// Show current question
function showQuestion() {
    const question = questions[currentQuestionIndex];

    // Update progress
    document.getElementById('progress-text').textContent =
        `Question ${currentQuestionIndex + 1} of ${questions.length}`;

    // Display question
    const questionText = document.getElementById('question-text');
    questionText.innerHTML = renderMath(question.question);

    // Display answer section
    const answerSection = document.getElementById('answer-section');
    answerSection.innerHTML = '';

    if (question.type === 'MCQ') {
        // Multiple choice
        const options = document.createElement('div');
        options.className = 'answer-options';

        question.options.forEach((option, index) => {
            const label = document.createElement('label');
            label.className = 'option-label';

            const radio = document.createElement('input');
            radio.type = 'radio';
            radio.name = 'answer';
            radio.value = option;
            radio.checked = userAnswers[currentQuestionIndex] === option;
            radio.onchange = () => {
                userAnswers[currentQuestionIndex] = option;
            };

            const span = document.createElement('span');
            span.className = 'option-text';
            span.innerHTML = renderMath(option);

            label.appendChild(radio);
            label.appendChild(span);
            options.appendChild(label);
        });

        answerSection.appendChild(options);
    } else {
        // Fill in the blank
        const input = document.createElement('input');
        input.type = 'text';
        input.className = 'answer-input';
        input.placeholder = 'Type your answer here (e.g., 5, (4, 6), or a matrix value)';
        input.value = userAnswers[currentQuestionIndex];
        input.oninput = (e) => {
            userAnswers[currentQuestionIndex] = e.target.value;
        };

        answerSection.appendChild(input);
    }

    // Update buttons
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const submitBtn = document.getElementById('submit-btn');

    // Show/hide Previous button
    if (currentQuestionIndex > 0) {
        prevBtn.style.display = 'block';
    } else {
        prevBtn.style.display = 'none';
    }

    if (currentQuestionIndex < questions.length - 1) {
        nextBtn.style.display = 'block';
        submitBtn.style.display = 'none';
    } else {
        nextBtn.style.display = 'none';
        submitBtn.style.display = 'block';
    }
}

// Previous question
function prevQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        showQuestion();
    }
}

// Next question
function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        showQuestion();
    }
}

// Submit quiz
function submitQuiz() {
    // Calculate score
    let score = 0;
    questions.forEach((q, i) => {
        const userAns = normalizeAnswer(userAnswers[i]);
        const correctAns = normalizeAnswer(q.answer);
        if (userAns === correctAns) {
            score++;
        }
    });

    // Show results
    document.getElementById('quiz-content').style.display = 'none';
    document.getElementById('results-screen').style.display = 'block';

    document.getElementById('final-score').textContent = `${score}/${questions.length}`;

    // Show review
    const reviewSection = document.getElementById('review-section');
    reviewSection.innerHTML = '';

    questions.forEach((q, i) => {
        const item = document.createElement('div');
        item.className = 'review-item';

        const userAns = userAnswers[i] || '(not answered)';
        const isCorrect = normalizeAnswer(userAns) === normalizeAnswer(q.answer);

        item.innerHTML = `
            <h3>Question ${i + 1}</h3>
            <p><strong>Q:</strong> ${renderMath(q.question)}</p>
            <p><strong>Your Answer:</strong> <span class="${isCorrect ? 'correct' : 'incorrect'}">${renderMath(userAns)}</span></p>
            <p><strong>Correct Answer:</strong> <span class="correct">${renderMath(q.answer)}</span></p>
            <p class="${isCorrect ? 'correct' : 'incorrect'}">${isCorrect ? '✅ Correct!' : '❌ Incorrect'}</p>
        `;

        reviewSection.appendChild(item);
    });
}

// Retake quiz
function retakeQuiz() {
    currentQuestionIndex = 0;
    userAnswers = new Array(questions.length).fill('');

    document.getElementById('results-screen').style.display = 'none';
    document.getElementById('quiz-content').style.display = 'block';

    showQuestion();
}

// Navigate to learn page for the current topic
function goToLearnPage() {
    const topicPageMap = {
        'matrix': 'matrix-multiplication',
        'identity-matrix': 'identity-matrix',
        'vectors': 'vectors',
        'dot-product': 'dot-product',
        'vector-magnitude': 'vector-magnitude',
        'vector-addition': 'vector-addition',
        'cross-product': 'cross-product',
        'matrix-transpose': 'matrix-transpose',
        'matrix-determinant': 'matrix-determinant',
        'matrix-inverse': 'matrix-inverse',
        'eigenvalues-eigenvectors': 'eigenvalues-eigenvectors',
        'vector-projection': 'vector-projection',
        'linear-independence': 'linear-independence',
        'basis-vectors': 'basis-vectors',
        'linear-transformations': 'linear-transformations',
        'orthogonality': 'orthogonality',
        'matrix-rank': 'matrix-rank',
        'null-space': 'null-space',
        'systems-linear-equations': 'systems-linear-equations',
        'gaussian-elimination': 'gaussian-elimination',
        'row-echelon-form': 'row-echelon-form',
        'matrix-trace': 'matrix-trace',
        'gram-schmidt': 'gram-schmidt',
        'diagonalization': 'diagonalization',
        'column-row-space': 'column-row-space',
        'lu-decomposition': 'lu-decomposition',
        'least-squares': 'least-squares',
        'change-of-basis': 'change-of-basis'
    };
    const page = topicPageMap[quizType] || 'matrix-multiplication';
    location.href = `topics/${page}.html`;
}
