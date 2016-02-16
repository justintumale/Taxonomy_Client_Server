import socket

def Main():
    '''
    Main function that connects to the server, prompts user for inputs, and then streams
    user inputs to the server via UDP.
    '''
    host = socket.gethostname()
    '''port has to be different from udpServer's.'''
    port = 5001

    '''the server is on this machine, but its port is on the udpServer??'''
    server = (host, 5000)
    '''create the udp socket'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    '''bind the socket to the port'''
    s.bind((host, port))

    message = input("-> Please insert<path>, list<path>, or search<category>, or quit\n")
    while message != 'quit':
        '''
        send the message.
        define where you want the message sent.
        send the message to the server that was setup earlier
        '''
        s.sendto(message.encode('utf-8'), server)

        '''get the data and the address that it came from'''

        data, address = s.recvfrom(2024)
        data = data.decode('utf-8')

        print("Received from server: " + data)
        message = input("-> Please insert<path>, list<path>, or quit\n")
    s.close()

if __name__ == '__main__':
    Main()
