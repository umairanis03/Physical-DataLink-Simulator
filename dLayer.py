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

obj=dataLinkLayer()

