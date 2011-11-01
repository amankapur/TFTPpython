import TFTPserver
import TFTPclient
import UDPkit
import Packet
import os.path

client_to_server = UDPkit.ToSocket(thatPort = 50021)
client_from_server = UDPkit.FromSocket(thisPort = 50020)

####### TO INITATE TRANSFER ASK USER INPUT ######
input1 = ""

while(input1 != "Read" and input1 != "Write"):
	input1 = raw_input("Read or Write :")
	

if(input1 == "Read"):	
		
	filename = raw_input("filename:")
	packet = Packet.Packet(01, filename, None, None, None, "ERROR", "octet")
	client_to_server.send(str(packet)) 

if(input1 == "Write"):	
	try:
		filename = ""	
		while(not os.path.exists(filename)):
			filename = raw_input("Please enter a valid filename:")		
		packet = Packet.Packet(0x0002, filename, None, None, None, "ERROR", "octet")		
		client_to_server.send(str(packet)) 
	except:	
		#ERROR#
		packet = Packet.Packet(0x0005, None, None, None, ErrorCode, "ERROR", None)
		client_to_server.send(str(packet))
		#close connetion
		
######## USER INPUT OVER, FILES EXCHANGE NOW #########
"""

apple = true
while apple:

	packet = client_from_server.recv()

	if(packet.opCode == 0x0002):
	
	if(packet.opCode == 0x0003):

	if(packet.opCode == 0x0004):

	if(packet.opCode) == 0x0005):

"""
