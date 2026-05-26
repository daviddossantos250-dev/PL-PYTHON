#INSTALAR A BIBLIOTECA REQUESTS NO TERMINAL: py -m pip install requests

import requests  #importar a biblioteca requests para fazer requisições HTTP

url = "https://jsonplaceholder.typicode.com/users"  #URL da API para obter os dados dos usuários
response = requests.get(url)  #fazer uma requisição GET para a URL e armazenar a resposta na variável response
if response.status_code == 200:  #verificar se a requisição foi bem-sucedida (status code 200)
    dados = response.json()  #converter a resposta para formato JSON e armazenar na variável dados
    print("Dados obtidos da API:")  #imprimir mensagem indicando que os dados foram obtidos
    print(dados)  #imprimir os dados obtidos da API
else:
    print("Erro ao obter dados da API.")
