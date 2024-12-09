from sisbanco import Banco, Conta

def terminal():
    sisbanco = Banco()
    while(True):
        print("SisBanco::Bem-Vindo!")
        print(".::Opcoes::.")
        print("[0]−CriarConta")
        print("[1]−Creditar")
        print("[2]−Debitar")
        print("[3]−Transferir")
        print("[4]−Saldo")
        print("[5]−Sair")

        opcao = int(input("Digite: "))

        if opcao == 0:
            numero = str(input("Digite o número da conta: "))
            conta = Conta(numero)
            sisbanco.cadastrar(conta)
        elif opcao == 1:
            numero = str(input("Digite o número da conta: "))
            valor = float(input("Digite o valor: "))
            sisbanco.creditar(numero,valor)
        elif opcao == 2:
            numero = str(input("Digite o número da conta: "))
            valor = float(input("Digite o valor: "))
            sisbanco.debitar(numero,valor)
        elif opcao == 3:
            numero_origem = str(input("Digite o número da conta de origem: "))
            numero_destino = str(input("Digite o número da conta destino: "))
            valor = float(input("Digite o valor: "))
            sisbanco.transferir(numero_origem,numero_destino,valor)
        elif opcao == 4:
            numero = str(input("Digite o número da conta: "))
            print(f"{sisbanco.saldo(numero):.2f}")
        elif opcao == 5:
            print("Sisbanco::Bye!")
            break
        else:
            print("Ação Inválida!")

terminal()