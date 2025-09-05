#!/usr/bin/env bash

# Exit on any error
set -e

echo "Stopping OpenWebUI service..."
sudo systemctl stop openwebui

echo "Activating virtual environment..."
source /media/darkdragon/ssd_data_1to/ai/python_ai/open-webui/venv/bin/activate

echo "Upgrading Open WebUI..."
pip install open-webui --upgrade

echo "Starting OpenWebUI service..."
sudo systemctl start openwebui

echo "Checking service status..."
sudo systemctl status openwebui --no-pager