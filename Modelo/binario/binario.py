class Binario:
    numero = 0
    decimal=0
    def __init__(self,numero) -> None:
        self.numero = numero
        self.decimal= self.getDecimal()

    def getDecimal(self):
        decimal = 0
        for i in range(len(self.numero)):
            decimal += int(self.numero[i]) * 2**(len(self.numero) - i - 1)
        return decimal
    
    def getHexadecimal(self):
        decimal = self.decimal
        hexadecimal = hex(decimal).replace("0x", "")
        return hexadecimal
    
    def getOctal(self):
        decimal = self.decimal
        octal = oct(decimal).replace("0o", "")
        return octal
    
    def getnumero(self):
        return self.numero
    
    def getAllConversion(self):
        return [self.getnumero(),self.getDecimal(), self.getHexadecimal(), self.getOctal()]