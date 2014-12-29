'''
	Code by Daniel Wirick 12-7-14
This program's purpose is to decypher a "command" configuration file which lists all the commands available on
this robot.  After reading the file and setting up the appropriate data elements in python, it should wait for input from a higher level (interface TBD) and execute the appropriate when instructed.

Ultimately the program should provide information to the higher level function, about which commands are available and how they operate.

Untested 12-7-14
'''

import serial
import string
import time

#Opens the serial port to Arduino Nano
#Should this open available serial ports sequentially and "search" for a keyword from the Nano?
#When run onboard, all of these delays for rfcomm will be meaningless
ser = serial.Serial ('/dev/rfcomm0', 115200)

print ("Connecting...")

#Its possible I should do some sort of handshake here

time.sleep (5) #need to wait for rfcomm bluetooth for some kernels

cmd_file = open ("4_leg_test", 'r')

cmds = {}
delay = 0
cmd_key = ""

#opens file which should contain various commands and corresponding instructions to send to the arduino controller.
#currently only setting servo positions and delaying for specific amounts of time are supported.
for line in cmd_file:
	if 'delay' in line:
		delay = int (line.translate (None, string.letters).translate (None, string.whitespace).translate (None, string.punctuation))
	elif line.strip() == '' or line.strip()[0] == '#':
		pass
	elif line.strip()[0] in string.letters and line.strip()[1] == ',':
		cmds[cmd_key].append (line)
		cmds[cmd_key].append (delay)
	else:
		cmd_key = line.strip().lstrip()
		cmds[cmd_key] = []

cmd_file.close ()

print (cmds)

#Reads in any data from the Nano
def read_in ():
	while ser.inWaiting() > 0:
		print (ser.read())

#Writes the commands out the serial port to the Nano
def write_cmd (cmd):
	cmd_lst = cmds[cmd]
	for instruction in cmd_lst:
		if type(instruction) is int:
			#delay for number milliseconds
			time.sleep (instruction/100.0)
		else:
			ser.write (instruction.encode())


#Haven't created a control loop yet, below code is for debugging
read_in ()
#Walk forward 10 times
i = 10
while i > 0:
	write_cmd ("forward")
	read_in ()
	i = i - 1
ser.close()
