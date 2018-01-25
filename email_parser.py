import smtplib
import re
import psycopg2
import pause, datetime
import imaplib

# Super Cool Comment

#set credentials for receiving email
emailaddr = 'your user'
passwd = 'yourpass'
#set smtp server receiving server and port
smtp_serv = 'your.mailsmtpserver.com'
smtp_port = 993


# reads emails from specified email then parse ip, mac, and port
# and put it into postgres server if it doesn't exist or updates
# if it does

def readmymailples():
	mail = imaplib.IMAP4_SSL(smtp_serv) # sets smtp server
	mail.login(email_addr,passwd) # login to email using credentials
	mail.select('filteredinbox') # select filtered inbox
	type, data = mail.search(None, 'ALL') # grab all emails
	mail_idz = data[0] # grab mails ids
	id_list = mail_idz.split() # creates an array of email ids
	first_email = int(id_list[0]) # gets id of first email 
	latest_email = int(id_list[-1]) # gets id of last email
	
	for i in range (latest_email, first_email, -1): # iterate through email
		type, data = mail.fetch(i, '(RFC822)')	# fetch current email
		body = data[0][1] # grab body of email
		myip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",body,flags=0) #grab ip from body
		mymac = re.search(r"((\d|[ABCDEF]){2})(:|-)((\d|[ABCDEF]){2})(:|-)((\d|[ABCDEF]){2})(:|-)((\d|[ABCDEF]){2})(:|-)((\d|[ABCDEF]){2})(:|-)((\d|[ABCDEF]){2})",body,flags=0) # grab mac address 
		myport = re.search(r"(port:)(\d{1,5})",body,flags=0) # grab port num
		try:
			conn = psycopg2.connect("dbname='db' user='user' password='password'") # connect to database
			cur = conn.cursor() # make the cursor a variable
			cur.execute("""SELECT mac from table""") # get all macs
			rows = cur.fetchall() # store all macs in array
			isitin = False # bool for whether the mac already exists
			for row in rows: 
				if row == mymac: # if the row contains the new mac
					isitin = True # change bool to truw
					break
			if isitin:
				cur.execute("UPDATE table SET ip = %s, port = %s WHERE mac = %s",\(myip.group(),myport.group(2),mymac.group())) 
				# update ip and port if eneded 
			else:
				cur.execute("INSERT INTO bots (ip,mac,port) VALUES (%s,%s,%s)",\(myip.group(),mymac.group(),myport.group(2))
				# insert new entry
		except:
			print("Can't sry bud") # couldnt enter entry fro some reason
			break
	for num in id_list:
		mail.store(num, '+FLAGS', '\\Deleted') # put in garbage
	mail.expunge() # empty garbage
	mail.logout # logut od mail server
	pause.days(1) # wait a day
	readmymailples() # rinse and repeat
