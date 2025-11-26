#!/usr/bin/env python3
"""
Personal Expense Tracker
Single-file CLI app that records, views, deletes, summarizes, and visualizes expenses.
Stores data in a CSV file (default: expenses.csv).

Usage examples:
  python expense_tracker.py add --date 2025-11-25 --category Food --amount 250 --notes "Lunch"
  python expense_tracker.py view --from 2025-11-01 --to 2025-11-30
  python expense_tracker.py delete --id <uuid>
  python expense_tracker.py summary --year 2025 --month 11
  python expense_tracker.py plot --year 2025 --month 11 --out monthly.png
  python expense_tracker.py export --out backup.csv

Dependencies: pandas, matplotlib
Install: pip install pandas matplotlib
"""

import argparse
import csv
import os
import uuid
import datetime
import sys
from pathlib import Path

try:
    import pandas as pd
except Exception as e:
    print("This script requires pandas. Run: pip install pandas matplotlib", file=sys.stderr)
    raise

import matplotlib.pyplot as plt

DEFAULT_CSV = Path.cwd() / 'expenses.csv'
CSV_COLUMNS = ['id', 'date', 'category', 'amount', 'currency', 'payment_method', 'notes']


def ensure_csv(path=DEFAULT_CSV):
    """Create CSV with header if not exists."""
    if not path.exists():
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CSV_COLUMNS)
    return path


def parse_date(s):
    """Parse a date string in YYYY-MM-DD format."""
    return datetime.datetime.strptime(s, '%Y-%m-%d').date()


def add_expense(date, category, amount, currency='INR', payment_method='', notes='', path=DEFAULT_CSV):
    ensure_csv(path)
    row = {
        'id': str(uuid.uuid4()),
        'date': date.isoformat(),
        'category': category,
        'amount': float(amount),
        'currency': currency,
        'payment_method': payment_method,
        'notes': notes
    }
    df = pd.DataFrame([row])
    df.to_csv(path, mode='a', index=False, header=False)
    return row['id']


def load_df(path=DEFAULT_CSV):
    ensure_csv(path)
    df = pd.read_csv(path, parse_dates=['date'])
    # normalize types
    if df.empty:
        return df
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['amount'] = df['amount'].astype(float)
    return df


def view_expenses(path=DEFAULT_CSV, from_date=None, to_date=None, category=None, limit=None):
    df = load_df(path)
    if df.empty:
        return df
    if from_date:
        df = df[df['date'] >= from_date]
    if to_date:
        df = df[df['date'] <= to_date]
    if category:
        df = df[df['category'].str.lower() == category.lower()]
    df = df.sort_values('date', ascending=False)
    if limit:
        df = df.head(limit)
    return df


def delete_expense(expense_id, path=DEFAULT_CSV):
    df = load_df(path)
    if df.empty:
        return False
    before = len(df)
    df = df[df['id'] != expense_id]
    if len(df) == before:
        return False
    df.to_csv(path, index=False)
    return True


def monthly_summary(year, month=None, path=DEFAULT_CSV):
    df = load_df(path)
    if df.empty:
        return pd.DataFrame()
    df2 = df.copy()
    df2['year'] = pd.to_datetime(df2['date']).dt.year
    df2['month'] = pd.to_datetime(df2['date']).dt.month
    df2 = df2[df2['year'] == int(year)]
    if month:
        df2 = df2[df2['month'] == int(month)]
    if df2.empty:
        return pd.DataFrame()
    summary_by_category = df2.groupby('category', as_index=False)['amount'].sum().sort_values('amount', ascending=False)
    total = df2['amount'].sum()
    return summary_by_category, float(total)


def plot_monthly_totals(path=DEFAULT_CSV, year=None, month=None, out=None):
    df = load_df(path)
    if df.empty:
        raise ValueError('No data to plot.')
    df2 = df.copy()
    df2['date'] = pd.to_datetime(df2['date'])
    if year:
        df2 = df2[df2['date'].dt.year == int(year)]
    if month:
        df2 = df2[df2['date'].dt.month == int(month)]
    if df2.empty:
        raise ValueError('No data for the given range.')
    # Group by month-day or by category depending on inputs
    if month:
        grouped = df2.groupby(df2['date'].dt.day)['amount'].sum()
        xlabel = 'Day of month'
        title = f'Daily totals for {year}-{int(month):02d}'
    elif year:
        grouped = df2.groupby(df2['date'].dt.month)['amount'].sum()
        xlabel = 'Month'
        title = f'Monthly totals for {year}'
    else:
        grouped = df2.groupby(df2['date'].dt.to_period('M'))['amount'].sum()
        xlabel = 'Month'
        title = 'Monthly totals'
    fig, ax = plt.subplots(figsize=(8, 4.5))
    grouped.plot(kind='bar', ax=ax)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Amount')
    plt.tight_layout()
    if out:
        plt.savefig(out)
        return out
    else:
        plt.show()
        return None


def export_csv(out, path=DEFAULT_CSV):
    df = load_df(path)
    df.to_csv(out, index=False)
    return out


def main():
    parser = argparse.ArgumentParser(description='Expense tracker CLI')
    sub = parser.add_subparsers(dest='cmd', required=True)
    # add
    p = sub.add_parser('add')
    p.add_argument('--date', required=True, help='YYYY-MM-DD')
    p.add_argument('--category', required=True)
    p.add_argument('--amount', required=True, type=float)
    p.add_argument('--currency', default='INR')
    p.add_argument('--payment_method', default='')
    p.add_argument('--notes', default='')
    # view
    p = sub.add_parser('view')
    p.add_argument('--from', dest='from_date', help='YYYY-MM-DD')
    p.add_argument('--to', dest='to_date', help='YYYY-MM-DD')
    p.add_argument('--category', help='filter by category')
    p.add_argument('--limit', type=int, help='limit rows')
    # delete
    p = sub.add_parser('delete')
    p.add_argument('--id', required=True, help='expense id to delete')
    # summary
    p = sub.add_parser('summary')
    p.add_argument('--year', required=True, type=int)
    p.add_argument('--month', type=int)
    # plot
    p = sub.add_parser('plot')
    p.add_argument('--year', type=int)
    p.add_argument('--month', type=int)
    p.add_argument('--out', help='output image file path (png recommended)')
    # export
    p = sub.add_parser('export')
    p.add_argument('--out', required=True, help='output csv file path')

    args = parser.parse_args()

    if args.cmd == 'add':
        d = parse_date(args.date)
        eid = add_expense(d, args.category, args.amount, currency=args.currency, payment_method=args.payment_method, notes=args.notes)
        print(f'Added expense with id: {eid}')
    elif args.cmd == 'view':
        fd = parse_date(args.from_date) if args.from_date else None
        td = parse_date(args.to_date) if args.to_date else None
        df = view_expenses(from_date=fd, to_date=td, category=args.category, limit=args.limit)
        if df.empty:
            print('No expenses found.')
        else:
            print(df.to_string(index=False))
    elif args.cmd == 'delete':
        ok = delete_expense(args.id)
        if ok:
            print('Deleted.')
        else:
            print('Expense not found.')
    elif args.cmd == 'summary':
        res = monthly_summary(args.year, args.month)
        if isinstance(res, tuple):
            summary_by_category, total = res
            if summary_by_category.empty:
                print('No data for the given period.')
            else:
                print(summary_by_category.to_string(index=False))
                print('----\nTotal: {0}'.format(total))
        else:
            print('No data found.')
    elif args.cmd == 'plot':
        try:
            out = plot_monthly_totals(year=args.year, month=args.month, out=args.out)
            if out:
                print(f'Plot saved to: {out}')
        except Exception as e:
            print('Error:', e)
    elif args.cmd == 'export':
        out = export_csv(args.out)
        print(f'Exported to {out}')


if __name__ == '__main__':
    main()
