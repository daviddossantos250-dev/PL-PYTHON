import requests

resposta = requests.get("https://api.chucknorris.io/jokes/random")
if resposta.status_code == 200:
    dados = resposta.json()
    print("Dados obtidos da API:")
    print(dados ["value"])