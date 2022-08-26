import pandas as pd

def consulta_geral():
    planilha = pd.read_excel('estoque.xlsx')
    print(planilha)
    