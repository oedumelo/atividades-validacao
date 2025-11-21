class Calculadora:

    def soma(numero_1, numero_2):
        return numero_1 + numero_2
    
    def subtracao(numero_1, numero_2):
        return numero_1 - numero_2
    
    def multiplicacao(numero_1, numero_2):
        return numero_1 * numero_2
    
    def divisao(numero_1, numero_2):
        if numero_2 == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return numero_1 / numero_2