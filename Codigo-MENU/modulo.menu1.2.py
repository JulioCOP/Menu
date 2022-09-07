from menupython.biblioteca.modulo import *

def arquivoreal(nome): #verificação da existência do arquivo txt para posteriormente ser criado
    try: #tratamento de erro, tentar abrir e fechar o arquivo
        a=open(nome,'rt') #rt= função read-text efetua a leitura de arquivo txt e da o retorno em caso de existência de txt
        a.close()
    except FileNotFoundError: #se o arquivo não for encontrado
        return False
    else:
        return True

#quando arquivo não for encontrado

def criararquivo(nome): #função para a criação do arquivo txt
    try:
        a=open(nome, 'wt+') #wt - write text + (cria arquivo)  -> função que abre um novo arquivo de texto e adiciona os itens txts
        a.close() #após a ultma listagem o arquivo é criado
    except:
        print("ERRO NA CRIAÇÃO DO ARQUIVO")
    else:
        print(f"ARQUIVO {nome} CRIADO COM SUCESSO")

def leraquivo(nome): #função que interpreta o código digitado pelo usuário e retorna a lista de nomes
    try:
        a=open(nome,'rt') #1º ocorre a tentativa, para verificar a existência de algum arquivo texto dentro do txt criado
    except: #se não houver nada
        print("ERRO AO LER O ARQUIVO")
    else: #havendo algo dentro do txt, retorna:
        titulo(f'{"PESSOAS CADASTRADAS":^20}')
        #print(a.read()) #função para mostar na tela o que foi encontrado no txt criado
        for linha in a: #para cada linha dentro da variavel "a"
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n',"")
            print(f'{dado[0]:<10}{dado[1]:>5} anos')
    finally:
        a.close() #dando certo ou dando errado, o arquivo fecha ao final

def cadastrar(arq,nome='desconhecido',idade=0): #função que adiciona ao arquivo txt, o nome e a idade
    #em caso do usuário não informar o nome ele sera tido como desconhecido e o mesmo ocorre com a idade recebendo valor 0
    try:
        a=open(arq,'at') #abre o arquivo txt
    except:
        print("HOUVE UM ERRO NA ABERTURA DO ARQUIVO")
    else:
        try:
            a.write(f'{nome};{idade}\n') #após abertura do arquivo txt, se não houver erros, é adicionado nome e idade
        except:
            print("HOUVE UM ERRO NA HORA DO REGISTRO DOS DADOS")
        else:
            print(f'\033[1;33mRegistro de {nome} realizado com sucesso\033[m')
            a.close()