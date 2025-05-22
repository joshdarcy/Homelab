# Kubernetes
I use [RKE2](https://github.com/rancher/rke2) with [Calico](https://github.com/projectcalico/calico) Calico for my home Kubernetes cluster.
This has it's own subnet range that connects to my internal network via iBGP.
I'm currently moving my workloads across to Kubernetes in order to get better at using deployment, ingress, services and config-maps with live services.

## Overview
### Compute:
Master
* Intel NUC
Worker
* Raspberry Pi 4

### Networking
Calico BGP (Dummy AS64512)
* Cluster IPs: 10.43.0.0/16
* Home Network: 192.168.49.0/24

### Current Workload
SFTP Server [sftpgo](https://github.com/drakkan/sftpgo)

### WIP Workload 
#### To be migrated from Docker:
NGINX
Grafana
Portainer
InfluxDB
UptimeKuma

#### To be created for adb/dev
Apache
Redis Cache
PostgreSQL

### Network Diagram
TBC
