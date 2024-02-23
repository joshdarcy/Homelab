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
* 64GB DDR4 RAM
* Asus GeForce GTX 1080 8GB GPU
* Samsung 870 EVO 500GB SSD
* WD Blue 1TB HDD

#### Storage
* Synology DS218+
* 2 x WD RED 4TB HDD (RAID1)
#### Networking
* MicroTik hAP ax3
* Ubiquiti Unifi AC Long-Range Access Point

#### Network Diagram
![Homelab](https://github.com/joshdarcy/Homelab/assets/130115650/dcaf4a73-b2c4-49dd-8d91-25ba56437e03)

Both the Proxmox Server, NAS and Access Point are connected directly to the MicroTik LAN bridged ports.


