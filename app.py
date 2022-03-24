from distutils.log import debug
from flask import Flask
from flask import Flask, jsonify
import math
import sympy

app = Flask(__name__)

@app.route('/biseccion/<string:inicial>/<string:final>/<string:tolerancia>/<string:dato>')
def metodo(inicial, final, tolerancia,dato):
    inicial = float(inicial)
    final = float(final)
    tol = float(tolerancia)
    dato = dato.replace('%','/')
    r = float(0)
    
    error = float(100)


    fa = float(0)
    fb = float(0)
    fc = float(0)
    xold = float(0)

    fa = funcion(inicial,dato)
    fb = funcion(final,dato)
    iterador = int(0)

    if(fa*fb>0):
        biseccion = print('el intervalo no es valido')
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

def funcion(a,dato):
    x = sympy.symbols('x')
    return sympy.sympify(dato).subs(x,a)

#Método de la regla falsa
@app.route('/reglaFalsa/<string:dato1>/<string:dato2>/<string:dato3>/<string:dato4>')
def reglaFalse(dato1,dato2,dato3,dato4):
    inicial = float(dato1)
    final = float(dato2)
    tol = float(dato3)
    dato4 = dato4
    c = float(0)
    
    if(funciones(inicial,dato4)*funciones(final,dato4)>0):
        reglaFalsa = print('No se cumple la condición')
        return jsonify({"reglaFalsa" : reglaFalsa})
    else:
        while(1>0):
            c = ((funciones(final,dato4)*inicial) - (funciones(inicial,dato4)*final)) / (funciones(final,dato4)-funciones(inicial,dato4))
            if(funciones(c,dato4)<=tol):
                reglaFalsa = c
                break  
            elif(funciones(inicial,dato4) * funciones(c,dato4)<0):
                final = c
            else:
                inicial = c

    return jsonify({"reglaFalsa":str(reglaFalsa)})

def funciones(a,datos):
    x = sympy.symbols('x')
    return sympy.sympify(datos).subs(x,a)




if __name__ == '__main__':
    app.run(debug=True, port=5000)

