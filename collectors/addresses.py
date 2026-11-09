import socket
import getpass
hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

username=getpass.getuser()


print(f"Hostname: {hostname}")
print(f"Local IP Address: {local_ip}")
print(f"Username: {username}")
