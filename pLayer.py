import random
class physicalLayer:
    def Encode(self, bitSequence):
        size = len(bitSequence)
        output=""
        last='z'
        for i in range(0,size):
            if i==0 and bitSequence[i]=='0':
                output+='y'
            elif   i == 0 and bitSequence[i] == '1':
                output += 'x'

            elif bitSequence[i]=='0':
                output+='y'
            else :
                if last=='z' :
                    output+='x'
                    last='x'
                else:
                    output+='z'
                    last='z'


        return output

    def Decode(self, bitsequence):
        output=""
        size =len(bitsequence)


        for i in range(0,size):
            if bitsequence[i] == 'y':
                output += '0'
            else:
                output += '1'

        return output

    def errorMaker(self,bitsequence):
        newSeq=list(bitsequence)
        length=len(bitsequence)
        k=random.randint(1,length)
        times = max(random.randint(0,length//k),1)
        for i in range(times):
            global yt
            if(length>0):
                yt = random.randint(0,length)
                if(bitsequence[yt]=='0'):
                    newSeq[yt]='1'
                else:
                    newSeq[yt]='0'

        newstr = "".join(newSeq)
        return newstr
