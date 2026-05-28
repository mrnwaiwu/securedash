# Dashboard Widget Reference

## Available Widgets

### Threat Overview
Displays a summary of active threats grouped by severity (critical, high, medium, low).

**Config options:**
```yaml
widget: threat-overview
refresh_interval: 60  # seconds
severity_filter: [critical, high]
```

### CVE Feed
Live feed of CVEs relevant to your registered assets.

**Config options:**
```yaml
widget: cve-feed
max_items: 20
min_cvss: 7.0
sources: [nvd, mitre]
```

### Auth Events
Timeline of authentication events (logins, failures, MFA prompts).

**Config options:**
```yaml
widget: auth-events
lookback_hours: 24
show_failures_only: false
```

### Compliance Score
Gauge showing current compliance posture across configured frameworks.

**Config options:**
```yaml
widget: compliance-score
frameworks: [soc2, nist-csf, hipaa]
```

### Asset Inventory
Table of monitored assets with last-seen timestamp and risk score.

**Config options:**
```yaml
widget: asset-inventory
sort_by: risk_score
descending: true
page_size: 50
```

## Adding Custom Widgets

Widgets are registered in `config/widgets.yaml`. Each widget must implement the `BaseWidget` interface and expose a `render()` method.
