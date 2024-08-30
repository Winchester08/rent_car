from flask import Flask, render_template
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='rigo_dev'
app.config['MYSQL_PASSWORD']='123456Ab'
app.config['MYSQL_DB']='renta_autos'

base_datos = MySQL(app)

@app.route('/inicio')
def arranca():
    titulo = "Catalogo de Autos Disponibles"
    
    return render_template('autos/index.html', letrero=titulo,)
    #return "Primer Flask Fallaste chiquitin"

@app.route('/renta')
def renta_autos():
    mensajes = {
    'alerta': 'Ventana de Rentas',
    'usuario':  'Visitante',
    'sistema':  'Sistema de renta de vehiculos',
    }
   
    return render_template ('autos/renta.html', ventana=mensajes)

@app.route('/lista')
def listados_autos():
    mensajes = {
    'alerta': 'Ventana de Listado',
    'sistema':  'Sistema de renta de vehiculos',
    }
    lista = base_datos.connection.cursor()
    lista.execute("Select * from autos ")
    muestra = lista.fetchall()
    return render_template ('autos/listado_autos.html', ventana=mensajes, muestra=muestra)

@app.route('/captura')
def captura_usuarios():
    mensajes = {
    'alerta': 'Ventana de captura de usuarios',
    'usuario':  'Visitante',
    'sistema':  'Sistema de renta de vehiculos',
    }
   
    return render_template ('usuarios/captura_usuarios.html', ventana=mensajes)

@app.route('/login')
def login_usuarios():
    mensajes = {
    'alerta': 'Ventana de Login',
    'usuario':  'Visitante',
    'sistema':  'Sistema de renta de vehiculos',
    }
    return render_template ('usuarios/login.html', ventana=mensajes)

app.run(debug= True, port=1800)
