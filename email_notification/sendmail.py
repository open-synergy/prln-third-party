import smtplib
def sendmail(sender,receiver,subject,message):
	
	message2 = """From: ERP Alert<%s>
To: <%s>
Subject: %s
Info : 
%s
	"""%(sender, receiver, subject, message)
	print message2
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, receiver, message2)         
