#pedindo dois numeros e comparando-os

num1 = int(input("num1: ")) #int() converte o valor introduzido para inteiro, caso contrario seria string
num2 = int(input("num2: ")) #int() converte o valor introduzido para inteiro, caso contrario seria string

#if num1 > num2:
#    print("maior: ", num1)
#else:
#    if num1 == num2:
#        print("sao iguais")
#    else:
#        print("maior: ", num2)
#print("fim condicao")

#condicao if-elif-else
if num1 > num2: 
    print("maior: ", num1)
elif num1 == num2:
     print("sao iguais")
else:
    print("maior: ", num2)