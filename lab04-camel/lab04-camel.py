import random
milesTravelled=0
thirst=0
camelTiredness=0
nativedistance=-20
numCantines=3

def main():
    print("Bienvenido a Camel")
    print("Robaste un camello para realizar tu viaje hasta el gran desierto Mobi")
    print("Los nativos quieren su camello de vuelta y te persiguen")
    print("Sobrevive en tu viaje y escapa de los nativos")
    done = False
    while done == False:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit")
        a=input("Your choice: ")
        if a.upper()=="Q":
            done=True
            print("you abandoned the game")
        elif a.upper()=="E":
            print("Miles traveled: ",milesTravelled)
            print("Drinks in canteen: ",numCantines)
            print("The natives are",nativedistance,"miles behind you")
