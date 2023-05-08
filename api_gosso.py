#!/usr/bin/python3

import flask
import gosso

app = flask.Flask(__name__)

@app.route("/perro/<edad_perro>")
def edad(edad_perro):
    perro = int(edad_perro)
    un_gos = gosso.Gosso(perro)
    un_gos.calculo_edad()
    return str(un_gos)

def main():
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    main()