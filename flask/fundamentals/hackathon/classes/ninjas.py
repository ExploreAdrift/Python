import random
class Ninja:
    ninjas = []

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 250
        Ninja.ninjas.append(self.name)

    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        dR = random.randint(0,20)
        dR1 = random.randint(0,12)
        if dR == 20:
            print("CRITICAL STRIKE!!")
            pirate.health -= self.strength * 3
            atTwo = input("Do you strike again? \n ***WARNING: HIGH RISK*** \n Y/N?")
            if atTwo == "y" or atTwo == "Y":
                if self.speed > dR1:
                    print("YOU LANDED SECOND ATTACK!!")
                    pirate.health -= 20
                else:
                    print("TOLD YOU IT WAS RISKY!!")
                    self.health *= 0.5
            else:
                print("probably a smart move...")
        elif dR > 12 and dR < 19:
            print("Attack Landed!")
            pirate.health -= self.strength + dR    
        elif dR < 12 and dR > 6:
            print("Attack Missed!")
        else:
            print("You slipped and the Pirate hit you!")
            self.health -= dR * 2
        return self