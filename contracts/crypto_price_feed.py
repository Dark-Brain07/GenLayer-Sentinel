# { "Depends": "py-genlayer:test" }
from genlayer import *

class CryptoPriceFeed(gl.Contract):
    """
    GenLayer Sentinel: Crypto Price Feed
    Provides aggregated crypto asset prices for DeFi applications.
    """
    asset_prices: TreeMap[str, u256]

    def __init__(self):
        self.asset_prices = TreeMap()

    @gl.public.write
    def update_price(self, ticker: str) -> str:
        """
        Fetches the current price for a cryptocurrency ticker.
        """
        prompt = (
            f"You are a crypto price API. What is the current price of {ticker} in USD? "
            "Respond ONLY with a JSON object in this exact format: {\"price\": 65000}"
        )
        
        def _fetch_price() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _fetch_price,
            principle="Both outcomes must yield a JSON object with the exact same 'price' integer value."
        )
        
        import json
        try:
            data = json.loads(result)
            price = u256(int(data.get("price", 0)))
            self.asset_prices[ticker] = price
            return f"{ticker} price updated to ${price}"
        except Exception:
            return "Failed to parse price data."

    @gl.public.view
    def get_price(self, ticker: str) -> u256:
        return self.asset_prices.get(ticker, u256(0))
