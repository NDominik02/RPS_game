import random
import time
from Player import Player
import os

def main():
    os.system("cls")
    mode = input("Greetings!\nDo you want to play against the computer, or against another player? (c/p) ")
    while(True):
        os.system("cls")
        if(mode == "c"):
            onePlayerMode()
            break
        elif(mode == "p"):
            twoPlayersMode()
            break
        elif(mode == "x"):
            break
        else:
            mode = input("Type c to play against the computer, p to play against another player or type x to exit! ")


def onePlayerMode():
        
    p1 = Player("player", 100, "rock")
    computer = Player("bot", 100, "rock")

    while(True):
        while(True):
            choice = input("Rock, Paper, Scissors? ").lower()
            if(choice != "rock" and choice != "paper" and choice != "scissors"):
                print("Wrong input!")
            else:
                os.system("cls")
                break

        myList = ["rock", "paper", "scissors"]
        computers_choice = random.choice(myList)

        p1.hand = choice
        computer.hand = computers_choice

        if(p1 < computer):
            p1.health -= random.randint(10, 40)
            print("Oh nooo, the computer won this turn! :(")
        elif(p1 > computer):
            computer.health -= random.randint(10, 40)
            print("You won this round, Congrats! ;)")
        else:
            print("Its DRAAW!")
        print(f"(The computer shows {computers_choice}!)")

        print(f"\nYour current health: {p1.health}\nThe computers current health: {computer.health}")
    
        if(computer.health <= 0):
            print("\nYou destroyed the computer, well played!!")
            break
        elif(p1.health <= 0):
            print("\nThe computer was luckier this time! :(")
            break


def twoPlayersMode():
    p1name = input("Well... player 1, whats your name? ")
    p2name = input("And yours, player 2? ")

    p1 = Player(p1name, 100, "rock")
    p2 = Player(p2name, 100, "rock")

    while(True):
        while(True):
            player1_choice = input(f"{p1name}...Rock, Paper, Scissors? ").lower()
            if(player1_choice != "rock" and player1_choice != "paper" and player1_choice != "scissors"):
                print("Wrong input!")
            else:
                os.system("cls")
                break


        print("Okey..")
        time.sleep(1)

        while(True):
            player2_choice = input(f"{p2name}...Rock, Paper, Scissors? ").lower()
            if(player2_choice != "rock" and player2_choice != "paper" and player2_choice != "scissors"):
                print("Wrong input!")
            else:
                os.system("cls")
                break

        p1.hand = player1_choice
        p2.hand = player2_choice
        
        time.sleep(1)

        if(p1 < p2):
            p1.health -= random.randint(10, 40)
            print(f"{p2.name}, Congrats! ;)")
        elif(p1 > p2):
            p2.health -= random.randint(10, 40)
            print(f"{p1.name}, Congrats! ;)")
        else:
            print("Oh nooo, its DRAAW!")

        print(f"\n{p1name} your current health: {p1.health}\n{p2name}'s current health: {p2.health}")

        if(p1.health <= 0):
            print(f"\nGOOD JOB {p2name}!! {p1name} HAD NO CHANCE :P")
            break
        elif(p2.health <= 0):
            print(f"\nWELL PLAYED {p1name}! DID {p2name} EVEN PLAY?")
            break


if __name__ == "__main__":
    main()
