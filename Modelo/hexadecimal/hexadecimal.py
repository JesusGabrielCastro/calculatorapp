class Hexadecimal:
    numero = 0
    def __init__(self,numero) -> None:
        self.numero= numero

    def getBinario(self):
        decimal = int(self.numero, 16)
        binario = bin(decimal).replace("0b", "")
        return binario
    
    def getDecimal(self):
        decimal = int(self.numero, 16)
        return decimal
    
    def getOctal(self):
        decimal = int(self.numero, 16)
        octal = oct(decimal).replace("0o", "")
        return octal
    
    def getHexadecimal(self):
        return self.numero
    
    def getAllConversion(self, ):
        return [self.getBinario(), self.getDecimal(),  self.getHexadecimal(),self.getOctal()]