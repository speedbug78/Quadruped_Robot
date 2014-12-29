'''
	Code by Daniel Wirick 12-7-14
This code executes onboard the Olinuxino and allows manual setting of servo positions via the serial bus
communication with the Arduino Nano

Tested working 12-7-14
'''
import serial

ser = serial.Serial ('/dev/ttyAPP0', 115200)

print ("Connecting...")

current_pos = ["s",90,90,90,90,90,90,90,90]
command = ''

while command != "quit":
	print ("Available coammnds:")
	print ("Sn = set servo position where n is the servo number to set (1-8)")
	print ("quit = stop this program and go back to the shell")
	command input ("Enter a command: ")

	if command[0] == 's' or command[0] == "S":
		servo_pos = input ("Enter a position for this servo (0-180): ")
		try:
			current_pos[int(command[1])] = int(servo_pos)
			write_str = ''
			for element in current_pos:
				write_str = write_str + str(element) + ','
			write_str = write_str.lstrip (",")
			ser.write (str(write_str))
		except:
			print ("invalid servo command")
