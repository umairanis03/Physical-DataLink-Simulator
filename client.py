import socket
import sys
from pLayer import physicalLayer
ob=physicalLayer()
from dLayer import dataLinkLayer
dobj=dataLinkLayer()
def main():
    #k=physicalModule.physicalLayer()
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8081

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    message = input(" -> ")
    obj = physicalLayer()
    while message != 'quit':
        #message = ''.join(format(ord(i), 'b') for i in message)
        res=""
        for i in message:
            temp=format(ord(i),'b')
            while(len(temp)<7):
                temp = "0"+temp
            res+=temp
        message = res

        message = dobj.CRCmaker(message)
        check = input("Send with error!! (Input y/n) ")
        if (check == "y"):
            message = ob.errorMaker(message)


        #Framing supposed to be added
        message  = dobj.framing(message)

        message = obj.Encode(message)

        soc.sendall(message.encode(encoding='UTF-8',errors='strict'))

        #soc.sendall(message.encode('UTF-8'))
        if soc.recv(5120).decode('UTF-8') == "-":
            pass        # null operation

        message = input(" -> ")








    soc.send(b'--quit--')


if __name__ == "__main__":
    main()


