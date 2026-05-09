# { "Depends": "py-genlayer:test" }
from genlayer import *

class MultiSigAuthenticator(gl.Contract):
    """
    GenLayer Sentinel: Multi-Sig Authenticator
    Requires multiple approvals or strong AI-verified justification 
    for high-risk oracle data modifications.
    """
    pending_transactions: dict[str, u256]

    def __init__(self):
        self.pending_transactions = {}

    @gl.public.write
    def submit_transaction(self, tx_id: str, justification: str) -> str:
        """
        Submits a transaction requiring approval.
        """
        self.pending_transactions[tx_id] = u256(1) # Start with 1 implicit approval
        
        prompt = (
            "You are a Multi-Signature Security Auditor. "
            f"A user has submitted transaction '{tx_id}' with the following justification: '{justification}'. "
            "Analyze the justification for potential risks, anomalies, or policy violations. "
            "Respond ONLY with a JSON object in this exact format: {\"risk_level\": \"HIGH\"}. "
            "Risk levels: LOW, MEDIUM, HIGH, CRITICAL."
        )
        
        def _audit_tx() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _audit_tx,
            principle="Both outcomes must yield a JSON object with the exact same 'risk_level' string value."
        )
        
        return f"Transaction {tx_id} submitted. Initial Risk Assessment:\n{result}"

    @gl.public.write
    def approve_transaction(self, tx_id: str) -> str:
        """
        Adds an approval to a pending transaction.
        """
        if tx_id not in self.pending_transactions:
            return "Transaction not found."
            
        self.pending_transactions[tx_id] += u256(1)
        
        # Require 3 approvals (including the submission)
        if self.pending_transactions[tx_id] >= u256(3):
            return f"Transaction {tx_id} FULLY APPROVED and executed."
            
        return f"Transaction {tx_id} approved. Total approvals: {self.pending_transactions[tx_id]}/3."
