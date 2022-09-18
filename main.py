import PySimpleGUI as sg
from cotaçaodemoedas import pegar_cotaçoes

layout = [
    [sg.Text('pegar cotaçao da moeda')],
    [sg.InputText(key='nome_cotaçao')],
    [sg.Button('pegar cotaçao'), sg.Button('cancelar')],
    [sg.Text("", key="texto_cotaçao")],

]

janela = sg.Window("sistema de cotaçoes", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "cancelar":
        break
    if evento == "pegar cotaçao":
       codigo_cotaçao = valores["nome_cotaçao"]
       cotaçao = pegar_cotaçoes(codigo_cotaçao)
       janela["texto_cotaçao"].update(f"A cotaçao do {codigo_cotaçao} é de R${cotaçao}")
janela.close()