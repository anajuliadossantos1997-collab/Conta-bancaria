from Contabancaria import *

def menu():
    print('=' * 40)
    print('MENU BANCÁRIO'.center(40))
    print('=' * 40)
    print('1- Depositar')
    print('2 - Sacar')
    print('3 - Transferir')
    print('4 - Extrato')
    print('5 - Criar nova conta')
    print('0 - Sair')
    print('=' * 40)

def operacoes(contas, conta_atual):
    while True:
        menu()
        try:
            opcao = input('Escolha uma opção: ')
        except:
            print('\033[31Por favor, Digite uma opção válida.\033[m')
        else: 
            if opcao == '1':
                try:
                    valor = float(input('Digite o valor do depósito: R$'))
                    if conta_atual.deposito(valor):
                        print('\033[32mDepósito realizado com sucesso. Volte sempre!\033[m')
                        conta_atual.extrato()
                except ValueError:
                    print('\033[31mDigite apenas números\033[m')

            elif opcao == '2':
                try:
                    valor = float(input('Digite o valor do saque: R$'))
                    if conta_atual.saque(valor):
                        print('\033[32mSaque realizado com sucesso. Volte sempre!\033[m')
                        conta_atual.extrato()
                except ValueError:
                    print('\033[31mDigite apenas números\033[m')

            elif opcao == '3':
                try:
                    id_destino = int(input("Digite o ID da conta destino: "))
                    conta_destino = None
                    for c in contas:
                        if c.id == id_destino:
                            conta_destino = c
                            break
                    if conta_destino is None:
                        print("\033[31mConta destino não encontrada!\033[m")
                        continue
                        
                    valor = float(input("Digite o valor da transferência: R$ "))
                
                    if conta_atual.transferencia(conta_destino, valor):
                        print("\033[32mTransferência realizada com sucesso!\033[m")
                        conta_atual.extrato()
                except ValueError:
                    print('\033[31mDigite apenas números\033[m')
               
            elif opcao == '4':
                conta_atual.extrato()

            elif opcao == '5':
                id_nova = int(input("Digite o ID da nova conta: "))
                nome_nova = input("Digite o nome do titular: ")
                saldo_inicial = float(input("Digite o saldo inicial (ou 0): R$ "))
            
                nova_conta = Contabancaria(id=id_nova, nome=nome_nova, saldo=saldo_inicial)
                contas.append(nova_conta)
                print("\033[32mNova conta criada com sucesso!\033[m")
                conta_atual.extrato()
           
            elif opcao == '0':
                print('Obrigado por usar nosso Banco!')
                break
            