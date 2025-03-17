import json
from urllib import request

def buscar_dados_api(url):
    with request.urlopen(url) as resposta:
        dados = resposta.read().decode('utf-8')
        return json.loads(dados)


url = "https://randomuser.me/api/"
resultado = buscar_dados_api(url)

print(resultado)