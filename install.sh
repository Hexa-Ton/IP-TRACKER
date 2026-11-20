#!/data/data/com.termux/files/usr/bin/bash
set -Eeuo pipefail
ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"
if ! command -v python >/dev/null 2>&1; then
  if command -v pkg >/dev/null 2>&1; then
    echo "Python 3 is missing. Installing it with Termux pkg..."
    pkg install -y python
  else
    echo "Python 3 is required. Install it with your system package manager."
    exit 1
  fi
fi
python --version
python -m py_compile main.py
echo "IP-TRACKER 1.0.0 installation check passed."
echo "Start with: ./run.sh"
