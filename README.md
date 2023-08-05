# dnf_collector.py

### A node-exporter collector for dnf upgrades

The community yum.sh collector did not include a separate metric for updates with security advisories. This does, as well as leverages dnf's python library directly.

This has been tested on RHEL9 and Fedora 38.

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
dnf_security_upgrades_pending{origin="grafana"} 1.0
dnf_security_upgrades_pending{origin="rhel-9-for-aarch64-baseos-rpms"} 34.0
dnf_security_upgrades_pending{origin="rhel-9-for-aarch64-appstream-rpms"} 21.0
# HELP dnf_upgrades_pending upgrades pending
# TYPE dnf_upgrades_pending gauge
dnf_upgrades_pending{origin="grafana"} 1.0
dnf_upgrades_pending{origin="hashicorp"} 1.0
dnf_upgrades_pending{origin="influxdb"} 1.0
dnf_upgrades_pending{origin="codeready-builder-for-rhel-9-aarch64-rpms"} 1.0
dnf_upgrades_pending{origin="rhel-9-for-aarch64-baseos-rpms"} 66.0
dnf_upgrades_pending{origin="rhel-9-for-aarch64-appstream-rpms"} 29.0
dnf_upgrades_pending{origin="rhel-9-for-aarch64-baseos-source-rpms"} 1.0
```