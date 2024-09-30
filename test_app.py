import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_valid_expression(self):
        response = self.app.post('/calculate', data=dict(expression='2+3'))
        self.assertIn(b'Resultado: 5', response.data)

    def test_invalid_expression(self):
        response = self.app.post('/calculate', data=dict(expression='2/0'))
        self.assertIn(b'Erro', response.data)

    def test_clear_expression(self):
        response = self.app.post('/calculate', data=dict(expression=''))
        self.assertNotIn(b'Resultado', response.data)

    def test_multiply_expression(self):
        response = self.app.post('/calculate', data=dict(expression='3*4'))
        self.assertIn(b'Resultado: 12', response.data)

if __name__ == '__main__':
    unittest.main()
