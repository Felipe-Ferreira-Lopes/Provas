from q1 import Pessoa, Vendedor, Cliente, Compra

v1 = Vendedor('felipe', 20, 1200)
c1 = Cliente('alisson', 20)
c1.registrar_compra(v1, 20)

print(f'nome v1: {v1.nome}, idade v1: {v1.idade}, v1 salario: {v1.salario}, nome c1: {c1.nome}, idade c1: {c1.idade}')