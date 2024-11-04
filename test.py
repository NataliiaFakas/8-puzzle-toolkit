from utils import descolocadas, secuencia

# Heurística Descolocadas

assert descolocadas("123804765") == 0  # no hay ninguna pieza descolocada

assert descolocadas("125804762") == 2  # no hay ninguna pieza descolocada
    
assert descolocadas("123840765") == 1  # hay una pieza descolocada

assert descolocadas("123456780") == 4  # hay cuatro piezas descolocadas

assert descolocadas("567048321") == 8  # todas las piezas están descolocadas

# Heurística Secuencias

assert secuencia("123804765") == 0    # Todas las secuencias son correctas  

assert secuencia("123084765") == 15   # Hay dos secuencias incorrectas y el centro

assert secuencia("132467850") == 51   # Todas las secuencias son incorrectas

assert secuencia("812703654") == 0    # Todas correctas, aunque no es el estado final

assert secuencia("283164705") == 33   # El ejemplo del boletín (3*S(n) = 3*11 = 33)

  