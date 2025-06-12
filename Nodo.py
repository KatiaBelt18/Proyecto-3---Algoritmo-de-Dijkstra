'Clase nodo'
class Nodo:
    def __init__(self,n):
        self.identificador = n      #Crear nodos
        self.atributos = {}         #Diccionario para atributos 
    
    def __hash__(self):
        return hash(self.identificador)

    def __eq__(self, other):
        return self.identificador == other.identificador