from flask import Flask, request, jsonify
from db import db
from datetime import datetime
from models import Agendamento

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///agendamentos.db"
db.init_app(app)

# endpoint agendamento
@app.route('/agendamento', methods=['POST'])
def create_agendamento():
    dados = request.get_json()
    data_hora = datetime.now()
    status = "AGENDADO"
    new_agendamento = Agendamento(data_hora=data_hora, 
                                  email_destinatario=dados['email_destinatario'], 
                                  telefone_destinatario=dados['telefone_destinatario'], 
                                  mensagem=dados['mensagem'],
                                  status=status)
    db.session.add(new_agendamento)
    db.session.commit()
    db.session.close()
    return jsonify({'mensagem': 'Agendamento efetuado com sucesso!'}), 201


# endpoint consulta
@app.route('/agendamento/<int:id>', methods=['GET'])
def get_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    return jsonify(agendamento.as_dict())


# endpoint cancelamento
@app.route('/agendamento/<int:id>', methods=['DELETE'])
def cancel_agendamento(id):
    data_hora = datetime.now()
    dados = {'mensagem': 'Seu agendamento foi cancelado às ' + str(data_hora),
             'status': 'CANCELADO'}
    agendamento = Agendamento.query.get_or_404(id)
    for key, value in dados.items():
        setattr(agendamento, key, value)
    db.session.commit()

    return jsonify(agendamento.as_dict()), 202


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()