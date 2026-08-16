"""
Sprint 1 exit criteria check: confirms both the KYC and CRIB MCP servers
respond correctly to a real MCP client over streamable-http.
Run from the host (not inside a container) since it targets the
docker-compose-published ports on localhost.
"""
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession


async def test_server(name: str, url: str, tool_name: str, arguments: dict):
    print(f"\n--- {name} ({url}) ---")
    async with streamablehttp_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print(f"Tools exposed: {[t.name for t in tools.tools]}")

            result = await session.call_tool(tool_name, arguments=arguments)
            print(f"Tool result: {result.content}")


async def main():
    await test_server(
        "kyc-mcp-server",
        "http://localhost:9001/mcp",
        "verify_identity",
        {"national_id": "199012345678", "document_image_ref": "test-doc.jpg"},
    )
    await test_server(
        "crib-mcp-server",
        "http://localhost:9002/mcp",
        "check_crib_record",
        {"national_id": "199012345678"},
    )


if __name__ == "__main__":
    asyncio.run(main())
