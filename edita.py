import pandas as pd
from openpyxl import Workbook, load_workbook
import os
os.system("cls")


def edita():
    print()
    while True:

        #Panda
        planilha = pd.read_excel('estoque.xlsx')
        #Openpyxl
        planilhap = load_workbook('estoque.xlsx') 
        aba_ativa = planilhap.active    

        item = input('\nDigite o codigo do item a ser editado ou "0" para voltar: ')
        os.system("cls")
        if item == '0':
            break
        if item.isnumeric():
            item = int(item)      
            item_pesquisa = planilha.loc[planilha['REF'] == item]
            print(item_pesquisa)
            print('\nSelecione a opção que deseja editar:\n ')
            print('Estoque Tamanhos  = 1 \nPreço Produtos    = 2\nDescrição Produto = 3\nVoltar            = 0\n')
            opcao = input('Digite sua Opção: ')
            os.system("cls")
            if opcao == '1':  #ESTOQUE TAMANHOS 
                print(f'{item_pesquisa}')
                while True:
                    print('\nSelecione a Opção de Tamanho que deseja alterar no Estoque!\n')
                    print('P     = 1\nM     = 2\nG     = 3\nGG    = 4\nVoltar = 0\n')
                    tamanho = input('Digite sua Opção: ')
                    os.system("cls")
                    if tamanho == '1':  #TAMANHO P
                        print('Qual "COR" Deseja Alterar\n')
                        print(item_pesquisa)
                        cor = input('\nDigite o nome da "COR" a ser alterada: ')
                        cor = cor.upper()
                        if cor.isnumeric():
                            os.system('cls')
                            print('**Digite somente Letras na "COR"!**')
                            print(f'\n{item_pesquisa}')
                        else:
                            estoque_p = input('\nDigite um valor para o Estoque Tamanho P: ')
                            if estoque_p.isnumeric():
                                os.system("cls")
                                #Seleção de celula expecifica P
                                for celula in aba_ativa['C']:
                                    if celula.value == cor:
                                        linha = celula.row
                                        for ref in aba_ativa['A']:
                                            linha_item = ref.row
                                            if ref.value == item and linha_item == linha:
                                                temp_item = item
                                                item = 0
                                                aba_ativa[f'D{linha}'] = estoque_p
                                                planilhap.save("estoque.xlsx")
                                                planilha_temp =pd.read_excel('estoque.xlsx')
                                print('**MUDANÇA REALIZADA**')
                                item = temp_item
                                temp_item = 0
                                item_pesquisa = planilha_temp.loc[planilha_temp['REF'] == item]
                                print(f'\n{item_pesquisa}')
                            else:
                                os.system('cls')
                                print('**Digite somente Números para valor de estoque!**')
                                print(f'\n{item_pesquisa}')
                    elif tamanho == '2':  #TAMANHO M
                        print('Qual "COR" Deseja Alterar\n')
                        print(item_pesquisa)
                        cor = input('\nDigite o nome da "COR" a ser alterada: ')
                        cor = cor.upper()
                        if cor.isnumeric():
                            os.system('cls')
                            print('**Digite somente Letras na "COR"!**')
                            print(f'\n{item_pesquisa}')
                        else:
                            estoque_M = input('\nDigite um valor para o Estoque Tamanho M: ')
                            if estoque_M.isnumeric():
                                os.system("cls")
                                #Seleção de celula expecifica M
                                for celula in aba_ativa['C']:
                                    if celula.value == cor:
                                        linha = celula.row
                                        for ref in aba_ativa['A']:
                                            linha_item = ref.row
                                            if ref.value == item and linha_item == linha:
                                                temp_item = item
                                                item = 0
                                                aba_ativa[f'E{linha}'] = estoque_M
                                                planilhap.save("estoque.xlsx")
                                                planilha_temp =pd.read_excel('estoque.xlsx')
                                print('**MUDANÇA REALIZADA**')
                                item = temp_item
                                item_pesquisa = planilha_temp.loc[planilha_temp['REF'] == item]
                                print(f'\n{item_pesquisa}')
                            else:
                                os.system('cls')
                                print('**Digite somente Números para valor de estoque!**')
                                print(f'\n{item_pesquisa}')
                    elif tamanho == '3':  #TAMANHO G
                        print('Qual "COR" Deseja Alterar\n')
                        print(item_pesquisa)
                        cor = input('\nDigite o nome da "COR" a ser alterada: ')
                        cor = cor.upper()
                        if cor.isnumeric():
                            os.system('cls')
                            print('**Digite somente Letras na "COR"!**')
                            print(f'\n{item_pesquisa}')
                        else:
                            estoque_G = input('\nDigite um valor para o Estoque Tamanho G: ')
                            if estoque_G.isnumeric():
                                os.system("cls")
                                #Seleção de celula expecifica G
                                for celula in aba_ativa['C']:
                                    if celula.value == cor:
                                        linha = celula.row
                                        for ref in aba_ativa['A']:
                                            linha_item = ref.row
                                            if ref.value == item and linha_item == linha:
                                                temp_item = item
                                                item = 0
                                                aba_ativa[f'F{linha}'] = estoque_G
                                                planilhap.save("estoque.xlsx")
                                                planilha_temp =pd.read_excel('estoque.xlsx')
                                print('**MUDANÇA REALIZADA**')
                                item = temp_item
                                item_pesquisa = planilha_temp.loc[planilha_temp['REF'] == item]
                                print(f'\n{item_pesquisa}')
                            else:
                                os.system('cls')
                                print('**Digite somente Números para valor de estoque!**')
                                print(f'\n{item_pesquisa}')
                    elif tamanho == '4':  #TAMANHO GG
                        print('Qual "COR" Deseja Alterar\n')
                        print(item_pesquisa)
                        cor = input('\nDigite o nome da "COR" a ser alterada: ')
                        cor = cor.upper()
                        if cor.isnumeric():
                            os.system('cls')
                            print('**Digite somente Letras na "COR"!**')
                            print(f'\n{item_pesquisa}')
                        else:
                            estoque_GG = input('\nDigite um valor para o Estoque Tamanho GG: ')
                            if estoque_GG.isnumeric():
                                os.system("cls")
                                #Seleção de celula expecifica GG
                                for celula in aba_ativa['C']:
                                    if celula.value == cor:
                                        linha = celula.row
                                        for ref in aba_ativa['A']:
                                            linha_item = ref.row
                                            if ref.value == item and linha_item == linha:
                                                temp_item = item
                                                item = 0
                                                aba_ativa[f'G{linha}'] = estoque_GG
                                                planilhap.save("estoque.xlsx")
                                                planilha_temp =pd.read_excel('estoque.xlsx')
                                print('**MUDANÇA REALIZADA**')
                                item = temp_item
                                item_pesquisa = planilha_temp.loc[planilha_temp['REF'] == item]
                                print(f'\n{item_pesquisa}')
                            else:
                                os.system('cls')
                                print('**Digite somente Números para valor de estoque!**')
                                print(f'\n{item_pesquisa}')
                    elif tamanho == '0':  #VOLTAR
                        break
                    else:
                        print('\nOpção Invalida!\n')
            elif opcao == '2':  #PREÇO
                preco = input('Digite o novo valor do produto: ')
                if preco.isnumeric():
                    preco = str(f'R$ '+ f'{preco},00')
                preco = str(f'R$ '+ f'{preco}')
                planilha.loc[planilha['REF'] == item, 'PREÇO'] = preco
                planilha.to_excel("estoque.xlsx", index = False)
                item_pesquisa = planilha.loc[planilha['REF'] == item]
                print(item_pesquisa)
            elif opcao == '3':  #DESCRIÇÂO PRODUTO
                print(item_pesquisa)
                descricao = input('\nDigite a nova Descrição do Produto: ')
                if descricao.isnumeric():
                    print('**Digite somente Letras na descrição**')
                else:
                    descricao = descricao.upper()
                    planilha.loc[planilha['REF'] == item, 'DESCRIÇÃO'] = descricao
                    planilha.to_excel("estoque.xlsx", index = False)
                    item_pesquisa = planilha.loc[planilha['REF'] == item]
                    os.system("cls")
                    print('MUDANÇA REALIZADA\n')
                    print(item_pesquisa)
            elif opcao == '0':  #VOLTAR 
                break
            else:
                print('Opção Invalida')
        elif item == 0:
            break
        else:
            print('Digite um código de produto válido!\n')
