/**
 * Thin client for the API Gateway (services/api-gateway, port 8000).
 * The frontend never calls agent services directly — always through the
 * gateway, per the layered architecture in the System Design.
 */
const API_GATEWAY_URL = process.env.NEXT_PUBLIC_API_GATEWAY_URL ?? "http://localhost:8000";

export async function getGatewayHealth() {
  const res = await fetch(`${API_GATEWAY_URL}/health`, { cache: "no-store" });
  if (!res.ok) throw new Error(`Gateway health check failed: ${res.status}`);
  return res.json();
}
