# api - interface que disponibiliza algum serviço.
#Via cep -> disponibiliza o endereço.

import requests

print("Verificando endereço")
cep = input("Digite o cep: ")
if len(cep) != 8:
    print("cep inválido!")
    exit()
consulta = requests.get(f'https://viacep.com.br/ws/{cep}/json')
print(consulta.json())

