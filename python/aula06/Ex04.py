#INSTALAR A BIBLIOTECA REQUESTS NO TERMINAL: py -m pip install requests
import json  #importar a biblioteca json para trabalhar com arquivos JSON
import requests  #importar a biblioteca requests para fazer requisições HTTP

url = "https://api.chucknorris.io/jokes/random"  #URL da API para obter os dados de uma piada aleatória do Chuck Norris
response = requests.get(url)  #fazer uma requisição GET para a URL e armazenar a resposta na variável response
if response.status_code == 200:  #verificar se a requisição foi bem-sucedida (status code 200)
    dados = response.json()  #converter a resposta para formato JSON e armazenar na variável dados
    print("Dados obtidos da API:")  #imprimir mensagem indicando que os dados foram obtidos
    print(json.dumps(dados, indent=2))  #imprimir os dados obtidos da API formatados com indentação de 2 espaços
else:
    print("Erro ao obter dados da API.")