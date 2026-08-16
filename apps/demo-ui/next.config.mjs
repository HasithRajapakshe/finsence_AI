/** @type {import('next').NextConfig} */
const nextConfig = {
  // API Gateway base URL — points at services/api-gateway (port 8000) per
  // the Development Plan's port table. Used by lib/api.ts.
  env: {
    NEXT_PUBLIC_API_GATEWAY_URL: process.env.NEXT_PUBLIC_API_GATEWAY_URL || "http://localhost:8000",
  },
};

export default nextConfig;
