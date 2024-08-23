from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def arranca():
    titulo = "Catalogo de Autos Disponibles"
    cabecera = "Rent | Car"
    return render_template('autos/index.html', letrero=titulo, head=cabecera)
    #return "Primer Flask Fallaste chiquitin"


app.run(debug= True, port=1800)
