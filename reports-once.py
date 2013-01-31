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
		#print br.response().get_data()
		br.select_form(name="sendreport")
		br.submit()
		print "Reported"
	except mechanize._mechanize.FormNotFoundError:
		print "Not allowed to report"
	except mechanize._mechanize.LinkNotFoundError:
		print "Nothing left"
		quit()
	except:
		print "Unknown exception"
		raise;
		quit()
