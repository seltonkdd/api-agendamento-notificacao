from db import db
from api_agendamento import app
import pytest

@pytest.fixture
def client():
    """Configuração do ambiente de testes"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
    
    client = app.test_client()
    yield client

    with app.app_context():
        db.drop_all()


def test_create_agendamento(client):
    """Teste para criar um agendamento"""
    print("\n=== Teste: Criando um Agendamento ===")
    response = client.post('/agendamento', json={
        'email_destinatario': 'teste@example.com',
        'telefone_destinatario': 1199999999,
        'mensagem': 'Teste de agendamento'
    })
    data = response.get_json()
    print(f"Resposta da API: {data}")

    assert response.status_code == 201
    assert 'mensagem' in data
    assert data['mensagem'] == 'Agendamento criado com sucesso'
