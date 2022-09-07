from menupython.biblioteca import modulo
from menupython.biblioteca import arquivo
from time import sleep


arq='listanomes.txt' #variavel que solicita a abertura de um arquivo txt
if not arquivo.arquivoreal(arq):  #se não existir o arquivo
    arquivo.criararquivo(arq)   #é criado a partir da função criarquivo(

modulo.titulo('MENU PRINCIPAL')
print(sleep(0.5))
while True:
    r=modulo.selecao(['\033[4;34mVer pessoas cadastradas\033[m', '\033[4;34mCadastrar nova pessoa\033[m',
                      '\033[4;34mSair do sistema\033[m'])
    if r==1:
        #LISTAGEM DE CONTEÚDO DO ARQUIVO
        arquivo.leraquivo(arq)  #ao selecionar a opção 1, é mostrado o arquivo txt criado pelo programa
    elif r==2:
        sleep(0.3)
        modulo.titulo('\033[1;31mNOVO CADASTRO:\033[m')
        nome=str(input('NOME: '))
        idade= modulo.leiaint('IDADE: ')
        arquivo.cadastrar(arq,nome,idade) #função para cadastrar novos dados
        #arq= arquivo de texto que será adicionado os nomes
        #nome e idade= os dados que serão registrados pelo usuário no arquivo txt
    elif r==3:
        print('\n\033[1;35;40mFINALIZANDO O SITEMA\033[m')
        sleep(0.5)
        print('\033[1;35m.\033[m',end=' ')
        sleep(0.5)
        print('\033[1;35m.\033[m', end=' ')
        sleep(0.5)
        print('\033[1;35m.\033[m', end=' ')
        sleep(0.5)
        print('\n\033[1;35;40mATÉ LOGO !\033[m')
        break
    else:
        print("\033[1;31mERRO !!!\033[m")
        print('\033[1;31mDIGITE UM OPÇÃO VALIDA\033[m')


