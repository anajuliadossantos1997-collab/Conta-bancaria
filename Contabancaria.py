class Contabancaria:
    '''
    Cria uma conta bancária simples que permite fazer saques e depósitos e transferências
    '''
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        self.historico = []
    
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"
    
    def deposito(self, valor):
        if valor <= 0:
            print(f'\033[31mValor inválido! O depósito deve ser positivo.\033[m')
            return False
        self.saldo += valor
        self.historico.append(f'Depósito: +R${valor:.2f}')
        return True
    
    def saque(self, valor):
        if self.saldo < valor:
            print('\033[31mSaldo insufuciente\033[m')
            return False
        else:
            self.saldo -= valor
            self.historico.append(f'Saque: -R${valor:.2f}')
            return True

    def transferencia(self, conta_destino, valor):
        if self.saldo < 0:
            print(f'\033[31mValor inválido!\033[m')
            return False
        if self.saldo < valor:
            print('\033[31mSaldo Insufuciente\033[m')
            return False
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f'Transferencia enviada: -R${valor:.2f} para {conta_destino.titular}')
            conta_destino.historico.append(f'Transferência recebida: +R${valor:.2f} de {self.titular}')
            
            print('\033[32Transferido com sucesso!\033[m')
            return True
        
    def extrato(self):
        print(f'\033[33mExtrato da conta {self.id}\033[m')
        if not self.historico:
            print('Nenhuma transação realizada.')
        else:
            for transacao in self.historico:
                print(transacao)
            print(f'Saldo atual: R${self.saldo:.2f}')
            print('-=' * 30)
