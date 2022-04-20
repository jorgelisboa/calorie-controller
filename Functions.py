class Function:

    def calcImc(altura, peso):

        imcValue = peso / (altura ** altura)
        return imcValue

    def findCategory(imc):
        classificacao = None
        if imc < 18.5:
            return "MAGREZA"
        elif imc >= 18.5 and imc <= 24.9:
            return "NORMAL"
        elif imc >= 25 and imc <= 29.9:
            return "SOBREPESO"
        elif imc >= 30 and imc <= 39.9:
            return "OBESIDADE"
        elif imc > 40:
            return "OBESIDADE GRAVE"
