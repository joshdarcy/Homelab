import os
import json
import logging
from netmiko import ConnectHandler, NetmikoTimeoutException

# Best Practice: Never hardcode credentials. Use Env Vars.
USERNAME = os.getenv('NET_USER')
PASSWORD = os.getenv('NET_PASS')

OPTICAL_LOW_THRESHOLD = -25.0

def get_devices():
    return [
        {
            'device_type': 'cisco_ios',
            'host': '192.168.49.230',
	    'username': USERNAME,
            'password': PASSWORD,
        },
        {
            'device_type': 'juniper_junos',
            'host': '192.168.49.231',
            'username': USERNAME,
            'password': PASSWORD,
        }
    ]

def check_optical_levels(conn, device_type):
    issues = []
    if device_type == 'cisco_ios':
        output = conn.send_command("show interfaces transceiver detail", use_textfsm=True)
        for interface in output:
            try:
                rx_power = float(interface.get('rx_power', 0))
                if rx_power < OPTICAL_LOW_THRESHOLD and rx_power != 0.0:
                    issues.append({
                        'interface': interface['port'],
                        'issue': 'Low Optical Power',
                        'value': rx_power
                    })
            except ValueError:
                continue

    elif device_type == 'juniper_junos':
        output = conn.send_command("show interfaces diagnostics optics | display json")
        data = json.loads(output)
    return issues

def main():
    logging.basicConfig(level=logging.INFO)
    devices = get_devices()
    report = {}

    for device in devices:
        logging.info(f"Connecting to {device['host']}...")
        try:
            with ConnectHandler(**device) as conn:
                optical_issues = check_optical_levels(conn, device['device_type'])
                if optical_issues:
                    report[device['host']] = optical_issues
                    logging.warning(f"Issues found on {device['host']}")
                else:
                    logging.info(f"{device['host']} is healthy.")

        except NetmikoTimeoutException:
            logging.error(f"Could not connect to {device['host']}")

    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()
