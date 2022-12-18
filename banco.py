menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = float(0)
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo

    valor = input("Digite o valor a ser depositado: ")
    deposito = (float(valor))

    while deposito <= 0 :
        deposito = input("Digite um valor valido para deposito: ")

    saldo = saldo + deposito

    return saldo






while True:
    opcao = input(menu)

    if opcao == "1":
        print("Deposito")
        depositar()
        print("Saldo restante: ", saldo)
    
    elif opcao == "2":
        print("Saque")
    
    elif opcao == "3":
        print("Extrato")
    
    elif opcao == "4":
        print("Saindo...")
        break
    else: 
        print("Opção inválida, escolha novamente a operação desejada.")

