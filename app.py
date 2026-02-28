from datetime import datetime, timezone

from flask import Flask, render_template

app = Flask(__name__)

SERVICES = [
    {
        "title": "Operational analytics and KPI engineering",
        "description": "Define measurable system health with normalized, decision-ready metrics built around real operating constraints.",
    },
    {
        "title": "Data pipelines (ETL/ELT, BigQuery, event logs)",
        "description": "Build reliable ingestion and modeling layers that keep timestamps, event semantics, and lineage clear.",
    },
    {
        "title": "Automation and internal tools",
        "description": "Turn repetitive operational workflows into deterministic automations that reduce manual triage time.",
    },
    {
        "title": "AI-assisted workflows",
        "description": "Apply pragmatic AI for classification, triage, and decision support where latency and accuracy both matter.",
    },
    {
        "title": "Dashboards and reporting",
        "description": "Ship dashboards that explain what happened, why it happened, and exactly where intervention changes outcomes.",
    },
]

PROCESS_STEPS = [
    {
        "step": "Instrument the system",
        "detail": "Events, timestamps, and shared definitions that map cleanly to operational reality.",
    },
    {
        "step": "Build reliable data models",
        "detail": "Clean, queryable, and tested models that can support decision cycles without rework.",
    },
    {
        "step": "Diagnose root cause",
        "detail": "Normalized KPIs and segmentation to separate symptoms from true upstream failure modes.",
    },
    {
        "step": "Deliver an intervention playbook",
        "detail": "A concrete action plan showing where to act, in what order, and why each move matters.",
    },
]

PROOF_POINTS = [
    "Reduced SLA risk by pinpointing upstream failure modes before breach hours.",
    "Improved staffing and incentive decisions by separating inherited backlog from demand volatility.",
    "Aligned executives and operators around a shared KPI system tied to renewal and retention risk.",
]

TOOL_BADGES = [
    "BigQuery",
    "Python",
    "Supabase",
    "HL7 / event logs",
    "Cloud Run",
    "Looker/BI",
    "Postgres",
    "APIs",
]

CASE_STUDIES = [
    {
        "id": "teleradiology",
        "title": "From a Weekend SLA Breakdown to a Repeatable Queue-Diagnostics System",
        "summary": "Validated root cause, replaced volume assumptions with queue diagnostics, and produced an hour-by-hour intervention playbook.",
        "tags": ["BigQuery", "Supabase", "Python", "HL7/event logs"],
    }
]


@app.context_processor
def inject_globals():
    return {
        "current_year": datetime.now(timezone.utc).year,
    }


@app.get("/")
def index():
    return render_template(
        "index.html",
        page_title="AI + Data Consultancy",
        services=SERVICES,
        process_steps=PROCESS_STEPS,
        proof_points=PROOF_POINTS,
        tool_badges=TOOL_BADGES,
    )


@app.get("/case-studies")
def case_studies():
    return render_template(
        "case_studies.html",
        page_title="Case Studies | AI + Data Consultancy",
        case_studies=CASE_STUDIES,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
