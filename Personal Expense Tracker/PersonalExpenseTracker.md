# 💰 Personal Expense Tracker — Python Mini Project

A complete personal finance tracking system built in Python with **three different user interfaces**, all sharing the same CSV data backend:

- ✅ **Command-Line Interface (CLI)** — `expense_tracker.py`
- ✅ **Streamlit Web App** — `streamlit_app.py`
- ✅ **Tkinter Desktop App** — `tkinter_app.py`

This mini project is designed for learning Python, GUI development, and web UI—all in one place.

---

# 🚀 Features

### ✔ CLI App
- Add expenses  
- View all or filter by date/category  
- Delete expenses  
- Monthly summary  
- Generate plots (PNG)  
- Export CSV backup  

### ✔ Streamlit Web App
- Add new expenses using a beautiful web UI  
- View all expenses  
- Monthly charts  
- Delete records  
- Runs locally in the browser  

### ✔ Tkinter Desktop App
- Offline desktop UI  
- Add expenses  
- Display all expenses in a table  
- Save automatically to CSV  

---

# 📂 Project Structure

personal-expense-tracker/
│
├─ .vscode/
│ ├─ launch.json
│ └─ tasks.json
│
├─ expense_tracker.py # CLI app
├─ streamlit_app.py # Streamlit Web UI
├─ tkinter_app.py # Tkinter Desktop UI
├─ requirements.txt
└─ README.md


---

# ⚙️ Setup Instructions (All Platforms)

## 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd personal-expense-tracker

2️⃣ Create & activate virtual environment
Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install dependencies
pip install --upgrade pip
pip install pandas matplotlib streamlit


Save your environment (optional):

pip freeze > requirements.txt

🖥️ CLI Expense Tracker (expense_tracker.py)

Run the script:

python expense_tracker.py --help

➕ Add an expense
python expense_tracker.py add --date 2025-11-25 --category Food --amount 250 --currency INR --payment_method Card --notes "Lunch"

📄 View all expenses
python expense_tracker.py view

📅 View by date range
python expense_tracker.py view --from 2025-11-01 --to 2025-11-30

📊 Monthly summary
python expense_tracker.py summary --year 2025 --month 11

📈 Generate plot
python expense_tracker.py plot --year 2025 --month 11 --out november_plot.png

💾 Export backup
python expense_tracker.py export --out backup.csv

🌐 Streamlit Web App (streamlit_app.py)

Start the app:

streamlit run streamlit_app.py


Browser URL:

http://localhost:8501

Features:

Add Expense

View Expenses

Monthly Summary Chart

Delete Expense

🖥️ Tkinter Desktop App (tkinter_app.py)

Run:

python tkinter_app.py


GUI includes:

Add Expense Form

Dropdown selections

Notes field

Full table view

🛠️ VS Code Setup (Optional)
.vscode/launch.json

Run/debug CLI commands with predefined arguments.

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Add Expense (Debug)",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/expense_tracker.py",
            "console": "integratedTerminal",
            "args": [
                "add",
                "--date", "2025-11-26",
                "--category", "Food",
                "--amount", "200",
                "--currency", "INR",
                "--payment_method", "UPI",
                "--notes", "Dinner debug test"
            ]
        },
        {
            "name": "Python: Plot (Debug)",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/expense_tracker.py",
            "console": "integratedTerminal",
            "args": [
                "plot",
                "--year", "2025",
                "--month", "11",
                "--out", "november_plot.png"
            ]
        }
    ]
}


