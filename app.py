import json
import sqlite3
from flask import Flask
from flask_restful import Resource, Api

banco = sqlite3.connect("bd_crud")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Clientes (id INT PRIMARY KEY, Nome text, Nascimento text, Foto text, endereco text, sexo text, password text, email text, pais text estado text, cidade text, cep text)")

app = Flask(__name__)
api = Api(app)

class User:
    def __init__(self, nome, nascimento, foto, endereco, sexo, password, email,pais, estado, cidade,cep):
        self.Nome = nome
        self.Nascimento = nascimento
        self.Foto = foto
        self.Endereco = endereco
        self.Estado = estado
        self.Cidade = cidade
        self.Cep = cep
        self.Pais = pais
        self.Sexo = sexo
        self.Password = password
        self.Email = email

class Users(Resource) :
    def get(self):
        return "ta foda"

api.add_resource(Users,'/Users')

if __name__ == '__main__' :
    app.run(debug=True)