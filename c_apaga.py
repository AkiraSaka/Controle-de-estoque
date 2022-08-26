import pandas as pd

#consulta simples para aba de APAGA
def c_apaga():
    planilha = pd.read_excel('estoque.xlsx')
    consulta = input('Digite o código do produto: ')
    print()
    try:
        consulta = int(consulta)
        retorno = planilha.loc[planilha['REF'] == consulta]
        print(retorno)
        print()
        print()
    except:
        print('Digite um código de produto válido!')
