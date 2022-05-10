import PySimpleGUI as sg
import Data as db

#Variables
username = None
password = None 
consumedFood = [[],[]]

class TelaLogin:

    ###IMC###
    def calcImc(altura, peso):

        imcValue = peso / (altura ** altura)
        return imcValue

    def findCategory(imc):
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



    #Layout
    def __init__(self):
        def createLayout():

            layout = [
                [sg.Text("Login", size=(10,0)), sg.Input(size=(25,0), key='username')],
                [sg.Text("Password", size=(10,0)), sg.Input(size=(25,0), key='password')],
                [sg.Button("Login", size=(35,0))]
            ]  
            return layout                               
                
        #Janela
        window = sg.Window("Login").layout(createLayout())  
        self.button, self.values = window.Read()

    def Iniciar(self):
        username = self.values['username']
        password = self.values['password']
        print('nome: '+username+' password: '+password)

    #def checkLogin():
        #DB class calling


tela = TelaLogin()
tela.Iniciar()
