"""
MCP server wrapping the company's EXISTING KYC verification system as a
standard MCP tool, per SRS FR-KYC-01/02 and BRD BR-002 ("integrate via
standardized MCP servers rather than replacing them").

This is a thin adapter: it does not re-implement KYC logic. It calls the
existing internal KYC service and exposes the result as an MCP tool the
KYC/Onboarding Agent can call.

Sprint 1 exit criteria: this responds to a basic MCP client test call.
Replace `call_existing_kyc_system()` with the real internal API call.
"""
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("kyc-mcp-server", host="0.0.0.0", port=9001)

# TODO(Sprint 1): point at the real internal KYC service base URL (from .env)
EXISTING_KYC_SYSTEM_URL = "http://internal-kyc-system.local/api/v1/verify"


@mcp.tool()
async def verify_identity(national_id: str, document_image_ref: str) -> dict:
    """
    Verify a customer's identity document against the existing KYC system.

    Args:
        national_id: National ID number extracted from the uploaded document.
        document_image_ref: Reference/path to the uploaded ID document image.

    Returns:
        dict with verification status, matched fields, and confidence score,
        as produced by the existing KYC verification system.
    """
    # Placeholder until wired to the real internal endpoint.
    # async with httpx.AsyncClient() as client:
    #     resp = await client.post(EXISTING_KYC_SYSTEM_URL, json={
    #         "national_id": national_id,
    #         "document_image_ref": document_image_ref,
    #     })
    #     resp.raise_for_status()
    #     return resp.json()
    return {
        "status": "stub_not_wired",
        "national_id": national_id,
        "note": "Replace with real call to existing KYC system before Sprint 1 exit.",
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
