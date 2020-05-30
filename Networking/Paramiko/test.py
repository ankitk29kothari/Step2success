import paramiko
import time


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="10.57.164.20", username="nirai0", password="Nishtharai15@", look_for_keys=False, allow_agent=False)
print('connected')