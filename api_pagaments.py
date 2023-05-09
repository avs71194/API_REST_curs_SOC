#!/usr/bin/python3

import flask
import pagaments

app = flask.Flask(__name__)

@app.route("/pagament/<total>/<pagado>")
def pago(total, pagado):
    pagado = int(pagado)
    total =  int(total)
    el_canvi = pagaments.Pagaments(total, pagado)
    el_canvi.canvi()
    return str(el_canvi)

def main():
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    main()