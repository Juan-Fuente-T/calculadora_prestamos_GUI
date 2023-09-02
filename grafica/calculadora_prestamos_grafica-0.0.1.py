import tkinter as tk
from tkinter import messagebox  #se importa messagebox para mostrar mensaje de error
from tkinter import ttk #ttk es necesario para los desplegables combobox 


class calculadora_prestamos(tk.Tk): 

    def __init__(self): 
        super().__init__()

        self.title("Calculadora de préstamos") #titulo de la aplicacion
        self.iconbitmap("conversor_divisas.ico") #icono de la aplicacion
        self.geometry("550x700+100+100") #tamaño de la aplicacion
        self.configure(bg="AntiqueWhite4") #color de fondo de la aplicacion

        self.pantalla_cuota_anual = tk.Entry(self, width=12, borderwidth=2, fg="navy", bg="LightSteelBlue1") #se define la pantalla donde se va a mostrar el resultado 
        self.pantalla_cuota_mensual = tk.Entry(self, width=12, borderwidth=2, fg="navy", bg="LightSteelBlue1") #se define la pantalla donde se va a mostrar el resultado 
        self.duracion_prestamo = tk.Entry(self, width=12, borderwidth=2, fg="navy", bg="LightSteelBlue1") #se define la ventana donde se van a introducir la cantidad de moneda
        
        self.capital = tk.Entry(self, width=12, borderwidth=2, fg="navy", bg="LightSteelBlue1")#se define el desplegable para moneda origen
        self.interes = tk.Entry(self, width=12, borderwidth=2, fg="navy", bg="LightSteelBlue1")#se define el desplegable para la moneda destino
        self.calcular_button = tk.Button(self, text="Calcular", fg="navy", bg="LightSteelBlue1", padx=40, pady=4, command=self.mostrar_cuota) #se define el boton para realizar la conversion

        self.pantalla_cuota_anual.place(x=480, y=120, anchor="center") #se define la colocacion de la patalla de resultados
        self.pantalla_cuota_mensual.place(x=480, y=180, anchor="center") #se define la colocacion de la patalla de resultados
        self.duracion_prestamo.place(x=120, y=180, anchor="center")#se define la colocacion de la ventana de cantidad de  moneda 
        self.capital.place(x=130, y=70, anchor="center")#se define la colocacion de la ventana de moneda origen
        self.interes.place(x=470, y=70, anchor="center")#se define la colocacion de la ventana de moneda destino
        self.calcular_button.place(x=300, y=265, anchor="center")#se define la colocacion del boton de convertir
        

        self.pantalla_cuota_anual.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.pantalla_cuota_mensual.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.duracion_prestamo.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.calcular_button.configure(font=("Arial", 14))#se configura el tipo de letra y tamaño del boton de convertir
        self.capital.configure(font=("Arial", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.interes.configure(font=("Arial", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 


        etiqueta_cuota_anual= tk.Label(self, text="Cuota anual:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13))#se define la etiqueta de la pantalla de resultados
        etiqueta_cuota_anual.place(x=480, y=120, anchor="center")#se define la colocacion de la etiqueta de la pantalla de resultado
        etiqueta_cuota_mensual= tk.Label(self, text="Cuota mensual:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13))#se define la etiqueta de la pantalla de resultados
        etiqueta_cuota_mensual.place(x=480, y=160, anchor="center")#se define la colocacion de la etiqueta de la pantalla de resultado
        

        duracion_prestamo_label = tk.Label(self, text="Plazo en años:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13) )#se define la etiqueta de cantidad de  moneda 
        duracion_prestamo_label.place(x=120, y=120, anchor="center")#se define la colocacion de la etiqueta de cantidad moneda 
        

        capital_label = tk.Label(self, text="Capital:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13))#se define la etiqueta de moneda origen
        capital_label.place(x=120, y=30, anchor="center")#se define la colocacion de la etiqueta de moneda origen

        interes_label = tk.Label(self, text="Interés:", fg="navy",bg="LightSteelBlue1", font=("Arial", 13))#se define la etiqueta de moneda destino
        interes_label.place(x=480, y=30, anchor="center") #se define la colocacion de la etiqueta de moneda destino
        calcular_button_label = tk.Label(self, text=""" 
Calculadora de préstamos
                    
Introduzca la cantidad de capital, el interés a aplicar 
y el número de años para su amortización 
y al pulsar el botón de calcular
obtendrá la cuota mensual y anual resultantes.                                   

        CC-BY-NC 2023 Juan Fuente         
                        """, fg="navy", bg="LightSteelBlue1", font=("Arial", 13))
        calcular_button_label.place(x=300, y=440, anchor="center") #se define la colocacion de la etiqueta bajo el boton de convertir
        

        

    def calcular_cuota(self):
        #cantidad = self.duracion_prestamo.get()
        capital = self.capital.get()
        interes = self.interes.get()
        duracion_prestamo = self.duracion_prestamo.get()
        duracion_meses = float(duracion_prestamo) * 12


        try:
            capital, interes, duracion_prestamo = float(capital), float(interes), float(duracion_prestamo)
        except ValueError:
            self.pantalla_cuota_anual.delete(0, tk.END)
            return
        cuota_anual = (capital * interes/100) / (1 - (1 + interes/100)** -duracion_prestamo)
        cuota_mensual = (capital * interes/1200) / (1 - (1 + interes/1200) ** -duracion_meses)
        return cuota_anual, cuota_mensual
        """#funcion para calcular la anualidad
        def calcular_anualidad(capital, interes, años): #toma tres argumentos y devueve el resultado
            return (capital * interes/100) / (1 - (1 + interes/100)** -años)
        #funcion para calcular la mensualidad
        def calcular_mensualidad(capital, interes, meses):#toma tres argumentos y devuelve el resultado
            return (capital * interes/1200) / (1 - (1 + interes/1200) ** -meses)"""

    def mostrar_cuota(self):  # New function to handle the calculation and display
        cuota_anual = self.calcular_cuota()
        cuota_mensual = self.calcular_cuota()
        
        self.pantalla_cuota_anual.delete(0, tk.END)
        self.pantalla_cuota_anual.insert(tk.END, cuota_anual)
    
        self.pantalla_cuota_mensual.delete(0, tk.END)
        self.pantalla_cuota_mensual.insert(tk.END, cuota_mensual)
    

if __name__ == "__main__":
    ventana = calculadora_prestamos()
    ventana.mainloop()