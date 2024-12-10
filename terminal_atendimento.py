from sisbanco import *

def terminal():
    sisbanco = Banco()
    while(True):
        print("SisBanco::Bem-Vindo!")
        print(".::Opcoes::.")
        print("[0]-Criar_Conta")
        print("[1]-Creditar")
        print("[2]-Debitar")
        print("[3]-Transferir")
        print("[4]-Consultar_Saldo")
        print("[5]-Render_Juros")
        print("[6]-Render_Bônus")
        print("[7]-Alterar_Taxa_de_Juros")
        print("[8]-Sair")

        opcao = int(input("Digite: "))

        if opcao == 0:
            tipo = str(input("S - Simples | P - Poupança | E - Especial\nDigite o tipo de Conta: "))
            numero = str(input("Digite o número da conta: "))
            if tipo == "S":
                conta = Conta(numero)
            elif tipo == "P":
                conta = ContaPoupanca(numero)
            elif tipo == "E":
                conta = ContaEspecial(numero)
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
        elif opcao == 8:
            print("Sisbanco::Bye!")
            break
        elif opcao == 5:
            numero = str(input("Digite o número da conta: "))
            sisbanco.render_juros(numero)
        elif opcao == 6:
            numero = str(input("Digite o número da conta: "))
            sisbanco.render_bonus(numero)
        elif opcao == 7:
            taxa = float(input("Digite a nova taxa: "))
            sisbanco.set_taxa(taxa)
        else:
            print("Ação Inválida!")

terminal()