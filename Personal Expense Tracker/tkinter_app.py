import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import uuid
import os

CSV_FILE = "expenses.csv"

def load_data():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["id", "date", "category", "amount", "currency", "payment_method", "notes"])
        df.to_csv(CSV_FILE, index=False)
    return pd.read_csv(CSV_FILE)

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

def add_expense():
    date = entry_date.get()
    category = entry_category.get()
    amount = entry_amount.get()
    currency = entry_currency.get()
    payment = entry_payment.get()
    notes = entry_notes.get()

    if not date or not amount:
        messagebox.showerror("Error", "Date and Amount required!")
        return

    df = load_data()
    new_row = {
        "id": str(uuid.uuid4()),
        "date": date,
        "category": category,
        "amount": float(amount),
        "currency": currency,
        "payment_method": payment,
        "notes": notes
    }
    df = pd.concat([df, pd.DataFrame([new_row])])
    save_data(df)
    messagebox.showinfo("Success", "Expense Added!")
    load_table()

def load_table():
    df = load_data()
    table.delete(*table.get_children())
    for _, row in df.iterrows():
        table.insert("", tk.END, values=list(row.values))

# ---------- UI ----------
app = tk.Tk()
app.title("Expense Tracker - Tkinter App")
app.geometry("900x500")

# Form inputs
tk.Label(app, text="Date (YYYY-MM-DD)").grid(row=0, column=0)
entry_date = tk.Entry(app)
entry_date.grid(row=0, column=1)

tk.Label(app, text="Category").grid(row=1, column=0)
entry_category = ttk.Combobox(app, values=["Food", "Groceries", "Transport", "Bills", "Entertainment", "Travel", "Other"])
entry_category.grid(row=1, column=1)

tk.Label(app, text="Amount").grid(row=2, column=0)
entry_amount = tk.Entry(app)
entry_amount.grid(row=2, column=1)

tk.Label(app, text="Currency").grid(row=3, column=0)
entry_currency = ttk.Combobox(app, values=["INR", "USD", "EUR"])
entry_currency.grid(row=3, column=1)

tk.Label(app, text="Payment Method").grid(row=4, column=0)
entry_payment = ttk.Combobox(app, values=["Cash", "Card", "UPI", "Netbanking"])
entry_payment.grid(row=4, column=1)

tk.Label(app, text="Notes").grid(row=5, column=0)
entry_notes = tk.Entry(app)
entry_notes.grid(row=5, column=1)

tk.Button(app, text="Add Expense", command=add_expense).grid(row=6, column=0, columnspan=2, pady=10)

# Table
columns = ["id", "date", "category", "amount", "currency", "payment_method", "notes"]
table = ttk.Treeview(app, columns=columns, show="headings", height=12)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120)
table.grid(row=7, column=0, columnspan=4)

load_table()

app.mainloop()
