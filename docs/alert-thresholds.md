# Alert Threshold Configuration

SecureDash raises dashboard alerts when a monitored security metric crosses a
configured threshold. Thresholds are defined per metric and mapped to a
severity level.

## Severity Levels

| Level    | Meaning                                  | Default Color |
|----------|------------------------------------------|---------------|
| Critical | Immediate action required                | Red           |
| High     | Investigate within the current shift     | Orange        |
| Medium   | Review during regular triage             | Yellow        |
| Low      | Informational, no action needed          | Blue          |

## Configuring Thresholds

Thresholds are set in `config/thresholds.yaml`. Each entry maps a metric key to
one or more severity bands:

```yaml
failed_logins_per_min:
  critical: 50
  high: 20
  medium: 5
open_critical_findings:
  critical: 1
  high: 0
tls_cert_days_remaining:
  critical: 3
  high: 7
  medium: 14
```

For descending metrics such as `tls_cert_days_remaining`, an alert fires when
the value falls **at or below** the band. For ascending metrics such as
`failed_logins_per_min`, an alert fires when the value rises **at or above** the
band.

## Notes

- A metric with no configured band is displayed on the dashboard but never
  triggers an alert.
- Bands are evaluated from most to least severe; the first match wins.
- Reload thresholds without restarting the app via the `/reload-config`
  endpoint.
