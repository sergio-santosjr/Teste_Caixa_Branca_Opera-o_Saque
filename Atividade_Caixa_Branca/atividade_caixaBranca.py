def saque(valor, saldo, limite_credito):
    status = False

    if valor <= saldo:
        saldo = saldo - valor
        status = True  # status é uma variável de controle (uma flag), serve para avisar quem chamou a função se a operação deu certo ou errado.
    elif valor <= (saldo + limite_credito):
        # Saque usando o saldo disponível + limite de credito disponível
        valor_restante = valor - saldo
        saldo = 0
        limite_credito = limite_credito - valor_restante
        status = True

    return status, saldo, limite_credito    # Se meu primeiro if der certo, é executado já á última linha. e encerra o bloco.

saldo = 1000
limite_credito = 500

status, saldo, limite_credito = saque(1600, saldo, limite_credito)
print("Saque realizado?", status)
print("Saldo: R$", saldo)
print("Limite de credito: R$", limite_credito)


