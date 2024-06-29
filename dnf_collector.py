#!/usr/bin/python3
import dnf, hawkey, argparse
from prometheus_client import CollectorRegistry, Gauge, generate_latest

parser = argparse.ArgumentParser(description="Expose metrics from dnf updates.")
parser.add_argument(
    "-o",
    "--outfile",
    default=None,
    metavar="FILENAME",
    help="Optional output file to use rather than standard output.",
)

args = parser.parse_args()

namespace = "dnf"
registry = CollectorRegistry()

metrics = {
    "security_upgrades_pending": Gauge(
        "security_upgrades_pending",
        "Security upgrades pending",
        ["origin"],
        namespace=namespace,
        registry=registry,
    ),
    "upgrades_pending": Gauge(
        "upgrades_pending",
        "upgrades pending",
        ["origin"],
        namespace=namespace,
        registry=registry,
    ),
}
base = dnf.Base()
base.conf.substitutions.update_from_etc("/")
base.read_all_repos()

for repo in base.repos.iter_enabled():
    metrics["upgrades_pending"].labels(repo.id).set(0)
    metrics["security_upgrades_pending"].labels(repo.id).set(0)

base.fill_sack()
q = base.sack.query()
q_up = q.upgrades().filter(latest=1)

updates = {}
security_updates = {}

for update in q_up:
    if update.reponame not in updates:
        updates[update.reponame] = 1
    else:
        updates[update.reponame] += 1
    advisories = update.get_advisories(hawkey.LT | hawkey.EQ | hawkey.GT)
    for advisory in advisories:
        if advisory.type == hawkey.ADVISORY_SECURITY:
            if update.reponame not in security_updates:
                security_updates[update.reponame] = 1
            else:
                security_updates[update.reponame] += 1
            break

for repo, n in updates.items():
    metrics["upgrades_pending"].labels(repo).set(n)

for repo, n in security_updates.items():
    metrics["security_upgrades_pending"].labels(repo).set(n)

if args.outfile:
    with open(args.outfile, "w") as f:
        f.write(generate_latest(registry).decode())
else:
    print(generate_latest(registry).decode(), end="")
