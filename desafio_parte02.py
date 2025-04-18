'''
Você foi encarregado de implementar as seguintes funcionalidades no sistema:
    - Estabelecer um limite de 10 transações diarias para uma conta
    - Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu 
    o numero de transações permitidas para aquele dia
    - Mostre no extrato, a data e hora de todas as transações - ok
'''
from datetime import datetime

#variaveis
nro_conta = 1
contas = []
usuarios = []
saldo = 0
limite = 500
extrato = ""
numero_transacoes = 0
LIMITE_TRANSACOES = 10
data_hora_saque = datetime.now()
menu = """


Digite a opção abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Novo Usuário
[c] Nova conta

"""

#funções do sistema

#função de saque
def saque(saldo, valor, numero_transacoes, extrato):
    if numero_transacoes >= LIMITE_TRANSACOES:
        print('Você excedeu o limite de transações no dia, volte amanha. Se preferir converse com o seu gerente.')
    elif valor > 500:
        print('Saque não permitido, valor excedido por saque. Tente novamente')
    elif valor < saldo:
        saldo -= valor
        numero_transacoes += 1
        extrato += f'{data_hora_saque.strftime("%d/%m/%Y %H:%M")} Sacou R$ {valor:.2f}\n'
    else:
        print('Saldo insficiente.')

    return saldo, numero_transacoes, extrato

#função de deposito
def depositando(saldo,  valor, extrato, numero_transacoes):
    if numero_transacoes >= LIMITE_TRANSACOES:
        print('Você excedeu o limite de transações no dia, volte amanha. Se preferir converse com o seu gerente.')
    else:
        saldo += valor
        numero_transacoes += 1
        extrato += f'{data_hora_saque.strftime("%d/%m/%Y %H:%M")} Depositou R$ {valor:.2f}\n'
        
    return saldo, extrato, numero_transacoes

#função de cadastro de novo usuário
def novo_usuario(usuarios):
    cpf = int(input("Digite seu CPF: "))

    for usuario in usuarios:
        if cpf in usuario:
            print("CPF já cadastrado!")
            return

    nome = str(input("Digite seu nome: "))
    endereco = str(input("Digite seu endereço: "))

    usuario = {
        cpf:{
        'nome': nome,
        'endereco': endereco
        }
    }

    usuarios.append(usuario)
    # print(usuarios)

#função de criação de conta
def nova_conta(contas):
    usuario_conta = input("Digite o cpf do usuario: ")

    for usuario in usuarios:
        if not cpf in usuario:
            print("CPF não cadastrado!")
            return
        
    nro_conta += 1
    agencia = "0001"


    conta ={
        nro_conta:{
            "gencia": agencia,
            "usuario_conta": usuario_conta
        }
    }

    contas.append(conta)
    print(contas)

#loop de funcionamento

while True:

    opcao = input(menu)

    if opcao == "d":
        valor=float(input('Digite o valor do deposito: R$ '))
        saldo, extrato, numero_transacoes = depositando(saldo, valor, extrato, numero_transacoes)
        print(f'Seu saldo atual é R$ {saldo:.2f}')
    
    elif opcao == "s":
        valor=float(input('Digite o valor do saque: R$ '))
        saldo, numero_transacoes, extrato = saque(saldo, valor, numero_transacoes, extrato)
        print(f'Seu saldo atual é R$ {saldo:.2f}')

    elif opcao == "e":
        print(f"""
              
================= Extrato ================


{extrato}

=============================================

{data_hora_saque.strftime("%d/%m/%Y %H:%M")} Seu saldo é R$ {saldo}

""")
        
    elif opcao == "u":
        novo_usuario(usuarios)

    elif opcao == "c":
        nova_conta(contas)

    elif opcao == "q":
        print("Obrigado por usar nosso sistema!")
        break

    else:
        print("Opção invalida tente novamente.")
         

