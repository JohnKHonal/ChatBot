# 🤖 Timetable Chatbot using Boyer–Moore Algorithm

This project is a **Python-based chatbot** that helps students quickly retrieve their class schedule, subject details, and faculty information using natural language queries.

It uses the **Boyer–Moore string searching algorithm** for efficient keyword detection and provides intelligent responses based on user input.

---

## 🚀 Project Overview

The chatbot allows users to ask questions like:

* *"What class is on Monday at 09:30?"*
* *"Friday schedule"*
* *"Which class do I have at 10:10 on Tuesday?"*

The system processes the query, extracts **day and time**, and returns the corresponding subject and faculty details.

---

## 🧠 Key Features

* 🔍 Fast text search using Boyer–Moore algorithm
* 📅 Day-wise timetable retrieval
* ⏰ Time-based class lookup
* 👨‍🏫 Subject + Faculty information
* 🧹 Input normalization for better accuracy
* 💬 Interactive chatbot interface

---

## 🏗️ Project Structure

* **Subject Info Mapping** → Maps subject codes to full names and faculty
* **Timetable Data** → Stores weekly schedule
* **Slot Timing System** → Defines class timings
* **Search Algorithm** → Boyer–Moore implementation
* **Query Processing Engine** → Extracts day and time
* **Chat Loop** → Interactive CLI chatbot

---

## ⚙️ Technologies Used

* Python
* Regular Expressions (`re`)
* Boyer–Moore Algorithm (String Matching)

---

## ▶️ How to Run

1. Make sure Python is installed
2. Save the file (e.g., `chatbot.py`)
3. Run the program:

```bash
python chatbot.py
```

4. Start asking questions!

---

## 💡 Example Queries

* What class is on Monday at 09:30?
* Wednesday schedule
* Which class do I have Friday?
* Hello

---

## 📊 How It Works

1. User enters a query
2. Text is normalized (lowercase, cleaned)
3. Day is detected using Boyer–Moore search
4. Time is extracted using regex
5. Matching timetable slot is identified
6. Output is generated with subject and faculty

---

## 📌 Timetable Coverage

* Monday to Friday
* Includes:

  * Class slots
  * Break
  * Lunch

---

## ⚠️ Limitations

* Works only for predefined timetable
* No GUI (CLI-based chatbot)
* Limited natural language understanding

---

## 🔮 Future Improvements

* Add GUI or web interface
* Voice-based chatbot
* Integration with database
* NLP-based understanding (instead of keyword matching)
* Mobile app version

---

## 👤 Author

**John Kamalakar**

---

## ⭐ Note

This project is ideal for:

* Data Structures & Algorithms (string searching)
* Mini projects / academic submissions
* Demonstrating chatbot logic without AI frameworks

---
