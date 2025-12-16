# 🧠 Quizzler – Python Quiz App (Tkinter)

Quizzler is an interactive quiz application built using **Python** and **Tkinter**.  
It fetches real-time True/False questions from the **Open Trivia Database (OpenTDB) API**, displays them in a clean GUI, provides instant feedback, and tracks the user's score.

This project demonstrates:
- GUI development with Tkinter
- API integration using `requests`
- Object-Oriented Programming (OOP)
- Handling HTML entities in API responses

---

## ✨ Features

- 🖥️ Clean and responsive Tkinter GUI
- 🌐 Live questions from OpenTDB API
- ✅❌ Instant visual feedback (green/red)
- 🧮 Real-time score tracking
- ⏱️ Automatic transition between questions
- 🧹 Proper handling of HTML-encoded text
- 🚫 Buttons disabled after quiz completion

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **Requests** (API calls)
- **HTML module** (`html.unescape`)
- Object-Oriented Programming (OOP)

---

## 🔌 API Integration

This application fetches quiz questions from the **Open Trivia Database**.

- **Endpoint:** `https://opentdb.com/api.php`
- **Category:** 18 (Science: Computers)
- **Type:** Boolean (True / False)
- **Amount:** 10 questions per session
