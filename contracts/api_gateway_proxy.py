# { "Depends": "py-genlayer:test" }
from genlayer import *

class ApiGatewayProxy(gl.Contract):
    """
    GenLayer Sentinel: API Gateway Proxy
    Acts as a secure entry point for DApps to request data from off-chain APIs.
    It routes requests while concealing the destination details.
    """
    total_requests_routed: u256
    authorized_dapps: dict[str, bool]

    def __init__(self):
        self.total_requests_routed = u256(0)
        self.authorized_dapps = {}

    @gl.public.write
    def register_dapp(self, dapp_address: str) -> str:
        """
        Registers a DApp to use the gateway.
        """
        self.authorized_dapps[dapp_address] = True
        return f"DApp {dapp_address} authorized for proxy access."

    @gl.public.write
    def route_request(self, dapp_address: str, request_payload: str) -> str:
        """
        Routes a request if the DApp is authorized.
        """
        if not self.authorized_dapps.get(dapp_address, False):
            return "ACCESS DENIED: DApp not authorized."
            
        self.total_requests_routed += u256(1)
        
        prompt = (
            "You are a secure API Gateway Proxy. "
            f"Analyze the following incoming request: '{request_payload}'. "
            "Determine the target service (Weather, Crypto, Stock, Social, GitHub) and return a routing command. "
            "Respond ONLY with a JSON object in this exact format: {\"route\": \"Crypto\"}"
        )
        
        def _determine_route() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _determine_route,
            principle="Both outcomes must yield a JSON object with the exact same 'route' string value."
        )
        
        return f"Request authorized and routed. Gateway analysis:\n{result}"

    @gl.public.view
    def get_gateway_stats(self) -> str:
        return f"Total requests routed: {self.total_requests_routed}"
