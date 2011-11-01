import socket
print "IN uuu"
BUFFERSIZE = 4096  # buffer size for recvfrom 

class FromSocket(object):
    """returns instantiated "receivefrom" socket"""
    
      
    def __init__(self , thisIPaddr = "127.0.0.1" , thisPort = 50001 ):
        """
        Create inbound socket 
                                                                               
        """
        try:

            self.thisIPAddr, self.thisPort = thisIPaddr , thisPort
            self.thisAddr = (self.thisIPAddr, self.thisPort)

            #super(ToSocket,self).__init__() # initialize next higher superclass
            
            self.from_sock = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )
            self.from_sock.settimeout(2.0)    # non-zero timeout used to catch exceptions
            print self.from_sock._sock
            print self.thisAddr
            self.from_sock.bind(self.thisAddr)
                
        except Exception as exeptn:
            print type(exeptn),exeptn
            self.from_sock.close()            # explicitly close socket on failure
            raise exeptn    # reraise exception
        finally: print "init for FromSocket done"

    def recv(self):    
    
        while True:         # input loop, also used to retry 
            try:
                self.thatPayload, self.thatAddr = self.from_sock.recvfrom( BUFFERSIZE )
                self.thatIPaddr , self.thatPort = self.thatAddr
                print self.thatAddr
                return self.thatPayload
            except socket.timeout: continue       # retry after timeout
            
            except Exception as exeptn:           # end loop on any exception
                self.from_sock.close()            # explicitly close socket 
                raise exeptn                      # then reraise exception
            
            #if TRACING: print self.ShowDataGram("inbound")  # Display IP and UDP formats
            finally: print "recv done"
    def close(self): self.from_sock.close()           # explicitly close socket

class ToSocket(object):
    """ Create instance of outbound UDP socket
            
            The constructor determines a destination address for all packets produced
            by sendto().  It is the tuple (thatIPaddr, thatPort).

            When recvfrom returns it provides the Payload and the sending
            address tuple (thisIPaddr, thisPort).  It gets these from
            the packet it receives. 

            The sendto call to the socket could block.
            This implementation uses timeout to ensure that a blocking write
            will eventually receive a timeout and any pending exogenous events.
            This permits signals such as ctl-c to terminate the sendto call and
            the process.

            If the operator uses the attention key (ctl-c) or the task terminates,
            the state of the underlying operating system's IPstack state
            is reset.

            """
    def __init__(self , thatIPaddr = "127.0.0.1" , thatPort = 50001 ):
        """UDPsocket.__init__(
                                thatIPaddr  = "127.0.0.1" # ipv4 address to send to
                                thatPort    = 50001       # port to send to
        """                                              
        try:
            
            self.thatIPaddr , self.thatPort = thatIPaddr , thatPort
            self.thatAddr = (self.thatIPaddr, self.thatPort)
            print self.thatAddr," in ToSocket"
            #super(ToSocket,self).__init__(self.thatAddr) # initialize next higher superclass
                        
            self.to_sock  = socket.socket( socket.AF_INET , socket.SOCK_DGRAM )

            self.to_sock.settimeout(2.0)    # non-zero timeout is used to catch exceptions
                    
        except Exception as exeptn:
            print type(exeptn),exeptn
            self.to_sock.close()         # explicitly close socket
            raise exeptn                # reraise exception

        finally:
            print "init for ToSocket done"

    def send(self,thisPayload):
        """ sends thisPayload to self.thatAddr
      
              """
        while True:
            self.thisPayload = thisPayload
            try:
                return self.to_sock.sendto(self.thisPayload, self.thatAddr)
                # returns number of bytes in thisPayload sent to thatAddr
                
            except socket.timeout: continue  # retry after timeout
            
            except Exception as exeptn:
                self.to_sock.close()         # explicitly close socket
                raise exeptn                 # reraise exception

            #if TRACING: print self.ShowDataGram("outbound")  # Display IP, UDP and Payload 

    def close(self):
        self.to_sock.close()
        


           

    
        
        
        
            
        
            
            
            
            
            
        
