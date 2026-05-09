# { "Depends": "py-genlayer:test" }
from genlayer import *

class StockMarketOracle(gl.Contract):
    """
    GenLayer Sentinel: Stock Market Oracle
    Brings traditional finance (TradFi) stock prices on-chain.
    """
    stock_prices: dict[str, u256]

    def __init__(self):
        self.stock_prices = {}

    @gl.public.write
    def update_stock_price(self, symbol: str) -> str:
        """
        Fetches the current price for a stock symbol (e.g. AAPL).
        """
        prompt = (
            f"You are a stock market API. What is the current closing price of {symbol} in USD? "
            "Respond ONLY with a JSON object in this exact format: {\"price\": 150}"
        )
        
        def _fetch_stock() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _fetch_stock,
            principle="Both outcomes must yield a JSON object with the exact same 'price' integer value."
        )
        
        import json
        try:
            data = json.loads(result)
            price = u256(int(data.get("price", 0)))
            self.stock_prices[symbol] = price
            return f"{symbol} stock price updated to ${price}"
        except Exception:
            return "Failed to parse stock price."

    @gl.public.view
    def get_stock_price(self, symbol: str) -> u256:
        return self.stock_prices.get(symbol, u256(0))
