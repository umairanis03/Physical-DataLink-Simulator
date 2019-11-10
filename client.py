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
    port = 8080

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
            if(len(temp)<7):

                temp = "0"+temp
            res+=temp
        message = res

        message = dobj.CRCmaker(message)
        message = obj.Encode(message)

        #print(message)
        soc.sendall(message.encode(encoding='UTF-8',errors='strict'))

        #soc.sendall(message.encode('UTF-8'))
        if soc.recv(5120).decode('UTF-8') == "-":
            pass        # null operation

        message = input(" -> ")
        #print("Send through error!! (Input Y) ")
        check = input("Send through error!! (Input Y) ")
        if(check=="Y"):
            print("ander")
            message=ob.errorMaker(message)






    soc.send(b'--quit--')


if __name__ == "__main__":
    main()
