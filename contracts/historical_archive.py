# { "Depends": "py-genlayer:test" }
from genlayer import *

class HistoricalArchive(gl.Contract):
    """
    GenLayer Sentinel: Historical Archive
    Stores snapshots of oracle data for back-testing and historical audits.
    """
    # Key is f"{asset}_{snapshot_id}" -> Data
    archive_data: TreeMap[str, str]
    snapshot_counters: TreeMap[str, u256]

    def __init__(self):
        self.archive_data = TreeMap()
        self.snapshot_counters = TreeMap()

    @gl.public.write
    def save_snapshot(self, asset: str, data: str) -> str:
        """
        Saves a historical snapshot.
        """
        if asset not in self.snapshot_counters:
            self.snapshot_counters[asset] = u256(0)
            
        counter = self.snapshot_counters[asset]
        key = f"{asset}_{counter}"
        
        self.archive_data[key] = data
        self.snapshot_counters[asset] = counter + u256(1)
        
        return f"Snapshot saved for {asset}. ID: {counter}"

    @gl.public.view
    def get_snapshot(self, asset: str, snapshot_id: u256) -> str:
        key = f"{asset}_{snapshot_id}"
        if key in self.archive_data:
            return self.archive_data[key]
        return "Snapshot not found."
