#!/usr/bin/env bash
set -euo pipefail

# Go to the directory where this script lives
cd "$(dirname "${BASH_SOURCE[0]}")"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment (.venv)..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null

# Install streamlit and pydantic from requirements.txt
echo "Installing streamlit and pydantic..."
pip install -q -r requirements.txt

# Install the latest ollama Python client (no version pin)
echo "Installing latest ollama Python client..."
pip install -q ollama

# Start Ollama server in background if not already running
if ! pgrep -f "ollama serve" > /dev/null; then
    echo "Starting Ollama server in background..."
    ollama serve > /dev/null 2>&1 &
    sleep 3
fi

# Launch Streamlit app
echo "Launching Neuromancer Companion"
echo "Open your browser: http://localhost:8501"
streamlit run app.py \
    --server.port=8501 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false
