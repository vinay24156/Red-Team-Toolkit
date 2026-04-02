import requests

def scan_website(url):
    output = f"\n[+] Scanning {url}...\n"

    try:
        response = requests.get(url)
        headers = response.headers

        if "X-Frame-Options" not in headers:
            output += "[!] Missing X-Frame-Options\n"

        if "Content-Security-Policy" not in headers:
            output += "[!] Missing Content-Security-Policy\n"

        output += f"Status Code: {response.status_code}\n"

    except:
        output += "Error connecting to website\n"

    print(output)
    return output
