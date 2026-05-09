# { "Depends": "py-genlayer:test" }
from genlayer import *

class KeyVaultController(gl.Contract):
    """
    GenLayer Sentinel: Key Vault Controller
    Maintains simulated encrypted references to private API keys.
    Prevents raw keys from being exposed in plaintext on the ledger.
    """
    stored_keys: TreeMap[str, str]

    def __init__(self):
        self.stored_keys = TreeMap()

    @gl.public.write
    def store_key_reference(self, service_name: str, encrypted_reference: str) -> str:
        """
        Stores an encrypted reference to an API key.
        """
        self.stored_keys[service_name] = encrypted_reference
        return f"Encrypted key reference stored for {service_name}."

    @gl.public.write
    def validate_key_access(self, service_name: str, access_token: str) -> str:
        """
        Uses AI to validate if the provided access token matches the pattern 
        expected for the encrypted key reference.
        """
        if service_name not in self.stored_keys:
            return "ERROR: Service not found in Vault."
            
        stored_ref = self.stored_keys[service_name]
        
        prompt = (
            "You are a secure Key Vault Controller. "
            f"Compare the access token '{access_token}' against the stored encrypted reference '{stored_ref}'. "
            "Determine if the token appears to be a valid authorization request for this reference. "
            "Respond ONLY with a JSON object in this exact format: {\"valid\": true}"
        )
        
        def _validate() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _validate,
            principle="Both outcomes must yield a JSON object with the exact same 'valid' boolean value."
        )
        
        return f"Validation result:\n{result}"
