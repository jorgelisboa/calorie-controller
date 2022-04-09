def verifyUser(username, password):
    if username == "nome de usuário":
        #check the password
        if password == "senha daquele usuário":
            #enter in his data
            print("Welcome " + username)
            return True
        else:
            #say incorrect password  
            print("Incorret password")  
    else:
        #user not found 
        print("User not found")

def Login():
    #Asks user to 
    username = input("What's your username? ")
    password = input("What's your password? ")

    verifyUser(username, password)
    
def startApp():
    print("Nutri app started")
    Login()

startApp()
