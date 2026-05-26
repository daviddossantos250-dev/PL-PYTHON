
import math

def bhaskara(a=None, b=None, c=None):
    if a is None or b is None or c is None:
        print("Parâmetros a, b e c são necessários.")
        return

    if a == 0:
        print("O coeficiente 'a' não pode ser zero.")
        return

    delta = b**2 - 4 * a * c

    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui duas raízes reais:", raiz1, "e", raiz2)
    elif delta == 0:
        raiz = -b / (2 * a)
        print("A equação possui uma raiz real:", raiz)
    else:
        print("A equação não possui raízes reais.")


#teste
bhaskara(1, -3, 2)  # Raízes reais: 2 e 1
bhaskara(1, -2, 1)  # Raiz real única: 1
bhaskara(1, 0, 1)   # Sem raízes reais