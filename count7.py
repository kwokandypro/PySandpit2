# -*- coding: utf-8 -*-

# yourword= raw_input("type your word \n")

def TypeYourWord():
    global YourWord
    YourWord = raw_input("type your word \n")
    while len(YourWord) != 4:
        YourWord = raw_input("type your word again \n")
    else:
        print("Now your word : ", YourWord, " has the correct format")
        return YourWord




#yourword='tata'


def MonMot(tonmot):
    global Var_Glob
    Var_Glob = list(tonmot)
    return Var_Glob



def Comptage(monmot):
    global Var_Comptage
    Var_Comptage = 0
    for cpte in range(0, (len(monmot))):
        print("this is your " + str(cpte+1) + " letter")
        for count in range(1, 5):
            Comptage_Mot = cpte+1
            b = raw_input("Type your letter \n")
            while len(b) != 1:
                b = raw_input("type your letter again \n")
            else:
                if Var_Glob[cpte] == b and Comptage_Mot < 4:
                    Var_Comptage += 1
                    print ("yes")
                    break
                elif Var_Glob[cpte] == b and Comptage_Mot == 4:
                    Var_Comptage += 1
                    print ("You won. End of game")
                    break
                else:
                    if count == 4 and Comptage_Mot < 4:
                        print("this was your "+str(count) + " last try for the " +
                              str(Comptage_Mot)+" letter. let's go to the next letter")
                    elif count == 4 and Comptage_Mot == 4:
                        print("this was your last try for the word. You guessed " +
                              str(count) + " letters. End of game.")
                    else:
                        print("wrong letter, try again" + " ,this was your " +
                              str(count) + " try. Now your " + str(count+1) + " try")
    print(Var_Comptage)
       


#   ce qu'il reste à faire

#1) au bout de combien de lettres deviné , le  jeu est-il gagné

def toto():
    TypeYourWord()
    MonMot(YourWord)
    Comptage(Var_Glob)

if __name__ == '__main__':
    toto()

