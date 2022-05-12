from flask import Flask
from flask import Flask, jsonify
from random import * 


app = Flask(__name__)

@app.route('/costoEnvio/<string:peso>/<string:alto>/<string:largo>/<string:ancho>')
def calcularEnvio(peso,alto,largo,ancho):
    peso = float(peso)
    alto = float(alto)
    largo = float(largo)
    ancho = float(ancho)
    costo = float(0)
    
    costo = (largo*ancho*alto/6000)

    if(costo<5):
        costoEnvio = costo
    elif(costo>=5):
        costoEnvio = costo + 88.34 
    elif(costo<=20.00):
        costoEnvio = costo + 100.18
    elif(costo>=35.00):
        costoEnvio = costo + 118.50
    elif(costo<=45.00):
        costoEnvio = costo + 125.00
    elif(costo>= 54.00):
        costoEnvio = costo + 131.50
    elif(costo<= 66):
        costoEnvio = costo + 138.00
    elif(costo>=70):
        costoEnvio = costo + 151.00
    
    costoEnvio = round(costoEnvio,2)

    return jsonify({ "costoEnvio" : costoEnvio})

#generarID
@app.route('/numAlt/<string:algo>')
def numAleat(algo):
    valor = float(algo)
    idPaquete = float(0)

    idPaquete = randint(1000000, 10000000000)

    if(idPaquete!=idPaquete):
            numAlt = idPaquete
            return jsonify({ "numAlt" : numAlt})
    else:
        idPaquete = randint(10000, 1000000)
        numAlt = idPaquete
        return jsonify({ "numAlt" : numAlt})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
