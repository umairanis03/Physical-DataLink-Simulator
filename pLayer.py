class physicalLayer:
    def encode(self, bitSequence, size):

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

    def decode(self, bitsequence, size):
        output=""


        for i in range(0,size):
            if bitsequence[i] == 'y':
                output += '0'
            else:
                output += '1'

        return output




obj =physicalLayer()
print(obj.encode("01001",5))

print(obj.decode("yxyyz",5))