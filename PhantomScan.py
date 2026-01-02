#!/usr/bin/env python3
"""
PhantomScan
Lightweight Cybersecurity Reconnaissance Tool
Developed by R-Dex Group of Industry | Rahul Majhi

Legal use only. Scan targets you own or have permission to test.
"""

import socket
import sys
import time

# -------------------- BANNER --------------------

def banner():
    print("=" * 60)
    print("        PhantomScan v1.0")
    print("  Cybersecurity Recon Tool")
    print("  Developed by R-Dex Group of Industry | RAHUL MAJHI")
    print("=" * 60)
    print()

# -------------------- UTILITIES --------------------

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print("[!] Error: Unable to resolve target.")
        sys.exit(1)

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user.")
            sys.exit(0)
        except Exception:
            pass
    return open_ports

# -------------------- MAIN SCAN FUNCTION --------------------

def quick_scan():
    banner()

    target = input("Enter domain or IP address: ").strip()
    print("\n[+] Resolving target...")
    time.sleep(1)

    ip = resolve_target(target)
    print(f"[+] Target IP Address: {ip}")

    print("\n[+] Starting basic port scan...")
    time.sleep(1)

    common_ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }

    open_ports = scan_ports(ip, common_ports.keys())

    print("\n========== Scan Results ==========")

    if open_ports:
        for port in open_ports:
            print(f"[OPEN] Port {port} ({common_ports[port]})")
    else:
        print("No common ports found open.")

    print("=================================")
    print("\nScan completed successfully.")
    print("\n© R-Dex Group of Industry")
    print("For educational and authorized testing only.\n")

# -------------------- EXECUTION --------------------

if __name__ == "__main__":
    quick_scan()
