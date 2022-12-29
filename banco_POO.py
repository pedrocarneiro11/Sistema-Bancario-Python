from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf_format, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf_format = cpf_format

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.limite = 500
        self.LIMITE_SAQUES = 3
        # self.historico = Historico() # TODO
    
    @classmethod
    def nova_conta(cls,cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    def depositar(self):
        global saldo, numero_depositos
        deposito = 0

        while deposito <= 0 :
            valor = input("Digite um valor valido para deposito: ")
            deposito = (float(valor))

        saldo = saldo + deposito
        numero_depositos = numero_depositos + 1

        return saldo, numero_depositos

    def sacar(self):
        global saldo, numero_saques, LIMITE_SAQUES, limite
        nao_excedeu_maximo_de_saques = numero_saques < LIMITE_SAQUES
        
        if (nao_excedeu_maximo_de_saques) :
            valor = float(input("Digite o valor para sacar: "))

            excedeu_limite = valor > limite
            valor_maior_que_saldo = valor > saldo

            while excedeu_limite:
                print("Valor digitado superior ao seu limite de " + str(limite))
                valor = float(input("Digite um valor inferior ao seu limite para sacar: "))
            
            while valor_maior_que_saldo:
                print("Seu saldo atual é de: " + str(saldo))
                valor = float(input("Digite um valor inferior ao seu saldo: "))
            
            saldo = saldo - valor
            numero_saques = numero_saques + 1
            print("Saque realizado com sucesso!")
        
            return saldo, numero_saques
        
        else :
            print("Limite diário de saques atingido")

    def extrato(self, saldo):
        print("Seu saldo: ", saldo)

class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite = float(500), limite_saques = 3):
        super().__init__(self, numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.limite_saques

        if excedeu_limite:
            print("\n O valor informado excedeu o limite")

        elif excedeu_saques:
            print("\n Numero maximo de saques atingido")

        else:
            return super().sacar(valor)

        return False
        
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}            
            C/C:\t{self.numero}            
            Titular:\t{self.cliente.nome}            
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)