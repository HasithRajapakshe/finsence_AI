"""
MCP server wrapping the company's EXISTING CRIB (credit bureau) check system,
per SRS FR-CRD-01 and BRD BR-002. Thin adapter only — no scoring logic here.

Sprint 1 exit criteria: this responds to a basic MCP client test call.
Replace `call_existing_crib_system()` with the real internal API call.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("crib-mcp-server", host="0.0.0.0", port=9002)

EXISTING_CRIB_SYSTEM_URL = "http://internal-crib-system.local/api/v1/check"


@mcp.tool()
async def check_crib_record(national_id: str) -> dict:
    """
    Query the existing CRIB system for a credit bureau record.

    Args:
        national_id: National ID number of the applicant.

    Returns:
        dict with has_record (bool), score (if available), and raw CRIB
        response fields. If has_record is False, the caller (Credit-Scoring
        Agent) falls back to alternative-data scoring per BR-001.
    """
    return {
        "status": "stub_not_wired",
        "national_id": national_id,
        "has_record": None,
        "note": "Replace with real call to existing CRIB-check system before Sprint 1 exit.",
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
