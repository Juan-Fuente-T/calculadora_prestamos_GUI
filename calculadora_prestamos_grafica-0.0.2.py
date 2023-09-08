# *** Calculadora de prestamos  :: Version 0.0.3 ***

# ©2023 Calculadora financiera de Juan Fuente

"""
Esta aplicación multiplataforma (Windows, Linux, Mac) ofrece una calculadora de prestamos utilizando el interes frances que opera mediante interfaz gráfica


Novedades de la versión 0.0.2
- Se añaden mensajes de error en caso de introducir valores incorrectos
- Se borra la pantalla del valor que se ha introducido si se introduce un valor incorrecto
- Se borran las pantallas de resultados si se introduce un valor incorrecto
- Se colocan en su lugar todas las ventanas y pantallas de resultados
- Se añaden todos los colores de la aplicación
- Se añade el icono


"""


import tkinter as tk
from tkinter import messagebox  #se importa messagebox para mostrar mensaje de error
from tkinter import ttk #ttk es necesario para los desplegables combobox 


class calculadora_prestamos(tk.Tk): 

    def __init__(self): 
        super().__init__()

        self.title("Calculadora de préstamos") #titulo de la aplicacion
        self.iconbitmap("calculadora_prestamo.ico") #icono de la aplicacion
        self.geometry("550x700+100+100") #tamaño de la aplicacion
        self.configure(bg="#FFDDB0") #color de fondo de la aplicacion

        self.pantalla_cuota_anual = tk.Entry(self, width=10, justify="right", borderwidth=2, fg="#191007", bg="#CFB38F") #se define la pantalla donde se va a mostrar el resultado 
        self.pantalla_cuota_mensual = tk.Entry(self, width=10, justify="right", borderwidth=2, fg="#191007", bg="#CFB38F") #se define la pantalla donde se va a mostrar el resultado 
        
        self.duracion_prestamo = tk.Entry(self, width=12, justify="right", borderwidth=2, fg="#191007", bg="#CFB38F") #se define la ventana donde se van a introducir la cantidad de moneda
        self.capital = tk.Entry(self, width=12, justify="right", borderwidth=2, fg="#191007", bg="#CFB38F")#se define el desplegable para moneda origen
        #self.interes = tk.Entry(self, width=15, justify="right", borderwidth=2, fg="navy", bg="LightSteelBlue1")#se define el desplegable para moneda origen
        self.interes = tk.Entry(self, width=12, justify="right", borderwidth=2, fg="#191007", bg="#CFB38F")#se define el desplegable para la moneda destino
        
        self.calcular_button = tk.Button(self, text="Calcular", fg="bisque", bg="#82715A", padx=40, pady=4, command=self.mostrar_cuota) #se define el boton para realizar la conversion


        self.pantalla_cuota_anual.place(x=430, y=100, anchor="center") #se define la colocacion de la patalla de resultados
        self.pantalla_cuota_mensual.place(x=430, y=200, anchor="center") #se define la colocacion de la patalla de resultados
        
        self.duracion_prestamo.place(x=130, y=270, anchor="center")#se define la colocacion de la ventana de cantidad de  moneda 
        self.capital.place(x=130, y=70, anchor="center")#se define la colocacion de la ventana de moneda origen
        self.interes.place(x=130, y=170, anchor="center")#se define la colocacion de la ventana de moneda destino
        
        self.calcular_button.place(x=430, y=350, anchor="center")#se define la colocacion del boton de convertir
        

        self.pantalla_cuota_anual.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.pantalla_cuota_mensual.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.duracion_prestamo.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.calcular_button.configure(font=("Arial", 14))#se configura el tipo de letra y tamaño del boton de convertir
        self.capital.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 
        self.interes.configure(font=("Arial Black", 18))#se configura el tipo de letra y tamaño de la ventana de cantidad de  moneda 


        etiqueta_cuota_anual= tk.Label(self, text="Cuota anual:", fg="#191007",bg="#FFC06E", font=("Arial", 13))#se define la etiqueta de la pantalla de resultados
        etiqueta_cuota_anual.place(x=430, y=50, anchor="center")#se define la colocacion de la etiqueta de la pantalla de resultado
        etiqueta_cuota_mensual= tk.Label(self, text="Cuota mensual:", fg="#191007",bg="#FFC06E", font=("Arial", 13))#se define la etiqueta de la pantalla de resultados
        etiqueta_cuota_mensual.place(x=430, y=150, anchor="center")#se define la colocacion de la etiqueta de la pantalla de resultado
        

        duracion_prestamo_label = tk.Label(self, text="Plazo en años:", fg="#191007",bg="#82715A", font=("Arial", 13) )#se define la etiqueta de cantidad de  moneda 
        duracion_prestamo_label.place(x=130, y=230, anchor="center")#se define la colocacion de la etiqueta de cantidad moneda 
        

        capital_label = tk.Label(self, text="Capital:", fg="#191007",bg="#82715A", font=("Arial", 13))#se define la etiqueta de moneda origen
        capital_label.place(x=130, y=30, anchor="center")#se define la colocacion de la etiqueta de moneda origen

        interes_label = tk.Label(self, text="Interés:", fg="#191007",bg="#82715A", font=("Arial", 13))#se define la etiqueta de moneda destino
        interes_label.place(x=130, y=130, anchor="center") #se define la colocacion de la etiqueta de moneda destino
        calcular_button_label = tk.Label(self, text=""" 
    Calculadora de préstamos
                    
Introduzca la cantidad de capital, el interés a aplicar 
y el número de años para su amortización 
Con el botón Calcular obtendrá la cuota mensual 
              y la cuota anual resultantes.                                   

        CC-BY-NC 2023 Juan Fuente         
                        """, fg="#191007", bg="#82715A", font=("Arial", 13),)
        calcular_button_label.place(x=275, y=520, anchor="center", width= 500) #se define la colocacion de la etiqueta bajo el boton de convertir
        

        

    def calcular_cuota(self):
        #cantidad = self.duracion_prestamo.get()
        capital = self.capital.get()
        interes = self.interes.get()
        duracion_prestamo = self.duracion_prestamo.get()

        if not capital.replace('.', '', 1).isdigit():
            self.capital.delete(0, tk.END)
            self.pantalla_cuota_mensual.delete(0, tk.END)
            self.pantalla_cuota_anual.delete(0, tk.END)
            messagebox.showerror("Error", "El valor del capital no es válido")
            return
        if not interes.replace('.', '', 1).isdigit():
            self.interes.delete(0, tk.END)
            self.pantalla_cuota_mensual.delete(0, tk.END)
            self.pantalla_cuota_anual.delete(0, tk.END)
            messagebox.showerror("Error", "El valor del interés no es válido")
            return
        #if not 1 <= float(duracion_prestamo) <= 35 or not duracion_prestamo.isdigit():
        if not duracion_prestamo.isdigit():

            self.duracion_prestamo.delete(0, tk.END)
            self.pantalla_cuota_mensual.delete(0, tk.END)
            self.pantalla_cuota_anual.delete(0, tk.END)
            messagebox.showerror("Error", "El valor de la duración del préstamo no es válido")
            return
        
        duracion_meses = float(duracion_prestamo) * 12
        capital, interes, duracion_prestamo = float(capital), float(interes), float(duracion_prestamo)
        cuota_anual = round(((capital * interes / 100) / (1 - (1 + interes / 100) ** -duracion_prestamo)), 2)
        cuota_mensual = round(((capital * interes / 1200) / (1 - (1 + interes / 1200) ** -duracion_meses)), 2)
        return cuota_anual, cuota_mensual
        """except ValueError:
            
            return None, None"""

        
        """ if not nombre_moneda_origen or not nombre_moneda_destino:
            if event is None or (event.widget == self.calcular_button if event else False):
                tk.messagebox.showerror("Error", "Por favor, seleccione la moneda de origen y la moneda de destino.")
                return
"""

    def mostrar_cuota(self):  # New function to handle the calculation and display
        cuota_anual,cuota_mensual = self.calcular_cuota()
        
    
        self.pantalla_cuota_anual.delete(0, tk.END)
        self.pantalla_cuota_anual.insert(tk.END, cuota_anual)

        self.pantalla_cuota_mensual.delete(0, tk.END)
        self.pantalla_cuota_mensual.insert(tk.END, cuota_mensual)
        

if __name__ == "__main__":
    ventana = calculadora_prestamos()
    ventana.mainloop()