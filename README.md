# Weather Retriever MCP

A Model Context Protocol (MCP) server that provides real-time weather alerts for US states using the National Weather Service API.

## Features

- **Real-time Weather Alerts**: Fetch current weather alerts, warnings, and advisories for any US state
- **National Weather Service API**: Official weather data from weather.gov
- **MCP Integration**: Seamlessly integrates with MCP-compatible applications like Cursor
- **Echo Resource**: Simple echo functionality for testing MCP connections

## Installation

### Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Install with uv (Recommended)

```bash
cd weather-retriever-mcp
uv sync
```

### Install with pip

```bash
pip install -e .
```

## Usage

### Running the MCP Server

#### Method 1: Direct Execution
```bash
python server/weather.py
```

#### Method 2: Using main.py
```bash
python main.py
```

#### Method 3: With MCP Inspector
```bash
uv run mcp-inspector python server/weather.py
```

### Available Tools

#### `get_alerts(state: str)`
Get active weather alerts for a US state.

**Parameters:**
- `state` (str): Two-letter US state code (e.g., "CA", "NY", "TX")

**Example Usage:**
```python
# Get California weather alerts
get_alerts("CA")

# Get Texas weather alerts  
get_alerts("TX")
```


#### `echo://{message}`
A simple echo resource for testing MCP connectivity.

**Example:**
- `echo://hello world` → `"Resource echo: hello world"`

## MCP Integration

### Cursor Integration

1. **Configure MCP Server** in `PATH TO mcp.json`:

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["server/weather.py"],
      "cwd": "E:\\MCP\\weather-retriever-mcp"
    }
  }
}
```

2. **Restart Cursor** to load the MCP configuration

3. **Use in Agent Mode**: Switch to agent mode in Cursor and ask:
   - "Get weather alerts for California"
   - "Check weather alerts for TX"
   - "Are there any active alerts in Florida?"

### Other MCP Clients

The server can be integrated with any MCP-compatible client by configuring it to run the weather server script.

## API Details

### Data Source
- **Provider**: National Weather Service (weather.gov)
- **API Endpoint**: `https://api.weather.gov/alerts/active/area/{state}`
- **Format**: GeoJSON
- **Rate Limits**: Follow NWS API guidelines

### Supported States
All 50 US states and territories using standard 2-letter codes:
- `CA` - California
- `NY` - New York
- `TX` - Texas
- `FL` - Florida
- `WA` - Washington
- etc.

### Alert Types
The server can retrieve various types of weather alerts:
- Severe Thunderstorm Warnings
- Tornado Warnings
- Flood Warnings
- Heat Advisories
- Winter Storm Warnings
- And many more...

---

**_Made with ❤️ by SIV RAAM KRISHNAN.K.V_**