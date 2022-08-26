import pandas as pd
import os

def consulta():
    while True:
        planilha = pd.read_excel('estoque.xlsx')
        consulta = input('Digite o código do produto ou "0" para voltar: ')
        print()
        if consulta == '0':
            os.system('cls')
            break
        else:
            try:
                os.system('cls')
                consulta = int(consulta)
                retorno = planilha.loc[planilha['REF'] == consulta]
                print(retorno)
                print()
                print()
            except:
                print('Digite um código de produto válido!')
        