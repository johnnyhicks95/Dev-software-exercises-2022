from abc import ABC, abstractclassmethod, abstractmethod

class Cafe( ABC):
    """decordador: Superclase, puede cambiar de caracteristicas  """
    def __init__(self) -> None:
        # super().__init__()
        self._descripcion = "Café normal"
        
    def set_descripcion(self, valor: str):
        self._descripcion = valor
        
    def get_decripcion(self):
        return self._descripcion
    
    @abstractmethod
    def calcular_costo(self) -> float:
        raise NotImplementedError
    
# Classes que van a componer de cafe
class Frappucino(Cafe):
    def __init__(self) :
        self._descripcion = "Café: Frappucino"

    def calcular_costo(self) -> float:
        return 1.99

class Latte(Cafe):
    def __init__(self) :
        self._descripcion = "Café: Latte"

    def calcular_costo(self) -> float:
        return 1.55
    
    
    