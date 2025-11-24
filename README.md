# 🌤️ Weather Retriever MCP

A comprehensive **Model Context Protocol (MCP)** implementation providing real-time weather data and AI-powered weather assistance. This project includes multiple MCP servers, AI-integrated clients, and testing utilities for robust weather information retrieval.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [API Reference](#-api-reference)
- [Integration Examples](#-integration-examples)
- [Development & Testing](#-development--testing)
- [Docker Deployment](#-docker-deployment)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

## ✨ Features

### Core Weather Functionality
- **🔴 Real-time Weather Alerts**: Active warnings, watches, and advisories for US states
- **🌤️ Location-based Forecasts**: 5-day weather forecasts with temperature, wind, and detailed conditions
- **📊 Official NWS Data**: Direct integration with National Weather Service API (weather.gov)
- **🌍 Geographic Coverage**: All 50 US states and territories

### MCP Integration
- **🔌 Multiple Transport Protocols**: Stdio and Server-Sent Events (SSE) support
- **🤖 AI Agent Integration**: Built-in Gemini AI chat interface with conversation memory
- **🛠️ Tool-based Architecture**: Extensible MCP tools for weather operations
- **📚 Resource Support**: Echo resources for connectivity testing

### Development & Deployment
- **🐳 Docker Support**: Containerized deployment with optimized builds
- **🧪 Comprehensive Testing**: Stdio and SSE client implementations for validation
- **📦 Modern Python**: uv package manager with Python 3.11+ support
- **🔧 Flexible Configuration**: Environment-based setup with .env support

## 🏗️ Project Structure

```
weather-retriever-mcp/
├── 📁 server/                    # Production MCP Server
│   ├── weather.py               # Main MCP server (stdio transport)
│   ├── weather.json             # MCP client configuration
│   └── client.py                # Gemini AI chat client
├── 📁 mcpserver/                # Enhanced MCP Server (Development)
│   ├── server.py                # Advanced server with SSE/stdio support
│   ├── client-stdio.py          # Stdio transport test client
│   ├── client-sse.py            # SSE transport test client
│   ├── Dockerfile               # Container deployment
│   └── requirements.txt         # Python dependencies
├── main.py                      # Alternative server entry point
├── pyproject.toml               # Project configuration & dependencies
├── uv.lock                      # Dependency lock file
├── README.md                    # This file
└── .env.example                 # Environment variables template
```

## 🚀 Installation

### Prerequisites

- **Python 3.11 or higher** (3.11 recommended)
- **[uv](https://github.com/astral-sh/uv)** package manager (recommended)
- **Google AI API key** (for Gemini AI client)

### Step-by-Step Installation

#### 1. Clone and Navigate
```bash
git clone <repository-url>
cd weather-retriever-mcp
```

#### 2. Install with uv (Recommended)
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Sync dependencies
uv sync
```

#### 3. Alternative: Install with pip
```bash
pip install -e .
```

#### 4. Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your Google AI API key
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```

## 🏃 Quick Start

### 1. Basic Weather Server
```bash
# Run the production weather server
uv run python server/weather.py
```

### 2. Test with MCP Inspector
```bash
# Inspect available tools and resources
uv run mcp-inspector python server/weather.py
```

### 3. AI Chat Interface
```bash
# Interactive chat with Gemini AI
uv run python server/client.py
```

## 📖 Usage Guide

### Component 1: Production MCP Server (`server/weather.py`)

**Purpose**: Standard MCP server for weather alerts with basic functionality.

#### Running the Server
```bash
# Method 1: Direct execution
uv run python server/weather.py

# Method 2: Using main.py
uv run python main.py

# Method 3: With MCP inspector
uv run mcp-inspector python server/weather.py
```

#### Available Tools
- **`get_alerts(state: str)`**: Get active weather alerts for a US state
- **Resource**: `echo://{message}` - Echo functionality for testing

#### Example Usage
```python
# In MCP inspector or client:
get_alerts("CA")  # Get California alerts
get_alerts("TX")  # Get Texas alerts
```

### Component 2: Enhanced MCP Server (`mcpserver/server.py`)

**Purpose**: Advanced server with forecast capabilities and multiple transport options.

#### Running with SSE Transport (Default)
```bash
cd mcpserver
uv run python server.py
# Server starts on http://localhost:8001
```

#### Running with Stdio Transport
```python
# Edit server.py line 100:
transport = "stdio"  # Change from "sse"

# Then run:
uv run python server.py
```

#### Available Tools
- **`get_alerts(state: str)`**: Weather alerts (same as basic server)
- **`get_forecast(latitude: float, longitude: float)`**: 5-day weather forecast

#### Example Usage
```python
# Weather alerts
get_alerts("FL")

# Location forecast (Miami, FL coordinates)
get_forecast(25.7617, -80.1918)
```

### Component 3: Gemini AI Chat Client (`server/client.py`)

**Purpose**: Interactive AI-powered weather assistant with conversation memory.

#### Prerequisites
- Google AI API key in `.env` file
- MCP server running (see Component 1)

#### Running the Client
```bash
cd server
uv run python client.py
```

#### Features
- **🤖 Gemini AI Integration**: Powered by Google's Gemini 2.5 Pro
- **💬 Conversation Memory**: Remembers chat history across sessions
- **🔄 Auto MCP Connection**: Connects to weather server automatically
- **🎯 Smart Commands**: Special commands for chat management

#### Interactive Usage
```
===== Interactive MCP Chat =====
Type 'exit' or 'quit' to end the conversation
Type 'clear' to clear conversation history
==================================

You: What are the current weather alerts for California?
Assistant: [Gemini AI processes request and queries weather server]

You: clear
Conversation history cleared.

You: exit
Ending conversation...
```

### Component 4: Test Clients

#### Stdio Test Client (`mcpserver/client-stdio.py`)
```bash
cd mcpserver
uv run python client-stdio.py
```
**Purpose**: Tests stdio transport by launching server as subprocess.

#### SSE Test Client (`mcpserver/client-sse.py`)
```bash
# First, start the SSE server in another terminal:
cd mcpserver
uv run python server.py

# Then run the client:
uv run python client-sse.py
```
**Purpose**: Tests SSE transport by connecting to running HTTP server.

## 🔌 Integration Examples

### Cursor IDE Integration

1. **Locate MCP Configuration**:
   - Windows: `%APPDATA%\Cursor\User\globalStorage\cursor.mcp.json`
   - macOS: `~/Library/Application Support/Cursor/User/globalStorage/cursor.mcp.json`
   - Linux: `~/.config/Cursor/User/globalStorage/cursor.mcp.json`

2. **Add Weather Server Configuration**:
   ```json
   {
     "mcpServers": {
       "weather": {
         "command": "uv",
         "args": ["run", "python", "server/weather.py"],
         "cwd": "E:\\MCP\\weather-retriever-mcp"
       }
     }
   }
   ```

3. **Restart Cursor** and use Agent Mode:
   ```
   "Get weather alerts for California"
   "What are the current warnings in Texas?"
   "Are there any active alerts in Florida?"
   ```

### Claude Desktop Integration

Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": ["run", "--project", "E:\\MCP\\weather-retriever-mcp", "python", "server/weather.py"]
    }
  }
}
```

### Other MCP Clients

The server works with any MCP-compatible client by configuring it to run:
```bash
uv run python server/weather.py
```

## 🧪 Development & Testing

### Running Tests

#### 1. Test Stdio Transport
```bash
cd mcpserver
uv run python client-stdio.py
```

#### 2. Test SSE Transport
```bash
# Terminal 1: Start server
cd mcpserver
uv run python server.py

# Terminal 2: Run client
cd mcpserver
uv run python client-sse.py
```

#### 3. Test MCP Inspector
```bash
uv run mcp-inspector python server/weather.py
```

### Development Workflow

#### Adding New Weather Tools
1. Edit `server/weather.py` or `mcpserver/server.py`
2. Add new `@mcp.tool()` decorated functions
3. Test with MCP inspector
4. Update client configurations if needed

#### Modifying AI Client
1. Edit `server/client.py`
2. Change LLM model or parameters
3. Update environment variables
4. Test interactive functionality

## 🐳 Docker Deployment

### Building and Running

#### 1. Build Docker Image
```bash
cd mcpserver
docker build -t weather-mcp .
```

#### 2. Run Container
```bash
# Run with SSE transport (default)
docker run -p 8001:8001 weather-mcp

# Access server at http://localhost:8001
```

#### 3. Test Containerized Server
```bash
# In another terminal
cd mcpserver
uv run python client-sse.py
```

### Docker Configuration

The `Dockerfile` includes:
- Python 3.11 slim base image
- uv package manager installation
- Virtual environment setup
- Port 8001 exposure for SSE transport
- Optimized for production deployment

## 🔧 API Reference

### Weather Tools

#### `get_alerts(state: str)`
**Description**: Retrieves active weather alerts for a US state.

**Parameters**:
- `state` (string): Two-letter US state code (e.g., "CA", "NY", "TX")

**Returns**: Formatted string with active alerts including:
- Event type (warning, watch, advisory)
- Affected area
- Severity level
- Description and instructions

**Example**:
```python
result = get_alerts("CA")
# Returns formatted alert information
```

#### `get_forecast(latitude: float, longitude: float)`
**Description**: Gets 5-day weather forecast for specific coordinates.

**Parameters**:
- `latitude` (float): Latitude coordinate (-90 to 90)
- `longitude` (float): Longitude coordinate (-180 to 180)

**Returns**: Formatted forecast with:
- Date/time periods
- Temperature (Fahrenheit)
- Wind speed and direction
- Detailed weather conditions

**Example**:
```python
result = get_forecast(40.7128, -74.0060)  # New York City
# Returns 5-day forecast
```

### Resources

#### `echo://{message}`
**Description**: Simple echo resource for testing MCP connectivity.

**Example**:
```
echo://hello world → "Resource echo: hello world"
```

## 🐛 Troubleshooting

### Common Issues

#### 1. "Connection closed" Error
**Problem**: Stdio client can't connect to server.
**Solution**:
```python
# Ensure client uses uv command:
server_params = StdioServerParameters(
    command="uv",
    args=["run", "mcpserver/server.py"]
)
```

#### 2. "Module not found" Errors
**Problem**: Dependencies not installed.
**Solution**:
```bash
uv sync  # Install all dependencies
```

#### 3. SSE Connection Failed
**Problem**: SSE client can't connect to server.
**Solution**:
- Ensure server is running: `uv run python mcpserver/server.py`
- Check port 8001 is available
- Verify server is using SSE transport (default)

#### 4. Gemini AI Not Working
**Problem**: Chat client fails with API errors.
**Solution**:
- Check `.env` file has valid `GOOGLE_API_KEY`
- Verify API key has Gemini API access
- Ensure network connectivity for Google AI API

#### 5. Weather Data Not Loading
**Problem**: Weather API requests fail.
**Solution**:
- Check internet connectivity
- Verify NWS API is accessible
- Valid state codes: CA, NY, TX, FL, etc.

### Debug Commands

#### Test Server Directly
```bash
# Test basic server
uv run python server/weather.py

# Test enhanced server
cd mcpserver && uv run python server.py
```

#### Inspect MCP Tools
```bash
# Inspect available tools
uv run mcp-inspector python server/weather.py
```

#### Check Dependencies
```bash
# Verify uv installation
uv --version

# Check Python version
python --version

# List installed packages
uv pip list
```

## 🤝 Contributing

### Development Setup

1. **Fork and Clone**:
   ```bash
   git clone https://github.com/your-username/weather-retriever-mcp.git
   cd weather-retriever-mcp
   ```

2. **Install Dependencies**:
   ```bash
   uv sync
   ```

3. **Create Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Run Tests**:
   ```bash
   # Test all components
   uv run python mcpserver/client-stdio.py
   uv run python mcpserver/client-sse.py
   uv run python server/client.py
   ```

### Code Guidelines

- **Python Version**: Use Python 3.11+ features
- **Type Hints**: Add type annotations to function parameters
- **Documentation**: Include docstrings for all functions
- **Error Handling**: Implement proper exception handling
- **Testing**: Test both stdio and SSE transports

### Adding New Features

1. **Weather Tools**: Add new `@mcp.tool()` functions
2. **Resources**: Implement `@mcp.resource()` handlers
3. **AI Integration**: Extend Gemini client capabilities
4. **Transport Support**: Add new transport protocols

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **National Weather Service** for providing weather data API
- **Google AI** for Gemini language model integration
- **MCP Community** for the Model Context Protocol specification
- **FastMCP** library for simplified MCP server implementation

---

**Made with ❤️ by SIV RAAM KRISHNAN.K.V**

*For questions or support, please open an issue on GitHub.*