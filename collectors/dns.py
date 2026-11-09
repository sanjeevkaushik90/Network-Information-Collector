import subprocess

result = subprocess.run(
    ["resolvectl", "status", "wlp58s0"],
    capture_output=True,
    text=True
)

print(result.stdout)    