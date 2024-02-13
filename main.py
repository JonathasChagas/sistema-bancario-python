

menu = """

-------------------------------
|                             |
|    [1]. Depositar           |
|    [2]. Sacar               |
|    [3]. Extrato             |
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

while True:

    opcao = input(menu)

    if opcao == '1':
        movimento_acao = input("Digite o valor do depósito: ")

        if movimento_acao <= '0':
            print("Depósito inválido! Valor negativo ou nulo.")

        else:
            movimento_acao = float(movimento_acao)
            extrato += f"Depositado: +R${movimento_acao:.2f}\n"
            pausa = input ("Digite enter para continuar")
            saldo += int(movimento_acao)

    elif opcao == '2':
        movimento_acao = input ("Digite o valor do saque! Máximo R$ 500: ")
     
        if movimento_acao > '500':
            print("Saque além do limite permitido!")

        elif numero_saques >= SAQUE_LIMITE:
            print("Número máximo de saques diários atingidos!")

        elif int(movimento_acao)> saldo:
            print("Saque além do valor contido no saldo!")
        
        else:
            print ("Saque efetuado!")
            movimento_acao = float(movimento_acao)
            extrato += f"Sacado: -R${movimento_acao:.2f}\n"
            pausa = input ("Digite enter para continuar")
            saldo -= int(movimento_acao)
            numero_saques += 1

    elif opcao == '3':

        print ("Nenhum extrato realizado") if not extrato else extrato 
        print (f"Saldo: {saldo:.2f}")
        print (extrato)
        pausa = input ("Digite enter para continuar")

    elif opcao == '0':
        print("Fim do programa!")
        break

    else:
        print("Opção Inválida")



