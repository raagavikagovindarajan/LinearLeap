# LinearLeap - HTML Frontend

## 🎉 Your HTML Frontend is Ready!

This new HTML/CSS/JavaScript frontend is a modern alternative to the Streamlit version. **Your original Streamlit code is completely untouched and safe!**

## 📁 File Structure

```
LinearLeap/
├── api.py                    # Flask API backend (NEW)
├── frontend/                 # HTML frontend (NEW)
│   ├── index.html           # Home page
│   ├── quiz.html            # Quiz page
│   ├── learn.html           # Learn page
│   ├── css/
│   │   └── style.css        # Styling with theme support
│   └── js/
│       ├── script.js        # Quiz logic
│       └── theme.js         # Theme toggle
│
├── app.py                   # Original Streamlit app (UNTOUCHED)
├── learn.py                 # Original Streamlit learn page (UNTOUCHED)
└── quizzes/                 # Original quiz files (UNTOUCHED)
```

## 🚀 How to Run

### Step 1: Install Flask (if not installed)
```bash
pip install flask flask-cors
```

### Step 2: Start the Flask API Server
```bash
python api.py
```
You should see:
```
🚀 LinearLeap API Server starting...
📡 Matrix Quiz: http://localhost:5000/api/quiz/matrix
📡 Vectors Quiz: http://localhost:5000/api/quiz/vectors
```

### Step 3: Open the Frontend
Open `frontend/index.html` in your browser:
- Double-click the file, OR
- Right-click → Open with → Your browser

## ✨ Features

- ✅ **Modern UI** with glassmorphism effects and gradients
- ✅ **Dark/Light Theme Toggle** with local storage
- ✅ **Matrix Quiz** with beautiful LaTeX rendering
- ✅ **Vectors Quiz** with LaTeX rendering
- ✅ **Learn Page** with educational content
- ✅ **Responsive Design** works on all devices
- ✅ **Flask API Backend** for serving quiz questions

## 🔄 Switching Back to Streamlit

Your original Streamlit app is completely safe! To go back:

```bash
streamlit run app.py
```

## 🎨 Customization

- **Colors**: Edit CSS variables in `frontend/css/style.css`
- **Quiz Questions**: Edit questions in `api.py`
- **Content**: Modify HTML files in `frontend/`

## 🐛 Troubleshooting

### "Failed to load quiz"
- Make sure `python api.py` is running
- Check that the API is at `http://localhost:5000`

### Matrices not rendering
- Ensure you have internet connection (KaTeX loads from CDN)
- Check browser console for errors

## 📝 Notes

- The API server must be running for quizzes to work
- Quiz questions are served from the Flask API
- Theme preference is saved in browser localStorage
- All your original Streamlit code remains intact!

Enjoy your new HTML frontend! 🎉
