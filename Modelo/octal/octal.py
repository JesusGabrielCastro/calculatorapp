class Octal:
    def __init__(self,numero):
        self.octal = numero

    def get_octal(self):
        return self.octal

    def getBinario(self):
        decimal = int(self.octal, 8)
        binario = bin(decimal).replace("0b", "")
        return binario
    
    def getHexadecimal(self):
        decimal = int(self.octal, 8)
        hexadecimal = hex(decimal).replace("0x", "")
        return hexadecimal
    
    def getDecimal(self):
        decimal = str(int(self.octal, 8)).replace("0b", "")
        return decimal
    
    def getAllConversion(self):
        return [self.getBinario(), self.getDecimal(), self.getHexadecimal(), self.get_octal()]
