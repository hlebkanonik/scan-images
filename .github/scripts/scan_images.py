import subprocess
import json
import os

registry_url = os.getenv('REGISTRY_URL')

if not registry_url:
    print("Please set the REGISTRY_URL environment variable.")
    exit(1)

report_dir = 'trivy_reports'  # Directory to store reports
os.makedirs(report_dir, exist_ok=True)

with open('images.json') as f:
    images = json.load(f)

for image in images:
    full_image_name = f"{registry_url}/{image}"
    report_path = os.path.join(report_dir, f"{image.replace(':', '_')}.json")
    print(f"Scanning image: {full_image_name}")
    subprocess.run(['trivy', 'image', '--format', 'json', '--output', report_path, '--no-progress', full_image_name])
