_All credit for this goes to https://github.com/keczejo/mikrotik-influxdb & https://github.com/pavelkim/mikrotik_


# MikroTik Grafana & InfluxDB Monitoring
Recommended Grafana dashboard https://grafana.com/grafana/dashboards/16601

## MikroTik Interface Traffic
Counts rx, tx and total transferred bytes on network interfaces. Stores results in interface's comment and pushes them to InfluxDB.

1. Initialise Comment Metadata On Each Interface

```
/interface ethernet set ether1 comment="{traffic:null}"
```

2. Import Script into MikroTik

3. Set your InfluxDB Site URL & Auth Token

```
:global influxDBURL "https://www.myinfluxdb.local:8087/api/v2/write"
/tool fetch url="$influxDBURL" http-header-field="Authorization: Token MY_TOKEN" keep-result=no http-method=post http-data="$postRequestPayload"
```

## MikroTik Health Exporter
Reads CPU, disk and memory metrics, and pushes them into InfluxDB.

1. Import Scripts into MikroTik
2. Set your InfluxDB Site URL & Auth Token

```
:global influxDBURL "https://www.myinfluxdb.local:8087/api/v2/write"
/tool fetch url="$influxDBURL" http-header-field="Authorization: Token MY_TOKEN" keep-result=no http-method=post http-data="$postRequestPayload"
```

## Configure Dashboard in Grafana for the corresponding bucket

![image](https://github.com/user-attachments/assets/ac84149e-a477-44ac-b361-f1e566c30966)
