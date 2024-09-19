from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key="lamborgini"

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='rigo_dev'
app.config['MYSQL_PASSWORD']='123456Ab'
app.config['MYSQL_DB']='renta_autos'

base_datos = MySQL(app)

@app.route('/inicio')
def arranca():
    mensajes = {
    'alerta': 'Bienvenido',
    'sistema':  'Sistema de renta de vehiculos',
    }
    lista = base_datos.connection.cursor()
    lista.execute("Select * from autos ")
    muestra = lista.fetchall()
    return render_template('autos/index.html', ventana = mensajes, autos = muestra)

@app.route('/guarda_renta', methods = ['POST'])
def guarda_renta():
    if request.method == 'POST':
        fol = request.form['folio']
        fe = request.form['fecha']
        tipo = request.form['auto']
        est = request.form['estado']
        des = request.form['descripcion']
        costo = request.form['crenta']
        dias = request.form['dias_renta']
        fent = request.form['fe_entrega']
        ab = request.form['abono']
        iusuario = request.form['usuario']
        cliente = request.form['cliente']
        obs = ' '
        penal = ''
        resto = 'Pendiente'
    
        #guarda_carro = base_datos.connection.cursor(MySQLdb.cursors.DictCursor)
        guarda_carro = base_datos.connection.cursor()
        guarda_carro.execute('''INSERT INTO renta (id_usuario, id_cliente, id_auto, folio, fecha, descripcion, fecha_entrega, cobro, abono, resto, dias_renta, estatus, observaciones, penalizaciones)
                            VALUES(%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(iusuario, cliente, tipo, fol, fe, des, fent, costo, ab, resto, dias, est,obs, penal))
        
        guarda_carro.execute("Update autos set estado='2' where id=%s",(tipo))
        base_datos.connection.commit()
        guarda_carro.close()
        return redirect(url_for('rentados'))
    else:
        mensaje_error = 'Error en la captura'
        return render_template('autos/index.html', mensaje = mensaje_error)

@app.route('/rentados')
def rentados():
    mensajes = {
    'alerta': 'Ventana de Listado',
    'sistema':  'Sistema de renta de vehiculos',
    }

    lista = base_datos.connection.cursor()
    lista.execute('''Select autos.marca, autos.modelo, autos.year, renta.fecha, renta.descripcion, renta.cobro, renta.abono,renta.resto,
                    renta.dias_renta, renta.folio, renta.id from renta JOIN 
                    autos ON autos.id = renta.id_auto
                  ''')
    #lista.execute("Select * from renta where resto='Pendiente' ")
    muestra = lista.fetchall()
    return render_template('autos/rentados.html', ventana = mensajes, datos = muestra)

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

@app.route('/borrado/<int:id>/')
def borrado(id):
    borra = base_datos.connection.cursor()
    borra.execute("Delete from renta where id=%s",(id,))
    borra.connection.commit()
    return redirect(url_for('rentados'))
    #return "Borrando Datos"
    borra.close()

@app.route('/modifica/<id>')
def modifica(id):
    mensajes = {
    'alerta': 'Registro Encontrado',
    'sistema':  'Sistema de renta de vehiculos',
    }
    titulo = "Registro  a Modificar"
    modificar = base_datos.connection.cursor()
    modificar.execute("Select * from renta where id=%s",(id,))
    datos = modificar.fetchall()
    modificar.close()
    return render_template('autos/datos_renta.html', mensaje = titulo, datos_renta = datos[0], ventana=mensajes)

@app.route('/actualiza_datos/<int:id>', methods = ['POST'])
def actualiza_datos(id):
    i=request.form['id']
    fol = request.form['folio']
    fe = request.form['fecha']
    edo = request.form['estado']
    costo = request.form['crenta']
    dias = request.form['dias_renta']
    feent = request.form['fe_entrega']
    abono = request.form['abono']
    resto = request.form['resto']
    obs = request.form['obs']
    pen = request.form['penalizados']

    editar = base_datos.connection.cursor()
    editar.execute("Update renta set observaciones=%s, resto=%s, estatus=%s, penalizaciones = %s where id=%s",(obs, resto,edo,pen,id))
    editar.close()
    return redirect(url_for('rentados'))
    

@app.route('/captura')
def captura_usuarios():
    mensajes = {
    'alerta': 'Ventana de captura de usuarios',
    'usuario':  'Visitante',
    'sistema':  'Sistema de renta de vehiculos',
    }
   
    return render_template ('usuarios/captura_usuarios.html', ventana=mensajes)

@app.route('/guarda_usuario', methods = ['POST', 'GET'])
def guarda_usuario():
    if request.method == 'POST':
        nom = request.form['nombre']
        ap = request.form['ap']
        user = request.form['usuario']
        password = '123'
        encriptado = generate_password_hash(password, method='scrypt')
        
        guarda = base_datos.connection.cursor(MySQLdb.cursors.DictCursor)
        guarda.execute(''' INSERT INTO usuarios (usuario, clave, nombre, apellidos)
                       VALUES (%s, %s, %s, %s)''', (user, encriptado, nom, ap))
        base_datos.connection.commit()
        guarda.close()
        return redirect (url_for('usuarios_exito'))
    else:
        mensaje = 'Existe un error en los datos verifica'
        return render_template('usuarios/captura_usuarios.html', msj = mensaje)

@app.route('/success')
def usuarios_exito():
    mensajes = {
    'alerta': 'Rent | Car',
    'usuario':  '',
    'sistema':  'Sistema de renta de vehiculos',
    'mensajes':'El usuario se guardo exitosamente'
    }
    
    return render_template("usuarios/exito.html", ventana = mensajes)

@app.route('/login')
def login_usuarios():
    mensajes = {
    'alerta': 'Ventana de Login',
    'usuario':  'Visitante',
    'sistema':  'Sistema de renta de vehiculos',
    }
    return render_template ('usuarios/login.html', ventana=mensajes)

@app.route('/val_login', methods = ['POST'])
def val_login():
        if request.method == 'POST':
            user = request.form['usuario']
            contra = request.form['clave']
            q = base_datos.connection.cursor()
            q.execute("Select * from usuarios where usuario = %s", (user,))
            us = q.fetchone()
            
            if us and check_password_hash(us[2],contra):
                session['usuario'] = us[1]
                return redirect(url_for('arranca'))
            else:
                return "Los datos son incorrectos"
        return render_template('usuarios/login.html')

app.run(debug= True, port=1800)
