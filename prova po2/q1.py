import datetime

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
                
    

class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.compras = []

    def __iter__(self):
        return self.compras.__iter__()

    def registrar_compra(self, compra, **kwargs):
        self.compra = Compra()
        self.compras.append(compra)
    
    def total_compras(self):
        total = 0
        for x in compras:
            total += valor 
        print(f'valor total: {total}')
    def get_data_ultima_compra(self):
        for i in compras:
            ultima = data
        print(f'ultima compra {ultima}')
    
    
class Compra:
    def __init__(self, vendedor, valor):
        self.vendedor = Vendedor()
        self.data = datetime.now()
        self.valor = valor

