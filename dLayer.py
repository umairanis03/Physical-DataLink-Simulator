from pLayer import physicalLayer
ob=physicalLayer()
def reverse(string):
    string = "".join(reversed(string))
    return string

def int_to_bin_string(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s
class dataLinkLayer:


    def framing(self, datagram):
        l = len(datagram)

        output=""
        flag = "1111"
        i=0
        while(i<l):
            #global i
            if i+3<=l-1 and datagram[i]=='1' and datagram[i+1]=='1' and datagram[i+2]=='1' and datagram[i+3]=='1':

                output+="11110"
                i=i+4
            else:
                output+=datagram[i]
                i+=1

        out= flag+output+flag
        return out

    def deframing(self,frame):
        i=4
        output=""
        l=len(frame)
        while(i<l-4):
            if i+3<=l-1 and frame[i]=='1' and frame[i+1]=='1' and frame[i+2]=='1' and frame[i+3]=='1':

                output+="1111"
                i=i+5
            else:
                output+=frame[i]
                i+=1

        return output

    def CRCmaker(self, bitsequence):
        k=len(bitsequence)
        divisor = "1011"
        newSeq=""
        newSeq=bitsequence
        for i in range(0, len(divisor)-1):
            newSeq += "0"

        a=int(divisor,2)
        b=int(newSeq,2)
        c=b%a
        c=c+b
        s = ''
        if c == 0:
            s = "0"

        while c:
            if c & 1 == 1:
                s = "1" + s
            else:
                s = "0" + s
            c //= 2

        # print(bitsequence)
        # print(newSeq)
        # print(s)
        # print(len(divisor)-len(s))
        # while len(s)<len(divisor)-1:
        #     s='0'+s
        #
        # #x = reverse(x)
        # bitsequence+=s
        # print(bitsequence)
        return  s


    def CRCchecker(self,bitsequence):
        divisor = "1011"
        a=int(divisor,2)
        b=int(bitsequence,2)
        if(b%2):
            print('Error detected!!')
        else:
            print('No error')







# obj=dataLinkLayer()
# f=ob.errorMaker("0111101")
# print(f)
# t=obj.CRCmaker(f)
# print(t)
#
# obj.CRCchecker(t)