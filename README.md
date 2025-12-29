# Homelab
My Homelab & Kubernetes Platform

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![ArgoCD](https://img.shields.io/badge/argocd-%23eb5b46.svg?style=for-the-badge&logo=argo&logoColor=white)
![Proxmox](https://img.shields.io/badge/proxmox-%23E57000.svg?style=for-the-badge&logo=proxmox&logoColor=white)
![InfluxDB](https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=InfluxDB&logoColor=white)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)

## Overview
Welcome to my homelab! I'm documenting my learning experience transitioning from traditional networking and virtualisation to a modern, cloud-native Kubernetes platform.

### About Me
I'm an Operations Engineer at Superloop <img src="https://s3-symbol-logo.tradingview.com/superloop-limited--600.png" height="20" style="vertical-align:text-bottom" alt="Superloop Logo" /> (**ASX: SLC**) a challenger telecommunications provider in Australia. I focus on implementing Modern Observability stacks and maintaining high levels of network and platform availability.

### Current Goals
The primary goal of this lab is to simulate a production-grade microservices environment with GitOps, High Availability and Modern Observability (while keeping power and noise to a minimum). 
All applications in this repository are pushed automatically by ArgoCD.

- [x] GitOps Implementation: Migrate manual installs to ArgoCD applications
- [x] Modern Observability: Implement Prometheus, InfluxDB and Loki with Grafana for cluster and network monitoring and logging
- [x] Ingress & TLS: Automate Let's Encrypt certificates via cert-manager and CloudFlare
- [ ] Custom Operators: Develop a custom Go operator to manage lab resources
- [x] Back-end & API: Build out a website back-end database and queriable API

---
## Architecture
Traffic enters the cluster via Cloudflare Proxy, which is forwarded from my MikroTik home router to the Kubernetes Nginx Ingress Controller (running in `HostNetwork` mode for bare-metal performance).

```mermaid
graph LR
    User((Internet)) -->|HTTPS/TLS| CF[Cloudflare Proxy]:::cloud
    CF -->|Port 443| Router[MikroTik hAP ax3]:::net

    %% --- Infrastructure Layer ---
    subgraph "Home Lab Infrastructure"
        Router -->|NAT 192.168.49.x| Metal[Proxmox Hypervisor]:::hw
        
        subgraph "Kubernetes Cluster (RKE2)"
            Metal -.->|Hosts| K8sMaster[K8s Control Plane]:::k8s
            
            K8sMaster -->|Deploys| Ingress[Nginx Ingress]:::k8s
            
            subgraph "Application Layer"
                Ingress -->|Route| Landing[Landing Page]:::app
                Ingress -->|Route| Obs[Grafana / Prometheus]:::app
                Ingress -->|Route| GitOps[ArgoCD]:::app
                Ingress -->|Route| API[FastAPI Backend]:::app
            end
        end
    end

    %% --- Data Flow / Logic ---
    GitOps -.->|Syncs| K8sMaster
```

### Compute:
**Intel NUC (NUC7i5DNHE)**
* CPU: Intel i5-7300 2.60 GHz CPU (4 Core)
* RAM: 8GB DDR4 RAM
* Role: 1 x RKE2 Master Node & 2 x RKE2 Worker Node

**Raspberry Pi 4**
* CPU: Broadcom BCM2711 1.80 GHz CPU (4 Core)
* RAM: 4GB DDR4 RAM
* Role: 1 x RKE2 Worker Node

### Dashboards
**Custom-built dashboard to access internal services, deployed via Docker & k8s**
https://joshdarcy.xyz
<img width="1815" height="913" alt="image" src="https://github.com/user-attachments/assets/73b7cce9-ac1e-49e9-a2ae-3b89e0cbc2d0" />

### Observability (Grafana)
**Real-time Proxmox Monitoring**
<img width="1586" height="kubectl apply -f k8s/apps/landing-page/probe.yaml794" alt="image" src="https://github.com/user-attachments/assets/85ab657f-4bf8-4e68-be29-566de008032b" />

**Real-time VM Monitoring**
<img width="1586" height="778" alt="image" src="https://github.com/user-attachments/assets/c43ca4fe-e691-410a-9275-db4558dd7fc6" />

**Real-time Cluster Monitoring**
<img width="1600" height="837" alt="image" src="https://github.com/user-attachments/assets/10841670-95c8-42da-afee-14662ffc3c7f" />
<img width="1591" height="764" alt="image" src="https://github.com/user-attachments/assets/8c217c34-3b95-4ad7-8b2c-549a35ca52f3" />
