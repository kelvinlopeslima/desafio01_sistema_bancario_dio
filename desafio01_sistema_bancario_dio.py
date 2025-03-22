#Criar um sistema bancario com as operações: sacar, depositar e visualizar extrato

''' 
Operação de deposito

Deve ser possivel depositar valores positivos para a minha conta bancaria. A V1 do projeto trabalha apenas com 1 usuario, dessa forma não precisamos
nos preocupar  em identificar qual é o numero da agencia e conta bancaria. Todos os depositos devem ser armazenados em uma variavel e exibidos na operação de extrato
'''

'''
Operação de saque

O sistema deve permitir realizar 3 saques diarios com limite maximo de R$ 500 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem
informando que não será possivel sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato
'''

'''
Operação de extrato

Essa operação deve listar todos os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores dever ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
'''

#variaveis

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
menu = """

Digite a opção abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
#print(menu)

#funções do sistema

def saque(saldo, valor, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print('Você excedeu o limite de saques, volte amanha. Se preferir converse com o seu gerente.')
    elif valor > 500:
        print('Saque não permitido, valor excedido por saque. Tente novamente')
    elif valor < saldo:
        saldo -= valor
        numero_saques += 1
    else:
        print('Saldo insficiente.')

    return saldo, numero_saques

def depositando(saldo,  valor):
    saldo += valor
    return saldo

def atualizando_extrato(extrato, valor):
    if opcao == "d":
        extrato += f'Depositou R$ {valor:.2f}\n'
    elif opcao == "s":
        extrato += f'Sacou R$ {valor:.2f}\n'
    return extrato
    

#loop de funcionamento

while True:

    opcao = input(menu)

    if opcao == "d":
        valor=float(input('Digite o valor do deposito: R$ '))
        extrato = atualizando_extrato(extrato, valor)
        saldo = depositando(saldo, valor)
        print(f'Seu saldo atual é R$ {saldo:.2f}')
    
    elif opcao == "s":
        valor=float(input('Digite o valor do saque: R$ '))
        extrato = atualizando_extrato(extrato, valor)
        saldo, numero_saques = saque(saldo, valor, numero_saques)
        print(f'Seu saldo atual é R$ {saldo:.2f}')

    elif opcao == "e":
        print(f"""
              
================= Extrato ================


{extrato}

=============================================

Seu saldo é R$ {saldo}

""")

    elif opcao == "q":
        break

    else:
        print("Opção invalida tente novamente.")
    