---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# RDS Blue Green vs EngineVersion Update vs Read Replica Promotion

| Mechanism | Purpose | Why it is not interchangeable |
|---|---|---|
| In-place EngineVersion update | Upgrade existing DB through a supported path | Deployment request can entail downtime; Multi-AZ topology/engine matters |
| RDS Blue/Green Deployment | Test a synchronized green environment and perform guarded switchover | Supported engines/features only; short switchover still needs app/data safeguards |
| Read-replica promotion | Turn an eligible replica into an independent writable DB | Breaks replication relationship; async lag and failback need planning |
| Aurora managed switchover/failover | Change global primary using supported Aurora features | Separate topology and service behavior |

For a major MySQL upgrade, do not assume an arbitrary replica plus a CloudFormation property update gives transparent zero downtime. Review replica upgrade order, compatibility, and actual switchover design.

Tasks 3.1 and 3.3. See [[Amazon RDS]], [[Amazon Aurora Global Database]], [[Domain 3 Transcript Corrections]].

- [RDS Blue/Green](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-overview.html)
- [MySQL upgrade strategy](https://aws.amazon.com/blogs/database/upgrade-strategies-for-amazon-rds-for-mysql-8-0-to-8-4/)
