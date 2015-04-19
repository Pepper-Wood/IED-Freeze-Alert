import smtplib							# Import smtplib for the actual sending function
from email.mime.text import MIMEText	# Import the email modules we'll need

# Global variables
me = dipippo.k@gmail.com	# This will temporarily be my email address
you = john.cena@gmail.com	# This will be replaced by reading from google document
cold_counter = 0			# keeps track of whether the system is too cold
filename = 'temperatures.txt'
threshold = 10				# number of times a temperature is too low before enabling motor

# ========================================================================
def main():
	while True: # loop everything below infinitely
		#---------------Reading the .txt file from the dropbox
		if len(sys.argv) == 2:		# Check the arguments passed to the script
			filename = sys.argv[1]		# The filename is the first argument
			if not os.path.isfile(filename):	# Check the File exists
			  print '[-] ' + filename + ' does not exist.'
			  exit(0)
			if not os.access(filename, os.R_OK):	# Check you can read the file
			  print '[-] ' + filename + ' access denied'
			  exit(0)
		else:
			print '[-] Usage: ' + str(sys.argv[0]) + ' <filename>' # Print usage if not all parameters passed/Checked
			exit(0)
		print '[+] Reading from : ' + filename	# Display Message and read the file contents
		# readfile(filename)		# This will print out text document for debugging
		
		#---------------Testing for whether temperature is too cold
		fyle = open(filename)
		for lyne in fyle :
			# increment cold counter if a series of numbers is below 25 degrees
			# reset if this is not the case
			if (lyne <= 25):
				cold_counter = cold_counter + 1		#increment
			else:
				cold_counter = 0	# reset otherwise
			
			if (cold_counter >= threshold):  # The pipes are too cold at this point
				#---------------Return the data as an email message
				# Open warning message to send as an email.
				fp = open('warning_message.txt', 'rb')
				# Create a text/plain message
				msg = MIMEText(fp.read())
				fp.close()

				# me == the sender's email address
				# you == the recipient's email address
				msg['Subject'] = 'FREEZE ALERT WARNING'
				msg['From'] = me # for now it's going to be my email address
				msg['To'] = you # This will be replaced as well

				# Send the message via our own SMTP server, but don't include the
				# envelope header.
				s = smtplib.SMTP('localhost')
				s.sendmail(me, [you], msg.as_string())
				s.quit()
				
				#---------------Enable the motor
				#UHHHHHHHHHH
				cold_counter = 0		# reset the counter to let the system reset
		fyle.close()
		
		#---------------Store the current cold_counter in a separate .txt file
		saving_progress = open('ccc.txt', 'w') #ccc stands for current cold_counter
		saving_progress.write(cold_counter)
		saving_progress.close()
	

# ------------------------------------------------------------------------
# function that reads a file
def readfile(filename):
	f = open(filename, 'r')
	line = f.read()
	print line
	
# ========================================================================	
if __name__ == '__main__':
	main()