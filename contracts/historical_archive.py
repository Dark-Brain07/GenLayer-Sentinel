# { "Depends": "py-genlayer:test" }
from genlayer import *

class HistoricalArchive(gl.Contract):
    """
    GenLayer Sentinel: Historical Archive
    Stores snapshots of oracle data for back-testing and historical audits.
    """
    # Asset -> Snapshot ID -> Data
    archive_data: TreeMap[str, TreeMap[u256, str]]
    snapshot_counters: TreeMap[str, u256]

    def __init__(self):
        self.archive_data = TreeMap()
        self.snapshot_counters = TreeMap()

    @gl.public.write
    def save_snapshot(self, asset: str, data: str) -> str:
        """
        Saves a historical snapshot.
        """
        if asset not in self.archive_data:
            self.archive_data[asset] = TreeMap()
            self.snapshot_counters[asset] = u256(0)
            
        counter = self.snapshot_counters[asset]
        self.archive_data[asset][counter] = data
        self.snapshot_counters[asset] = counter + u256(1)
        
        return f"Snapshot saved for {asset}. ID: {counter}"

    @gl.public.view
    def get_snapshot(self, asset: str, snapshot_id: u256) -> str:
        if asset in self.archive_data and snapshot_id in self.archive_data[asset]:
            return self.archive_data[asset][snapshot_id]
        return "Snapshot not found."
