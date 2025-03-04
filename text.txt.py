import requests
from bs4 import BeautifulSoup



URL_ITA = "https://openid.itau.com.br/services/oauth/"

def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print( resposta.text)
        else:
            print("Erro na Req")
    except Exception as error:
        print("Erro na Req")
        print(error)

def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, "html.parser")
        return soup
    except Exception as error:
        print("Erro no parsing")
        print(error)

resposta = buscar(URL_ITA)
if resposta:
    soup = parsing(resposta)






