from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def arranca():
    titulo = "Catalogo de Autos Disponibles"
    cabecera = "Rent | Car"
    return render_template('autos/index.html', letrero=titulo, head=cabecera)
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
    'usuario':  'Visitante',
    'sistema':  'Sistema de renta de vehiculos',
    }
   
    return render_template ('autos/listado_autos.html', ventana=mensajes)

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
