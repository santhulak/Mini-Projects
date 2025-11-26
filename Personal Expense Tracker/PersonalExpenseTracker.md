<!-- PROJECT BANNER -->
<p align="center">
  <img src="https://via.placeholder.com/1000x250?text=Personal+Expense+Tracker+%7C+Python+Mini+Project" alt="Project Banner">
</p>

<h1 align="center">💰 Personal Expense Tracker — Python Mini Project</h1>

<p align="center">
A simple, beginner-friendly personal finance system built with Python.<br>
Comes with a Command-Line Interface, a Streamlit Web App, and a Tkinter Desktop App — all connected to the same CSV database.
</p>

---

# 🧩 **Project Overview**

This mini project helps you **add, view, summarize, and manage daily expenses** through multiple interfaces:

| Interface | Description |
|----------|-------------|
| 🖥️ **CLI** | Add/view/delete/summary/plots via terminal |
| 🌐 **Streamlit Web App** | Beautiful browser UI with charts |
| 🪟 **Tkinter Desktop App** | Offline window-based GUI |

All versions share the same file:
expenses.csv

---

## 📁 Project Structure

📦 personal-expense-tracker
├─ 📄 expense_tracker.py — CLI Tool
├─ 🌐 streamlit_app.py — Streamlit Web UI
├─ 🖥️ tkinter_app.py — Tkinter Desktop App
├─ 📊 expenses.csv — Auto-created on first run
├─ 📘 requirements.txt
└─ 📝 README.md

---

# 🛠️ **1. Setup Instructions**

Follow these steps to configure the project on your system.

---

## 🔹 **Step 1 — Install Python**
Make sure Python 3.8 or above is installed 👍  
Download: https://www.python.org/downloads/

---

## 🔹 **Step 2 — Create and Open Your Project Folder**
personal-expense-tracker/
Open the folder in **VS Code**.

---

## 🔹 **Step 3 — Create a Virtual Environment**

**Windows PowerShell**
python -m venv .venv
..venv\Scripts\Activate.ps1

**Mac / Linux**

python3 -m venv .venv
source .venv/bin/activate

---

## 🔹 **Step 4 — Install Required Libraries**
Install:

- pandas  
- matplotlib  
- streamlit  

---

## 🔹 **Step 5 — Add Main Files**
Create these files in your project folder:

- `expense_tracker.py`
- `streamlit_app.py`
- `tkinter_app.py`

Paste the respective code into them.

---

# 💻 **2. Run Each Interface**

Below are the user steps for each app type.

---

## 🧮 **A. CLI Expense Tracker**

### ▶ **How to run**
- Open VS Code terminal  
- Activate the virtual environment  
- Run the CLI script  

### 🧾 Features
- Add expenses  
- View all expenses  
- View date-filtered expenses  
- Monthly summary  
- Plot charts (PNG)  
- Export CSV  

---

## 🌐 **B. Streamlit Web App**

### ▶ **How to launch**
Go to terminal → run Streamlit.

It will open automatically in your browser.

### 🌟 Features
- Add expenses via a friendly form  
- View records in a data table  
- Month-wise charts  
- Delete entries easily  

### 📍 Default URL
http://localhost:8501

---

## 🪟 **C. Tkinter Desktop App**

### ▶ **How to run**
Open terminal → activate venv → run the Tkinter file.

### 🌟 Features
- Offline GUI  
- Add new expenses  
- View expenses in a table  

---

# 🔧 **3. Optional: VS Code Automation**

You can make development easier with:

## ⚙️ `.vscode/launch.json`
- Debug CLI commands with predefined arguments

## 🚀 `.vscode/tasks.json`
- Run Streamlit / Tkinter / CLI with one click  
- `Terminal → Run Task…`

---

# 🔄 **4. App Workflow Diagram**

          ┌──────────────────────┐
          │   expense_tracker.py │
          │        (CLI)         │
          └──────────┬───────────┘
                     │
                     ▼
              ┌────────────┐
              │ expenses.csv│
              └────────────┘
                     ▲
    ┌────────────────┴────────────────┐
    │                                 │
    ▼                                 ▼

All three apps read/write the same CSV file.

---

# 🧰 **5. Troubleshooting**

### ❌ *ModuleNotFoundError: pandas*
- Virtual environment not activated  
- Wrong Python interpreter selected in VS Code  

### ❌ Streamlit not opening
- Copy URL from terminal  
- Or run on a different port  

### ❌ Tkinter error on macOS
Install Tk:
brew install python-tk

---

# 🚀 **6. Future Improvements**

Enhancements you can add:

- SQLite database (instead of CSV)  
- Login system  
- Pie charts & analytics  
- Export to Excel/PDF  
- Automate monthly budget alerts  
- Deploy Streamlit online (Streamlit Cloud / HuggingFace Spaces)  

---

# 👤 **7. Author**

**Santhana Lakshmi**  
GitHub: *santhulak*

---

# 📜 **8. License**

MIT License  
(You can replace this with any license you prefer.)

---

<p align="center">
✨ Built with Python. Designed for beginners. Ready for real-world use. ✨
</p>



