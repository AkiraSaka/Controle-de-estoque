import pandas as pd

#Realiza cadastros dentro do arquivo xlsx
def cadastro():
    planilha = pd.read_excel('estoque.xlsx')
    referencia = input('Digite o código de referência: ')
    try:
        referencia = int(referencia)
    except:
        print('Digite uma referência válida (apenas numeros)')
        cadastro()

    descricao = input('Digite a descrição do produto: ')
    descricao = descricao.upper()

    cor = input('Digite a cor do produto: ')
    cor = cor.upper()

    preco = input('Digite o preço do produto: ')
    preco = preco.replace(',', '.')

    try:
        preco = float(preco)
    except:
        print('Digite apenas o valor em números!')
        cadastro()
        
    tamanho_p = input('Digite o estoque do tamanho P: ')
    tamanho_p = tamanho_p.replace(',', '.')
    try:
        tamanho_p = int(tamanho_p)
    except:
        print('Digite apenas números')
        cadastro()

    tamanho_m = input('Digite o estoque do tamanho M: ')
    tamanho_m = tamanho_m.replace(',', '.')
    try:
        tamanho_m = int(tamanho_m)
    except:
        print('Digite apenas números')
        cadastro()

    tamanho_g = input('Digite o estoque do tamanho G: ')
    tamanho_g = tamanho_g.replace(',', '.')
    try:
        tamanho_g = int(tamanho_g)
    except:
        print('Digite apenas números')
        cadastro

    tamanho_gg = input('Digite o estoque do tamanho GG: ')
    tamanho_gg = tamanho_gg.replace(',', '.')
    try:
        tamanho_gg = int(tamanho_gg)
    except:
        print('Digite apenas números')
        cadastro()

# Cadastro dos produtos em células
    planilha = planilha.append({'REF': referencia, 'DESCRIÇÃO':descricao, 'CORES': cor, 'TAMANHO P':tamanho_p, 'TAMANHO M':tamanho_m, 'TAMANHO G':tamanho_g, 'TAMANHO GG':tamanho_gg,'PREÇO': preco}, ignore_index=True)
# Salva a planilha 
    consulta = referencia
    retorno = planilha.loc[planilha['REF'] == consulta]
    print(retorno)
    finaliza = input(
        'Os dados estão corretos?\n'
        '1 para SIM\n'
        '2 para NÃO\n')

    if finaliza == '1':
        planilha.to_excel('estoque.xlsx', index=False)
        print('Produto cadastrado com sucesso')
        print()
        print('Deseja cadastrar mais algum produto?')

        choice = input(
            '1 para SIM\n'
            '2 para NÃO\n'
        )
        if choice == '1':
            print()
            cadastro()
        else:
            pass


    if finaliza == '2':
        endereco = input('Digite o numero da linha a ser reescrita: ')
        endereco = int(endereco)
        planilha.drop(endereco, axis=0, inplace=True, errors='ignore')
        print()
        cadastro()
