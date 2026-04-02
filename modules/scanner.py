import socket

def scan_target(target):
    output = f"\n[+] Scanning {target}...\n"

    ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }

    open_ports = []

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            line = f"[OPEN] {port} ({service})"
            open_ports.append(port)
        else:
            line = f"[CLOSED] {port} ({service})"

        print(line)
        output += line + "\n"

        sock.close()

    with open("reports/scan.txt", "w") as f:
        f.write(output)

    return output, open_ports
