from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP(name="Simple Calculator server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.resource("info://server")
def server_info():
    """Return information about the server."""
    info = {
        "name":mcp.name,
        "version":"1.0",
        "description":"A simple calculator server using FastMCP.",
        "author":"Shees"
    }
    return json.dumps(info)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")