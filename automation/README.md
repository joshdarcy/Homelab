# Automation

Automation and AI Adoption is a big focus of today's world, especially in the telecommunications sector. Everything from automatic remediation, event correlation and customer self-service is being actively driven and all of these are supported in some way by automation.
There's a few kinds of automation that I think are really important:
- **Self-Service Diagnostics**: Giving the customer the ability to run realtime tests to diagnose, troubleshoot and restore connectivity. This improves the customer experience (no longer need to reach out to support via chat, email or phone) and can progress cases much faster if a physical visit is required.
- **Automatic Remediation**: When an alert triggers, have a way to automatically resolve (webhook > automation job). This might be restarting a microservice, disconnecting a malicious user or adjusting a configuration.
- **Repetitive Tasks**: Roll out bulk configuration changes (e.g. adding a VLAN), show output that can only be ran on CLI or re-authenticate a bunch of RADIUS sessions

### Tools
I primarily use Ansible (via Jenkins) for almost all automation. Jenkins is widely supported and has multiple authentication methods (NETCONF, Paramiko, etc.) so it can be incredibly versatile at automating tasks across network devices and Linux systems.

*Work in progress*
