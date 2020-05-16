import os

stdout=os.popen("ipconfig").read()
print(stdout)

