# database.py
import sqlite3
from portfolio import Portfolio

DB_FILE = 'portfolio.db'

# Simple Portfolio class
class Portfolio:
    def __init__(self, name, balance=0.0, holdings=None):
        self.name = name
        self.balance = balance
        self.holdings = holdings if holdings is not None else {}

    def __repr__(self):
        return f"<Portfolio name={self.name}, balance={self.balance}, holdings={self.holdings}>"


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
