#Librerias a usar
from ast import expr
from distutils.log import debug
import string
from flask import Flask
from flask import Flask, jsonify
import math
import sympy

app = Flask(__name__)

#metodo de biseccion
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
    

#Método de la regla falsa
@app.route('/reglaFalsa/<string:dato1>/<string:dato2>/<string:dato3>/<string:dato4>')
def reglaFalse(dato1,dato2,dato3,dato4):
    inicial = float(dato1)
    final = float(dato2)
    tol = float(dato3)
    op = int(dato4)
    c = float(0)

    if(funcion(inicial)*funcion(final)>0):
        print('No se cumple la condición')
        return jsonify({"reglaFalsa" : reglaFalsa})
    else:
        while(1>0):
            c = ((funcion(final)*inicial) - (funcion(inicial)*final)) / (funcion(final)-funcion(inicial))
            if(funcion(c)<=tol):
                reglaFalsa = c 
                return jsonify({"reglaFalsa" : reglaFalsa})
            elif(funcion(inicial) * funcion(c)<0):
                final = c
            else:
                inicial = c


#Método de newthon raphson
@app.route('/raphson/<string:dato1>/<string:dato2>')
def newthon(dato1,dato2):
    dato1 = float(dato1)
    dato2 = float(dato2)
    iteraciones = int(0)
    error= bool(True)
    x1 = float(0.0)
    while(error and iteraciones<1000):
        x1 = dato1 - (funcion1(dato1)/derivada(dato1))
        iteraciones+=iteraciones
        if(funcion1(x1)<=dato2):
            error = False
            raphson = funcion1(x1)
            return jsonify({ "raphson" : raphson})

def funcion1(x):
    return math.atan(math.cos(x))

def derivada(x):
    return -(math.sin(x)/1+x**2)



#Puerto del servidor
if __name__ == '__main__':
    app.run(debug=True, port=4000)