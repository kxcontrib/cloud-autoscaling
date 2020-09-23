Auto Scaling for a kdb+ realtime database
=========================================


Companion scripts to [Auto Scaling for a kdb+ realtime database](https://code.kx.com/q/cloud/autoscale/)


The paper presents a solution for a scalable real-time database cluster.
The simulations carried out show savings of up to 50% could be made.
These savings, along with the increased availability of the cluster, could make holding a whole day’s data in memory more feasible for kdb+ databases.

If not, the cluster can be used alongside an intraday write-down process.
If an intraday write is incorporated in a system it is usually one that needs to keep memory usage low.

The scalability of the cluster can guard against large spikes in intraday data volumes crippling the system.
Used in this way very small instances could be used to reduce costs.

The `.u.asg` functionality in the tickerplant also gives the opportunity to run multiple clusters at different levels of risk.
Highly important data can be placed in a cluster with a low scale threshold or larger instance size.

If certain data sources do not need to be available with a low latency clusters with smaller instances and higher scale thresholds can be used to reduce costs.


## Author

Jack Stapleton is a kdb+ consultant for Kx who has worked for some the world’s largest financial institutions.
Based in Dublin, Jack is currently working on the design, development, and maintenance of a range of kdb+ solutions in the cloud for a leading financial institution.

