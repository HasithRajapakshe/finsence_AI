"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [gatewayStatus, setGatewayStatus] = useState("checking...");

  useEffect(() => {
    async function checkGateway() {
      try {
        const res = await fetch(
          `${process.env.NEXT_PUBLIC_API_GATEWAY_URL || "http://localhost:8000"}/health`,
          { cache: "no-store" }
        );
        if (!res.ok) throw new Error(`status ${res.status}`);
        const data = await res.json();
        setGatewayStatus(data.status);
      } catch {
        // Gateway not running yet in Sprint 1 — expected until docker compose up.
        setGatewayStatus("unreachable");
      }
    }
    checkGateway();
  }, []);

  return (
    <main
      style={{
        display: "flex",
        minHeight: "100vh",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        gap: "1rem",
        padding: "2rem",
      }}
    >
      <h1 style={{ fontSize: "1.875rem", fontWeight: 600 }}>FinSense AI</h1>
      <p style={{ color: "#475569" }}>
        Multi-agent credit inclusion &amp; compliance copilot
      </p>
      <div
        style={{
          borderRadius: "0.5rem",
          border: "1px solid #e2e8f0",
          backgroundColor: "#ffffff",
          padding: "0.5rem 1rem",
          fontSize: "0.875rem",
        }}
      >
        API Gateway status:{" "}
        <span style={{ fontFamily: "monospace" }}>{gatewayStatus}</span>
      </div>
    </main>
  );
}