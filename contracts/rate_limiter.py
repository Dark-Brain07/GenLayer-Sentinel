# { "Depends": "py-genlayer:test" }
from genlayer import *

class RateLimiter(gl.Contract):
    """
    GenLayer Sentinel: Rate Limiter
    Tracks and limits the number of requests a DApp can make 
    to prevent spamming expensive off-chain APIs.
    """
    request_counts: TreeMap[str, u256]
    max_requests: u256

    def __init__(self):
        self.request_counts = TreeMap()
        self.max_requests = u256(100) # Default limit

    @gl.public.write
    def check_and_increment(self, dapp_address: str) -> str:
        """
        Increments the request count for a DApp. Reverts/Denies if over limit.
        """
        current_count = self.request_counts.get(dapp_address, u256(0))
        
        if current_count >= self.max_requests:
            return f"RATE LIMIT EXCEEDED for {dapp_address}. Maximum {self.max_requests} requests allowed."
            
        self.request_counts[dapp_address] = current_count + u256(1)
        return f"Request logged. Current count: {self.request_counts[dapp_address]}/{self.max_requests}."

    @gl.public.write
    def request_limit_increase(self, dapp_address: str, reason: str) -> str:
        """
        AI evaluates a request to increase the rate limit.
        """
        prompt = (
            f"You are a network administrator. DApp '{dapp_address}' is requesting a rate limit increase "
            f"for the following reason: '{reason}'. "
            "Evaluate if the reason is valid and business-critical. "
            "Respond ONLY with a JSON object in this exact format: {\"approved\": true}"
        )
        
        def _evaluate_increase() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _evaluate_increase,
            principle="Both outcomes must yield a JSON object with the exact same 'approved' boolean value."
        )
        
        import json
        try:
            data = json.loads(result)
            if data.get("approved", False):
                # Temporary logic: just grant 50 more requests
                self.max_requests += u256(50)
                return f"Limit increase approved. New max: {self.max_requests}"
            return "Limit increase denied."
        except Exception:
            return "Failed to process limit increase."
