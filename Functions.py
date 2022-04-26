class Function:
    
    #Variables
    consumedFood = [[],[]]
    
    ###IMC###
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

        
    ###CALORIES### 
    def returnFoodList():
        return consumedFood
    
    def addFood(foodName, calories):
        consumedFood[0].append(foodName)
        consumedFood[1].append(calories)

    def countTotalCalories():
        count = 0
        totalCalories = 0
        while count <= len(consumedFood)+1:
            totalCalories += consumedFood[1][count]
            count = count+1
            
    def listAllEatenFood():
        count = 0
        while count <= len(consumedFood)+1:
            print(str(consumedFood[0][count]) + " -> " + str(consumedFood[1][count]))
            count = count+1
