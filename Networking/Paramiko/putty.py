from pywinauto.application import Application
import time

#app = Application ().Start (cmd_line=u'notepad')
app = Application ().Start (cmd_line=u'putty -ssh {}@{}'.format("nirai0",'10.57.164.20'))
putty = app.PuTTY
putty.wait ('ready')

putty.type_keys ("Nishtharai15@")
putty.type_keys ("{ENTER}")
time.sleep(5)
putty.type_keys ("Nishtharai15@")
putty.type_keys ("{ENTER}")
time.sleep (5)


####################################################################################
def connect_device(device, cmd):
	putty.type_keys ("fping {}".format(device),with_spaces=True)
	putty.type_keys ("{ENTER}")
	time.sleep(3)

	##use ssh or telnet
	#command to connet your router
	putty.type_keys ("l {}".format(device),with_spaces=True)
	putty.type_keys ("{ENTER}")


	time.sleep(14)
	putty.type_keys ("{}".format(cmd),with_spaces=True)
	putty.type_keys ("{ENTER}")

	time.sleep(4)
	putty.type_keys ("exit",with_spaces=True)
	putty.type_keys ("{ENTER}")
	time.sleep(2)

#######################################################################################################################

for i in range(0,10):
	connect_device('pxvu130','sh ver | in up')



