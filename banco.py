menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = float(0)
limite = float(500)
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, numero_depositos

    valor = input("Digite o valor a ser depositado: ")
    deposito = (float(valor))

    while deposito <= 0 :
        deposito = input("Digite um valor valido para deposito: ")

    saldo = saldo + deposito
    numero_depositos = numero_depositos + 1

    return saldo, numero_depositos

def sacar():
    global saldo, numero_saques
    if (numero_saques < LIMITE_SAQUES) :
        valor = float(input("Digite o valor para sacar: "))
        while valor > limite:
            print("Valor digitado superior ao seu limite de " + str(limite))
            valor = float(input("Digite um valor inferior ao seu limite para sacar: "))
        while valor > saldo:
            valor = float(input("Digite um valor inferior ao seu saldo: "))
        
        saldo = saldo - valor
        numero_saques = numero_saques + 1

        return saldo, numero_saques  
    
    else :
        print("Limite diário de saques atingido")


while True:
    opcao = input(menu)

    if opcao == "1": 
        print("Deposito")
        depositar()
        print("Saldo restante: ", saldo)
    
    elif opcao == "2":
        print("Saque")
        sacar()
        print("Saldo restante: ", saldo)
    
    elif opcao == "3":
        print("Extrato")
        print("Seu saldo: ", saldo)
    
    elif opcao == "4":
        print("Saindo...")
        break
    else: 
        print("Opção inválida, escolha novamente a operação desejada.")

