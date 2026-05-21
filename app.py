"""
securedash
-----------
Flask security dashboard showing findings, severity counts, and alerts.

Install: pip install flask
Run:     python app.py  -> open http://localhost:5000
"""

from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

FINDINGS = [
    {"id": "F-001", "severity": "CRITICAL", "title": "Unpatched CVE-2024-1234 on web01", "status": "Open", "date": "2024-03-01"},
    {"id": "F-002", "severity": "HIGH",     "title": "Overprivileged IAM roles (AWS)", "status": "Open", "date": "2024-03-02"},
    {"id": "F-003", "severity": "HIGH",     "title": "Missing MFA on 4 admin accounts", "status": "In Progress", "date": "2024-03-03"},
    {"id": "F-004", "severity": "MEDIUM",   "title": "Verbose error messages in prod", "status": "Open", "date": "2024-03-04"},
    {"id": "F-005", "severity": "MEDIUM",   "title": "S3 bucket with public read ACL", "status": "Resolved", "date": "2024-03-05"},
    {"id": "F-006", "severity": "LOW",      "title": "Outdated SSL cipher suites", "status": "Open", "date": "2024-03-06"},
]

ALERTS = [
    {"time": "08:14", "message": "Failed SSH login - root@10.0.0.15 (47 attempts)"},
    {"time": "08:33", "message": "Outbound connection to flagged IP 45.33.32.156"},
    {"time": "09:01", "message": "Admin account login outside business hours"},
    {"time": "09:45", "message": "Large file download by user jdoe (4.2 GB)"},
]


def get_summary():
    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in FINDINGS:
        if f["status"] != "Resolved":
            counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    return counts


@app.route("/")
def index():
    return render_template(
        "dashboard.html",
        summary=get_summary(),
        findings=[f for f in FINDINGS if f["status"] != "Resolved"],
        alerts=ALERTS,
        generated=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )


@app.route("/api/findings")
def api_findings():
    return jsonify(FINDINGS)


@app.route("/api/summary")
def api_summary():
    return jsonify(get_summary())


if __name__ == "__main__":
    app.run(debug=True)
