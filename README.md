# 🧙 SQLAgent

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)  
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)  
![Gemini AI](https://img.shields.io/badge/AI-Google%20Gemini-green)  
![SpeechRecognition](https://img.shields.io/badge/Voice-SpeechRecognition-yellow)  

---

SQLAgent is an **AI-powered database assistant** that makes it super easy to talk to your database in plain language.  
No need to remember complicated SQL queries — just type (or even speak) what you want, and SQLAgent will handle the rest.  

The goal is simple:  
👉 To help beginners, non-technical users, and even busy professionals interact with databases without stress.  

---

## ✨ What It Can Do
- **Ask in Your Own Words** → Write queries in natural language and get correct SQL instantly.  
- **Talk Instead of Typing** → Use voice input if you prefer speaking your query.  
- **Instant Execution** → Run generated queries directly on MySQL and see results on the spot.  
- **Know Your Database** → Get a quick view of table names and columns before writing queries.  
- **Multi-Language Support** → Query in different languages, no barriers.   
- **Easy to Grow** → Modular design so new features can be plugged in later.  
- **Learn as You Go** → Each generated SQL comes with a short explanation of what it does.  
- **Never Lose Track** → History of past queries and results for review.  

---

## 🛠️ Tech Stack

- **Frontend**  
  - Streamlit → clean and interactive web interface  

- **Backend / Core**  
  - Python → application logic and integration  
  - Google Gemini → converts natural language(NLP) into SQL  
  - SpeechRecognition → enables voice-based query input  
  - Deep Translator → supports queries in multiple languages(English, Hindi, etc)

- **Database**  
  - MySQL → query execution and data storage  

- **Other Tools**  
  - venv → virtual environment for dependency management  
  - pip → package installation and management  

---


## 📸 A Quick Look
Here’s how the system works in action (screenshots to be added):  

| User Interface |


| Natural Query | SQL Generated | Results | Explanation |
|---------------|--------------|---------|-------------|
| ![input](images/input.png) | ![sql](images/sql.png) | ![results](images/results.png) | ![explanation](images/explanation.png) |

👉 Add 4–5 screenshots in an `images/` folder and link them here.

---

## 🔑 How to Use
1. **Log in** → Start the app and sign in with your credentials.  
2. **Pick a Database** → Select the MySQL database you want to query.  
3. **Ask Your Question**  
   - 💬 Type in natural language, or  
   - 🎙️ Speak directly using the microphone.  
4. **Review the SQL** → See the query generated for you, along with a simple explanation.  
5. **Execute** → Run the SQL and check results instantly.  
6. **History** → Look back at previous queries and outputs anytime.  

---

## 🔮 Future goals
- Rich visual outputs (graphs & charts)  
- Multiple AI model support  
- Role-based access control  
- Cloud-hosted database connectivity  
- Mobile-friendly UI  

---

