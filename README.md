# 🎬 Netflix-Style Movie Recommendation System using Python, Machine Learning, NLP, FastAPI & Streamlit

A Full-Stack **Netflix-style Movie Recommendation Web Application** built using Python, Machine Learning, NLP, FastAPI, Streamlit & External APIs.

This project mimics how streaming platforms like Netflix recommend similar movies using Content-Based Filtering and NLP.
---
## 🚀 Live Demo
👉 Frontend (Streamlit):  
👉 Backend (FastAPI): https://end-to-end-movie-recommendation-system-toqn.onrender.com/docs#/ 
---
## 📌 Project Journey (End-to-End Workflow)

This project follows an **industry-style ML workflow**:

1. Collected real-world movie dataset from Kaggle  
2. Performed initial data analysis in Excel  
3. Conducted EDA in Jupyter Notebook  
4. Applied Feature Engineering & NLP  
5. Built Movie Recommendation ML Model  
6. Integrated Movie Poster API from RapidAPI  
7. Created FastAPI backend for model serving  
8. Built Streamlit frontend UI  
9. Developed using VS Code  
10. Version controlled with Git & GitHub  

This makes the project a true **Production-Ready End-to-End ML Application**.

---
## ✨ Features

- Search any movie from dataset  
- Get Top 10 similar movie recommendations  
- Fetch movie posters using RapidAPI  
- NLP-based similarity engine  
- FastAPI REST API backend  
- Interactive Streamlit web UI  
- Login / Signup system  
- Fully deployable full-stack project
---
## 🧠 Machine Learning Pipeline

### Data Analysis
- Dataset cleaned using Excel & Pandas  
- Missing values handled  
- Dataset understanding & preprocessing  

### Exploratory Data Analysis (Jupyter)
- Distribution & trend analysis  
- Text data exploration  

### Feature Engineering
Combined movie metadata into one text corpus:
- Genres  
- Keywords  
- Overview  
- Cast & Crew  

### NLP + Recommendation Model
Algorithms Used:
- TF-IDF Vectorization  
- Cosine Similarity  
- Content-Based Filtering  

Model returns **Top 10 most similar movies instantly**.

---
## 🔗 API Integration
Movie posters are fetched using RapidAPI Movie Database API.

---
## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| IDE | VS Code(Jupyter Notebook) |
| Data Analysis | Excel, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF |
| Backend | FastAPI |
| Frontend | Streamlit |
| API | RapidAPI |
| Version Control | Git & GitHub |
| Deployment | Render |
|Deployment  |Streamlit |
---
## 📂 Project Structure

End-to-End-Movie-Recommendation-System
│
├── movies.ipynb
├── movies_metadata.csv
├── tfidf.pkl
├── tfidf_matrix.pkl
├── indices.pkl
├── df.pkl
│
├── main.py
├── app.py
├── users.json
├── requirements.txt
└── .gitignore

---

## ⚙️ Installation & Setup

### Clone Repository
Git Clone https://github.com/Ramesh8dsaiml/End-to-End-Movie-Recommendation-System
cd End-to-End-Movie-Recommendation-System

### Create Virtual Environment
python -m venv myenv
myenv\Scripts\activate

### Install Dependencies  
pip install -r requirements.txt

---

## ▶️ Run Backend
uvicorn main:app --reload

## ▶️ Run Frontend
streamlit run app.py

---

## 🔮 Future Improvements
- Add Collaborative Filtering  
- Docker Deployment  
- Cloud Database Integration  
- Better Authentication  
- Improve UI/UX  

---

## 👨‍💻 Author
Ramesh Kumar

If you like this project, please give it a ⭐ on GitHub!

