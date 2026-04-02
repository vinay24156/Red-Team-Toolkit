import argparse
from modules import scanner, password, logs, webscan, payload

def main():
    parser = argparse.ArgumentParser(description="Red Team Toolkit")

    subparsers = parser.add_subparsers(dest="command")

    # Scan
    scan = subparsers.add_parser("scan")
    scan.add_argument("--target", required=True)

    # Password (manual check)
    pwd = subparsers.add_parser("password")
    pwd.add_argument("--check")

    # Logs
    lg = subparsers.add_parser("logs")
    lg.add_argument("--file")

    # Webscan
    web = subparsers.add_parser("webscan")
    web.add_argument("--url")

    # Payload
    pay = subparsers.add_parser("payload")
    pay.add_argument("--type")

    # 🔥 Attack Mode (UPDATED)
    attack = subparsers.add_parser("attack")
    attack.add_argument("--target", required=True)
    attack.add_argument("--wordlist", default="wordlists/creds.txt",
                        help="Path to combo wordlist (default: wordlists/creds.txt)")

    args = parser.parse_args()

    if args.command == "scan":
        scanner.scan_target(args.target)

    elif args.command == "password":
        password.check_password(args.check)

    elif args.command == "logs":
        logs.analyze_logs(args.file)

    elif args.command == "webscan":
        webscan.scan_website(args.url)

    elif args.command == "payload":
        payload.generate_payload(args.type)

    elif args.command == "attack":
        run_attack(args.target, args.wordlist)


# 🔥 ATTACK WORKFLOW (UPDATED)
def run_attack(target, wordlist):
    print("\n[ATTACK MODE STARTED]\n")

    report = []

    # 🔍 RECON
    scan_results, open_ports = scanner.scan_target(target)
    report.append("[RECON]\n" + scan_results)

    # 🔐 CREDENTIAL ATTACK (COMBO WORDLIST)
    if 21 in open_ports or 22 in open_ports:
        report.append("\n[CREDENTIAL]\n")

        if 21 in open_ports:
            msg = "FTP service detected (Port 21)"
            print(msg)
            report.append(msg)

        if 22 in open_ports:
            msg = "SSH service detected (Port 22)"
            print(msg)
            report.append(msg)

        # 🔥 Use combo attack
        result = password.combo_brute_force(wordlist)
        report.append(result)

    else:
        msg = "No FTP/SSH service found. Skipping."
        print(msg)
        report.append("\n[CREDENTIAL]\n" + msg + "\n")

    # 🌐 WEB ATTACK
    if 80 in open_ports or 443 in open_ports:
        report.append("\n[WEB]\n")

        if 80 in open_ports:
            msg = "HTTP service detected (Port 80)"
            print(msg)
            report.append(msg)

            result = webscan.scan_website(f"http://{target}")
            report.append(result)

        if 443 in open_ports:
            msg = "HTTPS service detected (Port 443)"
            print(msg)
            report.append(msg)

            result = webscan.scan_website(f"https://{target}")
            report.append(result)

    else:
        msg = "No HTTP/HTTPS service found. Skipping."
        print(msg)
        report.append("\n[WEB]\n" + msg + "\n")

    # 🎭 PAYLOAD
    report.append("\n[PAYLOAD]\n")
    payload_result = payload.generate_payload("reverse_shell")
    report.append(payload_result)

    # 📊 SAVE REPORT
    with open("reports/attack_report.txt", "w") as f:
        f.write("\n".join(report))

    print("\n[✔] Attack completed. Report saved.\n")


if __name__ == "__main__":
    main()
