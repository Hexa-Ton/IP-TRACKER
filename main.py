#!/usr/bin/env python3
"""IP-TRACKER 1.0 — Termux-first public IP lookup utility."""
from __future__ import annotations
import argparse, ipaddress, json, socket, sys, time, shutil
import subprocess, threading, re
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.parse import quote, parse_qs
from urllib.request import Request, urlopen

VERSION = "1.0"
API_BASE = "https://ipwho.is/"
TIMEOUT = 12
MAX_BULK = 25
PROMPT = "IP-TRACKER (^• •^) >> "

PROMPT = "IP-TRACKER (^• •^) >> "
PURPLE = "\033[95m"
RESET = "\033[0m"

def ask(label: str = PROMPT) -> str:
    try:
        if label == PROMPT:
            return input(f"{PURPLE}{label}{RESET}")
        return input(label)
    except EOFError:
        return "05"



def show_banner():
    import shutil
    import sys

    columns = shutil.get_terminal_size(fallback=(80, 24)).columns
    width = max(20, columns - 2)

    use_color = (
        sys.stdout.isatty()
        and "NO_COLOR" not in os.environ
        and os.environ.get("TERM", "") != "dumb"
    )

    PURPLE = "\033[38;5;141m"
    CYAN = "\033[38;5;51m"
    BLUE = "\033[38;5;75m"
    RESET = "\033[0m"

    def paint(text, color):
        return f"{color}{text}{RESET}" if use_color else text

    def center(text):
        return text.center(width)

    def gradient(text):
        colors = [PURPLE, BLUE, CYAN, BLUE]
        if not use_color:
            return text

        return "".join(
            f"{colors[i % len(colors)]}{char}"
            for i, char in enumerate(text)
        ) + RESET

    print()

    if width < 36:
        print(gradient(">> IP-TRACKER <<"))
        print(paint("NETWORK INTELLIGENCE", CYAN))
        print(paint("Tool Developer: Hexa Ton", PURPLE))
        print()
        return

    top = "  .       .       .       ."
    network = " / \\_____/ \\_____/ \\_____/ \\"

    print(paint(center(top), BLUE))
    print(paint(center(network), CYAN))
    print()
    print(gradient(center("╱╲  I P - T R A C K E R  ╱╲")))
    print(paint(center("N E T W O R K   I N T E L L I G E N C E"), CYAN))
    print()
    print(paint(center("●━━━━━━◆━━━━━━━━◆━━━━━━●"), BLUE))
    print(paint(center("Tool Developer: Hexa Ton"), PURPLE))
    print(paint(center("[ TRACE ] ━ [ ANALYZE ] ━ [ TRACK ]"), CYAN))
    print()
    print(paint(center("SECURE  •  >  •  INTELLIGENT"), BLUE))
    print()

    def centered(text: str) -> str:
        inner = width - 4
        return text.center(inner)

    top = "╭" + "─" * (width - 2) + "╮"
    bottom = "╰" + "─" * (width - 2) + "╯"

    print()
    print(PURPLE + top)
    print("│ " + centered("◈ NETWORK INTELLIGENCE ◈") + " │")
    print("│ " + centered("IP-TRACKER") + " │")
    print("│ " + centered("Tool Developer: Hexa Ton") + " │")
    print(bottom + RESET)
    print()

def display(value):
    if value is None or value == "": return "UNKNOWN"
    if isinstance(value, bool): return "YES" if value else "NO"
    return str(value)

def validate_public_ip(raw: str) -> str:
    try: address = ipaddress.ip_address(raw.strip())
    except ValueError as exc: raise ValueError(f"Invalid IP address: {raw}") from exc
    if not address.is_global: raise ValueError(f"{address} is not a globally routable public IP address.")
    return str(address)

def fetch_ip_data(ip: str | None = None) -> dict:
    target = "" if ip is None else quote(ip, safe=":")
    request = Request(API_BASE + target, headers={"User-Agent": f"IP-TRACKER/{VERSION}", "Accept": "application/json"})
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            payload = response.read(1_000_001)
            if response.status != 200: raise RuntimeError(f"Lookup API returned HTTP {response.status}.")
    except HTTPError as exc:
        if exc.code == 429: raise RuntimeError("API rate limit reached (HTTP 429). Try later.") from exc
        raise RuntimeError(f"Lookup API returned HTTP {exc.code}.") from exc
    except (URLError, TimeoutError, socket.timeout, OSError) as exc:
        raise RuntimeError(f"Network/API connection failed: {exc}") from exc
    if len(payload) > 1_000_000: raise RuntimeError("Lookup API response was unexpectedly large.")
    try: data = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc: raise RuntimeError("Lookup API returned invalid data.") from exc
    if not isinstance(data, dict): raise RuntimeError("Lookup API returned an unsupported response.")
    if data.get("success") is False: raise RuntimeError(str(data.get("message") or "IP lookup failed."))
    return data

def show_report(data: dict) -> None:
    connection = data.get("connection") if isinstance(data.get("connection"), dict) else {}
    timezone = data.get("timezone") if isinstance(data.get("timezone"), dict) else {}
    flag = data.get("flag") if isinstance(data.get("flag"), dict) else {}
    security = data.get("security") if isinstance(data.get("security"), dict) else None
    rows = [("IP ADDRESS", data.get("ip")), ("IP VERSION", data.get("type")), ("CONTINENT", data.get("continent")),
            ("COUNTRY", f"{display(flag.get('emoji'))} {display(data.get('country'))}"), ("REGION", data.get("region")),
            ("CITY", data.get("city")), ("POSTAL CODE", data.get("postal")), ("LATITUDE", data.get("latitude")),
            ("LONGITUDE", data.get("longitude")), ("TIME ZONE", timezone.get("id")), ("UTC OFFSET", timezone.get("utc")),
            ("ISP", connection.get("isp")), ("ORGANIZATION", connection.get("org")), ("ASN", connection.get("asn")),
            ("DOMAIN", connection.get("domain"))]
    print("\n" + "=" * 58 + "\nIP-TRACKER — IP INFORMATION\n" + "=" * 58)
    for label, value in rows: print(f"{label:<18}: {display(value)}")
    print("-" * 58 + "\nSECURITY INTELLIGENCE")
    if security is None: print("VPN / PROXY / TOR / HOSTING : UNKNOWN (not provided by API)")
    else:
        for key in ("vpn", "proxy", "tor", "hosting", "relay", "mobile", "anonymous"):
            print(f"{key.upper():<18}: {display(security.get(key))}")
    print("=" * 58 + "\nNote: IP geolocation is approximate; it is not GPS or an exact address.\n")

def parse_ip_list(raw) -> list[str]:
    if isinstance(raw, (list, tuple)): raw = "\n".join(str(item) for item in raw)
    tokens = raw.replace(",", " ").replace(";", " ").split()
    result, seen = [], set()
    for token in tokens:
        address = validate_public_ip(token)
        if address not in seen: result.append(address); seen.add(address)
    if not result: raise ValueError("No IP addresses were entered.")
    if len(result) > MAX_BULK: raise ValueError(f"Maximum {MAX_BULK} IP addresses per batch.")
    return result

def scan_one(raw):
    address = validate_public_ip(raw)
    print(f"\nLooking up {address} ...")
    show_report(fetch_ip_data(address))

def scan_many(raw):
    addresses = parse_ip_list(raw)
    print(f"\nStarting batch lookup: {len(addresses)} public IP address(es).")
    for index, address in enumerate(addresses, 1):
        print(f"\n[{index}/{len(addresses)}] {address}")
        try: show_report(fetch_ip_data(address))
        except RuntimeError as exc: print(f"ERROR: {exc}")
        if index < len(addresses): time.sleep(0.25)

def interactive_bulk():
    print("Enter public IPv4/IPv6 addresses. Type END on a separate line to finish.")

    lines = []

    try:
        while True:
            line = input("IP> ").strip()

            if line.upper() == "END":
                break

            if line:
                lines.append(line)

    except KeyboardInterrupt:
        print("\n[!] Bulk input cancelled. Returning to main menu.")
        return

    except EOFError:
        print("\n[!] Input ended. Returning to main menu.")
        return

    try:
        scan_many("\n".join(lines))
    except ValueError as exc:
        print(f"ERROR: {exc}")




class VisitorHandler(BaseHTTPRequestHandler):
    def log_message(self, _format, *_args):
        pass

    def send_page(self, status, html):
        body = html.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Welcome</title>
<style>
body {
    margin: 0;
    min-height: 100vh;
    display: grid;
    place-items: center;
    background: #fff;
    color: #222;
    font-family: Arial, sans-serif;
    text-align: center;
}
main { width: 85%; max-width: 360px; }
h1 { font-size: 30px; }
p { color: #666; line-height: 1.5; }
button {
    width: 100%;
    padding: 14px;
    margin-top: 15px;
    background: #222;
    color: white;
    border: 0;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
}
</style>
</head>
<body>
<main>
<h1>Welcome</h1>
<h3>Have a nice day!</h3>
<button id="continueBtn" type="button">CONTINUE</button>
<p id="status"></p>
</main>

<script>
async function reportEvent(eventName) {
    const status = document.getElementById("status");

    try {
        const response = await fetch(
            "https://api.ipify.org?format=json",
            { cache: "no-store" }
        );

        if (!response.ok) throw new Error("IP lookup failed");

        const result = await response.json();

        const report = await fetch("/event", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                event: eventName,
                ip: result.ip
            })
        });

        if (!report.ok) throw new Error("Report failed");

        return true;
    } catch (error) {
        status.textContent =
            "Could not detect your public IP. Please check your connection.";
        return false;
    }
}

window.addEventListener("load", () => {
    reportEvent("PAGE OPEN");
});

document.getElementById("continueBtn").addEventListener("click",
async () => {
    const button = document.getElementById("continueBtn");
    button.disabled = true;

    const success = await reportEvent("CONTINUE CLICK");

    if (success) {
        document.querySelector("main").innerHTML =
            "<h1>Thank you!</h1><h3>Have a nice day!</h3>";
    } else {
        button.disabled = false;
    }
});
</script>
</body>
</html>"""

        self.send_page(200, html)

    def do_POST(self):
        try:
            if self.path != "/event":
                self.send_page(404, "Not found")
                return

            length = int(self.headers.get("Content-Length", "0"))

            if length <= 0 or length > 2048:
                self.send_page(400, "Invalid request")
                return

            data = json.loads(
                self.rfile.read(length).decode("utf-8")
            )

            event = data.get("event")
            raw_ip = data.get("ip")

            if event not in ("PAGE OPEN", "CONTINUE CLICK"):
                self.send_page(400, "Invalid event")
                return

            try:
                address = ipaddress.ip_address(raw_ip)
            except (ValueError, TypeError):
                self.send_page(400, "Invalid IP")
                return

            if not address.is_global:
                self.send_page(400, "Public IP required")
                return

            print("\n" + "=" * 55)
            print("IP-TRACKER — VISITOR EVENT")
            print(f"EVENT       : {event}")
            print(f"PUBLIC IP   : {address}")
            print(f"TIME        : {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print("=" * 55, flush=True)

            self.send_page(200, "OK")

        except (ValueError, OSError, json.JSONDecodeError) as exc:
            print(f"Visitor request error: {exc}")
            try:
                self.send_page(400, "Request could not be processed")
            except OSError:
                pass


def start_finder():
    print("\nIP FINDER — CONSENT-BASED VISITOR IP DEMO")
    print("\nChoose link type:")
    print("1. Localhost only (This device)")
    print("2. SSH public link (Any device)")
    
    choice = input("\nSelect [1/2]: ").strip()

    if choice not in ("1", "2"):
        print("[!] Invalid choice.")
        return

    try:
        server = ThreadingHTTPServer(
            ("127.0.0.1", 8080),
            VisitorHandler
        )
    except OSError as exc:
        print(f"Could not start local server: {exc}")
        return

    tunnel = None

    try:
        print("\nIP FINDER — CONSENT-BASED VISITOR IP DEMO")
        print("Visitor IP is displayed only after consent submission.")
        print("No GPS or browser location is collected.")

        if choice == "1":
            print("\nLOCALHOST LINK = http://127.0.0.1:8080")
            print("Access is limited to this device.")

        elif choice == "2":
            ssh_path = shutil.which("ssh")

            if not ssh_path:
                print("\n[!] SSH is not installed.")
                print("Install using: pkg install openssh")
                return

            command = [
                ssh_path,
                "-T",
                "-o", "ExitOnForwardFailure=yes",
                "-o", "ServerAliveInterval=60",
                "-o", "StrictHostKeyChecking=accept-new",
                "-R", "80:127.0.0.1:8080",
                "nokey@localhost.run"
            ]

            try:
                tunnel = subprocess.Popen(
                    command,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1
                )

                def read_tunnel_output():
                    if tunnel.stdout is None:
                        return

                    for line in tunnel.stdout:
                        line = line.strip()

                        if "tunneled with tls termination" in line:
                            match = re.search(
                                r"(https://[A-Za-z0-9.-]+)",
                                line
                            )

                            if match:
                                print(
                                    "\nSSH LINK = " + match.group(1),
                                    flush=True
                                )

                        elif any(error in line.lower() for error in (
                            "permission denied",
                            "connection refused",
                            "remote port forwarding failed",
                            "could not resolve hostname"
                        )):
                            print("[SSH ERROR] " + line, flush=True)

                threading.Thread(
                    target=read_tunnel_output,
                    daemon=True
                ).start()

                print("\nStarting SSH public tunnel...")
                print("Waiting for SSH public link...")

            except OSError as exc:
                print(f"\nSSH tunnel could not start: {exc}")
                return

        print("\nWaiting for visitors. Press Ctrl+C to stop.")
        server.serve_forever()

    except KeyboardInterrupt:
        print("\n[!] IP FINDER stopped.")

    finally:
        server.server_close()

        if tunnel is not None and tunnel.poll() is None:
            tunnel.terminate()
            try:
                tunnel.wait(timeout=3)
            except subprocess.TimeoutExpired:
                tunnel.kill()
                tunnel.wait()

        print("[!] Local server and SSH tunnel closed.")



def show_help():
    print("""
IP-TRACKER 1.0.0 — HELP & COMMANDS

01 IP TRACKER       Single IP analysis and multiple IP research
02 IP FINDER        Transparent visitor-IP demo server
03 WHAT IS MY IP?   Look up the public IP seen by the API
04 HELP & COMMANDS  Show this help
05 EXIT             Close IP-TRACKER

COMMANDS:
  ./run.sh scan 8.8.8.8
  ./run.sh scan 8.8.8.8 1.1.1.1
  ./run.sh bulk
  ./run.sh myip
  ./run.sh finder

Bulk input accepts spaces, commas, or semicolons; maximum 25 IPs.
Only globally routable public IP addresses are queried.
Missing security fields display UNKNOWN, not NO.
IP geolocation is approximate, not GPS.
IP FINDER shows the visitor's connection IP; use only with consent.
""")

def tracker_menu():
    while True:
        print("\n01 SINGLE IP ANALYSIS\n02 MULTIPLE IP RESEARCH\n03 BACK\n")
        choice = ask().strip()
        if choice in ("01", "1"):
            try: scan_one(ask("Enter public IP: ").strip())
            except (ValueError, RuntimeError) as exc: print(f"ERROR: {exc}")
        elif choice in ("02", "2"): interactive_bulk()
        elif choice in ("03", "3"): return
        else: print("Invalid selection. Choose 01, 02, or 03.")

def main_menu():
    while True:
        print("\n01 IP TRACKER\n02 IP FINDER\n03 WHAT IS MY IP?\n04 HELP & COMMANDS\n05 EXIT\n")
        choice = ask().strip()
        if choice in ("01", "1"): tracker_menu()
        elif choice in ("02", "2"): start_finder()
        elif choice in ("03", "3"):
            try: show_report(fetch_ip_data())
            except RuntimeError as exc: print(f"ERROR: {exc}")
        elif choice in ("04", "4"): show_help()
        elif choice in ("05", "5"): print("IP-TRACKER closed."); return
        else: print("Invalid selection. Choose 01–05.")

def build_parser():
    parser = argparse.ArgumentParser(description=f"IP-TRACKER {VERSION}")
    sub = parser.add_subparsers(dest="command")
    scan = sub.add_parser("scan", help="Look up one or more public IP addresses"); scan.add_argument("ips", nargs="+")
    sub.add_parser("bulk", help="Interactive multi-IP lookup")
    sub.add_parser("myip", help="Look up your public IP")
    sub.add_parser("finder", help="Start the visitor-IP demo server")
    return parser

def main():
    args = build_parser().parse_args()

    try:
        if args.command == "scan":
            if len(args.ips) == 1:
                scan_one(args.ips[0])
            else:
                scan_many(args.ips)

        elif args.command == "bulk":
            interactive_bulk()

        elif args.command == "myip":
            show_report(fetch_ip_data())

        elif args.command == "finder":
            start_finder()

        else:
            show_banner()
            main_menu()

        return 0

    except KeyboardInterrupt:
        print("\n[!] Operation cancelled. IP-TRACKER closed.")
        return 130

    except (ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
