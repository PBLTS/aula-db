from flask import Flask, request, jsonify, make_response
import json
from flask_mysqldb import MySQL



class ClienteModel():

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


    def cadastrarEmail():
        nome = 'Alexandre'
        email = 'aaaa@aaaa.com'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO clientes VALUES(%s,%s)''',(nome,email))
        mysql.connection.commit()
        cursor.close()

        return 'Criado com sucesso'




    def atualizar():
        #regra de negocio
        #Banco de dados e atualizando os dados
        return 'Atualizado com sucesso'
