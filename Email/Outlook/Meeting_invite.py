import win32com.client
outlook = win32com.client.Dispatch("Outlook.Application")


def sendMeeting(start_time,duration,subject,reason):

	  appt = outlook.CreateItem(1) # AppointmentItem
	  print(start_time)
	  appt.Start = str(start_time)# yyyy-MM-dd hh:mm
	  appt.Subject = subject
	  appt.Duration = duration # In minutes (60 Minutes)
	  appt.Location = "Meeting Location"
	  appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added
	  appt.Body = "HI ALL,"+'\n\n'+'\n\n'+reason
	  
	  appt.Recipients.Add('ankit.kothari@orange.com') 
	  appt.Save()
	  appt.Send()






sendMeeting('2020-04-05 15:33',60,'na','naaaaa')







def sendRecurringMeeting():    
	  appt = outlook.CreateItem(1) # AppointmentItem
	  appt.Start = "2018-10-28 10:10" # yyyy-MM-dd hh:mm
	  appt.Subject = "Subject of the meeting"
	  appt.Duration = 60 # In minutes (60 Minutes)
	  appt.Location = "Location Name"
	  appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added

	  appt.Recipients.Add("ankit.kothari@orange.com") # Don't end ; as delimiter

	  # Set Pattern, to recur every day, for the next 5 days
	  pattern = appt.GetRecurrencePattern()
	  pattern.RecurrenceType = 0
	  pattern.Occurrences = "5"

	  appt.Save()
	  appt.Send()