# { "Depends": "py-genlayer:test" }
from genlayer import *

class GitHubActivityOracle(gl.Contract):
    """
    GenLayer Sentinel: GitHub Activity Oracle
    Tracks open-source developer activity to distribute grants automatically.
    """
    dev_activity_score: TreeMap[str, u256]

    def __init__(self):
        self.dev_activity_score = TreeMap()

    @gl.public.write
    def check_activity(self, github_handle: str) -> str:
        """
        Evaluates the recent activity of a GitHub user.
        """
        prompt = (
            f"You are a GitHub tracking API. Analyze the recent public activity of GitHub user '{github_handle}'. "
            "Assign an activity score from 0 to 100 based on commits, PRs, and issues in the last 30 days. "
            "Respond ONLY with a JSON object in this exact format: {\"score\": 85}"
        )
        
        def _fetch_activity() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _fetch_activity,
            principle="Both outcomes must yield a JSON object with the exact same 'score' integer value."
        )
        
        import json
        try:
            data = json.loads(result)
            score = u256(int(data.get("score", 0)))
            self.dev_activity_score[github_handle] = score
            return f"Activity score for {github_handle} updated to {score}"
        except Exception:
            return "Failed to parse activity data."

    @gl.public.view
    def get_activity_score(self, github_handle: str) -> u256:
        return self.dev_activity_score.get(github_handle, u256(0))
