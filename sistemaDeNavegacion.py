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