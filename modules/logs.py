def analyze_logs(file):
    if not file:
        print("Provide log file")
        return

    print(f"\n[+] Analyzing {file}...\n")

    try:
        with open(file, "r") as f:
            lines = f.readlines()

        failed = 0

        for line in lines:
            if "failed" in line.lower():
                failed += 1

        print(f"Failed login attempts: {failed}")

        if failed > 5:
            print("⚠ Possible brute-force attack detected")

    except:
        print("Error reading file")
