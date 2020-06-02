
import paramiko
import time
#os.popen("pip freeze").read()


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="host", username="username", password = psw , allow_agent=False)
print('connected')


shell_object = client.invoke_shell()
time.sleep(8)
## only for tacas 
shell_object.send(psw+'\n')
time.sleep(4)
shell_object.send('fping device'+'\n')
time.sleep(3)
shell_object.send('l device'+'\n')
time.sleep(14)
output = str(shell_object.recv(10000).decode("utf-8"))
shell_object.send('Sh int GigabitEthernet0/0/0 | I rate'+'\n')
time.sleep(3)
output1 = str(shell_object.recv(10000).decode("utf-8"))
shell_object.send('sh ver'+'\n')
time.sleep(3)
output2 = str(shell_object.recv(10000).decode("utf-8"))
shell_object.send('exit'+'\n')
time.sleep(3)
output = str(shell_object.recv(10000).decode("utf-8"))
print(output)

print('++++++')

print('output1',output1)
print('output2',output2)
