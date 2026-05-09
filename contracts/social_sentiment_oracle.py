# { "Depends": "py-genlayer:test" }
from genlayer import *

class SocialSentimentOracle(gl.Contract):
    """
    GenLayer Sentinel: Social Sentiment Oracle
    Analyzes Twitter/X sentiment for crypto assets to drive automated trading logic.
    """
    asset_sentiment: dict[str, str]

    def __init__(self):
        self.asset_sentiment = {}

    @gl.public.write
    def analyze_sentiment(self, asset: str) -> str:
        """
        Fetches the current overall social sentiment for an asset.
        """
        prompt = (
            f"You are a social media sentiment analysis tool. What is the current overall sentiment for {asset} on Twitter/X? "
            "Respond ONLY with a JSON object in this exact format: {\"sentiment\": \"BULLISH\"}. "
            "The sentiment must be one of: BULLISH, BEARISH, or NEUTRAL."
        )
        
        def _fetch_sentiment() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _fetch_sentiment,
            principle="Both outcomes must yield a JSON object with the exact same 'sentiment' string value (BULLISH, BEARISH, or NEUTRAL)."
        )
        
        import json
        try:
            data = json.loads(result)
            sentiment = str(data.get("sentiment", "NEUTRAL")).upper()
            self.asset_sentiment[asset] = sentiment
            return f"{asset} sentiment updated to {sentiment}"
        except Exception:
            return "Failed to parse sentiment data."

    @gl.public.view
    def get_sentiment(self, asset: str) -> str:
        return self.asset_sentiment.get(asset, "UNKNOWN")
