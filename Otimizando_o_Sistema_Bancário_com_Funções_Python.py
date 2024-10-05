def exibir_menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
=> """

# Dados do sistema
usuarios = []
contas = []
numero_conta = 1
AGENCIA_FIXA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Função para criar um novo usuário
def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro! Já existe uma usuária com esse CPF.")
            return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (rua, número, bairro, cidade/estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuária criada com sucesso!")

# Função para criar uma nova conta
def criar_conta():
    global numero_conta
    cpf = input("Informe o CPF da usuária para vincular à conta: ")
    
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Erro! Não foi encontrado uma usuária com esse CPF.")
        return

    contas.append({
        "agencia": AGENCIA_FIXA,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    })
    print(f"Conta criada com sucesso! Agência: {AGENCIA_FIXA} Conta: {numero_conta}")
    numero_conta += 1

# Função para listar todas as contas
def listar_contas():
    if not contas:
        print("Não há contas cadastradas.")
    else:
        for conta in contas:
            usuario = conta['usuario']
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Usuária: {usuario['nome']} | CPF: {usuario['cpf']}")

# Função para depositar valores
def depositar(saldo, extrato):
    valor = input("Qual valor deseja depositar ou digite [v] para voltar ao menu: ")

    if valor == "v":
        return saldo, extrato
    else:
        valor = float(valor)
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido💁‍♀️.")
        return saldo, extrato

# Função para sacar valores
def sacar(saldo, extrato, numero_saques):
    valor = input("Informe o valor do saque ou digite [v] para voltar ao menu: ")

    if valor == "v":
        return saldo, extrato, numero_saques
    else:
        valor = float(valor)
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente💁‍♀️.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite💁‍♀️.")
        elif excedeu_saques:
            print("Desculpe, a operação falhou! Número máximo de saques excedido😒.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido😒.")
        return saldo, extrato, numero_saques

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função principal
def main():
    global saldo, extrato, numero_saques

    print("Seja bem-vindo(a) ao sistema bancário!")

    while True:
        opcao = input(exibir_menu())

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "nc":
            criar_conta()

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            print("Obrigado por usar nosso sistema! Até a próxima!")
            break
        
        else:
            print("Operação inválida, por favor selecione uma operação válida💁‍♀️.")

# Executar o programa principal
main()
