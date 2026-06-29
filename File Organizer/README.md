# 📁 Directory Organizer Utility

A lightweight, zero-dependency automation script engineered to parse unorganized file structures and cleanly map files into isolated, extension-specific directories dynamically.

---

## 🧬 Core Mechanics

* **Zero Footprint:** Relies entirely on built-in modules (`os`, `shutil`)—no pip installations required.
* **Smart Isolation:** Safely skips active system scripts and nested directories to prevent recursive execution loops.
* **Dynamic Generation:** Instantly builds missing target roots (e.g., `TXT_Files/`, `PNG_Files/`) on the fly.

---

## 🚀 Deployment Terminal

### Run the Script
Execute the command below within this directory to run the optimization sweep:
```bash
python organizer.py
