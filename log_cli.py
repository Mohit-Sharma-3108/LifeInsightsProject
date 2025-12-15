"""This file only creates a cli to make the logging process frictionless
I have also used the following powershell command to run only log <minutes value> <focus score value> in the command line
`function {python "C:\Users\Mohit\Desktop\Mohit\Projects\LifeInsightsProject\log_cli.py" @args}`
"""

import sys
import requests
from datetime import date

if len(sys.argv) != 3:
    print("Usage: log<minutes>")
    sys.exit(1)

minutes = int(sys.argv[1])
focus_score = int(sys.argv[2])

payload = {
    "value_minutes": minutes,
    "value_focus_score": focus_score,
    "log_date": date.today().isoformat()
}

response = requests.post(
    "http://localhost:8000/log",
    json=payload
)

if response.status_code == 200:
    print(f"Logged {minutes} minutes for today")

else:
    print(f"Failed to log: {response.text}")