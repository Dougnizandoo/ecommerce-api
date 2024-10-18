from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>hello World! good luck!</p>"


@app.route("/teste")
def teste_git():
    return "<body><p>teste do git!</p></body>"


@app.route("/Produtos")
def produtos():
    response = jsonify([
        {
            "title": "Caneca Personalisada de Porcelana",
            "amount": 123.45,
            "installments": {"number": 3, "total": 41.15, "hasFee": True}
        },
        {
            "title": "Caneca do Goku",
            "amount": 149.99,
            "installments": {"number": 3, "total": 50.00}
        }
    ])

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=6789, debug=True)
