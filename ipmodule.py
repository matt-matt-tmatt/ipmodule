import random

class IPmodule:
    """ Random IPv4 and subnet mask generator"""       
    def getRandomIp(self):
        """returns random IPv4"""        
        return ".".join(str(random.randint(0,255)) for n in range(4))
    def getRandomPMask(self):
        """returns random subnet mask in prefix format"""
        return f"/{random.randint(0,32)}"
    def getRandomDMask(self):
        """returns random subnetmask in dotted decimal format"""
        maskValue = (128,192,224,240,248,252,254)
        randBit = random.randint(1,32)
        newMask = []
        if randBit == 32: return "255.255.255.255"
        div = int (randBit / 8)
        mod = randBit % 8
        newMask = [255] * div
        if mod != 0: 
            newMask.append(maskValue[mod-1]) 
        for n in range(0, 4 - len(newMask)):
                newMask.append(0)   
        return ".".join(str(i) for i in newMask)
    
    #Methods:
    def randip(self, n=1):
        """returns num numbers of random IPv4"""
        ips = []
        for i in range(0,n):
            ips.append(self.getRandomIp())
        return ips    

    def randmask(self, n=1, mode="p"):
        """returns n numbers of random masks \n
        mode: "p": prefix | "d": dotted
        """
        masks = []
        if mode == "p":
            for i in range(0,n):
                masks.append(self.getRandomPMask())
        elif mode == "d":
            for i in range(0,n):
                masks.append(self.getRandomDMask())
        else:
            raise Exception("Enter a valid mode parameter")
        return masks
            
    def randipmask(self, n=1, mask="p"):
        """returns n numbers of IPv4 + mask \n
        mask= "p": prefix | "d": dotted        
         """
        randomMask = ""
        randomIpMask = []
        for i in range(0,n):
            if mask == "p":
                randomMask = self.getRandomPMask()
            elif mask == "d":
                randomMask = self.getRandomDMask()
            else:
                raise Exception("Enter a valid mask parameter")
            randomIpMask.append(self.getRandomIp() + " " + randomMask)           
        return randomIpMask
        
