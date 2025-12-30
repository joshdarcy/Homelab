# Automation

Automation and AI adoption are big focus areas in today's world, especially in the telecommunications sector. Automatic remediation, event correlation, and customer self-service are being actively driven by the need for speed & reliability and all of these are supported by automation.

There are a few kinds of automation that I think are critical:
- **Self-Service Diagnostics**: Giving the customer the ability to run real-time tests to diagnose, troubleshoot, and restore connectivity. This improves the customer experience (reducing the need to reach out to support) and can progress cases much faster if a physical visit is required.
- **Automatic Remediation**: Triggering automatic resolution workflows based on alerts (Webhook $\rightarrow$ Automation Job). This might be restarting a microservice, disconnecting a malicious user, or adjusting a traffic policy.
- **Operational Efficiency**: Rolling out bulk configuration changes (e.g., adding a VLAN across 50 switches), gathering complex CLI outputs for reports, or re-authenticating stale RADIUS sessions.
- **Configuration Management**: Preventing configuration drift between manual troubleshooting and config changes by continuously comparing the live state to a master template (usually stored in Git).

### Tools
I primarily use **Ansible** (via Jenkins) for the majority of my automation workflows. Ansible is widely supported and utilizes agentless connection methods (SSH, NETCONF, RESTconf), making it incredibly versatile for automating tasks across legacy network devices and modern Linux systems alike.
I also utilize **Python** for Network Programming. While Ansible is excellent for defining "desired state," I use Python when I need complex logic, such as parsing unstructured CLI data or performing advanced health checks that require arithmetic logic (e.g., comparing optical light levels against a threshold).

### Key Concept: Idempotency
One of the most important principles of Ansible is **Idempotency**. This means that an automation script can be run multiple times without changing the result beyond the initial application.
- **Bad Automation:** A script that sends "add vlan 10" every time it runs. If run twice, it might error out or create duplicates.
- **Idempotent Automation:** A script that checks "Does VLAN 10 exist?" If yes, do nothing. If no, create it.
This allows me to run playbooks safely against production environments without fear of breaking existing configurations.

### Challenges in Telecom
In physical networking, there are real automation constraints compared to cloud computing or standard DevOps principles that are often overlooked:
- **Production Hardware:** We aren't just spinning up new resources in AWS. We are automating changes on live physical routers carrying customer traffic. You can't just "destroy and recreate" a core router, so it is vital that adequate controls are in place to prevent major outages.
- **Vendor Agnosticism:** The business goal is usually to "deploy Service X," so the automation must be able to translate that into specific syntax for Cisco, Juniper, Nokia, or MikroTik.
- **Safety Mechanisms:** It is critical to implement **Pre-checks** (verifying state before change) and **Post-checks** (verifying service health after). If a deployment fails or a config is incorrect, the management session could drop, locking you out of a production device.

### Codifying Infrastructure (GitOps)
By migrating master configurations to **Git**, I am able to safely test, stage, and deploy configuration changes to hundreds of devices across different vendors without risking major outages.
This treats the network as **Infrastructure as Code (IaC)** and helps to keep a precise changelog of *when* and *why* a configuration change was required. It has the added advantage of allowing multiple active branches, making peer review of configuration changes streamlined and auditable.

### Current Homelab Projects
- [ ] **Node Deployment:** Create an Ansible playbook to deploy a node from base Debian12 image to RKE2 worker joined to the k8s cluster and taking on workloads
- [ ] **Automatic Configuration Sync:** Scheduled configuration syncs of my MikroTik hAP ax3 to a master template stored in Git
- [ ] **API-Driven Checks:** Implement something on my homelab landing page that allows visitors to live-check parts of my network (number of leases, current traffic, etc.)


