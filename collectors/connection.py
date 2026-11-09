import subprocess

result = subprocess.run(
    ["nmcli", "device", "status"],
    capture_output=True,
    text=True
)

print(result.stdout)