# api - interface que disponibiliza algum serviço.
#Via cep -> disponibiliza o endereço.

import requests
import mysql.connector

nome = input("Digite seu nome: ")
cep = input("Digite o cep: ")
if len(cep) != 8:
    print("cep inválido!")
    exit()
link = f'https://viacep.com.br/ws/{cep}/json'
requisicao = requests.get(link)
endereco = requisicao.json()
cep = endereco['cep']
logradouro = endereco['logradouro']
complemento = endereco['complemento']
bairro = endereco['bairro']
localidade = endereco['localidade']
uf = endereco['uf']

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='desafio_B'
)
meucursor = banco.cursor()
sql = 'insert into enderecos (nome,logradouro,complemento,cep,bairro,localidade,uf) values (%s,%s,%s,%s,%s,%s,%s)'
data = (nome,logradouro,complemento,cep,bairro,localidade,uf)
meucursor.execute(sql,data)
banco.commit()