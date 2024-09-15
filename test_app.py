import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Testa se a página inicial carrega com sucesso"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Calculadora' in response.data
