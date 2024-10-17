from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<p>hello World! good luck!</p>"


@app.route("/teste")
def teste_git():
    return "<body><p>teste do git!</p></body>"


if __name__ == '__main__':
    app.run(host="localhost", port=1337, debug=True)
