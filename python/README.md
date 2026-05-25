# Explicações sobre Loops em Python

Este documento contém as explicações detalhadas sobre o código `Ex07.py` e conceitos relacionados a loops em Python, baseadas na conversa que tivemos.

## Código Ex07.py - Somatório de N Primeiros Números

```python
#SOMATORIO DE N-PRIMEIROS NUMEROS
#NUMERO FORNECIDO PELO USUÁRIO
print("---SOMATORIO DE N-PRIMEIROS NUMEROS---")
n = int(input("Digite um número: "))
soma = 0
for i in range(1, n+1): #range(1, n+1) gera uma sequência de números de 1 a n
    soma += i #soma = soma + i
print("Soma dos primeiros", n, "números: ", soma)
```

## Como Funciona o `for` Loop

O `for` é um loop que passa por cada item de uma sequência. No caso:

```python
for i in range(1, n+1):
    soma += i
```

### Exemplo com n = 5

| Iteração | Valor de i | soma antes | soma += i | soma depois |
|----------|-----------|-----------|-----------|-------------|
| 1 | 1 | 0 | 0 + 1 | 1 |
| 2 | 2 | 1 | 1 + 2 | 3 |
| 3 | 3 | 3 | 3 + 3 | 6 |
| 4 | 4 | 6 | 6 + 4 | 10 |
| 5 | 5 | 10 | 10 + 5 | **15** |

**Resultado: 1 + 2 + 3 + 4 + 5 = 15**

### Os 3 Componentes do `for`:

- **`for`** = "repita para"
- **`i in range(1, n+1)`** = "cada número de 1 até n"
- **`soma += i`** = "some esse número ao total"

## O que é `range(1, n+1)`?

`range` é uma função que gera uma sequência de números.

```python
range(1, n+1)
```

Significa: **"gera números começando em 1 até n (inclusive)"**

### Exemplos:

**Se n = 5:**
```python
range(1, 6)  # Gera: 1, 2, 3, 4, 5
```

**Se n = 10:**
```python
range(1, 11)  # Gera: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

### Os 2 números do `range`:

- **1º número (1)** = onde começa
- **2º número (n+1)** = onde termina (**mas NÃO inclui esse número!**)

Por isso usamos `n+1`: queremos ir até `n`, mas `range` não inclui o último número.

### Analogia:

É como um ônibus que vai da parada 1 até a parada 5:
- `range(1, 5)` = ônibus vai de 1 até 4 ❌
- `range(1, 6)` = ônibus vai de 1 até 5 ✓

## Ordem de Entendimento

1. **`range`** = entenda que cria uma lista de números
2. **`for`** = entenda que pega cada número dessa lista
3. **O corpo do `for`** = entenda o que fazer com cada número

## Tipos de `for`

Nem todo `for` usa `range`:

```python
# Tipo 1: com range
for i in range(1, 6):
    print(i)

# Tipo 2: com uma lista
lista = [10, 20, 30]
for numero in lista:
    print(numero)

# Tipo 3: com uma string
for letra in "HELLO":
    print(letra)
```

**Padrão geral:**
```python
for VARIAVEL in SEQUÊNCIA:
    # o que fazer com cada item
```

## `for` vs `while`

### `for`:
- Você **sabe quantas voltas vai dar**
- Usa `range` ou uma lista
- Automático

### `while`:
- Você **NÃO sabe quantas voltas vai dar**
- Você coloca uma **condição**
- Repete enquanto a condição for verdadeira

### Exemplo com números (1 a 5):

**COM `for`:**
```python
for i in range(1, 6):
    print(i)
```

**COM `while`:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### Como funciona o `while`:

```python
i = 1              # começa em 1
while i <= 5:      # ENQUANTO i for menor ou igual a 5:
    print(i)       #   imprima i
    i += 1         #   aumente i em 1
```

**Passo a passo:**
```
i=1, é ≤5? SIM  → imprima 1, i vira 2
i=2, é ≤5? SIM  → imprima 2, i vira 3
i=3, é ≤5? SIM  → imprima 3, i vira 4
i=4, é ≤5? SIM  → imprima 4, i vira 5
i=5, é ≤5? SIM  → imprima 5, i vira 6
i=6, é ≤5? NÃO  → PARA!
```

### Resumo:
- **`for`** = "repita X vezes"
- **`while`** = "repita enquanto isso for verdadeiro"