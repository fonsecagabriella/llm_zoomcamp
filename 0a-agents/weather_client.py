import asyncio
from fastmcp import Client

async def main():
    # Spawn weather_server.py as a subprocess and auto-attach to its stdio transport
    async with Client("weather_server.py") as mcp_client:
        tools = await mcp_client.tools.list()
        print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())
