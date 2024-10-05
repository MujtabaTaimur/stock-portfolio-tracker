# database.py

import sqlite3
from portfolio import Portfolio

DB_FILE = 'portfolio.db'

def init_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolios (
            name TEXT PRIMARY KEY
        )
    ''')

    conn.commit()
    conn.close()

def save_portfolio(portfolio):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Save portfolio
    cursor.execute('INSERT OR REPLACE INTO portfolios (name) VALUES (?)', (portfolio.name,))
    conn.commit()
    conn.close()

def load_portfolios():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('SELECT name FROM portfolios')
    rows = cursor.fetchall()

    portfolios = []
    for row in rows:
        portfolio_name = row[0]
        portfolio = Portfolio(portfolio_name)
        portfolios.append(portfolio)

    conn.close()

    return portfolios
