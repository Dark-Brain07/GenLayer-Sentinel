# { "Depends": "py-genlayer:test" }
from genlayer import *

class WeatherOracle(gl.Contract):
    """
    GenLayer Sentinel: Weather Oracle
    Fetches real-world weather data for parametric insurance.
    """
    latest_temperature: i32
    latest_conditions: str
    last_updated: u256

    def __init__(self):
        self.latest_temperature = i32(0)
        self.latest_conditions = "Unknown"
        self.last_updated = u256(0)

    @gl.public.write
    def update_weather(self, city: str) -> str:
        """
        Fetches current weather for a city.
        """
        prompt = (
            f"You are a weather API. What is the current temperature in {city} in Celsius? "
            "Respond ONLY with a JSON object in this exact format: {\"temp\": 25, \"conditions\": \"Sunny\"}"
        )
        
        def _fetch_weather() -> str:
            return gl.nondet.exec_prompt(prompt)
            
        result = gl.eq_principle.prompt_comparative(
            _fetch_weather,
            principle="Both outcomes must yield a JSON object with the exact same 'temp' integer value."
        )
        
        import json
        try:
            data = json.loads(result)
            self.latest_temperature = i32(int(data.get("temp", 0)))
            self.latest_conditions = str(data.get("conditions", "Unknown"))
            self.last_updated += u256(1)
            return f"Weather updated: {self.latest_temperature}°C, {self.latest_conditions}"
        except Exception:
            return "Failed to parse weather data."

    @gl.public.view
    def get_latest_weather(self) -> str:
        return f"Temp: {self.latest_temperature}°C | Conditions: {self.latest_conditions} | Update count: {self.last_updated}"
