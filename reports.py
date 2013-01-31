import re
import mechanize
import time

br = mechanize.Browser()
br.set_handle_robots(False)
br.add_password("http://members.spamcop.net/", 'username','password',realm=None)
br.open("http://members.spamcop.net/")
while 1:
	try:
		br.follow_link(text="Report Now")
		br.select_form(name="sendreport")
		br.submit()
		print "Reported"
	except:
		print "Sleeping ten minutes"
		time.sleep(600)

