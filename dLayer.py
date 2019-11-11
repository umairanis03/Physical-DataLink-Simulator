from pLayer import physicalLayer
ob=physicalLayer()

def xor(a, b):
    res = ""

    for i in range(1, len(b)):
        if a[i] == b[i]:
            res+='0'
        else:
            res+='1'

    return res

def mod2div(bitsequence, divisor):
    pick = len(divisor)


    tmp = bitsequence[0: pick]

    while pick < len(bitsequence):

        if tmp[0] == '1':


            tmp = xor(divisor, tmp) + bitsequence[pick]

        else:
            tmp = xor('0' * pick, tmp) + bitsequence[pick]

        pick += 1


    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


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
            if i+3<=l-5 and frame[i]=='1' and frame[i+1]=='1' and frame[i+2]=='1' and frame[i+3]=='1':

                output+="1111"
                i=i+5
            else:
                output+=frame[i]
                i+=1

        return output

    def CRCmaker(self, bitsequence):
        divisor = "1011"
        divlen = len(divisor)

        newSeq = bitsequence + '0' * (divlen - 1)
        rem = mod2div(newSeq, divisor)


        codeword = bitsequence + rem
        return codeword


    def CRCchecker(self,bitsequence):
        divisor = "1011"
        divlen = len(divisor)

        # Appends n-1 zeroes at end of data
        newSeq = bitsequence + '0' * (divlen - 1)
        rem = mod2div(newSeq, divisor)

        a = int(rem,2)
        if a==0:
            print("NO ERROR")
        else:
            print("ERROR DETECTED")

