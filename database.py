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


# Initialize database and table
def init_database():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS portfolios (
                name TEXT PRIMARY KEY,
                balance REAL DEFAULT 0,
                holdings TEXT DEFAULT '{}'
            )
        ''')


# Save or update a portfolio
def save_portfolio(portfolio):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        holdings_json = json.dumps(portfolio.holdings)  # Convert dict to JSON string
        cursor.execute(
            '''
            INSERT OR REPLACE INTO portfolios (name, balance, holdings)
            VALUES (?, ?, ?)
            ''',
            (portfolio.name, portfolio.balance, holdings_json)
        )
