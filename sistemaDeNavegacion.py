class HistorialNavegacion:
    def __init__(self):
        self.historialAtras = []  # Pila para páginas anteriores
        self.historialAdelante = []  # Pila para páginas siguientes

    def visitarPagina(self, url):
        """Agrega una nueva URL al historial."""
        self.historialAtras.append(url)
        self.historialAdelante.clear()
        print(f"visitado: {url}")

    def retrocederPagina(self):
        """Retrocede a la página anterior."""
        if len(self.historialAtras) <= 1:
            print("No hay páginas anteriores")
            return None
        
        # Obtiene la página actual y la mueve al historial hacia adelante
        paginaActual = self.historialAtras.pop()
        self.historialAdelante.append(paginaActual)
        
        # Retorna la nueva página actual
        print(f"Retrocediendo a: {self.historialAtras[-1]}")
        return self.historialAtras[-1]
    
    def avanzarPagina(self):
        """Avanza a la siguiente página."""
        if not self.historialAdelante:
            print("No hay páginas siguientes")
            return None
        
        # Obtiene la siguiente página y la mueve al historial hacia atrás
        siguientePagina = self.historialAdelante.pop()
        self.historialAtras.append(siguientePagina)
        print(f"Avanzando a: {siguientePagina}")
        return siguientePagina
    
    def mostrarHistorial(self):
        """Muestra el historial completo."""
        print("\n=== Historial de Navegación ===")
        if not self.historialAtras:
            print("El historial está vacío")
            return
        
        print("\nPáginas anteriores:")
        for i, url in enumerate(reversed(self.historialAtras)):
            print(f"{i + 1}. {url}")
        
        if self.historialAdelante:
            print("\nPáginas siguientes:")
            for i, url in enumerate(reversed(self.historialAdelante)):
                print(f"{i + 1}. {url}")

    def borrarHistorial(self):
        """Borra todo el historial."""
        self.historialAtras.clear()
        self.historialAdelante.clear()
        print("Historial borrado")

def menuPrincipal():
    historial = HistorialNavegacion()
    
    while True:
        print("\n=== MENÚ ===")
        print("1. Visitar nueva página")
        print("2. Retroceder página")
        print("3. Avanzar página")
        print("4. Mostrar historial")
        print("5. Borrar historial")
        print("6. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 1:
                url = input("Ingrese URL: ")
                historial.visitarPagina(url)
            elif opcion == 2:
                historial.retrocederPagina()
            elif opcion == 3:
                historial.avanzarPagina()
            elif opcion == 4:
                historial.mostrarHistorial()
            elif opcion == 5:
                historial.borrarHistorial()
            elif opcion == 6:
                print("¡Te extrañaremos :(!")
                break
            else:
                print("Opción no válida")
        except ValueError:
            print("Por favor, ingrese un número válido")

if __name__ == "__main__":
    menuPrincipal()
