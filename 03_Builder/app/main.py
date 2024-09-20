from flask import Flask 
from flask import render_template
from clases.builder_form.login_builder import LoginBuilder
from clases.builder_form.register_builder import RegisterBuilder
from clases.builder_form.recover_builder import RecoverBuilder
from clases.builder_form.form_builder_director import FormBuilderDirector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', dato=[])


@app.route('/login/')
def login():
    builder = LoginBuilder()
    director = FormBuilderDirector(builder)
    director.contruct_login()
    form = builder.build()
    return render_template('index.html', dato=form)


@app.route('/registro/')
def registro():
    builder = RegisterBuilder()
    director = FormBuilderDirector(builder)
    director.construct_registro_de_usuario()
    form = builder.build()
    return render_template('index.html', dato=form)


@app.route('/recuperar_contrasenia/')
def recuperar_contrasenia():
    builder = RecoverBuilder()
    director = FormBuilderDirector(builder)
    director.construct_recuperar_contrasenia()
    form = builder.build()
    print(form)
    return render_template('index.html', dato=form)
