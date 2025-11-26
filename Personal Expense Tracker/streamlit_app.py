import streamlit as st
import pandas as pd
import uuid
import datetime
import os

CSV_FILE = "expenses.csv"

# ------------------ Utility Functions ------------------

def load_data():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=["id", "date", "category", "amount", "currency", "payment_method", "notes"])
        df.to_csv(CSV_FILE, index=False)
    return pd.read_csv(CSV_FILE)

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

def add_expense(date, category, amount, currency, payment_method, notes):
    df = load_data()
    new_entry = {
        "id": str(uuid.uuid4()),
        "date": str(date),
        "category": category,
        "amount": float(amount),
        "currency": currency,
        "payment_method": payment_method,
        "notes": notes,
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    save_data(df)
    return new_entry["id"]

def delete_expense(expense_id):
    df = load_data()
    df = df[df["id"] != expense_id]
    save_data(df)

# ------------------ Streamlit UI ------------------

st.title("💰 Personal Expense Tracker")

menu = st.sidebar.selectbox("Menu", ["Add Expense", "View Expenses", "Summary", "Delete Expense"])

# ------------------ Add Expense ------------------
if menu == "Add Expense":
    st.header("➕ Add New Expense")

    date = st.date_input("Date", datetime.date.today())
    category = st.selectbox("Category", ["Food", "Groceries", "Transport", "Bills", "Entertainment", "Travel", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=10.0)
    currency = st.selectbox("Currency", ["INR", "USD", "EUR"])
    payment_method = st.selectbox("Payment Method", ["Cash", "Card", "UPI", "Netbanking"])
    notes = st.text_area("Notes")

    if st.button("Add Expense"):
        expense_id = add_expense(date, category, amount, currency, payment_method, notes)
        st.success(f"Expense added! ID: {expense_id}")

# ------------------ View Expenses ------------------
elif menu == "View Expenses":
    st.header("📄 All Expenses")
    df = load_data()
    st.dataframe(df)

# ------------------ Summary ------------------
elif menu == "Summary":
    st.header("📊 Monthly Summary")

    df = load_data()

    if df.empty:
        st.warning("No data available.")
    else:
        df["date"] = pd.to_datetime(df["date"])
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        year = st.selectbox("Year", sorted(df["year"].unique(), reverse=True))
        month = st.selectbox("Month", sorted(df["month"].unique()))

        filtered = df[(df["year"] == year) & (df["month"] == month)]

        if not filtered.empty:
            category_summary = filtered.groupby("category")["amount"].sum()
            st.bar_chart(category_summary)
            st.write(filtered)
        else:
            st.warning("No expenses for this period.")

# ------------------ Delete Expense ------------------
elif menu == "Delete Expense":
    st.header("🗑 Delete Expense")

    df = load_data()

    if df.empty:
        st.warning("No expenses to delete.")
    else:
        delete_id = st.selectbox("Select Entry ID to delete", df["id"].tolist())

        if st.button("Delete"):
            delete_expense(delete_id)
            st.success("Expense deleted successfully!")
