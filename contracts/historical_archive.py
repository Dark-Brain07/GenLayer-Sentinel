# { "Depends": "py-genlayer:test" }
from genlayer import *

class HistoricalArchive(gl.Contract):
    """
    GenLayer Sentinel: Historical Archive
    Stores snapshots of oracle data for back-testing and historical audits.
    """
    archive_data: TreeMap[str, str]
    total_snapshots: u256

    def __init__(self):
        self.archive_data = TreeMap()
        self.total_snapshots = u256(0)

    @gl.public.write
    def save_snapshot(self, asset: str, data: str) -> str:
        """
        Saves a historical snapshot using a sequential ID.
        """
        snapshot_id = self.total_snapshots
        key = asset + "_" + str(snapshot_id)

        self.archive_data[key] = data
        self.total_snapshots = snapshot_id + u256(1)

        return "Snapshot saved for " + asset + " with ID " + str(snapshot_id)

    @gl.public.view
    def get_snapshot(self, asset: str, snapshot_id: u256) -> str:
        key = asset + "_" + str(snapshot_id)
        return self.archive_data.get(key, "Snapshot not found.")

    @gl.public.view
    def get_total_snapshots(self) -> u256:
        return self.total_snapshots
