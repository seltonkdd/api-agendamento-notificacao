from db import db

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime)
    email_destinatario = db.Column(db.String(255), nullable=False)
    telefone_destinatario = db.Column(db.String(255), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum('AGENDADO', 'ENVIADO', 'CANCELADO', name='status_enum'))


    def as_dict(self):
        return {
            'id': self.id,
            'data_hora': self.data_hora,
            'email_destinatario': self.email_destinatario,
            'telefone_destinatario': self.telefone_destinatario,
            'mensagem': self.mensagem,
            'status': self.status
        }