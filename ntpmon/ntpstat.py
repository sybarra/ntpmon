#!/usr/bin/python
import time
import os
import datetime

end_time = int(raw_input('How long, in seconds, should this to run?:'))

def get_ntp_status():
	now = datetime.datetime.now()
	start_time = time.time() 

	while (time.time() - start_time) < end_time:
		print ""
		print ""
		print now.strftime("%y-%m-%d %H:%M:%S")
		os.system("ntpq -pn")
		time.sleep(1) #Sleep 30 min

get_ntp_status()

	
				
