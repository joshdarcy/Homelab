# Homelab
My Homelab

Working in primarily in a Windows, Windows Server & 365/Azure environment, this lab is used as an environment to test configurations with:
* Linux
* Proxmox
* Docker
* Ansible & Automation
* Monitoring via HTTP POST/GET requests

Current goals:
* Better understand SSL certificate processes (Specifically through LetsEncrypt and related automation)
* Better understand how webservers are hosted, accessed and secured
* Dive into load balancers and reverse-proxy for accessing my internal network remotely

## Overview
### Hardware:
I recently replaced an old PC for an Intel NUC (NUC7i5DNHE) for lower power draw:
* Intel i5-7300 2.60 GHz CPU (4 Core)
* 8GB DDR4 SDRAM
* Samsung 870 EVO 256GB SSD

#### Storage
* Synology DS916+
* 2 x WD RED 4TB HDD (RAID1)
#### Networking
* MicroTik hAP ax3
* Ubiquiti Unifi AC Long-Range Access Point

### Network Diagram

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

