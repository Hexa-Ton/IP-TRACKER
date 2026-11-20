
#!/usr/bin/env bash
set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

install_python() {
  if command -v pkg >/dev/null 2>&1; then
    echo "Installing Python using Termux pkg..."
    pkg install -y python
  elif command -v apk >/dev/null 2>&1; then
    echo "Installing Python using Alpine apk..."
    apk add python3 py3-pip
  elif command -v apt-get >/dev/null 2>&1; then
    echo "Installing Python using apt..."
    apt-get update
    apt-get install -y python3 python3-pip
  else
    echo "Unsupported package manager."
    echo "Please install Python 3 manually."
    exit 1
  fi
}

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3)"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python)"
else
  install_python

  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3)"
  elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python)"
  else
    echo "Python 3 installation failed."
    exit 1
  fi
fi

"$PYTHON_BIN" --version
"$PYTHON_BIN" -m py_compile main.py

echo "IP-TRACKER 1.0 installation check passed."
echo "Start with: ./run.sh"
