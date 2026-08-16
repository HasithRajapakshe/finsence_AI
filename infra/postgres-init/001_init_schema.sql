-- Sprint 1: minimal schema so the DB is not empty on first boot.
-- Real tables (applications, decisions, audit_log, consent_records) are
-- designed and migrated properly in Sprint 2+ alongside the agents that own them.

CREATE TABLE IF NOT EXISTS service_health_check (
    id SERIAL PRIMARY KEY,
    service_name TEXT NOT NULL,
    checked_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
