import json


def load_threat_feed():
    with open("threat_feed.json") as f:
        return json.load(f)


def load_logs():
    with open("sample_logs.txt") as f:
        return f.readlines()


def scan_logs(logs, feed):

    matches = []

    for line in logs:

        for ip in feed["malicious_ips"]:
            if ip in line:
                matches.append(("Malicious IP", ip, line.strip()))

        for domain in feed["malicious_domains"]:
            if domain in line:
                matches.append(("Malicious Domain", domain, line.strip()))

        for h in feed["malicious_hashes"]:
            if h in line:
                matches.append(("Malicious File Hash", h, line.strip()))

    return matches


def main():

    feed = load_threat_feed()
    logs = load_logs()

    results = scan_logs(logs, feed)

    print("\nTHREAT INTELLIGENCE IOC SCAN RESULTS")
    print("=" * 45)

    if not results:
        print("No indicators detected")
        return

    for match in results:
        print(f"\nType: {match[0]}")
        print(f"Indicator: {match[1]}")
        print(f"Log Entry: {match[2]}")


if __name__ == "__main__":
    main()