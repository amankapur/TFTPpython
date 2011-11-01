import UDPkit
import Packet
import os.path


server_from_client = UDPkit.FromSocket(thisPort = 50021)
server_to_client = UDPkit.ToSocket(thatPort = 50020)

apple = True

while(apple):
	Packet =  (server_from_client.recv())
	print Packet
	print id(Packet)
	print "%s" % (Packet.opCode, )
	print Packet.opCode


"""
	if(Packet.opCode == "00000000000000000001"):	
		print str(packet)
	
	if(packet.opCode == 0x0002): 		######## INCOMING FILE TO WRITE ###########
		print packet
	
	if(packet.opCode == 0x0003):
	
		TFTPserver.uploadData()	

	if(packet.opCode == 0x0005):
			
		TFTPserver.sendERR()	#Send error packet to client
		TFTPserver.showErr() #Display error
		#close socket			


"""
    

