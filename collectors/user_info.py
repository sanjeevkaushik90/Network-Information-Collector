import os
import pwd

user = pwd.getpwuid(os.geteuid())

print("Username:", user.pw_name)
print("User ID:", user.pw_uid)
print("Home Directory:", user.pw_dir)
print("Shell:", user.pw_shell)