# portfolio.py

from stock import Stock

class PortfolioManager:
    def __init__(self):
        self.portfolios = {}

     def add_portfolio(self, portfolio):  # NEW (accepts Portfolio object directly)
        self.portfolios[portfolio.name] = portfolio  # NEW

    def get_portfolio(self, name):
        return self.portfolios.get(name)

    def print_portfolios(self):
        if not self.portfolios:
            print("No portfolios available.")

    def remove_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            if self.stocks[stock.symbol]['quantity'] >= quantity:
                self.stocks[stock.symbol]['quantity'] -= quantity
                if self.stocks[stock.symbol]['quantity'] == 0:
                    del self.stocks[stock.symbol]

    def calculate_portfolio_value(self):
        total_value = 0.0
        for stock_data in self.stocks.values():
            stock = stock_data['stock']
            quantity = stock_data['quantity']
            total_value += stock.price * quantity
        return total_value

    def __str__(self):
        return f"Portfolio: {self.name}, Total Value: ${self.calculate_portfolio_value()}"

symbol = transaction.symbol
        quantity = transaction.quantity
        price = transaction.price
        total_cost = price * quantity

        if transaction.type == 'buy':  # NEW
            if portfolio.balance >= total_cost:
                stock = Stock(symbol, price=price)
                portfolio.add_stock(stock, quantity)
                portfolio.balance -= total_cost  # Deduct from cash balance # NEW
                print(f"Bought {quantity} shares of {symbol} at ${price} each.")
            else:
                print("Insufficient balance to complete purchase.")  # NEW
                
def process_transaction(self, portfolio_name, transaction):  # NEW
        portfolio = self.get_portfolio(portfolio_name)
        if not portfolio:
            print(f"Portfolio {portfolio_name} not found.")
            return
    def print_stocks(self):
        print(f"\nStocks in Portfolio '{self.name}':")
        for stock_data in self.stocks.values():
            print(f"{stock_data['stock']} - Quantity: {stock_data['quantity']}")

    def has_stock(self, symbol):
        return symbol in self.stocks

    def get_stock_quantity(self, symbol):
        if symbol in self.stocks:
            return self.stocks[symbol]['quantity']
        return 0

lif transaction.type == 'sell':  # NEW
            if portfolio.get_stock_quantity(symbol) >= quantity:
                stock = Stock(symbol, price=price)
                portfolio.remove_stock(stock, quantity)
                portfolio.balance += total_cost  # Add to cash balance # NEW
                print(f"Sold {quantity} shares of {symbol} at ${price} each.")
            else:
                print("Not enough shares to sell.")  # NEW
