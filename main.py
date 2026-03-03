from Contabancaria import *
from Interface import *

# Criar lista de contas
contas = []

# Criar conta inicial
c1 = Contabancaria(id=112, nome='Gustavo', saldo=3000)
c2 = Contabancaria(id=568, nome='Ana')

# Executar o menu com a conta inicial
operacoes(contas, c1)
