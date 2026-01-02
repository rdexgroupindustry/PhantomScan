# 👻 PhantomScan

**Lightweight, Fast & Stealthy Cybersecurity Reconnaissance Tool**

> Developed by **R-Dex Group of Industry**
> Author: **Rahul Majhi**
> Version: **v1.0**

---

## 📌 Overview

**PhantomScan** is a lightweight, Python-based cybersecurity reconnaissance and port scanning tool designed for **fast initial assessment**, **network visibility**, and **educational security testing**.

It focuses on **speed, simplicity, and stealth**, making it ideal for:

* Beginners in cybersecurity
* Students & researchers
* SOC analysts
* Blue team & red team reconnaissance
* Quick security posture checks

PhantomScan is intentionally minimalistic, avoiding heavy dependencies while delivering **accurate and actionable results**.

---

## 🚀 Key Features

* 🔍 **Domain & IP Resolution**
* ⚡ **Fast TCP Port Scanning**
* 🧠 **Common Service Detection**
* 🛡️ **Safe & Permission-Focused Design**
* 📦 **Zero External Dependencies**
* 🐧 **Linux / Kali / Windows / macOS Compatible**
* 🧪 **Ideal for Labs & Learning Environments**

---

## 🧩 Supported Scans

| Port | Service |
| ---- | ------- |
| 21   | FTP     |
| 22   | SSH     |
| 80   | HTTP    |
| 443  | HTTPS   |

> Future versions will support **custom port ranges**, **threading**, and **banner grabbing**.

---

## 🛠️ Technology Stack

* **Language:** Python 3
* **Libraries Used:**

  * `socket`
  * `sys`
  * `time`
* **Architecture:** CLI-based
* **Platform:** Cross-platform

---

## 📂 Project Structure

```
PhantomScan/
│
├── phantomscan.py        # Main scanning engine
├── README.md             # Documentation
├── LICENSE               # MIT License
├── .gitignore            # Git ignore rules
└── requirements.txt      # (Optional – future use)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rdexgroupofindustry/PhantomScan.git
```

### 2️⃣ Navigate to the Directory

```bash
cd PhantomScan
```

### 3️⃣ Run the Tool

```bash
python3 phantomscan.py
```

> ✅ No additional installation required

---

## 🧪 Usage Example

```bash
$ python3 phantomscan.py

Enter domain or IP address: example.com

[+] Resolving target...
[+] Target IP Address: 93.184.216.34

[+] Starting basic port scan...

========== Scan Results ==========
[OPEN] Port 80 (HTTP)
[OPEN] Port 443 (HTTPS)
=================================

Scan completed successfully.
```

---

## 🔐 Legal & Ethical Disclaimer

> **PhantomScan is intended strictly for educational purposes and authorized security testing only.**

You **MUST**:

* Scan systems you **own**, or
* Have **explicit written permission** to test

🚫 Unauthorized scanning is **illegal** and punishable under cybercrime laws.

The developers **are not responsible** for misuse or damage caused by this tool.

---

## 📜 License

This project is licensed under the **MIT License**.

✔ Free to use
✔ Free to modify
✔ Free to distribute
✔ Attribution required

See the `LICENSE` file for full details.

---

## 🧠 Learning Purpose

PhantomScan is perfect for understanding:

* How port scanning works internally
* Socket-level networking
* Reconnaissance fundamentals
* Ethical hacking basics
* Python networking programming

---

## 🔮 Roadmap (Upcoming Features)

* [ ] Custom port range scanning
* [ ] Multi-threaded scanning
* [ ] Service banner grabbing
* [ ] Export scan results (TXT/JSON)
* [ ] OS detection (basic)
* [ ] Modular plugin support
* [ ] GUI version (future)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Please ensure **ethical use** and **clean code standards**.

---

## 🏢 About R-Dex Group of Industry

**R-Dex Group of Industry** is a cybersecurity-focused initiative dedicated to:

* Cybersecurity education
* Open-source security tools
* Ethical hacking research
* AI-powered security innovation

🌐 *Building the next generation of cyber defenders.*

---

## 📬 Contact

* 👤 **Author:** Rahul Majhi
* 📧 Email: [workforrdex@gmail.com](mailto:workforrdex@gmail.com)
* 🔗 LinkedIn: [https://www.linkedin.com/in/r-dex26](https://www.linkedin.com/in/r-dex26)
* 🎥 YouTube: **R dex** (Cybersecurity Content)

---

## ⭐ Support the Project

If you find **PhantomScan** useful:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share with learners

> *“Scan responsibly. Defend intelligently.”* 👻🛡️

---
