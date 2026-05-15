# 🎬 Netflix-Style Movie Recommendation System using Python, Machine Learning, NLP, FastAPI & Streamlit

A Full-Stack **Netflix-style Movie Recommendation Web Application** built using Python, Machine Learning, NLP, FastAPI, Streamlit & External APIs.

This project mimics how streaming platforms like Netflix recommend similar movies using Content-Based Filtering and NLP.
---
## 📸 App Screenshots

### Home Page
<img width="1918" height="1142" alt="{DAEF18A8-B507-4470-A586-DA9F7DC01194}" src="https://github.com/user-attachments/assets/d1916daa-0882-4f14-b50e-5b8c6e93fdf0" />
### Recommendations
<img width="1920" height="1137" alt="{6C22A8C5-B6F8-462D-93D5-F948D511F5C2}" src="https://github.com/user-attachments/assets/ddb10811-30b4-4792-96ec-f6302dfab8dd" />
<img width="1920" height="1141" alt="{C17ACAF1-510B-4E69-B0F5-5462C499E13F}" src="https://github.com/user-attachments/assets/58f2a9c9-2281-4307-a863-fc3014d15362" />
<img width="1920" height="1143" alt="{10226A71-FCB1-48E8-84A4-37C402431F46}" src="https://github.com/user-attachments/assets/3bb644d9-7880-436c-9761-fc8f5b31e761" />
### API Response Screenshots
<img width="1920" height="1140" alt="{F0A1D2C0-334A-4FCD-B38F-B8473C418249}" src="https://github.com/user-attachments/assets/0901b985-186e-46be-b18c-a20860076aaa" />

<img width="1920" height="1138" alt="{5C0786B9-A26C-47DD-9B2C-C2F95201895C}" src="https://github.com/user-attachments/assets/fb52bc38-cf7e-4dbb-9dd1-18027e23807b" />
<img width="1920" height="1140" alt="{F0A1D2C0-334A-4FCD-B38F-B8473C418249}" src="https://github.com/user-attachments/assets/e52aa313-893a-4b50-89c8-1190edeb76e5" />



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

