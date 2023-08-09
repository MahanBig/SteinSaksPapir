import random

Options = [
    "Stein",
    "Saks",
    "Papir"
]

optionList = (
    """Stein Saks Eller Papir (bruk nummer):
    1. Stein
    2. Saks
    3. Papir"""
)

player1Point = 0
player2Point = 0
IsGameOn = True

def whoWon(input1,input2):
    if input1 == input2:
        return("Uavgjort")
    elif input1 == 1:
        if input2 == 2:
            return("Win")
        if input2 == 3:
            return("Tap")
    elif input1 == 2:
        if input2 == 1:
            return("Tap")
        if input2 == 3:
            return("Win")
    elif input1 == 3:
        if input2 == 1:
            return("Win")
        if input2 == 2:
            return("Tap")

while IsGameOn:
    if player1Point < 3 and player2Point < 3:
        print(optionList)
        playerOption = input()
        Resultat = 0
        ComputerOption = random.randint(1,3)
        lookup = Options[(ComputerOption - 1)]

        if playerOption == '1':
            Resultat = whoWon(1,ComputerOption)
        elif playerOption == '2':
            Resultat = whoWon(2,ComputerOption)
        elif playerOption == '3':
            Resultat = whoWon(3,ComputerOption)
        else:
            print("Ugyldig input")

        if Resultat  == ("Uavgjort"):
            print("Computer valgte ",lookup)
            print("Det ble uavgjort")
        elif Resultat  == ("Win"):
            player1Point += 1
            print("Computer valgte ",lookup)
            print("Du fikk et poeng, du har nå ",player1Point,"poeng")
        elif Resultat  == ("Tap"):
            player2Point += 1
            print("Computer valgte ",lookup)
            print("Computer fikk et poeng, computer har nå ",player2Point,"poeng")
    else:
        if player1Point > player2Point:
            print("Du har vunnet")
        elif player2Point > player1Point:
            print("Du har tapt")
        elif player1Point == player2Point:
            print("Spillet ble uavgjort")

        print("""
Vil du spille på nytt?
1. Ja
2. Nei
        """)
        svar = input()
        if svar == '1':
           player1Point = 0
           player2Point = 0
        elif svar == '2':
            IsGameOn = False
            break
