🌐 IP-TRACKER

<p align="center">
  <b>Cross-Platform IP Intelligence Tool</b>
</p><p align="center">
  Public IP Lookup · Geolocation Insights · IP Analysis · Visitor IP Demonstration
</p><p align="center">
  🐉 Kali Linux &nbsp;|&nbsp; 🪟 Windows &nbsp;|&nbsp; 📱 Termux &nbsp;|&nbsp; 🏔️ Alpine Linux
</p><p align="center">
  <b>Version 1.0</b>
</p>---

📖 Overview

IP-TRACKER is a Python-based, cross-platform IP intelligence utility designed to provide public IP information, approximate geolocation insights, and network-related IP analysis through an interactive command-line interface.

Built for simplicity, portability, and practical use across multiple operating environments, IP-TRACKER brings essential IP lookup functionality into one lightweight tool.

Whether you're using Kali Linux, Windows, Termux, or Alpine Linux, IP-TRACKER provides a straightforward way to explore publicly available IP information.

✨ Features

Feature| Description
🌐 IP TRACKER| Retrieve information about a public IP address
🔎 IP FINDER| Run a visitor IP demonstration server
📡 WHAT IS MY IP?| Check your current public IP address
📍 Geolocation| View approximate IP-based location information
🛡️ IP Analysis| Display available IP and network-related information
🔗 SSH Tunnel| Share a local demonstration server through an SSH tunnel
💻 Cross-Platform| Designed for multiple operating environments

---

🖥️ Installation

Choose your operating system and follow the corresponding instructions.

🐉 1. Kali Linux

Step 1 — Update system packages
```bash
sudo apt update && sudo apt upgrade -y
```
Step 2 — Install requirements
```bash
sudo apt install python3 python3-pip git openssh-client -y
```
Step 3 — Clone the repository
```bash
git clone https://github.com/Hexa-Ton/IP-TRACKER.git
```
Step 4 — Enter the project directory
```bash
cd IP-TRACKER
```
Step 5 — Install IP-TRACKER
```bash
chmod +x install.sh run.sh
./install.sh
```
Step 6 — Launch the tool
```bash
./run.sh
```
---

🪟 2. Windows

Requirements

- Python 3
- Git for Windows
- PowerShell

Step 1 — Clone the repository

Open PowerShell and run:
```bash
git clone https://github.com/Hexa-Ton/IP-TRACKER.git
```
Step 2 — Enter the project directory
```bash
cd IP-TRACKER
```
Step 3 — Install IP-TRACKER
```bash
powershell -ExecutionPolicy Bypass -File .\install.ps1
```
Step 4 — Launch the tool
```bash
powershell -ExecutionPolicy Bypass -File .\run.ps1
```
---

📱 3. Termux

Step 1 — Update Termux packages
```bash
pkg update && pkg upgrade -y
```
Step 2 — Install requirements
```bash
pkg install python git openssh bash -y
```
Step 3 — Clone the repository
```bash
git clone https://github.com/Hexa-Ton/IP-TRACKER.git
```
Step 4 — Enter the project directory
```bash
cd IP-TRACKER
```
Step 5 — Install IP-TRACKER
```bash
chmod +x install.sh run.sh
./install.sh
```
Step 6 — Launch the tool
```bash
./run.sh
```
🔗 SSH Tunnel Setup

OpenSSH is required for SSH tunnel functionality.

Install OpenSSH:
```bash
pkg install openssh -y
```
Verify installation:
```bash
ssh -V
```
---

🏔️ 4. Alpine Linux

IP-TRACKER includes a portable Bash installer designed to detect Alpine's "apk" package manager.

Step 1 — Update Alpine packages
```bash
sudo apk update
```
Step 2 — Install requirements
```bash
sudo apk add bash python3 py3-pip git openssh-client
```
Step 3 — Clone the repository
```bash
git clone https://github.com/Hexa-Ton/IP-TRACKER.git
```
Step 4 — Enter the project directory
```bash
cd IP-TRACKER
```
Step 5 — Make scripts executable
```bash
chmod +x install.sh run.sh
```
Step 6 — Install IP-TRACKER
```bash
./install.sh
```
Step 7 — Launch the tool
```bash
./run.sh


«Alpine Note: The installer detects "apk" and can install Python packages. Alpine compatibility should be verified on the target Alpine release and environment before treating it as fully tested support. If you're using a minimal container, make sure Bash, Git, Python 3, and the SSH client are installed.»
```
---

📋 Main Menu

IP-TRACKER provides an interactive command-line menu:

01 IP TRACKER
02 IP FINDER
03 WHAT IS MY IP?
04 HELP & COMMANDS
05 EXIT

Interactive Prompt

IP-TRACKER (^• •^) >>

---

🔗 IP FINDER — Demonstration Modes

IP FINDER provides two hosting modes for its visitor IP demonstration.

1. Localhost Mode

- Starts a local demonstration server.
- Default address: "http://127.0.0.1:8080"
- Intended for access from the same device.
- Does not require a public SSH tunnel.

2. SSH Tunnel Mode

- Uses an SSH reverse tunnel through localhost.run.
- Can provide a public HTTPS link for remote access.
- Requires OpenSSH and an active internet connection.
- Public tunnel availability depends on the third-party provider.

Important: Public tunnel services may change their availability, policies, or connection requirements.

---

⚙️ Requirements

Requirement| Purpose
Python 3| Application runtime
Bash| Linux shell scripts
Git| Repository cloning
OpenSSH| SSH tunnel functionality
Internet connection| Public IP and geolocation lookups

---

🛠️ Troubleshooting

Python 3 not found

Install Python 3 using your platform's package manager.

Kali Linux:

sudo apt install python3 -y

Termux:

pkg install python -y

Alpine Linux:

sudo apk add python3

Permission denied

Make the shell scripts executable:

chmod +x install.sh run.sh

SSH command not found

Install OpenSSH for your operating system.

Kali Linux:

sudo apt install openssh-client -y

Termux:

pkg install openssh -y

Alpine Linux:

sudo apk add openssh-client

---

🔐 Privacy & Responsible Use

IP-TRACKER uses publicly available IP information and provides a visitor IP demonstration feature.

Please keep the following points in mind:

- IP-based geolocation is approximate and does not provide GPS-level location.
- A public IP address does not necessarily identify a specific person or device.
- VPNs, proxies, and carrier-grade NAT may affect IP information.
- Visitor IP demonstrations should clearly disclose IP collection and obtain appropriate consent.
- Browser-based public IP lookup services may receive the visitor's public IP address.
- Never use this tool for unauthorized tracking, harassment, or unlawful activities.

---

⚖️ Disclaimer

IP-TRACKER is provided for educational, informational, and authorized testing purposes.

The developer is not responsible for misuse, unauthorized activity, or damages arising from the use of this software.

Users are solely responsible for ensuring that their use of IP-TRACKER complies with applicable laws and regulations.

---

👨‍💻 Developer

Hexa Ton

GitHub: "@Hexa-Ton" (https://github.com/Hexa-Ton)

Project Repository:

"https://github.com/Hexa-Ton/IP-TRACKER" (https://github.com/Hexa-Ton/IP-TRACKER)

---

📜 License

This project is licensed under the MIT License.

See the "LICENSE" (LICENSE) file for details.

---

⭐ Support the Project

If you find IP-TRACKER useful:

- ⭐ Star this repository.
- 🍴 Fork the project.
- 🐛 Report issues and bugs.
- 💡 Share suggestions for improvements.

---

<p align="center">
  ⭐ If you like this project, consider giving it a star!
  <br><br>
  <b>IP-TRACKER v1.0</b>
</p>

<p align="center">
  Crafted by <b>Hexa Ton</b>
</p>
