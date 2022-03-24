from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify
import math
import sympy

app = Flask(__name__)

@app.route('/biseccion/<string:inicial>/<string:final>/<string:tolerancia>/<string:dato>')
def get_datosD(inicial,final,tolerancia,dato):
    inicial = float(inicial)
    final = float(final)
    tol = float(tolerancia)
    dato = dato.replace('&','/')
    r = float(0)
    error = float(100)

    #variables
    fa = float(0)
    fb = float(0)
    fc = float(0)
    xold = float(0)
    fa = funcion(inicial,dato)
    fb = funcion(final,dato)

    iterador = int(0)
    
    if(fa*fb>0):
        biseccion = print('El intervalo no es valido')
        return jsonify({ "biseccion" : biseccion})
        
    while(error>tol):
        r = (inicial+final)/2
        fc=funcion(r,dato)
        if(fa*fc>0):
                inicial = r
                fa = fc
        else:
            final = r
            fb = fc

        iterador +=1
        error = abs( ((r-xold)/r)*100)
        xold = r
        biseccion = r
    return jsonify({ "biseccion" : biseccion})
    
#funciones
def funcion(a,exp):
    x = sympy.symbols('x')
    return sympy.sympify(exp).subs(x,a)

if __name__ == '__main__':
    app.run(debug=True, port=4000)