from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Esta es una app desplegada en Heroku!</h1><br><h2>Un subtítulo casual</h2>'


if __name__ == '__main__':
    app.run()