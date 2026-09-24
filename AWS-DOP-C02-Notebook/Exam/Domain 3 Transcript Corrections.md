---
tags: [aws, dop-c02, domain-3]
verified: 2026-09-18
read: false
---

# Domain 3 Transcript Corrections

## Reading rule

The supplied course transcript is the input, not an authority when it conflicts with current service behavior. These corrections were checked against official AWS material on 2026-09-18. Current features are not a prediction of exam refresh timing.

| Transcript statement/shortcut | Correct study interpretation | Evidence note |
|---|---|---|
| Separate ALB stack is the canary solution | Valid option, not the only one; one ALB can weight two target groups | [[Elastic Load Balancing]] |
| A healthy alternative TG automatically saves a bad canary | Weighted ALB groups do not automatically transfer weights on failure | [[Elastic Load Balancing]] |
| Update EngineVersion and add a replica for minimal downtime | Property update is not a complete upgrade/cutover design; evaluate supported Blue/Green | [[Amazon RDS]] |
| New replica automatically upgrades and acts as operational writer | MySQL replica upgrade order matters; replica needs promotion for independent writes | [[Amazon RDS]] |
| RDS always upgrades primary and secondary together | Classic Multi-AZ instance versus Multi-AZ cluster and engine behavior differ | [[Amazon RDS]] |
| ALB cross-zone is always on, so cannot disable anything | On at LB level; supported TG-level override can disable it | [[Elastic Load Balancing]] |
| Disabling cross-zone generally saves money | Charges depend on LB/traffic type; do not generalize NLB charges to ALB | [[Domain 3 Official Sources]] |
| Cross-zone setting automatically adds per-AZ scaling | ASG policy/metric selection and zonal capacity are separate | [[Amazon EC2 Auto Scaling]] |
| NLB always retains both IPs in the given scenario | True under cross-zone/default thresholds; configured thresholds and other TGs matter | [[Elastic Load Balancing]] |
| One healthy TG is sufficient for NLB DNS | An unhealthy attached TG can cause withdrawal affecting all TG traffic | [[Elastic Load Balancing]] |
| DAX increases throughput and saves cost universally | Eligible read offload; workload-dependent total savings; not write capacity | [[Amazon DynamoDB Accelerator (DAX)]] |
| DAX caches every read | Strongly consistent and transactional reads pass through | [[Amazon DynamoDB Accelerator (DAX)]] |
| RDS SNS notification is an immediate ordered failure signal | Notifications can take up to five minutes and are not ordered | [[Amazon RDS]] |
| Lambda promotion + DNS is the whole recovery plan | Health confirmation, freshness, fencing, compute readiness and reconnect are needed | [[Disaster Recovery Strategies]] |
| DynamoDB global tables improve Aurora as an interchangeable choice | Different NoSQL data model; not a drop-in relational database replacement | [[RDS Multi-AZ vs Read Replicas vs Aurora Global Database]] |
| DNS changes propagate instantly if caches are flushed | Only caches you control can be flushed; resolver TTLs and connections still matter | [[Amazon Route 53]] |
| Global Accelerator can be attached to any service endpoint | Standard endpoints are ALB/NLB/EC2/EIP; not direct API Gateway/RDS | [[AWS Global Accelerator]] |
| EKS automatically scales applications across Regions | Regional clusters; pod and node scaling are distinct configured mechanisms | [[Amazon EKS]] |
| Fargate automatically chooses application replica capacity | Supplies compute; ECS/HPA replica policies still needed | [[AWS Fargate]] |
| Serverless never incurs idle-capacity cost | Running Fargate allocations and Lambda provisioned concurrency can cost while idle | [[AWS Fargate]], [[AWS Lambda]] |
| Transit gateways use intra-Region peering between Regions | Inter-Region peering; static routes needed on both sides | [[AWS Transit Gateway]] |
| ECR replication makes all existing images local | Newly pushed/restored images replicate after configuration; preexisting images need handling | [[Amazon ECR]] |
| Regional API means only same-Region clients can access it | Public Regional endpoint can serve public clients; not an edge-optimized CloudFront endpoint | [[Amazon API Gateway]] |
| SAM container build means Lambda must deploy as a container image | Build isolation and deployment package type are different choices | [[AWS SAM]] |
| Warmup blocks all target tracking/step scaling | New capacity changes aggregate metrics; further scale-out can occur, scale-in is constrained | [[Amazon EC2 Auto Scaling]] |
| Route 53 failover makes a read replica writable | DNS routing does not promote the replica | [[Amazon Route 53]], [[Amazon RDS]] |
| Any backup supports automatic or on-demand regional copy equally | Service/type support varies; continuous copies become snapshots; no on-demand continuous-copy support | [[AWS Backup]] |
| Snapshot cross-Region copying always takes hours | Duration depends on data/Region/service; measure copy and restore, do not assume a fixed time | [[Disaster Recovery Strategies]] |
| S3 replication guarantees five-minute RPO | Async behavior; RTC's 15-minute objective is not a five-minute guarantee | [[Amazon S3]] |
| S3 live replication covers every old object | Existing/failed objects may need Batch Replication | [[Amazon S3]] |
| Config/CloudFormation drift detection proves DR readiness | Useful configuration checks, not full restore/failover/failback validation | [[Disaster Recovery Testing and Failback]] |
| ARC is only the older DNS routing-control service | Current ARC also includes zonal capabilities and Region switch orchestration | [[Amazon Application Recovery Controller]] |

## Preserved versus extended scope

The transcript's underlying resilience/scaling/DR goals are retained. ARC Region switch and controlled resilience testing are current/supplementary detail, clearly separated from the original transcript. See [[Domain 3 Transcript Coverage]] and [[Domain 3 Official Sources]].
