import re

# 🔐 1. Password Strength Checker
def check_password(password):
    if not password:
        return "No password provided"

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*]", password):
        score += 1

    result = f"Password Score: {score}/4\n"

    if score == 4:
        result += "Strong password"
    else:
        result += "Weak password"

    print(result)
    return result


# 🔥 2. Wordlist-based brute force (password only)
def brute_force_simulation(wordlist_path):
    print("\n[+] Using password wordlist...\n")

    try:
        with open(wordlist_path, "r") as file:
            passwords = [line.strip() for line in file]

        target_password = "admin123"  # simulated correct password
        attempts = 0

        for pwd in passwords:
            attempts += 1
            print(f"[{attempts}] Trying password: {pwd}")

            if pwd == target_password:
                result = f"\n[✔] Password FOUND: {pwd} (Attempts: {attempts})"
                print(result)
                return result

        result = f"\n[✘] Password not found after {attempts} attempts"
        print(result)
        return result

    except FileNotFoundError:
        return "Wordlist file not found"
    except Exception as e:
        return f"Error: {str(e)}"


# 🔥 3. Username + Password Combo Attack
def combo_brute_force(wordlist_path):
    print("\n[+] Starting Username:Password Combo Attack...\n")

    try:
        with open(wordlist_path, "r") as file:
            combos = [line.strip() for line in file]

        # Simulated correct credentials
        correct_username = "admin"
        correct_password = "admin123"

        attempts = 0

        for combo in combos:
            if ":" not in combo:
                continue

            username, password = combo.split(":", 1)
            attempts += 1

            print(f"[{attempts}] Trying -> {username}:{password}")

            # Simulated login check
            if username == correct_username and password == correct_password:
                result = f"\n[✔] VALID CREDENTIALS FOUND: {username}:{password} (Attempts: {attempts})"
                print(result)
                return result

        result = f"\n[✘] No valid credentials found after {attempts} attempts"
        print(result)
        return result

    except FileNotFoundError:
        return "Combo wordlist file not found"
    except Exception as e:
        return f"Error: {str(e)}"
