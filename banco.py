import textwrap

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar novo Usuario
[5] Criar conta corrente
[6] Sair

=> """

AGENCIA = "0001"
saldo = float(0)
limite = float(500)
extrato = ""
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3
usuarios = [] 
count_usuarios = 0
contas = []

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
            print("Seu saldo atual é de: " + str(saldo))
            valor = float(input("Digite um valor inferior ao seu saldo: "))
        
        saldo = saldo - valor
        numero_saques = numero_saques + 1

        return saldo, numero_saques  
    
    else :
        print("Limite diário de saques atingido")

def extrato():
    print("Seu saldo: ", saldo)

def criar_usuario():
    global count_usuarios
    print("a fazer...")
    #JA FEITO:
    # Usuario é composto por NOME, DATA DE NASCIMENTO, CPF E ENDERECO OK
    # Endereco possui logradouro, numero, bairro, cidade, estado OK
    # Sugestao de formato para endereco: logradouro, numero - bairro - cidade/sigla estado OK
    # cpf deve guardar apenas os numeros do cpf, sem tracos nem pontos OK
    # ex de cpf: 123.098.234-94 => devera ficar assim 12309823494 OK
    # nao pode cadastrar 2 usuarios com o mesmo cpf OK
    
    nome = input("Digite o nome do usuario: ")

    data_nascimento = input("Digite a data de nascimento: ")

    cpf_format = input("Digite o cpf: ")
    cpf_f= cpf_format.replace("-","")
    cpf= cpf_f.replace(".","")

    if count_usuarios == 0:
        count_usuarios = count_usuarios + 1
    else:
        i = 0
        for i in range(count_usuarios):
            if cpf[i] in usuarios == cpf[count_usuarios]:
                print("CPF ja cadastrado")
                criar_usuario()    

    confirmacao = "N"
    while confirmacao == "N":
        print ("Digite o endereco")
        logradouro = input("Digite o nome da rua: ")
        numero = input("Digite o numero da rua: ")
        bairro = input("Digite o nome do bairro: ")
        cidade = input("Digite o nome do municipio: ")
        estado = input("Digite a sigla do estado: ")
        endereco = [logradouro, numero, bairro, cidade, estado]

        print("O endereco é:", logradouro, ", numero:", numero, ", bairro:", bairro, ", municipio:", cidade, "estado:",estado)
        print("\n")
        
        confirmacao = input("Está correto? (S) (N): ") 
        if (confirmacao != 'S' and confirmacao != 's' and confirmacao != 'N' and confirmacao != 'n'):
            confirmacao = input("Digite uma das opcoes: (S) (N): ")  
    
    usuarios.append({"Numero do usuario: ": count_usuarios, " Nome do usuario: ":nome, " Endereco: ":endereco, " Data de nascimento: ":data_nascimento})

    print(usuarios)

    count_usuarios = count_usuarios + 1    

def criar_conta_corrente():
    print("a fazer...")
    global AGENCIA
    global contas
    count_contas = 0    
    numero_conta = count_contas + 1
    

    contas[count_contas] = [AGENCIA, numero_conta]    

    count_contas = count_contas + 1
    

    #TODO:
    # O programa deve armazenar contas e uma lista
    # A conta é composta por: agência, numero da conta e usuário
    # O numero da conta é sequencial, iniciando em 1
    # O numero da agencia é fixo: 0001
    # O usuario pode ter mais de uma conta
    # Mas uma conta pertence SOMENTE a um usuario

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
        extrato() 

    elif opcao == "4":
        print("Criar novo usuario")
        criar_usuario()        
    
    elif opcao == "5":
        print("Criar conta corrente")
        criar_conta_corrente()       
    
    elif opcao == "6":
        print("Saindo...")
        break
    else: 
        print("Opção inválida, escolha novamente a operação desejada:")

