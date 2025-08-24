import subprocess
import json
import sys

if len(sys.argv) != 2:
    print("用法: python check_status.py <rtpengine_uri>")
    sys.exit(1)

uri = sys.argv[1]
cmd = ["kamcmd","rtpengine.ping",uri]  
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    output = result.stdout.strip()
    if "status: success" in output:
        print(1)
    else:
        print(0)
except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError):
    print(0)

