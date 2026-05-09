# { "Depends": "py-genlayer:test" }
from genlayer import *

class SubscriptionManager(gl.Contract):
    """
    GenLayer Sentinel: Subscription Manager
    Allows DApps to subscribe to oracle feeds.
    """
    active_subscriptions: TreeMap[str, u256] # DApp address -> Expiration block/time

    def __init__(self):
        self.active_subscriptions = TreeMap()

    @gl.public.write
    def subscribe(self, dapp_address: str, duration: u256) -> str:
        """
        Subscribes a DApp for a certain duration.
        """
        # In reality, this would require payment handling (gl.msg.value)
        current_exp = self.active_subscriptions.get(dapp_address, u256(0))
        self.active_subscriptions[dapp_address] = current_exp + duration
        return f"Subscription active for {dapp_address}. Duration added: {duration}."

    @gl.public.view
    def is_subscribed(self, dapp_address: str) -> bool:
        return self.active_subscriptions.get(dapp_address, u256(0)) > u256(0)
