# Homelab
My Homelab

Working in primarily in a Windows, Windows Server & 365/Azure environment, this lab is used as an environment to test configurations with:
* Linux
* Proxmox
* Docker

Current goals:
* Better understand SSL certificate processes (Specifically through LetsEncrypt and related automation)
* Better understand how webservers are hosted, accessed and secured
* Dive into load balancers and reverse-proxy for accessing my internal network remotely

## Overview
### Hardware:
By Frankenstein-ing some old gear from work and friends, I've got a machine powerful enough for my virtualization needs with relatively low power draw:
* Intel i7 9700F CPU
* 16GB DDR4 RAM
* Asus GeForce GTX 1080 8GB GPU
* Samsung 870 EVO 500GB SSD
* WD Blue 1TB HDD

#### Storage
* Synology DS218+
* 2 x WD RED 4TB HDD (RAID1)
#### Networking
* MicroTik hAP ax3
* Ubiquiti Unifi AC Long-Range Access Point

### Network Diagram

![Homelab(2) drawio](https://github.com/joshdarcy/Homelab/assets/130115650/788f0cd6-dda8-4ad9-b889-1b6f7962fdbb)

The Proxmox Server, NAS and Access Point are connected directly to the MicroTik LAN bridged ports.

### Dashboards
#### Website https://joshdarcy.xyz/
#### Uptime Kuma https://uptime.joshdarcy.xyz/

![image](https://github.com/joshdarcy/Homelab/assets/130115650/44304812-28e9-4396-b6bc-dd10b9543ba4)
#### Grafana https://grafana.joshdarcy.xyz/

![image](https://github.com/joshdarcy/Homelab/assets/130115650/4e9a3301-3fb1-45bc-be00-55d5a46609ae)
#### Portainer https://portainer.joshdarcy.xyz/

![image](https://github.com/joshdarcy/Homelab/assets/130115650/68f7447d-90dd-445c-b186-1d2b766291c0)

