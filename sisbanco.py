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

class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)
    
    def render_juros(self,taxa):
        self.creditar(self.get_saldo()*taxa)
    
class ContaEspecial(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.__bonus = 0

    def render_bonus(self):
        super().creditar(self.__bonus)
        self.__bonus = 0
    
    def creditar(self, valor):
        self.__bonus += valor*0.01
        super().creditar(valor)

class ContaImposto(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.__taxa = 0.001

    def debitar(self, valor):
        self.__saldo -= (valor + valor*self.__taxa) 

    def get_taxa(self):
        return self.__taxa

    def set_taxa(self,taxa):
        self.__taxa = taxa


class Banco:
    def __init__(self):
        self.__contas = []
        self.__taxa = 0.01
    
    def get_taxa(self):
        return self.__taxa
    
    def set_taxa(self, taxa):
        self.__taxa = taxa

    
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
    
    def render_juros(self, numero):
        conta = self.procurar(numero)
        if (conta is not None) and (isinstance(conta,ContaPoupanca)):
            conta.render_juros(self.__taxa)
        else:
            return None
        
    def render_bonus(self,numero):
        conta = self.procurar(numero)
        if (conta is not None) and (isinstance(conta,ContaEspecial)):
            conta.render_bonus()
        else:
            return None
