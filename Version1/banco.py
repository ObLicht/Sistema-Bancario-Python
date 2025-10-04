
lista_extrato = []
saldo = 0
saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR = 500

while True:
    print("---Menu---:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("0 - Sair")
    opcao = int(input("Digite uma opcao:"))
    if opcao == 1:
        valor_depositado = float(input("Digite o valor do depósito: "))
        saldo += valor_depositado
        lista_extrato.append(f"Depósito: {valor_depositado:.2f}")
    elif opcao == 2:
        if saques < LIMITE_SAQUES:
            valor_saque = float(input("Valor do saque: "))
            if valor_saque <= LIMITE_VALOR and valor_saque <= saldo:
                saldo -= valor_saque
                saques += 1
                lista_extrato.append(f"Saque: {valor_saque:.2f}")
            else:
                print("O valor não pode ser retirado.")
                lista_extrato.append(f"Tentativa da saque inválida: {valor_saque:.2f}")
        else:
            print("Limite de saques atingido!")
    elif opcao == 3:
        print("----Extrato----")
        for item in lista_extrato:
            print(item)

    elif opcao == 0:
        print('Saindo..')
        break
    else:
        print("Operação inválida")
      
