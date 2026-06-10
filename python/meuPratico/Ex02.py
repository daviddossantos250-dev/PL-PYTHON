
#Exercício 1: Pede ao utilizador dois números e mostra: soma, subtração, #multiplicação, divisão, divisão inteira, resto e potência.
#Exercício 2: Pede uma idade ao utilizador. Usando operadores de comparação e #lógicos, mostra True ou False para:

#A pessoa tem 18 ou mais anos?
#A pessoa tem entre 18 e 65 anos?

#Exercício 3: Pede um número ao utilizador. Mostra se é par ou ímpar usando o #operador %.



numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

soma = numero1 + numero2
print(f"A soma dos números é: {soma}")  
subtraçao = numero1 - numero2
print(f"A subtração dos números é: {subtraçao}")
multiplicacao = numero1 * numero2
print(f"A multiplicação dos números é: {multiplicacao}")
divisao = numero1 // numero2
print(f"A divisão dos números é: {divisao}")
resto = numero1 % numero2
print(f"O resto da divisão dos números é: {resto}")
potencia = numero1 ** numero2
print(f"A potência dos números é: {potencia}")



idade = int(input("Digite sua idade: "))

print("Tem 18 ou mais anos:", idade >= 18)
print("Tem entre 18 e 65 anos:", idade >= 18 and idade <= 65)



numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:    
    print(f"O número {numero} é ímpar.")