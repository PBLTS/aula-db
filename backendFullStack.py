from flask import Flask, jsonify, request, json
import mysql.connector

bancoDeDados = mysql.connector.connect(host="localhost",user="root",password="password",database="db_Alunos")

app = Flask(__name__)

@app.route('/listarTodos', methods=['GET'])
def listarAlunos():
    selectAllSql = f"select * from tb_aluno"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()

    return jsonify(resultado)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = json.loads(request.data)
    nome = data.get("nome", None)
    turma = data.get("turma", None)
    disci = data.get("disciplina", None)
    query = "INSERT INTO tb_aluno (nome, turma,disciplina) VALUES (%s, %s, %s)"
    val = (nome, turma, disci)
    cursor = bancoDeDados.cursor()
    cursor.execute(query, val)
    bancoDeDados.commit()
    return "Cadastrado"

if __name__ == '__main__':
    app.run( port=5000, debug=True)
