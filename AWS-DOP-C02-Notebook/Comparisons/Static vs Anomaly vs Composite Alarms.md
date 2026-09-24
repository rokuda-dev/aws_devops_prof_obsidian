---
tags: [aws, dop-c02, domain-4]
verified: 2026-09-18
read: false
---

# Static vs Anomaly vs Composite Alarms

| Type | Decision basis | Good cue | Caution |
|---|---|---|---|
| Static | Known fixed limit | At least one policy-change match; established saturation limit | Statistic, period and missing data must match meaning |
| Anomaly | Learned upper/lower metric band | Seasonal/variable baseline | Unexpected != malicious; training/sensitivity matters |
| Composite | Conditions over alarm states | Page only when multiple symptoms indicate impact | Action support differs; not a new metric |

Warning/critical alarms can independently watch the same metric with different evaluation settings. Use M-of-N to tune noise versus detection speed; avoid an arbitrary universal threshold.

Alarms do not prove action success. Test state transitions, subscriptions/permissions and the resulting deployment/runbook behavior.

Tasks 4.2–4.3. See [[Metric Alarms and Anomaly Detection]], [[Monitoring Correlation Tracing and Dashboards]].
