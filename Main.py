import customtkinter as ctk
from DataBase import Database
from Bicicletas import GestionBicicletas
import customtkinter as ctk

class Bienvenida:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Sistema de gestión de bicicletas")
        self.ventana.geometry("400x250")
        self.configurar_interfaz()

    def configurar_interfaz(self):
        etiqueta = ctk.CTkLabel(self.ventana, text="Bienvenido al sistema de gestión de bicicletas", font=("Arial", 14))
        etiqueta.pack(pady=20)

        etiqueta_tema = ctk.CTkLabel(self.ventana, text="Seleccione un tema:", font=("Arial", 12))
        etiqueta_tema.pack(pady=10)

        self.seleccion_tema = ctk.CTkOptionMenu(self.ventana, values=["Oscuro", "Claro"], command=self.seleccionar_tema)
        self.seleccion_tema.pack(pady=10)

        boton = ctk.CTkButton(self.ventana, text="Iniciar", command=self.iniciar_sistema)
        boton.pack(pady=20)

    def seleccionar_tema(self, tema):
        if tema == "Claro":
            ctk.set_appearance_mode("light")
        elif tema == "Oscuro":
            ctk.set_appearance_mode("dark")

    def iniciar_sistema(self):
        self.ventana.destroy()
        GestionBicicletas.menu_principal()

    def mostrar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    Database.inicializar_db()
    bienvenida = Bienvenida()
    bienvenida.mostrar()