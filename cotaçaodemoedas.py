import requests

def pegar_cotaçoes(codigo_moeda):
    try:
        requisiçao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisiçao_dic = requisiçao.json()
        cotaçao = requisiçao_dic[f'{codigo_moeda}BRL']['bid']
        return cotaçao
    except:
         print('codigo de moeda invalido')
         return None