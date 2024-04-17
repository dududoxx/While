# pontos = 0
# questao = 1
# while questao <= 3:
#     resposta = input(f'Resposta da Questão {questao}:')
#     if questao == 1 and resposta == 'b':
#         pontos = pontos + 1
#     elif questao == 2 and resposta == 'a':
#         pontos = pontos + 1
#     elif questao == 3 and resposta == 'd':
#         pontos = pontos + 1
#     questao = questao + 1
#     print(f"O aluno fez {pontos} ponto(s)")


# n = 1 #contador
# soma = 0 #acumulador
# while n <= 10:
#     x = float(input(f"Digite o número {n}: "))
#     soma = soma + x
#     n = n + 1
# print(f"Soma = {soma:.2f}")
# print(f"A média dos 10 numeros é igual a = {soma / 10:.2f}")
# print(f"Média = {soma/(n-1):.2f}")

# 8. Escreva um programa que pergunte o depósito inicial
# e a taxa de juros de uma poupança. Exiba os valores
# mês a mês para os 24 primeiros meses. Escreva o total
# do ganho com juros no período

# deposito = float(input("Valor do depósito inicial: R$"))
# taxa = float(input("Valor da taxa de juros da poupança em porcentagem: "))
# mes = 1
# while mes <= 24:
#     deposito = deposito + (deposito * (taxa / 100))
#     print(f"Saldo do mês {mes} é de R${deposito:.2f}.")
#     mes += 1
# print(f"O ganho obtido com os juros foi de R${deposito:.2f}.")

soma = 0
while True:
    num = input(f"Digite um numero a somar ou FIM para sair: ")
    if num == "FIM":
        break
    soma += float(num)
print(soma)
