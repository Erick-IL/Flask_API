from flask import Flask
from app.controller import users


app = Flask(__name__)
app.register_blueprint(users.blueprint)

@app.route('/')
def home():
    return "Flask está funcionando!"

if __name__ == '__main__':
        app.run(debug=True)