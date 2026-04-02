# 🔐 Red Team Toolkit

A beginner-friendly cybersecurity toolkit built in Python that simulates real-world attack workflows including reconnaissance, credential attacks, and web security analysis.

## 🚀 Features

- 🔍 **Port Scanner**
  - Scans common ports (21, 22, 80, 443)
  - Identifies active services (FTP, SSH, HTTP, HTTPS)

- 🔐 **Password Tools**
  - Password strength checker
  - Wordlist-based brute force simulation
  - Username:Password combo attack

- 🌐 **Web Security Scanner**
  - Detects missing security headers
  - Checks for basic web misconfigurations

- 📊 **Log Analyzer**
  - Detects multiple failed login attempts
  - Identifies possible brute-force attacks

- 🎭 **Payload Generator**
  - Generates reverse shell payloads

## ⚔️ Attack Mode (Automation)

This toolkit includes an automated attack workflow:

1. 🔍 Reconnaissance (Port Scan)  
2. 🔐 Credential Attack (if FTP/SSH detected)  
3. 🌐 Web Scan (if HTTP/HTTPS detected)  
4. 🎭 Payload Generation  
5. 📊 Report Generation  


## 🛠 Technologies Used

- Python  
- Socket Programming  
- Requests Library  

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/red-team-toolkit.git
cd red-team-toolkit
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔍 Port Scan

```bash
python main.py scan --target example.com
```

### 🔐 Password Check

```bash
python main.py password --check Password123!
```

### 📊 Log Analysis

```bash
python main.py logs --file logs.txt
```

### 🌐 Web Scan

```bash
python main.py webscan --url http://example.com
```

### ⚔️ Full Attack Mode

```bash
python main.py attack --target example.com
```

---

## 📊 Output

* Scan results are saved in: `reports/scan.txt`
* Attack results are saved in: `reports/attack_report.txt`

---

## ⚠️ Disclaimer

This project is developed for **educational purposes only**.
Do **NOT** use this tool on systems without proper authorization.

---

## 👤 Author

Vinay Kumar Kode

---

## ⭐ Future Improvements

* Add JSON report export
* Add more ports/services scanning
* Add vulnerability detection (SQLi, XSS basics)
* Improve UI/CLI output

---

## 💡 Note

This project demonstrates beginner-level understanding of:

* Networking
* Cybersecurity fundamentals
* Python scripting
* Attack simulation workflows

