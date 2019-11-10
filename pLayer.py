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
        newSeq=""
        length=len(bitsequence)
        k=random.randint(2,length)
        print(k)
        for i in range (0,k):
            if(bitsequence[i]=='0'):
                newSeq+='1'
            else:
                newSeq+='0'
        for i in range(k,length):
            newSeq+=bitsequence[i]
        return newSeq




