# 🧠 GenAI Practical 1 – NLP Pipeline Demo

A beginner-friendly **Natural Language Processing (NLP) Pipeline** built using **Python, Streamlit, and spaCy**. This application demonstrates essential NLP preprocessing techniques through an interactive web interface.

---

## 📌 Project Overview

This project allows users to enter any text and explore the different stages of an NLP pipeline. It is designed as a practical implementation for learning the fundamentals of Natural Language Processing.

---

## ✨ Features

- 📝 Text Input Interface
- 🔤 Tokenization
- 🚫 Stopword Removal
- 🏷️ Part-of-Speech (POS) Tagging
- 📚 Lemmatization
- 🧑‍💼 Named Entity Recognition (NER)
- 🔗 Dependency Parsing
- 📄 Sentence Segmentation
- 📊 Word Frequency Analysis
- 📈 Text Statistics

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- spaCy
- Pandas

---

## 📂 Project Structure

```
Gen_AI_Practical_1/
│
├── practical1.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Srushti-bit/Gen_AI_Practical_1.git
cd Gen_AI_Practical_1
```

### 2. Create a Virtual Environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the spaCy English Model

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the Application

```bash
streamlit run practical1.py
```

or

```bash
python -m streamlit run practical1.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📷 Sample Input

```
Artificial Intelligence is transforming industries around the world. Companies such as Microsoft, Google, Amazon, and OpenAI are investing heavily in AI research. Python is one of the most popular programming languages for Machine Learning and Natural Language Processing.
```

---

## 📊 Output

The application performs:

- Tokenization
- Stopword Removal
- POS Tagging
- Lemmatization
- Named Entity Recognition
- Dependency Parsing
- Sentence Segmentation
- Word Frequency Analysis
- Text Statistics

---

## 📦 Dependencies

```
streamlit
spacy
pandas
```

---

## 🎯 Learning Outcomes

Through this project, you will understand:

- NLP preprocessing pipeline
- Text tokenization
- Removing stopwords
- Part-of-speech tagging
- Lemmatization
- Named Entity Recognition
- Dependency parsing
- Sentence segmentation
- Word frequency analysis
- Building interactive NLP applications using Streamlit

---

## 👩‍💻 Author

**Srushti Lohakare**

MCA Student | AI & Machine Learning Enthusiast

GitHub: https://github.com/Srushti-bit

---

## 📄 License

This project is created for educational and learning purposes.
