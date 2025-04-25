from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Esta es una app desplegada en Heroku!</h1>'


if __name__ == '__main__':
    app.run()