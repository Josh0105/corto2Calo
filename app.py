from flask import Flask, request, jsonify

app = Flask(__name__)

def inversa(cadena):
    cadena_inversa=""
    for caracter in cadena:
        cadena_inversa= caracter + cadena_inversa
    return cadena_inversa

def validar_nit(nit):
    nit_n = nit.replace(' ', '')
    nit_ok = nit_n.replace('-', '')
    base = 1

    dig_validador = nit_ok[-1]
    dig_nit = list(nit_ok[0:-1])
    #dig_nit_rev = dig_nit.reverse()  # None


    try:
        suma = 0
        for n in dig_nit:
            base += 1
            suma += int(n) * base
        resultado = suma % 11
        comprobacion = 11 - resultado
        if suma >= 11:
            resultado = suma % 11
            comprobacion = 11 - resultado
        if comprobacion == 10:
            if dig_validador.upper() == 'K':
                return True
        elif comprobacion == int(dig_validador):
            return True
        else:
            return False
    except:
        return False

@app.route("/misDatos", methods=["GET"])
def metodoGet():

    if request.method == "GET":

        return {
            'carne' : "201213330",
            'nombre': "Jonathan Josué Calo Hernández"
        }

@app.route("/inversor", methods=["POST"])
def metodoPost():

    if request.method == "POST":

        cadena = request.form.get('cadena_entrada')
        resultado = inversa(cadena)
        
        return {
            'resultado' : resultado
        }

@app.route("/comprobarNIT", methods=["POST"])
def metodoPostNit():

    if request.method == "POST":
        nit = request.form.get('no_nit')
        resultadoNIT = validar_nit(nit)

        return {
            'resultado' : resultadoNIT
        }

@app.route("/")
def index():
    return "<h1>" + "</h1>"


if __name__ == "__main__":
    app.run(threaded=True, port=5000,debug=True)