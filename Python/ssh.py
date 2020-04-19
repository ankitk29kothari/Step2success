import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time
import paramiko
import time
import pandas as pd
import time
import openpyxl
import sys
import threading
host='10.57.164.20'

username='nirai0'
password='Nishtharai15@'
gsk_login='hhj70755'
gsk_password='India@2wsx'

excel_name="input.xlsx"




global_lock = threading.Lock()

def UpdateRoutersResultsToSheet_fping(routers,fping,current_index):
	while global_lock.locked():
		time.sleep(0.01)
		continue
	global_lock.acquire()
	workbook_obj = openpyxl.load_workbook(excel_name)
	
	sheet_obj = workbook_obj['Sheet1']
	name = routers
	sheet_obj.cell(row=current_index, column=2).value = fping
	workbook_obj.save(excel_name)
	print('Excel save',current_index)
	global_lock.release()



def do_something(device):
	print('start')
	client = paramiko.SSHClient()
	
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False)
	
	command22 = "/usr/local/sbin/fping {0}".format(device)
	stdin, stdout, stderr = client.exec_command(command22, bufsize=1024)
	data = stdout.read()
	print(data)


	shell_object = client.invoke_shell()
	time.sleep (0.2)



	output = str(shell_object.recv(999999))
	
	while not 'TACACS Nmstel password' in output:
		time.sleep(0.1)
		print(".")
		output = str(shell_object.recv(999999))
		
	shell_object.send(password + "\n")
	#print('Shell Invoked')


	time.sleep (0.2)
	output = str(shell_object.recv(999999))
	while not 'Nmstel credentials registered successfully' in output:
		time.sleep(0.1)
		print('.')
		output = str(shell_object.recv(999999))
		

	print('Tacas Registered successfully')
	
	shell_object.send("l {}".format(device)+'\n')

	
	output = str(shell_object.recv(999999))
	while not 'Device connected' in output:
		time.sleep(0.1)
		print('.')
		output = str(shell_object.recv(999999))

		continue
	print('Device connected firing coomand')
	time.sleep(0.2)
	shell_object.send("sh ver"+'\n')
	time.sleep(1.5)
	output = (shell_object.recv(999999))
	output=(output.decode("utf-8"))
	current_index=(devices.index(device))+2
	UpdateRoutersResultsToSheet_fping(device,output,current_index)
	
	#print(output)
	return(output)



def ConnectControlNetAndRunCommand(device):
    pass
    try:
      text = []
      
    
      current_index=(devices.index(device))+2
      ssh = paramiko.SSHClient()
      ssh.load_system_host_keys()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      time.sleep(0.01)
      
      
      ssh.connect(hostname=host, port=22, username=username, password=password)
     

      command22 = "/usr/local/sbin/fping {0}".format(device)
      stdin, stdout, stderr = ssh.exec_command(command22, bufsize=1024)
      error = stderr.read()
      data = stdout.read()
      if error:
        decode_data=(error.decode("utf-8"))
        UpdateRoutersResultsToSheet_fping(device,decode_data,current_index) 
      if data:
        decode_data=(data.decode("utf-8"))
        UpdateRoutersResultsToSheet_fping(device,decode_data,current_index)
        return(data)
    except Exception as e:
      print("connection failed\n", e)


def main():
	df = pd.read_excel(excel_name)
	global devices
	devices=list(df['switch'])
	print('main')
	
	t1=time.perf_counter()

	#with concurrent.futures.ProcessPoolExecutor() as executor:
	with concurrent.futures.ThreadPoolExecutor(max_workers = 1) as executor:
		secs=[]

	

		#a=executor.submit(do_something,1)
		#print(a.result())
		results=executor.map(do_something, devices)

		for result in results:
			print(result)
		
		
		t2=time.perf_counter()
		print('Finsihed in',(t2-t1/2),'sec')




if __name__ == '__main__':
	main()