import PySimpleGUI as sg
import Data as db

#Variables
username = None
password = None 

class TelaLogin:


    def __init__(self):
        #Layout
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

    def checkLogin():
        #DB class calling

tela = TelaLogin()
tela.Iniciar()
