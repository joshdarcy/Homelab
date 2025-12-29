# Modern Monitoring & Network Observability

I recently completed the **"Modern Network Observability"** course by **David Flores, Christian Adell** and **Josh VanDeraa** on ExpertEdge (Packt) and it really changed the way I thought about network observability, especially in the modern age of networks and platforms.
One of the first chapters is "The Importance of Using Business Terms" which talks about the importance of mapping business goals into network observability data to drive incident response, reporting and customer experience.
There are three key terms that I thought were very important:
- **Service Level Indicator (SLI)**: The metric that defines the quality of the service perceived by the end-users or customers
- **Service Level Objective (SLO)**: The goal for our SLI
- **Service Level Agreement (SLA)**: The SLO translated into a formal commitment. If breached, there can be business and legal ramifications.

This means that maybe our SLA for network or platform uptime is 99.00%, our SLO at 99.99% and our real SLI sitting around 99.50%. While we're not technically breaching our SLA by providing 99.50% uptime, it shows that we're still below our goal.

### SNMP vs Telemetry
SNMP is obviously a very common and widely supported tool, has great support out of the box for a bunch of different NMS and is capable on almost all network devices in production. However, it does have some very serious limitations such as:
- **Queued Polling**: Polling is a scheduled queue that occurs at regular intervals (usually once every 5 minutes). This is counter-productive if you're trying to alert when a device, port or service goes down. It may be down for 10+ minutes before it's even reached the NOC's desk.
- **Blind Spots**: If a microburst saturates an interface for just a few seconds and vanishes before the next poll, SNMP will never see it.
- **CPU Overead**: As you need to poll more metrics from a device, the CPU overhead scales linearly which incentivises polling as litle data as possible.
- **Scaling**: SNMP Servers struggle at scale. When it comes to hundreds of thousands of ports, network devices or servers, you will need multiple polling servers and even leveraging distributed polling will result in missed or incomplete polls in most environments.

Telemetry represents "Modern Observability" - it broadcasts "Here is exactly what I'm doing right now" continually. This doesn't mean that telemetry doesn't have its own limitations:
- **Data Storage & Retention**: Due to the sheer amount of data points that come from telemetry streaming, you can not store raw data forever. You must implement Retention Policies and downsampling immediately.
- **Implementation**: Whereas many SNMP NMS solutions are out-of-the-box, Modern Telemetry stacks (such as Telegraf, InfluxDB, Grafana) need to be manually spun up and maintained. This can be a major blocker for smaller companies.
- **Legacy**: Telemetry is a feature of modern devices and operating systems. There may not be an option for telemetry streaming on a number of devices that support SNMP. 

| Feature | SNMP (Classic) | Streaming Telemetry (Modern) |
| :--- | :--- | :--- |
| **Model** | **Pull (Polling):** NMS requests data periodically. | **Push (Streaming):** Device sends data automatically. |
| **Granularity** | **Coarse:** Usually 1–5 minutes. | **Fine:** Sub-second to seconds. |
| **Data Structure** | **Unstructured/Rigid:** Uses MIBs (Management Information Bases). Parsing OIDs is computationally expensive and complex to maintain. | **Structured/Schema-driven:** Uses YANG models encoded in JSON, XML, or GPB (Google Protocol Buffers). Easy for software to ingest. |
| **Transport** | **UDP:** Unreliable, no guarantee of delivery (mostly). | **TCP / gRPC:** Reliable, efficient, supports TLS encryption. |
| **Overhead** | **High:** Linear increase in CPU load as you poll more metrics. | **Low:** "Collect once, publish to many." Optimized for bulk transfer. |
| **Primary Use** | Device health, Up/Down status, Legacy equipment. | Traffic engineering, Anomaly detection, Real-time debugging. |

### Measuring Customer Experience
Once you've set your SLI, SLO and SLA and implemented some form of hybrid stack for telemetry streaming and SNMP - now you can dive into measuring customer experience. This can be very arbitrary and issues can sometimes be harder to spot. A busier system isn't always a sign of a "better" experience and a quiet system may not be as performant as you may expect.
I'm currently working on implementing customer experience metrics for:
**Network:**
- [ ] **Wireless Performance:** Signal Strength, RSSI, Roaming, etc.
- [ ] **DHCP Handshake:** Mean time for DORA (Discover, Offer, Request, Ack) process
- [ ] **CDN Reachability:** Reachability to common CDNs such as Cloudflare and Akamai
- [ ] **TCP Retransmission Rate:** High retransmissions means the network is dropping packets
- [ ] **Jitter:** Variance in packet delay
- [ ] **Bufferbloat:** Queue latency under load

**Platform:**
- [ ] **Core Web Vitals (Google's Gold Standard):**
    - [ ] **LCP (Largest Contentful Paint):** How long until the main content is visible?
    - [ ] **CLS (Cumulative Layout Shift):** Does the page jump around while loading?
    - [ ] **INP (Interaction to Next Paint):** When I click a button, how long until the browser paints the result? This measures "responsiveness."
- [ ] **HTTP Error Rate:** Count of 5xx Errors / Total Requests
- [ ] **Database Lookups:** The P99 (slowest 1%) of lookups
- [ ] **Database Pooler Saturation:** App waiting to get a connection to the database
- [ ] **Cache Hit Ratio:** Percentage of requests served from Redis vs. hitting the database

### Conclusion
So this is the end of my braindump on my learnings of what Monitoring and Modern Observability means in todays world. I find it to be one of the most interesting topics, as it bridges the technical side of designing, implementing and maintaining to the business impact of how we are performing as a team and by extension as a business. Engineers often have a "I firmly think we should do it this way" which can sometimes be hard to justify to the business - why do we need X, how will Y upgrade help, etc. and proper observability is the key to all of this. Being able to quantify the negative impact something is having on user experience is the best way to get stakeholder buy in to implement some meaningful change.
Thanks for reading!
