import random
def main():

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    num_canteen = 3
    dead = False
    done = False

    print("Bienvenido a Camel")
    print("Robaste un camello para realizar tu viaje hasta el gran desierto Mobi")
    print("Los nativos quieren su camello de vuelta y te persiguen")
    print("Sobrevive en tu viaje y escapa de los nativos")

    while done == False:
        oasis = random.randint(1, 20)
        print("A. Beber de tu cantimplora.")
        print("B. Velocidad normal.")
        print("C. Maxima velociada.")
        print("D. Descansar en la noche.")
        print("E. Revisar estado.")
        print("Q. Salir")
        a = input("¿Que escoges:? ")

        if a.upper() == "Q":
            done = True
            print("Saliste de juego")
        elif a.upper() == "E":
            print("Millas recorridas: ",miles_traveled)
            print("Numero de cantimploras: ",num_canteen)
            print("Los nativos estan a ",-native_distance,"millas deetras de ti")
        elif a.upper() == "D":
            camel_tiredness = 0
            print("Tu camello está feliz")
            native_move = random.randint(7, 14)
            native_distance += native_move
        elif a.upper() == "C":
            forward=random.randint(10,20)
            miles_traveled += forward
            print("Distancia recorrida ",forward,"millas")
            thirst += 1
            camel_tiredness += 1
            native_move = random.randint(7,14)
            native_distance += native_move
            native_distance -= forward
        elif a.upper() == "B":
            forward=random.randint(5,12)
            miles_traveled += forward
            print("distancia recorrida",forward,"miles")
            thirst += 1
            camel_tiredness += 1
            native_move = random.randint(7, 14)
            native_distance += native_move
            native_distance -= forward
        elif a.upper() == "A":
            if num_canteen>0:
                thirst = 0
                num_canteen -= 1
            else:
                print("No tienes cantimploras")

        if thirst > 4 and thirst <= 6:
            print("Estas sediento")
        elif thirst > 6:
            print("Moriste de sed")
            done = True
            dead = True
            camel_tiredness = 0
        if camel_tiredness > 5 and camel_tiredness <= 8:
            print("Tu camello se está cansando.")
        elif camel_tiredness > 8:
            print("Tu camello está muerto.")
            thirst = 0
            dead = True
            done = True
        if native_distance == 0:
            print("¡Los nativos de atraparon!")
            done = True
            dead = True
            thirst = 0
            camel_tiredness = 0
        elif native_distance < 15 and native_distance > 0:
            print("¡Los nativos se están acercando!")
        if miles_traveled > 200 and dead == False:
            print("¡Enorabuena,escapaste!")
            done = True
        if oasis == 1 and (a == "B" or a == "C"):
            drinks = 3
            thirst = 0
            camel_tiredness = 0

main()

