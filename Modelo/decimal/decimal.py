class Decimal:
    def __init__(self, numero) -> None:
        self.decimal = numero

    def getBinario(self):
        binario = bin(int(self.decimal)).replace("0b", "")
        return binario
    
    def getHexadecimal(self):
        hexadecimal = hex(int(self.decimal)).replace("0x", "")
        return hexadecimal
    
    def getOctal(self):
        octal = oct(int(self.decimal)).replace("0o", "")
        return octal
    
    def getDecimal(self):
        return self.decimal
    
    def getAllConversion(self):
        return [self.getBinario(), self.getDecimal(), self.getHexadecimal(), self.getOctal()]

   