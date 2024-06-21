#atividade(r10)
print('dom dia tudo bem com vc hoje')
5
# Solicita ao usuário para inserir um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa a variável para armazenar a soma dos divisores próprios
soma_divisores = 0

# Calcula a soma dos divisores próprios do número
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

# Verifica se o número é perfeito
if soma_divisores == numero:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")