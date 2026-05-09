# { "Depends": "py-genlayer:test" }
from genlayer import *

class SentinelRegistry(gl.Contract):
    """
    GenLayer Sentinel: Sentinel Registry
    The Master contract that indexes all active oracles and middleware services in the suite.
    """
    registered_services: dict[str, str] # Service Name -> Contract Address

    def __init__(self):
        self.registered_services = {}

    @gl.public.write
    def register_service(self, service_name: str, contract_address: str) -> str:
        """
        Registers a new Oracle or Middleware contract.
        """
        self.registered_services[service_name] = contract_address
        return f"Service '{service_name}' registered at {contract_address}."

    @gl.public.view
    def get_service_address(self, service_name: str) -> str:
        return self.registered_services.get(service_name, "Not found")
        
    @gl.public.write
    def analyze_network_health(self) -> str:
        """
        AI evaluates the overall health of the Sentinel network based on registered services.
        """
        service_list = ", ".join(self.registered_services.keys())
        prompt = (
            f"You are the Sentinel Network Health AI. The following services are currently active: {service_list}. "
            "Based on the presence of these services, assess the network's capabilities (e.g., Data availability, Security). "
            "Respond ONLY with a JSON object in this exact format: {\"status\": \"HEALTHY\", \"capabilities\": \"Data, Security\"}"
        )
        
        def _analyze_health() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _analyze_health,
            principle="Both outcomes must yield a JSON object with the exact same 'status' string value."
        )
        
        return f"Network Health Report:\n{result}"
