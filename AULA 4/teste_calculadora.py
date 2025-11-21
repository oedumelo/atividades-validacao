import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

# ISSO precisa ser instalado:
# pip install unittest-xml-reporting
# pip install coverage
# USE um desses códigos para executar os casos de teste
# py -m unittest discover -v
# py -m unittest teste_calculadora.py

    def test_soma(self):
        self.assertEqual(Calculadora.soma(3, 2), 5)
        self.assertEqual(Calculadora.soma(-1, 1), 0)

    def test_subtracao(self):
        self.assertEqual(Calculadora.subtracao(3, 2), 1)
        self.assertEqual(Calculadora.subtracao(-1, 1), -2)

    def test_multiplicacao(self):
        self.assertEqual(Calculadora.multiplicacao(3, 2), 6)
        self.assertEqual(Calculadora.multiplicacao(-1, 5), -5)

    def test_divisao(self):
        self.assertEqual(Calculadora.divisao(6, 2), 3)
        self.assertEqual(Calculadora.divisao(9, 3), 3)

        # Divisão com resultado decimal
        self.assertAlmostEqual(Calculadora.divisao(7, 2), 3.5)

        # Teste de exceção para divisão por zero
        with self.assertRaises(ValueError):
            Calculadora.divisao(10, 0)

if __name__ == '__main__':
    unittest.main()
