# { "Depends": "py-genlayer:test" }
from genlayer import *

class DataAggregator(gl.Contract):
    """
    GenLayer Sentinel: Data Aggregator
    Combines data points from multiple oracle sources into a cohesive summary.
    """
    aggregated_summaries: TreeMap[str, str]

    def __init__(self):
        self.aggregated_summaries = TreeMap()

    @gl.public.write
    def aggregate_market_data(self, ticker: str, crypto_price: str, stock_price: str, sentiment: str) -> str:
        """
        AI generates an aggregated summary based on provided data points.
        (In a real deployment, it would call the other contracts directly if cross-contract calls are enabled).
        """
        prompt = (
            f"You are a financial analyst AI. Aggregate the following data for {ticker}: "
            f"Crypto Price: {crypto_price}, Stock Price: {stock_price}, Sentiment: {sentiment}. "
            "Write a very brief (1 sentence) summary of the current market state for this asset. "
            "Respond ONLY with a JSON object in this exact format: {\"summary\": \"The asset shows bullish momentum...\"}"
        )
        
        def _aggregate() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _aggregate,
            principle="Both outcomes must yield a JSON object with a 'summary' string that conveys the same fundamental meaning."
        )
        
        import json
        try:
            data = json.loads(result)
            summary = str(data.get("summary", "No summary available."))
            self.aggregated_summaries[ticker] = summary
            return f"Aggregated summary for {ticker} updated."
        except Exception:
            return "Failed to parse aggregated data."

    @gl.public.view
    def get_summary(self, ticker: str) -> str:
        return self.aggregated_summaries.get(ticker, "No data.")
