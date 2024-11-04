import sqlalchemy
from flask import Flask, render_template, request, flash, Response, render_template_string, jsonify, url_for, redirect
from flask_restful import Api, Resource
import json
from sqlalchemy import select

from models import Esmalte, db_session, Funcionario

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return redirect('/login')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/add_login', methods=['GET', 'POST'])
def add_login():
    if request.method == 'POST':
        if not request.form.get('form_cpf'):
            flash("*Preencher Cpf", "error")
        if not request.form.get('form_senha'):
            flash("*Preencher senha", "error")
        else:
            form_login = login(cpf=request.form.get('form_cpf'), senha=request.form.get('form_senha'))
            form_login.save()
            flash("Logado com sucesso!", "success")
            return url_for('home')

    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('dashboard.html')


@app.route('/inventario')
def inventario():
    return render_template('inventario.html')


@app.route('/cadastro_dep', methods=['GET', 'POST'])
def cadastro_dep():
    if request.method == 'POST':
        if not request.form.get('form_nome'):
            flash("*Preencher Nome", "error")
        if not request.form.get('form_cpf'):
            flash("*Preencher Cpf", "error")
        if not request.form.get('form_senha'):
            flash("*Preencher senha", "error")
        else:
            form_cadastro_dep = cadastro_dep(nome=request.form.get('form_nome'), cpf=request.form.get('form_cpf'),
                                             senha=request.form.get('form_senha'))
            form_cadastro_dep.save()
            flash("cadastrado com sucesso!", "success")
            return url_for('login')
    return render_template('cadastro_dep.html')


@app.route('/retirar')
def retirar():
    return render_template('retirar.html')


@app.route('/colecao')
def colecao():
    return render_template('colecao.html')


@app.route('/cadastro_esmalte')
def cadastro_esmalte():
    return render_template('cadastro_esmalte.html')


@app.route('/cadastro_marca')
def cadastro_marca():
    return render_template('cadastro_marca.html')


@app.route('/cad_moviment')
def cad_moviment():
    return render_template('cad_moviment.html')


@app.route('/moviment')
def moviment():
    return render_template('moviment.html')


esmaltes = {}


@app.route('/esmaltes', methods=['GET'])
def get_esmaltes():
    return jsonify(Esmalte)


@app.route('/add_esmalte', methods=['POST', 'GET'])
def add_esmalte():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['marca'] or not request.form['quantidade']:
            flash('Preencher todos os campos')
        else:
            nome = request.form.get('nome')
            marca = request.form.get('marca')
            quantidade = request.form.get('quantidade')

            esmalte = Esmalte(nome, marca, quantidade)
            esmalte.save()
            flash('O esmalte foi cadastrado')
            return redirect(url_for('get_esmaltes'))

    return render_template('esmalte.html')


# select


if __name__ == '__main__':
    app.run(debug=True)
