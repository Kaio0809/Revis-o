class Conta:
    def __init__(self,numero):
        self.__numero = numero
        self.__saldo = 0.0

    def creditar(self, valor):
        self.__saldo += valor

    def debitar(self, valor):
        self.__saldo -= valor

    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo
    
class Banco:
    def __init__(self):
        self.__contas = []
    
    def cadastrar(self, conta:Conta):
        self.__contas.append(conta)
    
    def procurar(self, numero):
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        else:
            return None
    
    def creditar(self, numero, valor):
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)
        else:
            return None
    
    def debitar(self, numero, valor):
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)
        else:
            return None
    
    def saldo(self, numero):
        conta = self.procurar(numero)
        if conta is not None:
            return conta.get_saldo()
        else:
            return None
    
    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar(origem)
        conta_destino = self.procurar(destino)
        if (conta_destino is not None) and (conta_origem is not None):
            conta_origem.debitar(valor)
            conta_destino.creditar(valor)
        else:
            return None
        
