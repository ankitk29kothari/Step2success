#This windlw_aler program will not work in browserless beacause of its sending keys to windows application throguh keyboard control

from easyselenium import *
import time
driver=open_browser(browser='firefox')
open_url('https://authiad2.apps.ocn.infra.ftgroup/login.php?timeout=14400')

time.sleep(3)
window_alert(text="your login name")
time.sleep(3)
window_alert(text='{TAB}')
window_alert(with_enter=True)