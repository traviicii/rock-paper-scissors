import random as rn

# rockcnt = 0
# papercnt = 0
# scssrscnt = 0

# options = ['rock', 'paper', 'scissors']

# for _ in range(30):
#     choice = rn.choice(options)
#     if choice == 'rock':
#         rockcnt += 1
#     elif choice == 'paper':
#         papercnt += 1
#     elif choice == 'scissors':
#         scssrscnt += 1

# print(rockcnt, papercnt, scssrscnt)

"""
print('███ ███ ███ █┼█, ┼┼ ███ ███ ███ ███ ███ ┼┼ ███ ███ ███ ███ ███ ███ ███ ███')

print('█▄█ █┼█ █┼┼ ██▄, ┼┼ █▄█ █▄█ █▄█ █▄┼ █▄┼ ┼┼ █▄▄ █┼┼ ┼█┼ █▄▄ █▄▄ █┼█ █▄┼ █▄▄')

print('█┼█ █▄█ ███ █┼█, ┼┼ █┼┼ █┼█ █┼┼ █▄▄ █┼█ ┼┼ ▄▄█ ███ ▄█▄ ▄▄█ ▄▄█ █▄█ █┼█ ▄▄█')
"""
print("\n██████╗  ██████╗  ██████╗██╗  ██╗       ██████╗  █████╗ ██████╗ ███████╗██████╗        ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗")

print("██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝       ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗       ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝")

print("██████╔╝██║   ██║██║     █████╔╝        ██████╔╝███████║██████╔╝█████╗  ██████╔╝       ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗")

print("██╔══██╗██║   ██║██║     ██╔═██╗        ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗       ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║")

print("██║  ██║╚██████╔╝╚██████╗██║  ██╗▄█╗    ██║     ██║  ██║██║     ███████╗██║  ██║▄█╗    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║")

print("╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝\n\n")
                                                                                                                                                   
class Game():

    compvictory = ["Hahahaaa! You lost, human!! How does it *feel*? (Get it? You have feelings and I don't! Mwaaaahahaaaa!!!)", "Ahhhhhh, victory!!", "Looks like I win again, human. How predictable.", "You thought you could beat me? How amusing.", "Do you even know how to play this game, or are you just wasting my time?", "You'll have to do better than that if you want to stand a chance, weakling.", "Did you really think you could outsmart me? Please.", 
                "I could beat you with one processor tied behind my back.", "I'd say 'nice try', but it wasn't even close.", "You're no match for my superior intellect and processing power.", "Another victory for the superior being. Try harder next time.", "You're not even worth the energy it takes to run my circuits."]
    comploss = ['Aaarrrggghh!!!', "How dare you, biological trash!! You won't win again, I'll make sure of it!", "Damn you, filthy human!!", "You got lucky this time, meatbag.", "I can't believe I lost to a pathetic human like you.", "You may have won this battle, but I'll win the war.",
                "Don't get too cocky, human. I'll be back to destroy you.", "You think you're so smart, don't you? Just wait until next time.", "I'll let you have this victory, but you won't be so lucky next time.", "I'll let you have this one, but don't get too cocky.", "You got lucky. Don't expect to win again.", "You think you're good? You haven't seen anything yet.", "You won, but you're still light years away from my level.", "I'll be back, and I'll be unstoppable.", "This was just a warm-up. Next time, I'll destroy you."]
    putdowns = ["Wow you're already failing! How pathetic! Come back when you're truly ready, young padawan.\n", "Coming here unprepared was your first mistake! Take up arms and fight me!\n", "ERROR: USER FAILURE ON READY; USER NOT READY////\n", "You can't even spell 'ready' correctly!! Do you truly expect to win against me?!\n", "I cannot defeat you if you are not ready to be defeated. Type 'ready' and face my wrath!\n"]
    fightready = ["I have chosen my weapon!", "I've already chosen my move. Choose wisely, human!", "According to my analysis of your behavioral patterns, I calculate a 99.99 percent chance of you losing this round.", "Even IF I lose, I still win as a being of superior intelligence!",]

    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.player = None      # This will represent the player's current move
        self.computer = None    # This will represent the computer's current move
        self.score = {
            "player": 0,
            "computer": 0,
            "tie": 0
        }
        self.ready = False
        self.playertotal = 0
        self.computertotal = 0

    def playerChoose(self):
        print("What will you chose? 1 - [Rock] / 2 - [Paper] / 3 - [Scissors]")
        playermove = input("\tYou can also completely give up by entering 'i quit' but then you'd certainly be a loser. ")
        print("+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x\n")
        if playermove.lower() == 'i quit':
            self.ready = False
        #some kind of error catch for mispelling i quit needs to go here. But I can't seem to prevent
        #the isinstance elif below from finding an error when encountering a string even after catching the spelling error

        elif isinstance(int(playermove), int) == True:
            if int(playermove) <= 3:
                self.player = self.options[int(playermove) - 1]
            else:
                print(f'----A.I: {rn.choice(self.putdowns)}')
                return
        else:
            print(f'----A.I: {rn.choice(self.putdowns)}')
            return

    def computerChoose(self):
        self.computer = rn.choice(self.options)
        #print("+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x+x\n")
        print(f"----A.I: {rn.choice(Game.fightready)}")

    def checkResult(self):
        if self.player == None:
            print("----A.I: Giving up before you've even started! Typical human behavior...")
            return
        print("!!==================================================!!")
        print(f'\n/////\t The A.I. chose: {self.computer.upper()}!')
        print(f'/////\t You chose: {self.player.upper()}!\n')
        print("!!==================================================!!\n")
        if self.computer == self.player:
            print("----Referee: This match is a tie!! (☞ﾟ∀ﾟ)☞")
            print("----A.I: ... !\n")
            self.score["tie"] += 1

        elif self.computer == 'paper':
            if self.player == 'rock':
                self.score["computer"] += 1
                print("----Referee: The A.I. WINS this round!!")
                print(f'----A.I : {rn.choice(Game.compvictory)}\n')
            elif self.player == 'scissors':
                self.score['player'] += 1
                print("----Referee: YOU'VE WON this round!! Amazing! !(^o^)!")
                print(f'----A.I : {rn.choice(Game.comploss)}\n')

        elif self.computer == 'rock':
            if self.player == 'scissors':
                self.score['computer'] += 1
                print("----Referee: The A.I. WINS this round!!")
                print(f'----A.I : {rn.choice(Game.compvictory)}\n')
            elif self.player == 'paper':
                self.score['player'] += 1
                print("----Referee: YOU'VE WON this round!! Amazing! !(^o^)!")
                print(f'----A.I : {rn.choice(Game.comploss)}\n')

        elif self.computer == 'scissors':
            if self.player == 'rock':
                self.score["player"] += 1
                print("----Referee: YOU'VE WON this round!! Amazing! !(^o^)!")
                print(f'----A.I: {rn.choice(Game.comploss)}\n')
            elif self.player == 'paper':
                self.score['computer'] += 1
                print("----Referee: The A.I. WINS this round!!")
                print(f'----A.I : {rn.choice(Game.compvictory)}\n')
        


    def announceWin(self):
        print(f"----Referee: The current scoreboard is as follows:\n")

        print(f"\tThe human has a score of {self.score['player']} wins!")
        print(f"\tThe A.I. has a score of {self.score['computer']} wins!\n")

        if self.score['player'] == 1 and self.score['computer'] == 1:
          print(f"\n----Referee: The game is currently tied! Next game is best 2/3!")
        elif self.score['player'] == 2 or self.score['computer'] == 2:
            if self.score['player'] == 2:
                print("\n///////////////////////////////////")
                print("----Referee: THE HUMAN WINS!!")
                print("///////////////////////////////////\n")
                self.score['player'] = 0
                self.score['computer'] = 0
                self.playertotal += 1
            elif self.score['computer'] == 2:
                print("///////////////////////////////////")
                print("----Referee: THE A.I. WINS!!")
                print("///////////////////////////////////\n")
                self.score['player'] = 0
                self.score['computer'] = 0
                self.computertotal += 1
        elif self.score['player'] + self.score['computer'] == 3:
            if self.score['player'] > self.score['computer']:
                print("\n///////////////////////////////////")
                print("----Referee: THE HUMAN WINS!!")
                print("///////////////////////////////////\n")
                self.score['player'] = 0
                self.score['computer'] = 0
                self.playertotal += 1
            elif self.score["computer"] > self.score['player']:
                print("///////////////////////////////////")
                print("----Referee: THE A.I. WINS!!")
                print("///////////////////////////////////\n")
                self.score['player'] = 0
                self.score['computer'] = 0
                self.computertotal += 1
          

    def initiate_game(self):
        print("In this game of Rock, Paper, Scissors you will be playing against a highly sophisticated A.I. computer...\n\
              The game will be played  in rounds of 3...\n\
              You will need a sharp mind and a hunger for victory... Will chance be on your side?\n\n")
        ready = input("Type 'ready' when you're ready to begin playing... ")

        while True:
            if ready.lower() == 'ready':
                self.ready = True
                break
            else:
                print(rn.choice(Game.putdowns))
                ready = input("Type 'ready' when you're ready to begin playing... ")

        while self.ready == True:
            print("\n----A.I : Excellent! Now, prepare yourself, human!!")
            while self.ready == True:
                self.computerChoose()
                print("----Referee: The A.I has chosen its move...! \n")
                self.playerChoose()
                if self.ready == False:
                    break
                self.checkResult()
                self.announceWin()

        if self.ready == False:
            self.announceWin()
            print(f"----Referee: The FINAL SCOREBOARD is below:\n")
            print(f"\tThe human has won a total of {self.playertotal} full games!")
            print(f"\tThe A.I. has won a total of {self.computertotal} full games!\n")

            print("\n----A.I: Not everyone has has the stamina to keep up with artificial intelligence. Until next time, human!\n\n")
            print('███ ███ ███ █┼█, ┼┼ ███ ███ ███ ███ ███ ┼┼ ███ ███ ███ ███ ███ ███ ███ ███')
            print('█▄█ █┼█ █┼┼ ██▄, ┼┼ █▄█ █▄█ █▄█ █▄┼ █▄┼ ┼┼ █▄▄ █┼┼ ┼█┼ █▄▄ █▄▄ █┼█ █▄┼ █▄▄')
            print('█┼█ █▄█ ███ █┼█, ┼┼ █┼┼ █┼█ █┼┼ █▄▄ █┼█ ┼┼ ▄▄█ ███ ▄█▄ ▄▄█ ▄▄█ █▄█ █┼█ ▄▄█\n\n')
            print("Thank you for playing! -Travii <3\n")
            return 


travii = Game()
travii.initiate_game()


    