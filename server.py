import socket
import sys
import traceback
from threading import Thread
from pLayer import  physicalLayer
from dLayer import dataLinkLayer
obj=physicalLayer()
ob=dataLinkLayer()

def main():
    start_server()


def start_server():
    host = "127.0.0.1"
    port = 8081        # arbitrary non-privileged port

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
    print("Socket created")

    try:
        soc.bind((host, port))
        #print('hey')
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(500000)       # queue up to 5 requests
    print("Socket now listening")

    # infinite loop- do not reset for every requests
    while True:
        #print ('here')
        connection, address = soc.accept()
        #print ('hey')
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()

    soc.close()


def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True

    while is_active:
        client_input = receive_input(connection, max_buffer_size)

        if "--QUIT--" in client_input:
            print("Client is requesting to quit")
            connection.close()
            print("Connection " + ip + ":" + port + " closed")
            is_active = False
        else:
            print("Processed result: {}".format(client_input))
            connection.sendall("-".encode("UTF-8"))


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))

    decoded_input = client_input.decode("UTF-8").rstrip() # decode and strip end of line
    decoded_input = obj.Decode(decoded_input)
    decoded_input = ob.deframing(decoded_input)
    result = process_input(decoded_input)

    return result


def process_input(input_str):
    print("Processing the input received from client")
    ob.CRCchecker(input_str)
    res=""

    i=0
    while(i<len(input_str)-3):
        temp=input_str[i:i+7]
        a = int(temp, 2)
        res += str(chr(a))
        i += 7


    return "Message from client:  " + str(res)

if __name__ == "__main__":
    main()
