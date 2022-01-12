from easyselenium import *

def browser(ticket_nos,names):
	global driver
	driver=open_browser(headless=False,browser='chrome',debug=True)
	open_url(url="https://mytools-portal.sso.infra.ftgroup/binbeemytools/Home/Portfolio")
	time.sleep(6)
	open_url(url="https://mytools-portal.sso.infra.ftgroup/binbeemytools/Home/Portfolio")
	try:
		click_on(xpath='idgroup="1077122"')
	except:
		pass
	time.sleep(7)

	#switch_frame(driver,no=1)

	window_handle(1,timeout=100)
	switch_frame(name='OCEANE',timeout=100)
	#click_on(text='creation',timeout=100)
	#click_on(id='menu_hlnk_I1_L1',timeout=100)
	for ticket,name in zip(ticket_nos,names):
		try:
			ticket_create(ticket,name)
		except:
			try:
				close_window (no=2)
			except:
				pass
	close_window (no=1)
	close_window (no=0)


def ticket_create(ticket_no,name):

	window_handle(1)
	switch_frame(name='OCEANE')
	send_text(id='IDTTIC',text=ticket_no,with_enter=True)
	title=window_handle(2)
	switch_frame(name='PopupOCEANE')
	click_on(text='modify')
	title=window_handle(2)
	switch_frame(name='PopupOCEANE')
	technician=severity=select_dropdown(id='IDTUTLPEC',option=name)
	save=click_on(id ='ENRTIC')
	close_window (no=2)



#browser(['2010W12818'],['Chaurasia Swati'])

