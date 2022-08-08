from flask import json, request, jsonify
import flask
from bson import json_util
from app import app
from app import db
from bson.objectid import ObjectId

@app.route('/')
@app.route('/index')
def index():
    return flask.jsonify(json.loads(json_util.dumps(db.livros.find({}).sort("_id", 1))))

@app.route('/reserva')
def reserva():
    return flask.jsonify(json.loads(json_util.dumps(db.livrosReservados.find({}).sort("_id", 1))))

@app.route('/criarLivro', methods=['POST'])
def criarLivro():
    json_data = request.json
    if json_data is not None:
        db.livros.insert_one(json_data)
        return jsonify(mensagem='Livro adicionado')
    else:
        return jsonify(mensagem='Livro não adicionado')

@app.route("/getid/<string:userId>")
def getid(userId):
    livros = db.livros.find_one({"_id": ObjectId(userId)})
    return flask.jsonify(json.loads(json_util.dumps(livros)))

@app.route("/deletarLivro/<string:userId>")
def deletarLivro(userId):
    result = db.livros.delete_one({"_id": ObjectId(userId)})
    if(result.deleted_count > 0):
        return jsonify(mensagem='Livro removido')
    else:
        return jsonify(mensagem='Livro não removido')

#@app.route("/getid/<string:idremUsuario>")
#def getid(userId):
 #   usuario = db.usuario.find_one({"_id": ObjectId(userId)})
  #  return flask.jsonify(json.loads(json_util.dumps(usuario)))

@app.route("/removerUsuario/<string:userId>")
def removerUsuario(userId):
    result = db.usuario.delete_one({"_id": ObjectId(userId)})
    if(result.deleted_count > 0):
        return jsonify(mensagem='Usuário removido')
    else:
        return jsonify(mensagem='Usuário não removido')

@app.route("/getidreserva/<string:userId>")
def getidreserva(userId):
    livrosReservados = db.livrosReservados.find_one({"_id": ObjectId(userId)})
    return flask.jsonify(json.loads(json_util.dumps(livrosReservados)))

@app.route("/devolverLivro/<string:userId>")
def devolverLivro(userId):
    resultado = db.livrosReservados.delete_one({"_id": ObjectId(userId)})
    if(resultado.deleted_count > 0):
        return jsonify(mensagem='Livro devolvido')
    else:
        return jsonify(mensagem='Livro não devolvido')

@app.route('/atualizarLivro', methods=['POST'])
def atualizarLivro():
    json_data = request.json
    if json_data is not None and db.livros.find_one({"_id": ObjectId(json_data["id"])}) is not None:
        db.livros.update_one({'_id': ObjectId(json_data["id"])}, {"$set": 
        {'titulo': json_data["titulo"], 'autores': json_data["autores"], 'editora': json_data["editora"], 
        'ano': json_data["ano"], 'isbn': json_data["isbn"], 'preco': json_data["preco"]}})
        return jsonify(mensagem='Livro atualizado')
    else:
        return jsonify(mensagem='Livro atualizado')

@app.route('/cadastrarFuncionario', methods=['POST'])
def cadastrarFuncionario():
    json_data = request.json
    if json_data is not None:
        db.funcionario.insert_one(json_data)
        return jsonify(mensagem='Cadastro realizado')
    else:
        return jsonify(mensagem='Cadastro não realizado')

@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    json_data = request.json
    if json_data is not None:
        db.usuario.insert_one(json_data)
        return jsonify(mensagem='Cadastro realizado')
    else:
        return jsonify(mensagem='Cadastro não realizado')

@app.route('/alugarLivro', methods=['POST'])
def alugarLivro():
    json_data = request.json
    if json_data is not None:
        db.livrosReservados.insert_one(json_data)
        return jsonify(mensagem='Livro reservado')
    else:
        return jsonify(mensagem='Livro não reservado')
