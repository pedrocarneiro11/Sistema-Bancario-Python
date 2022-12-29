from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(cliente):
    def __init__(self, cpf_format, nome, data_nascimento):
        super().__init__(cpf_format)
        self.cpf_format = cpf_format
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.limite = 500
        self.LIMITE_SAQUES = 3
        # self.historico = Historico() # TODO

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
        
