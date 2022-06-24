import random
class Pirate:
    pirates = []

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 250
        Pirate.pirates.append(self.name)

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        dR = random.randint(0,20)
        dR1 = random.randint(0,12)
        if dR == 20:
            print("CRITICAL STRIKE!!")
            ninja.health -= self.strength * 3
            atTwo = input("Do you strike again? \n ***WARNING: HIGH RISK*** \n Y/N?")
            if atTwo == "y" or atTwo == "Y":
                if self.speed > dR1:
                    print("YOU LANDED SECOND ATTACK!!")
                    ninja.health -= 20
                else:
                    print("TOLD YOU IT WAS RISKY!!")
                    self.health *= 0.5
            else:
                print("probably a smart move...")
        elif dR > 12 and dR < 19:
            print("Attack Landed!")
            ninja.health -= self.strength + dR    
        elif dR < 12 and dR > 6:
            print("Attack Missed!")
        else:
            print("You slipped and the Ninja hit you!")
            self.health -= dR * 2
        return self

