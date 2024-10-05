# report.py

class ReportGenerator:
    def __init__(self, portfolio_manager):
        self.portfolio_manager = portfolio_manager

    def generate_portfolio_report(self, portfolio_name):
        portfolio = self.portfolio_manager.get_portfolio(portfolio_name)
        if portfolio:
            return f"Portfolio Report for '{portfolio.name}':\n" \
                   f"Total Value: ${portfolio.calculate_portfolio_value()}"
        else:
            return f"Portfolio '{portfolio_name}' not found."
