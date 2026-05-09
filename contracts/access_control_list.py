# { "Depends": "py-genlayer:test" }
from genlayer import *

class AccessControlList(gl.Contract):
    """
    GenLayer Sentinel: Access Control List (ACL)
    Manages role-based permissions for interacting with Oracles.
    """
    user_roles: dict[str, str]

    def __init__(self):
        self.user_roles = {}
        # Initial setup: deploying address could be an admin, but we keep it simple here.

    @gl.public.write
    def assign_role(self, address: str, role: str) -> str:
        """
        Assigns a role (e.g., ADMIN, SUBSCRIBER, GUEST) to an address.
        """
        # In a real system, this would be restricted to ADMINs.
        self.user_roles[address] = role.upper()
        return f"Assigned role {role.upper()} to {address}."

    @gl.public.write
    def verify_permission(self, address: str, action_description: str) -> str:
        """
        AI evaluates if the user's role permits the requested action.
        """
        role = self.user_roles.get(address, "GUEST")
        
        prompt = (
            f"You are a strict Access Control manager. A user with the role '{role}' "
            f"is attempting to perform the following action: '{action_description}'. "
            "Determine if this role has sufficient privileges for this action. "
            "Respond ONLY with a JSON object in this exact format: {\"permitted\": false}"
        )
        
        def _evaluate_permission() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _evaluate_permission,
            principle="Both outcomes must yield a JSON object with the exact same 'permitted' boolean value."
        )
        
        return f"Permission Evaluation for {address} ({role}):\n{result}"
