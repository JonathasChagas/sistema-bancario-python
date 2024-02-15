import os

menu = """

-------------------------------
|                             |
|    [1]. Depositar           |
|    [2]. Sacar               |
|    [3]. Extrato             |
|    [4]. Criar usuário       |
|    [5]. Lista usuários      |
|    [6]. Criar conta         |
|    [7]. Lista contas        |
|    [0]. Sair do programa    |
|                             |
-------------------------------

"""

pausa = 0
movimento_acao = 0
saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
SAQUE_LIMITE = 3
usuarios = []
agencias = []
numero_contas = 1

def deposito(extrato, saldo):
    movimento_acao = input("Digite o valor do depósito: ")

    if float(movimento_acao) <= 0:
        print("Depósito inválido! Valor negativo ou nulo.")
    else:
        movimento_acao = float(movimento_acao)
        extrato += f"Depositado: +R${movimento_acao:.2f}\n"
        pausa = input("Digite enter para continuar")
        saldo += movimento_acao
    return extrato, saldo

def saque(saque_limite, extrato, saldo, numero_saques):
    movimento_acao = input("Digite o valor do saque! Máximo R$ 500: ")

    if float(movimento_acao) > 500:
        print("Saque além do limite permitido!")
    
    elif numero_saques >= SAQUE_LIMITE:
        print("Número máximo de saques diários atingidos!")
    
    elif float(movimento_acao) > saldo:
        print("Saque além do valor contido no saldo!")
   
    else:
        print("Saque efetuado!")
        movimento_acao = float(movimento_acao)
        extrato += f"Sacado: -R${movimento_acao:.2f}\n"
        pausa = input("Digite enter para continuar")
        saldo -= movimento_acao
        numero_saques += 1
    return extrato, saldo, numero_saques

def extrato_mostrar(saldo, extrato):
    print("Nenhum extrato realizado") if not extrato else print(extrato)
    print(f"Saldo: {saldo:.2f}")
    pausa = input("Digite enter para continuar")

def criar_usuarios(usuarios):
    usuario = {}
    usuario['nome'] = input("Digite o seu nome: ")
    usuario['data'] = input("Digite a sua data de nascimento (XX/XX/XXXX): ")
    usuario['cpf'] = input ("Digite seu CPF (apenas números): ")
    usuario['endereço'] = input ("Digite o seu endereço: ")

    for usuario2 in usuarios:
        if usuario2['cpf'] == usuario['cpf']:
            print ("CPF já cadastrado!")
            pausa = input("Digite enter para continuar")
            break

    else: 
        print("Usuário cadastrado!")
        usuarios.append(usuario)
        pausa = input("Digite enter para continuar")

def criar_agencia(agencias, usuarios, numero_contas):
    conta_agencia = {}
    conta_agencia['numero'] = '0001'
    conta_agencia['conta'] = numero_contas
    conta_agencia['usuario'] = input ("Digite o seu CPF: ")

    for usuario in usuarios:
        if conta_agencia['usuario'] == usuario['cpf']:
            print("Conta criada!")
            agencias.append(conta_agencia)
            numero_contas += 1
            pausa = input("Digite enter para continuar")
            return numero_contas
    
    else: 
        print("CPF inexistente em nosso sistema! Conta não foi criada")
        pausa = input("Digite enter para continuar")
        return numero_contas

        

while True:

    opcao = input(menu)

    if opcao == '1':
        extrato, saldo = deposito(extrato, saldo)

    elif opcao == '2':
        extrato, saldo, numero_saques = saque(SAQUE_LIMITE, extrato, saldo, numero_saques)

    elif opcao == '3':
        extrato_mostrar(saldo, extrato)

    elif opcao == '4':
        criar_usuarios(usuarios)

    elif opcao == '5':
        print(usuarios)
        pausa = input("Digite enter para continuar")

    elif opcao == '6':
        numero_contas = criar_agencia(agencias, usuarios, numero_contas)

    elif opcao == '7':
        print(agencias)
        pausa = input("Digite enter para continuar")

    elif opcao == '0':
        print("Fim do programa!")
        os.system('cls')
        break

    else:
        print("Opção Inválida")

    os.system('cls')
