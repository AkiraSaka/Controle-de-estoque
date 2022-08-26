from consulta import consulta
from cadastro import cadastro
from consulta_geral import consulta_geral
from edita import edita
from apaga import apaga
import os

while True:
        print('\n1 para CONSULTA DE ESTOQUE')
        print('2 para CONSULTA GERAL')
        print('3 para CADASTRAR PRODUTO')
        print('4 para EDITAR PRODUTO')
        print('5 para REMOVER PRODUTO')
        acao = input('\nDigite ação a ser executada: ')
        if acao == '1':
            os.system("cls")
            consulta()        
        elif acao == '2':
            os.system("cls")
            consulta_geral()
        elif acao == '3':
            os.system("cls")
            cadastro()           
        elif acao == '4':
            os.system("cls")
            edita()
        elif acao == '5':
            os.system("cls")
            apaga()
        else:
            os.system("cls")
            print('**Opção Invalida**')
            