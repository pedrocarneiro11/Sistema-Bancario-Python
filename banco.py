import textwrap

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar novo Usuario
[5] Criar conta corrente
[6] Listar contas
[7] Sair

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
numero_contas = 0
count_contas = 1

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
    
    cpf_format = input("Digite o cpf: ")
    cpf_f= cpf_format.replace("-","")
    cpf= cpf_f.replace(".","")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n @@@ Já existe usuario com esse CPF!")
        return
    
    nome = input("Digite o nome do usuario: ")
    data_nascimento = input("Digite a data de nascimento: ")

    confirmacao = "N"
    while confirmacao == "N" or confirmacao == "n":
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
            confirmacao = input("Digite uma das opcoes validas: (S) (N): ")  
    
    usuarios.append({"Numero do usuario: ": count_usuarios, " Nome do usuario: ,": nome,"CPF": cpf, " Endereco: ": endereco, " Data de nascimento: ":data_nascimento})

    print(usuarios)

    print("contador ",count_usuarios)   

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(AGENCIA, numero_conta, usuarios):
    global contas 

    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return{"agencia": AGENCIA, "numero": numero_conta, "usuario": usuario}    
    
    print("\n Usuario nao encontrado, fluxo de criacao de contas encerrado")
    return None
    
def listar_contas(contas):
    print(contas)
    for conta in contas:
        linha = f"""\
            Agência: \t{conta["agencia"]}
            C/C:\t\t{conta["numero"]}
            Titular:\t{conta["usuario"]}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

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
        numero_conta = len(contas) + 1
        conta =criar_conta_corrente(AGENCIA, numero_conta, usuarios)      

        if conta:
            contas.append(conta)
            count_contas += 1
    
    elif opcao == "6":
        print("Listando contas")
        listar_contas(contas)

    elif opcao == "7":
        print("Saindo...")
        break
    else: 
        print("Opção inválida, escolha novamente a operação desejada:")

