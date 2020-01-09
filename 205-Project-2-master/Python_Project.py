"""
Title: Project 1
Abstract: Text Based Game
Names: Akoni Morrison, Garred Murphy, Devon Nair
Date: 10/14/2016
"""
#https://github.com/Akoni8/205-Project-2
"""
Akoni: Game class and Room class
Garred: Storyline
Devon: sleep, and quit functions
"""

import time # For time function
import cmd #For commands
from room import get_room #Getting the get_room function from the room class
import textwrap #Used to wrap the story and make it easier to read
class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        self.loc = get_room(1) #Gets the first room
        self.look()

    def move(self,dir): #Allows you to move
        newroom = self.loc._neighbors(dir)
        if newroom is None: #If there isn't a room
            print("you can't go that way")
        else:#conditions that automatically end the story
            self.loc = get_room(newroom)
            self.look()
            if (newroom == 11) or (newroom == 7) or (newroom == 15):
                print("Congrats, you made it!")
                time.sleep(8)
                exit()
            if (newroom == 16) or (newroom == 17) or (newroom == 18) or (newroom == 19) or (newroom == 20) or (newroom == 21) or (newroom == 22) or (newroom == 23) or (newroom == 24):
                print("You suffer a horrible death")
                print("Game Over")
                time.sleep(8)
                exit()

    def look(self): #This function displays the location and the story of the room
        print("")
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 72):
           print(line)
        print("")
    
    # These are the cmd functions that define movements/directions
    def do_n(self,args): 
        """Go North"""
        self.move('n')

    def do_s(self,args):
        """Go South"""
        self.move('s')

    def do_e(self,args):
        """Go East"""
        self.move('e')
    def do_w(self,args):
        """Go West"""
        self.move('w')
   
    def do_up(self,args):
        """Go up"""
        self.move('up')

    def do_down(self,args):
        """Go down"""
        self.move('down')

    def do_quit(self,args):
        """Leaves the game"""
        print("Goodbye")
        return True

if __name__ == "__main__":
    print("")
    print("Site 19 is a massive prizon and research facility ")
    print("where supernatural opjects and being are contained and studied.")
    print("Site is now under attack by the agents of a rival organization,")	
    print("and several of the most dangerous prizoners are escaping.")
    print("Can you get to a safe place before the monsters or the enemy kills you?")
    print("")	
    print("Type 'help' for a list of commands.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    g = Game()#Story loop
    g.cmdloop()
