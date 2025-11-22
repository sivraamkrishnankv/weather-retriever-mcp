from server.weather import mcp
import asyncio

if __name__ == "__main__":
    asyncio.run(mcp.run())