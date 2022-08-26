import pandas as pd
from c_apaga import c_apaga

#exclui linhas do arquivo xlsx
def apaga():
    c_apaga()
    planilha = pd.read_excel('estoque.xlsx')
    endereco = input('Digite o numero da linha a ser apagada: ')
    endereco = int(endereco)
    planilha.drop(endereco, axis=0, inplace=True, errors='ignore')
    planilha.to_excel('estoque.xlsx', index=False)
    print('\nProduto deletado com sucesso\n')    
    