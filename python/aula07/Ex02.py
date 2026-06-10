#Criar uma aplicação em Python em que se pede o nome do país e se
#tem como respost a capital do referido país.
#API: https://restcountries.com

import requests

url = "https://restcountries.com"
resposta = requests.get(url)

pais = input("Digite o nome do pais! ")

if resposta.status_code == 200:
    
    #converter a resposta para formato JSON e armazenar na variável dados
    dados = resposta.json()
    #Percorrer a lista de países obtida da API e verificar se o nome do país corresponde ao país digitado pelo usuário
    for pais in dados:
        if pais["name"] == pais:
            print(pais["capital"])
        else:
            print("Pais não encontrado.")
