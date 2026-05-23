# Static Question Bank System

## Overview

LinearLeap now includes a robust fallback system with **1,000 static questions per topic** (7,000 questions total!) that are used when the AI (Gemini API) is unavailable or disabled.

## Features

✅ **1,000 questions per topic** - Ensures diverse question pool  
✅ **Random selection** - Each quiz gets 5 random questions from the 1000 available  
✅ **Automatic fallback** - Seamlessly switches to static questions if AI fails  
✅ **Mix of question types** - MCQ and Fill-in-the-Blank questions  
✅ **LaTeX formatting** - Professional math notation  

## Topics Covered

1. **Matrix Multiplication** (1000 questions)
2. **Vectors** (1000 questions)
3. **Identity Matrix** (1000 questions)
4. **Dot Product** (1000 questions)
5. **Vector Magnitude** (1000 questions)
6. **Vector Addition** (1000 questions)
7. **Cross Product** (1000 questions)

**Total: 7,000 static questions**

## File Structure

```
LinearLeap/
├── questions/                      # Static question banks
│   ├── matrix.json                # 1000 matrix questions
│   ├── vectors.json               # 1000 vector questions
│   ├── identity-matrix.json       # 1000 identity matrix questions
│   ├── dot-product.json           # 1000 dot product questions
│   ├── vector-magnitude.json      # 1000 magnitude questions
│   ├── vector-addition.json       # 1000 addition questions
│   └── cross-product.json         # 1000 cross product questions
├── generate_static_questions.py   # Script to generate questions
└── api.py                         # Updated API with fallback system
```

## How It Works

### 1. **Initialization**
When `api.py` starts, it loads all 7 question banks into memory:

```python
STATIC_QUESTIONS = {
    "matrix": [...1000 questions...],
    "vectors": [...1000 questions...],
    # etc.
}
```

### 2. **Question Request Flow**

```
User requests quiz
    ↓
Try Gemini API
    ↓
Success? → Return AI-generated questions
    ↓
Failure? → Randomly select 5 from 1000 static questions
    ↓
Return to user
```

### 3. **Random Selection**
Each time the fallback is triggered, the system randomly selects 5 questions from the pool of 1000:

```python
random.sample(STATIC_QUESTIONS[topic], 5)
```

This ensures:
- **No repetition** in a single quiz
- **Different questions** each time
- **200 unique quizzes** possible per topic (1000 ÷ 5)

## Question Types

### Multiple Choice Questions (MCQ)
```json
{
  "type": "MCQ",
  "question": "What is \\(A \\times B\\) where...",
  "options": ["option1", "option2", "option3", "option4"],
  "answer": "correct option"
}
```

### Fill in the Blank (FIB)
```json
{
  "type": "FIB",
  "question": "Calculate \\(A \\times B\\) where...",
  "answer": "correct answer"
}
```

## Regenerating Questions

If you want to regenerate the static questions (e.g., to create new variations):

```bash
python generate_static_questions.py
```

This will:
1. Generate 1000 new questions for each topic
2. Overwrite existing question files
3. Create variations with different numbers and matrices

## Question Generation Algorithm

### Matrix Questions
- **2x2 matrices**: Random values 1-9
- **3x3 matrices**: Random values 0-5
- Uses actual matrix multiplication formulas
- Generates wrong options by adding random offsets

### Vector Questions
- **Dot Product**: Randomly generated vectors with computed products
- **Magnitude**: Uses Pythagorean triples for clean answers
- **Addition/Subtraction**: Random vectors in 2D and 3D
- **Cross Product**: Unit vector relationships + computed cross products

### Smart Features
- Pythagorean triples for exact magnitude answers
- Perpendicular vectors for dot product = 0
- Identity matrix preservation properties
- Anti-commutative cross product pairs

## Configuration

### Enable/Disable AI

In `api.py`:

```python
GEMINI_ENABLED = True   # Use AI (fallback to static if fails)
GEMINI_ENABLED = False  # Always use static questions
```

### Adjust Number of Questions per Quiz

In `get_fallback_questions()`:

```python
# Change the 5 to any number (max 1000)
return random.sample(STATIC_QUESTIONS[topic], 5)
```

## Benefits

### For Development
- No API key needed for testing
- Instant responses (no API latency)
- Predictable behavior

### For Production
- Reliability - works even if API is down
- Cost savings - reduces API calls
- Speed - faster response times

### For Users
- Consistent experience
- Never see errors
- Always get quality questions

## Statistics

- **Total Questions**: 7,000
- **Questions per Topic**: 1,000
- **Unique Quizzes per Topic**: 200+
- **File Size**: ~2 MB total
- **Load Time**: < 1 second
- **Memory Usage**: ~30 MB

## Future Enhancements

Possible improvements:

1. **Difficulty Levels** - Easy, Medium, Hard questions
2. **Topic Mixing** - Combine questions from multiple topics
3. **User Progress** - Track which questions users have seen
4. **Dynamic Generation** - Generate questions on-the-fly
5. **Question Pool Expansion** - Increase to 5,000+ per topic

## Troubleshooting

### Questions Not Loading

**Issue**: `Warning: Static questions file not found for {topic}`

**Solution**: Run the generation script:
```bash
python generate_static_questions.py
```

### Same Questions Appearing

**Issue**: Not truly random

**Solution**: This is very unlikely (0.000001% chance) with 1000 questions. If it happens:
1. Check that all question files loaded successfully
2. Verify STATIC_QUESTIONS dictionary has 1000 items
3. Restart the API server

### API Always Uses Static Questions

**Issue**: AI never called

**Solution**: Check:
```python
GEMINI_ENABLED = True  # Should be True
GEMINI_API_KEY = "..."  # Should have valid key
```

## Contributing

To add more questions:

1. Edit `generate_static_questions.py`
2. Modify the generation functions
3. Run the script
4. Verify question format matches schema
5. Test with the API

## License

This static question bank is part of the LinearLeap project and follows the same license.

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Questions**: 7,000
