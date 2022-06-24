# THIS IS OUR GAME

# PIRATES VS NINJAS

from classes.ninjas import Ninja
from classes.pirates import Pirate
import random

michelangelo = Ninja("Michelanglo")
miagi = Ninja("Mr Miagi")
ralph = Ninja("Ralph Macchio")


jack_sparrow = Pirate("Jack Sparrow")
capt_jay = Pirate("Captian Jay")
john = Pirate("john")




# turn based

player = input("Choose a Side!!!  // A: Ninja  //  B: Pirate:  ")
# Decision 1 (character)
if player == "a" or player =="A":
    print("You are now a Ninja!! Your name is Michelangelo!")
    michelangelo.show_stats()
    cont = input("do you wish to continue? Y/N:  ")
    while michelangelo.health > 0 and jack_sparrow.health> 0:
        if cont == "y" or cont == "Y":
            # decision 2 ( )
            print("A rogue pirate attacks you!")
            jack_sparrow.show_stats()
            d2 = input("Do you fight or flee?? \n // A: Fight // B: Flee:   ")
            if d2 == "a" or d2 == "A":
                michelangelo.attack(jack_sparrow)
                lb1 = input("press any key to coninue")
                print("The Rogue Pirate:")
                jack_sparrow.show_stats()
                lb1 = input("press any key to coninue")
                print("Your new stats:")
                michelangelo.show_stats()
                lb1 = input("press any key to coninue")
            if d2 == "b" or d2 == "B":
                print("The Pirate attacks you as you run!")
                jack_sparrow.attack(michelangelo)
                lb1 = input("press any key to coninue")
                print("The Rogue Pirate: ")
                jack_sparrow.show_stats()
                lb1 = input("press any key to coninue")
                print("Your new stats:")
                michelangelo.show_stats()
                lb1 = input("press any key to coninue")
    else:
        print(f"GAME OVER!! Your health:{michelangelo.health} Pirate health:{jack_sparrow.health}")




elif player == "b" or player == "B":
    print("You are now a Pirate!! Your name is Jack Sparrow!")
    jack_sparrow.show_stats()
    cont = input("do you wish to continue? Y/N:  ")
    while jack_sparrow.health > 0 and michelangelo.health > 0:
        if cont == "y" or cont == "Y":
            # decision 2 ( )
            print("A rogue Ninja attacks you!")
            jack_sparrow.show_stats()
            d2 = input("Do you fight or flee?? \n // A: Fight // B: Flee:   ")
            if d2 == "a" or d2 == "A":
                jack_sparrow.attack(michelangelo)
                lb1 = input("press any key to coninue")
                print("The Rogue Ninja:")
                michelangelo.show_stats()
                lb1 = input("press any key to coninue")
                print("Your new stats: ")
                jack_sparrow.show_stats()
            if d2 == "b" or d2 == "B":
                print("The Ninja attacks you as you run!")
                michelangelo.attack(jack_sparrow)
                lb1 = input("press any key to coninue")
                print("The Rogue Ninja: ")
                michelangelo.show_stats()
                lb1 = input("press any key to coninue")
                print("Your new stats: ")
                jack_sparrow.show_stats()
    else:
        print(f"GAME OVER!! Your health:{jack_sparrow.health} Pirate health:{michelangelo.health}")




# force enemy[0] to be first one fought
# remove from list when health hits 0
# when emeny removed from list, add +50 health
# new end game message if you beat all enemies
# added a hide/sneak option to use speed/steal attr
#   option to check barrel next to you
#            possibility (d20 roller) to get potion to increase health/strength
#           
#
# flee option has to be method
#    return strike gets own method
#    if lower than speed of player then miss maybe between 7-9
#  print attack missed, you gained randint 1, 3 * self.health += .1-3 * self.health
#    give a d10 roll of health increase return doesnt land


# add new class (samurai) to play as... different stats
# 
# multiplayer mode:
#   each player selects class
#   runs attack/flee option
#
# if you beat the list
# LEVEL UP OPTION < have to beat the boss
#      increase all stats by % per level
#      increase instances of enemies
#      allow for multiple attack/defends per turn
#      
# 
# 
# 
# 


