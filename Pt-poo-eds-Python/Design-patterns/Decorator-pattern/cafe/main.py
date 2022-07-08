from cafe import Cafe, Latte, Frappucino
from decoradores import Leche, CremaBatida

def ver_detalle(cafe: Cafe)-> None:
    print( f"{cafe.get_descripcion()} cuesta {cafe.calcular_costo()}" )

if __name__ == "__main__":
    cafe01 = Frappucino()
    cafe01 = CremaBatida( cafe01 )
    # cafe01 = Leche(CremaBatida( cafe01 ))
    ver_detalle(cafe01)
    
# Frappucino cuesta 1.99
# **Pasando el decorador:
# Café: Frappucino, con crema batida. cuesta 2.99
# Café: Frappucino, con crema batida., con leche. cuesta 3.8400000000000003