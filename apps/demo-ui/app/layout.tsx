import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "FinSense AI",
  description: "AI-driven credit inclusion and compliance copilot for South Asian digital lenders",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-slate-50 text-slate-900">{children}</body>
    </html>
  );
}
