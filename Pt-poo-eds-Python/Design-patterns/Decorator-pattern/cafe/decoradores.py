from abc import abstractmethod
from cafe import Cafe

class Extra(Cafe):
    """Here we develop the decorator, the abstract function"""
    @abstractmethod
    def get_descripcion(self)-> str:
        raise NotImplementedError
    
    @abstractmethod
    def calcular_costo(self) -> float:
        raise NotImplementedError
    
class CremaBatida(Extra):
    """This are the instatiations from subclass 'Cafe' 
        Decorator class
    """
    def __init__(self, cafe: Cafe) ->None:
        """Save an original superclass'Cafe' instance"""
        self._cafe = cafe
    
    def get_descripcion(self) -> str:
        return f"{self._cafe.get_decripcion()}, con crema batida."

    def calcular_costo(self)-> float:
        return self._cafe.calcular_costo()+ 1.0
    
class Leche(Extra):
    """ Decorator class:
    This are the instatiations from subclass 'Cafe' """
    def __init__(self, cafe: Cafe) ->None:
        """Save an original superclass'Cafe' instance"""
        self._cafe = cafe
    
    def get_descripcion(self) -> str:
        return f"{self._cafe.get_descripcion()}, con leche."

    def calcular_costo(self)-> float:
        return self._cafe.calcular_costo()+ .85
    
