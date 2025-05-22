# Homelab
My Homelab

I've expanded my homelab outside of the traditional docker running on Ubuntu server to incorporate a Kubernetes environment to further progress my platform/infrastructure knowledge in a modern environment.
The Intel NUC hosts the same traditional services listed below through Docker but also acts as the master node in my RKE2 k8s cluster.

Current goals:
* Better understand Kubernetes networking specifically with Calico (load balancers, BGP peering, etc.)
* Better understand Kubernetes workload management including resource caps and using labels/tags to allocate to specific nodes
* Complete SSL certificate automations for internal and ingress traffic to my k8s cluster 
* Build out a development environment for testing and staging changes for a production environment

## Overview
### Compute:
Intel NUC (NUC7i5DNHE)
* Intel i5-7300 2.60 GHz CPU (4 Core)
* 8GB DDR4 RAM

Raspberry Pi 4
* Broadcom BCM2711 1.80 GHz CPU (4 Core)
* 4GB DDR4 RAM

#### Storage
* Synology DS916+ NAS
* 2 x WD RED 4TB HDD (RAID1)

#### Networking
* MicroTik hAP ax3
* Ubiquiti Unifi AC Long-Range Access Point

### Network Diagram

#### Outdated

The Proxmox Server, NAS and Access Point are connected directly to the MicroTik LAN bridged ports.
Domain and Sub-domains are automatically renewed by Certbot with LetsEncrypt certificates
![image](https://github.com/user-attachments/assets/8d8ea642-8a6a-4f3b-bb91-572c9d2094e9)

### Dashboards
#### Website https://joshdarcy.xyz/
#### Uptime Kuma https://uptime.joshdarcy.xyz/

![image](https://github.com/joshdarcy/Homelab/assets/130115650/44304812-28e9-4396-b6bc-dd10b9543ba4)
#### Grafana https://grafana.joshdarcy.xyz/

![image](https://github.com/user-attachments/assets/3eff5ba0-e3e8-48e8-afe1-b72468f9d1f0)
![359754046-ac84149e-a477-44ac-b361-f1e566c30966](https://github.com/user-attachments/assets/5b247c6f-eb89-4510-9442-1cd902f9abdc)


#### Portainer https://portainer.joshdarcy.xyz/

![image](https://github.com/joshdarcy/Homelab/assets/130115650/68f7447d-90dd-445c-b186-1d2b766291c0)

