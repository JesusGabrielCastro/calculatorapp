import tkinter as tk
from Modelo.binario.binario import Binario as binario
from Modelo.decimal.decimal import Decimal as decimal
from Modelo.hexadecimal.hexadecimal import Hexadecimal as hexadecimal
from Modelo.octal.octal import Octal as octal



class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Números")

        # entrada de datos
        self.dato_label = tk.Label(root, text="Introduce un número:")
        self.dato_label.grid(row=0, column=0)

        self.dato_entry = tk.Entry(root)
        self.dato_entry.grid(row=0, column=1)

        # botones para seleccion del tipo de origen (binario, octal, hexadecimal, decimal)
        self.boton_binario = tk.Button(root, text="Binario", command=lambda: self.convertir('binario'))
        self.boton_binario.grid(row=1, column=0)

        self.boton_octal = tk.Button(root, text="Octal", command=lambda: self.convertir('octal'))
        self.boton_octal.grid(row=1, column=1)

        self.boton_hexadecimal = tk.Button(root, text="Hexadecimal", command=lambda: self.convertir('hexadecimal'))
        self.boton_hexadecimal.grid(row=1, column=2)

        self.boton_decimal = tk.Button(root, text="Decimal", command=lambda: self.convertir('decimal'))
        self.boton_decimal.grid(row=1, column=3)

        #  mostrar los resultados de las conversiones
        self.resultado_binario = tk.Label(root, text="Binario:")
        self.resultado_binario.grid(row=2, column=0)

        self.resultado_octal = tk.Label(root, text="Octal:")
        self.resultado_octal.grid(row=2, column=1)

        self.resultado_hexadecimal = tk.Label(root, text="Hexadecimal:")
        self.resultado_hexadecimal.grid(row=2, column=2)

        self.resultado_decimal = tk.Label(root, text="Decimal:")
        self.resultado_decimal.grid(row=2, column=3)

    def convertir(self, tipo_origen):
        # Obtener el valor ingresado
        valor = self.dato_entry.get()

        # Realizar las conversiones y actualizar los resultados 
        if tipo_origen == 'binario':
            bn=binario(valor).getAllConversion()
            self.resultado_binario.config(text=f"Binario: {bn[0]}")
            self.resultado_octal.config(text=f"Octal: {bn[3]}")
            self.resultado_hexadecimal.config(text=f"Hexadecimal: {bn[2]}")
            self.resultado_decimal.config(text=f"Decimal: {bn[1]}")
        elif tipo_origen == 'octal':
            bn=octal(valor).getAllConversion()
            self.resultado_binario.config(text=f"Binario: {bn[0]}")
            self.resultado_octal.config(text=f"Octal: {bn[3]}")
            self.resultado_hexadecimal.config(text=f"Hexadecimal: {bn[2]}")
            self.resultado_decimal.config(text=f"Decimal: {bn[1]}")
        elif tipo_origen == 'hexadecimal':
            bn=hexadecimal(valor).getAllConversion()
            self.resultado_binario.config(text=f"Binario: {bn[0]}")
            self.resultado_octal.config(text=f"Octal: {bn[3]}")
            self.resultado_hexadecimal.config(text=f"Hexadecimal: {bn[2]}")
            self.resultado_decimal.config(text=f"Decimal: {bn[1]}")
        elif tipo_origen == 'decimal':
            bn=decimal(valor).getAllConversion()
            self.resultado_binario.config(text=f"Binario: {bn[0]}")
            self.resultado_octal.config(text=f"Octal: {bn[3]}")
            self.resultado_hexadecimal.config(text=f"Hexadecimal: {bn[2]}")
            self.resultado_decimal.config(text=f"Decimal: {bn[1]}")

# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
