from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Esta es una app desplegada en Heroku!'


if __name__ == '__main__':
    app.run()