def leiaint(n):
    while True:
        try:
            num = int(input(n))
        except (ValueError, TypeError):
            print("\033[1;31mERRO! INFORME UM VALOR INTEIRO\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[1;31mO USUÁRIO DECIDIU PARAR O PROGRAMA\033[m")
            return f'\033[7;31;40mNão foi informado nenhum valor\033[m'
        else:   #se tudo der certo, retorne o número informado
            return num

def titulo(msg):
    tam=len(msg)
    print("\033[1m-\033[m"*tam)
    print(f'\033[7;40m{msg}\033[m')
    print("\033[1m-\033[m"*tam)


def selecao(lista):
    print("\033[1m=\033[m"*30)
    c=1
    for item in lista:
        print(f'\033[1;34m{c}- {item}\033[m')
        c+=1
    print()
    opc= leiaint('\033[1;36;40mEscolha uma opção:\033[m ')
    return opc



