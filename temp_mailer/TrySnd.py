import sendmail
import csv

def Mail_System(msg_recipient, recipient_name):
	import sendmail

	mail = sendmail.SendMail('srmgupta', 'SRM@75000')

	msg_from 	  =  'HDFC RED <recommendation@hdfcred.com>'
	msg_subject   = 'HDFC RED: Recommended Properties For You'

	msg_text      = '<html><body><p>Hi %s, </p><p>Hope you are doing well.</p><p><b>Recommended Projects</b></p><p>Take a look at our exclusive recommendation for you.</p><br><table><tbody><tr><td><div style="float:left;width:125px;padding-right:5px;padding-bottom:35px"><a href="http://mandrillapp.com/track/click/30604381/www.hdfcred.com?p=eyJzIjoid096Mktxck1Ea1pMNFRDeTlldkRZXzdnSWgwIiwidiI6MSwicCI6IntcInVcIjozMDYwNDM4MSxcInZcIjoxLFwidXJsXCI6XCJodHRwOlxcXC9cXFwvd3d3LmhkZmNyZWQuY29tXFxcL3BpZC0xMjkxXCIsXCJpZFwiOlwiNTUyNGU3NjYzODQyNGQwMGE1M2U5ODU5MDYyYjg4Y2VcIixcInVybF9pZHNcIjpbXCI0MDRmNzUxZjFmNjgwZjQyOTFlZDI4NzA0NWY1OTA1ZGJiYzcxYzcxXCJdfSJ9" style="display:block" target="_blank"><div><div><img class="CToWUd" src="https://www.hdfcred.com/project-images1/728/728_Lifestyle_City_HD.jpg" height="100" width="100"><small>Vinay Unique Developers <br> <span>32 L+  </span></small></div></div></a></div></td><td><div style="float:left;width:125px;padding-right:5px;padding-bottom:35px"><a href="http://mandrillapp.com/track/click/30604381/www.hdfcred.com?p=eyJzIjoiaWJIdXVqajYxRkNwREpsS3QzZ2VmUVFjWjlrIiwidiI6MSwicCI6IntcInVcIjozMDYwNDM4MSxcInZcIjoxLFwidXJsXCI6XCJodHRwOlxcXC9cXFwvd3d3LmhkZmNyZWQuY29tXFxcL3BpZC0xNDMwXCIsXCJpZFwiOlwiNTUyNGU3NjYzODQyNGQwMGE1M2U5ODU5MDYyYjg4Y2VcIixcInVybF9pZHNcIjpbXCI0MDRmNzUxZjFmNjgwZjQyOTFlZDI4NzA0NWY1OTA1ZGJiYzcxYzcxXCJdfSJ9" style="display:block" target="_blank"><div><div><img class="CToWUd" src="https://ci5.googleusercontent.com/proxy/XGEjoax_09OerduoAMdIX7KookLjMucm16ok6FwZV7cx40R89b-3StUlOjB-M9mTyQ-ARv3M-TR3_a5NYuCcGUq6zkwfA2ySUQ6T-ceoG8rWM2uDOwZh9Q=s0-d-e1-ft#https://www.hdfcred.com/project-images1/1430/1430_Chhaya_Niwas.jpg" height="100" width="100"><small>Usha Breco Realty Limited<br> <span>25 L+  </span></small></div></div></a></div></td><td><div style="float:left;width:125px;padding-right:5px;padding-bottom:35px"><a href="http://mandrillapp.com/track/click/30604381/www.hdfcred.com?p=eyJzIjoiTWp0MlUwZVZaSUkydGUxQWlGQXl6TEdGZUkwIiwidiI6MSwicCI6IntcInVcIjozMDYwNDM4MSxcInZcIjoxLFwidXJsXCI6XCJodHRwOlxcXC9cXFwvd3d3LmhkZmNyZWQuY29tXFxcL3BpZC0xNTY4XCIsXCJpZFwiOlwiNTUyNGU3NjYzODQyNGQwMGE1M2U5ODU5MDYyYjg4Y2VcIixcInVybF9pZHNcIjpbXCI0MDRmNzUxZjFmNjgwZjQyOTFlZDI4NzA0NWY1OTA1ZGJiYzcxYzcxXCJdfSJ9" style="display:block" target="_blank"><div><div><img class="CToWUd" src="https://ci4.googleusercontent.com/proxy/6vLYuconv2DMb_gnwdiB2wtJsiioU2YdlupJEHDc2Pp0-a3Y83t-Mrah9svzYh1DFpqeGDNPPbIiexqaoKEvIoYhRKly4ReLx0n3O0Qx8r3ALmFuKM34LZQ=s0-d-e1-ft#https://www.hdfcred.com/project-images1/1568/1568_Eco_Eden_City.jpg" height="100" width="100"><small>Mayuresh Group<br> <span>31 L+  </span></small></div></div></a></div></td></tr></tbody></table></body></html>' % (recipient_name)

	mail.send_mail(msg_recipient, msg_from, msg_subject, msg_text)


my_csv = csv.reader(open('test1.csv'))

for row in my_csv:
	recipient_name	= row[0]
	msg_recipient 	= row[1]

	Mail_System(msg_recipient, recipient_name)


	