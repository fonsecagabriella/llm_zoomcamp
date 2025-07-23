# weather_server.py
"""
FastMCP demo – exposes two tools:
  • get_weather(city) -> float  – read the current temperature
  • set_weather(city, temp) -> str ('OK') – write/update the temperature
Run:  python weather_server.py
Then connect an MCP-aware client or the agent you built in Q1–Q3.
"""

import random
from typing import Dict

from fastmcp import FastMCP

# -------------------------------------------------------------------
# 0️⃣  Minimal in-memory “database”
# -------------------------------------------------------------------
known_weather_data: Dict[str, float] = {}

# -------------------------------------------------------------------
# 1️⃣  Create the MCP server
# -------------------------------------------------------------------
mcp = FastMCP("Demo 🚀")        # the banner you saw earlier

# -------------------------------------------------------------------
# 2️⃣  Expose the tools
# -------------------------------------------------------------------
@mcp.tool
def get_weather(city: str) -> float:
    """
    Retrieve the current temperature for *city*.

    Parameters
    ----------
    city : str
        Name of the city (case-insensitive).

    Returns
    -------
    float
        Temperature in °C.  If the city was never written before,
        a random placeholder is generated so we always return a number.
    """
    city = city.strip().lower()
    if city in known_weather_data:
        return known_weather_data[city]

    # fallback – pretend we queried a real weather API
    return round(random.uniform(-5, 35), 1)


@mcp.tool
def set_weather(city: str, temp: float) -> str:
    """
    Store or update the temperature for *city*.

    Parameters
    ----------
    city : str
        Name of the city (case-insensitive).
    temp : float
        Temperature in °C to associate with the city.

    Returns
    -------
    str
        Always "OK" to signal success.
    """
    city = city.strip().lower()
    known_weather_data[city] = temp
    return "OK"


# -------------------------------------------------------------------
# 3️⃣  Run the server
# -------------------------------------------------------------------
if __name__ == "__main__":
    # You should see:
    #   Starting MCP server 'Demo 🚀' with transport 'stdio'
    # which confirms the default stdio transport is active.
    mcp.run()
