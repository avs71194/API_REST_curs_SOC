#!/usr/bin/python3

import flask
import radar

app = flask.Flask(__name__)

@app.route("/radar/<velocidad_coche>/<velocidad_via>")
def edad(velocidad_coche, velocidad_via):
    velocidad = float(velocidad_coche)
    permitido = float(velocidad_via)
    calculo = radar.Radar(velocidad, permitido)
    final = calculo.calculo_velocidad()
    return str(final)

def main():
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    main()