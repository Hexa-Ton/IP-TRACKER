🌐 IP-TRACKER

<p align="center">
  <b>Cross-Platform IP Intelligence Tool</b><br>
  Public IP Lookup • Geolocation Insights • IP Analysis
</p><p align="center">
  🐉 Kali Linux &nbsp;•&nbsp; 🪟 Windows &nbsp;•&nbsp; 📱 Termux
</p>---

🚀 About

IP-TRACKER is a cross-platform IP intelligence tool designed for public IP lookup, geolocation insights, IP information analysis, and consent-based visitor IP demonstrations.

Built with Python and designed for a simple, interactive command-line experience.

✨ Features

- 🌐 IP TRACKER — Retrieve public IP information.
- 🔎 IP FINDER — Run a visitor IP demonstration server.
- 📡 WHAT IS MY IP? — Check your current public IP address.
- 📍 Geolocation Insights — View approximate IP-based location information.
- 🛡️ IP Analysis — Display available IP and network-related information.
- 🔗 SSH Tunnel — Share a local demonstration server through an SSH tunnel.
- 💻 Cross-Platform — Kali Linux, Windows, and Termux support.

📋 Main Menu

01 IP TRACKER
02 IP FINDER
03 WHAT IS MY IP?
04 HELP & COMMANDS
05 EXIT

---

🖥️ Installation & Usage

Choose your operating system and follow the instructions.

1. 🐉 Kali Linux

Install requirements:

sudo apt update
sudo apt install python3 python3-pip git openssh-client -y

Clone repository:

git clone https://github.com/Hexa-Ton/IP-TRACKER.git

Enter project directory:

cd IP-TRACKER

Install:

chmod +x install.sh run.sh
./install.sh

Run:

./run.sh

---

2. 🪟 Windows

Requirements:

- Python 3
- Git for Windows
- PowerShell

Clone repository:

git clone https://github.com/Hexa-Ton/IP-TRACKER.git

Enter project directory:

cd IP-TRACKER

Install:

powershell -ExecutionPolicy Bypass -File .\install.ps1

Run:

powershell -ExecutionPolicy Bypass -File .\run.ps1

---

3. 📱 Termux

Update packages:

pkg update && pkg upgrade -y

Install requirements:

pkg install python git openssh nano -y

Clone repository:

git clone https://github.com/Hexa-Ton/IP-TRACKER.git

Enter project directory:

cd IP-TRACKER

Install:

chmod +x install.sh run.sh
./install.sh

Run:

./run.sh

🔗 SSH Tunnel Requirements

For SSH tunnel functionality, install OpenSSH:

pkg install openssh -y

Check SSH installation:

ssh -V

---

⚙️ Requirements

Requirement| Purpose
Python 3| Application runtime
Git| Repository cloning
OpenSSH| SSH tunnel functionality
Internet| Public IP and geolocation lookups

---

🔗 IP FINDER Modes

Localhost Mode

- Runs the demonstration server on the local device.
- Default address: "http://127.0.0.1:8080"
- Intended for same-device access.

SSH Tunnel Mode

- Uses an SSH reverse tunnel through localhost.run.
- Can provide a public HTTPS link for remote access.
- Requires OpenSSH and an internet connection.

---

⚠️ Disclaimer

IP-TRACKER is intended for educational, informational, and authorized testing purposes.

- IP geolocation is approximate and is not GPS tracking.
- A public IP address does not necessarily identify a specific person or device.
- VPNs, proxies, and carrier-grade NAT may affect IP information.
- Visitor IP demonstrations should be transparent and consent-based.
- Users are responsible for complying with applicable laws and regulations.

---

👨‍💻 Developer

Hexa Ton

GitHub: "@Hexa-Ton" (https://github.com/Hexa-Ton)

Repository: "IP-TRACKER" (https://github.com/Hexa-Ton/IP-TRACKER)

---

<p align="center">
  ⭐ If you like this project, consider giving it a star!
</p><p align="center">
  Made by Hexa Ton
</p>
