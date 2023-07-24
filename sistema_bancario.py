# ======================= Constantes =======================
LIMITE_SAQUE = 3

# Variáveis iniciais
saldo = 0
limite = 1000
extrato = ""
quantidade_saques = 0

# ======================= Funções =======================
def realizar_deposito():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! => O valor informado é inválido.")

def realizar_saque():
    global saldo, extrato, quantidade_saques
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = quantidade_saques >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Operação falhou! => Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! => O valor do saque excede o limite.")
    elif excedeu_saque:
        print("Operação falhou! => Número máximo de saques do dia foi excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        quantidade_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Nenhuma movimentações" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=========================================")

# ======================= Menu =======================
menu = """
============== Menu ==============
Olá, seja bem-vindo...

Escolha uma das opções a seguir.
_________________________________

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
_________________________________

==================================
Selecionar a opção:  """

while True:
    opcao = input(menu)

    if opcao == "1":
        realizar_deposito()
    elif opcao == "2":
        realizar_saque()
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
