from flask import Flask, request, jsonify
from db import db
from models import Agendamento

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///agendamentos.db"
db.init_app(app)

# endpoint agendamento

# endpoint consulta

# endpoint cancelamento


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()