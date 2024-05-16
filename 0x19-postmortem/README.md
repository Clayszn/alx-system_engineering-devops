#postmortem
Server Outage Due to Power Failure

Issue Summary:
Duration of the Outage: The outage lasted for  2 minutes, starting at 2:20 PM and ending at 2:22 PM (UTC) on May 8, 2024.
Impact: The outage affected the internet connectivity, all applications hosted on our servers, resulting in a complete service downtime. Users and Clients were unable to access any hosted applications, with 100% of users experiencing service disruption.
Root Cause: The root cause of the outage was a power failure in the data centre housing our servers, which caused all systems to go offline.
Timeline:
2:20 PM: Issue detected after noise from ups indicated that the primary power source was malfunctioning
2:22 PM: In-House and On-Call engineers confirmed the issue and initiated an investigation.
2:30PM: Customers and Users began reporting inability to access services.
2:30 PM: Initial assumption was inverter not being charged efficiently; network team was notified and began diagnostics.
2:31 PM: Data centre operations team confirmed power failure affecting the entire facility.
2:31 PM: The Servers went down, Backup generators were activated and full reboot and reload was initiated but several servers failed to restart automatically
2:40 PM: Infrastructure team started manual reboot procedures for affected servers.
3:15 PM: Most critical servers back online; services and  wireless internet gradually restored.
4:00 PM: Full service restoration confirmed; all applications functional.
Root Cause and Resolution:
Root Cause: The power failure at the data centre was due to a malfunction in the primary power supply system. The automatic transfer switch (ATS) failed to switch to backup power, leading to a complete power loss. When backup generators were manually activated, several servers required manual intervention to reboot.
Resolution: The issue was resolved by manually activating the backup generators and manually restarting the affected servers. The data centre operations team fixed the ATS malfunction, ensuring that backup power would engage automatically in the future.



Corrective and Preventative Measures:
Improvements Needed:
Enhance power redundancy and automatic failover mechanisms.
Improve server auto-reboot configurations.
Enhance monitoring to detect power issues faster.

Specific Tasks:
Inspect and Repair ATS: Ensure the automatic transfer switch is fully functional and undergoes regular maintenance checks.
Configure Auto-Reboot: Update server configurations to ensure all systems automatically reboot after power restoration.
Implement Power Redundancy: Install additional power redundancy measures, such as additional UPS systems.
Enhance Monitoring: Deploy enhanced monitoring tools to detect power issues more quickly and accurately.
Conduct Drills: Schedule regular disaster recovery drills to ensure all teams are prepared for similar incidents.
Review Data Center SLA: Review and potentially update the service level agreement with the data centre to ensure faster response times for power-related issues.
Customer Communication Plan: Develop a robust customer communication plan to provide timely updates during outages.

