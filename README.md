# dnf_collector.py

### A node-exporter collector for dnf upgrades

The community yum.sh collector did not include a separate metric for updates with security advisories. This reports the separate metric as well as leverages dnf's python library directly.

This has been tested on:
* RHEL 9, 10
* CentOS Stream 9, 10
* AlmaLinux 8, 9, 10
* RockyLinux 8, 9, 10
* Fedora 38-42

Enterprise Linux variants (everything here except Fedora) [need EPEL configured](https://docs.fedoraproject.org/en-US/epel/).

Depends on the Prometheus client library and is tested with the EPEL/Fedora provided versions for all aforementioned distros.
```
# dnf install python3-prometheus_client
```

NOTE: although this appears to be fixed in 10.1 based on CentOS Stream, EL10 does not include python3-prometheus_client in EPEL. Installing from pip won't pull in other dependencies, so you can do that without making a mess. Alternatively, this can be ignored on 10.1 or higher images going forward.

Help:
```
% ./dnf_collector.py -h
usage: dnf_collector.py [-h] [-o FILENAME]

Expose metrics from dnf updates.

options:
  -h, --help            show this help message and exit
  -o FILENAME, --outfile FILENAME
                        Optional output file to use rather than standard output.
```

Example output
```
# HELP dnf_security_upgrades_pending Security upgrades pending
# TYPE dnf_security_upgrades_pending gauge
dnf_security_upgrades_pending{origin="epel"} 0.0
dnf_security_upgrades_pending{origin="epel-cisco-openh264"} 0.0
dnf_security_upgrades_pending{origin="grafana"} 1.0
dnf_security_upgrades_pending{origin="hashicorp"} 0.0
dnf_security_upgrades_pending{origin="influxdb"} 0.0
dnf_security_upgrades_pending{origin="kubernetes"} 0.0
dnf_security_upgrades_pending{origin="ookla_speedtest-cli"} 0.0
dnf_security_upgrades_pending{origin="ookla_speedtest-cli-source"} 0.0
dnf_security_upgrades_pending{origin="opentofu"} 0.0
dnf_security_upgrades_pending{origin="opentofu-source"} 0.0
dnf_security_upgrades_pending{origin="rhel-9-for-aarch64-appstream-rpms"} 1.0
dnf_security_upgrades_pending{origin="rhel-9-for-aarch64-baseos-rpms"} 6.0
# HELP dnf_upgrades_pending upgrades pending
# TYPE dnf_upgrades_pending gauge
dnf_upgrades_pending{origin="epel"} 0.0
dnf_upgrades_pending{origin="epel-cisco-openh264"} 0.0
dnf_upgrades_pending{origin="grafana"} 1.0
dnf_upgrades_pending{origin="hashicorp"} 1.0
dnf_upgrades_pending{origin="influxdb"} 0.0
dnf_upgrades_pending{origin="kubernetes"} 0.0
dnf_upgrades_pending{origin="ookla_speedtest-cli"} 0.0
dnf_upgrades_pending{origin="ookla_speedtest-cli-source"} 0.0
dnf_upgrades_pending{origin="opentofu"} 0.0
dnf_upgrades_pending{origin="opentofu-source"} 0.0
dnf_upgrades_pending{origin="rhel-9-for-aarch64-appstream-rpms"} 1.0
dnf_upgrades_pending{origin="rhel-9-for-aarch64-baseos-rpms"} 6.0
```
