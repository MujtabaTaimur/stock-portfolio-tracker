# portfolio.py

from stock import Stock

class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = {}

    def add_stock(self, stock, quantity):
        if stock.symbol in self.stocks:
            self.stocks[stock.symbol]['quantity'] += quantity
        else:
            self.stocks[stock.symbol] = {
                'stock': stock,
                'quantity': quantity
            }

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
