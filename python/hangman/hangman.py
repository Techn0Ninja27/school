import random
# hangman in python
# obtains words from text file
# text file is words.txt

# maybe i will add a GUI


class Hangman:

    def __init__(self):

        # randomly chooses line for word
        self.wordNumber = random.randint(0, 1000)

        # opens text file
        with open("words.txt", "r") as words:
            for i, line in enumerate(words):
                if i == self.wordNumber:
                    # if the line is the same as the randomly chosen line
                    self.wordStr = words.readline()
                elif i > self.wordNumber:
                    break

        # removes newline
        self.wordStr = self.wordStr.rstrip("\n")
        # turns word into list
        self.word = []
        for i in self.wordStr:
            self.word.append(i)

        self.discovered = []
        for i in self.word:
            self.discovered.append("_")
        # the alphabet
        self.alphabetStr = "abcdefghijklmnopqrstuvwxyz"
        self.alphabetDict = {}
        self.alphabetList = []

        # Alphabet as a dictionary
        for i in self.alphabetStr:
            self.alphabetDict[i] = False

        # Alphabet as a list
        for i in self.alphabetStr:
            self.alphabetList.append(i)

        # images of hangman
        self.man0 = ["_____      ",
                     "|    |     ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|__________"
                     ]
        self.man1 = ["_____      ",
                     "|    |     ",
                     "|    O     ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|__________"
                     ]
        self.man2 = ["_____      ",
                     "|    |     ",
                     "|    O     ",
                     "|    |     ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|__________"
                     ]
        self.man3 = ["_____      ",
                     "|    |     ",
                     "|    O     ",
                     "|  --|     ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|__________"
                     ]
        self.man4 = ["_____      ",
                     "|    |     ",
                     "|    O     ",
                     "|  --|--   ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|__________"
                     ]
        self.man5 = ["_____      ",
                     "|    |     ",
                     "|    O     ",
                     "|  --|--   ",
                     "|    |     ",
                     "|          ",
                     "|          ",
                     "|          ",
                     "|__________"
                     ]
        self.man6 = ["_____      ",
                     "|    |     ",
                     "|    O     ",
                     "|  --|--   ",
                     "|    |     ",
                     "|   /      ",
                     "|  /       ",
                     "|          ",
                     "|__________"
                     ]
        self.man7 = ["_____      ",
                     "|    |     ",
                     "|    O     ",
                     "|  --|--   ",
                     "|    |     ",
                     "|   / \\    ",
                     "|  /   \\   ",
                     "|          ",
                     "|__________"
                     ]

        # how many bodyparts of the man have been drawn
        self.state = 0

        # if the game is over
        self.gameover = False

        # the active pool of characters
        self.activePool = self.alphabetList

        # the pool of characters that have been used
        self.usedPool = []

    def print_list(self, list):
        '''prints list of strings'''
        for i in list:
            print(i)

    def list_to_string(self, list):
        '''Concatenates list into string'''
        string = ""
        for i in list:
            string += i
        return string

    def string_index_replace(self, string, index, replace):
        '''replaces an element at an index of a string'''
        # basically this one just slices the string into whats before
        # the index and whats after it. Then it joins them together with
        # the element we want to place into that index
        newString = string[:index] + replace + string[index+1:]
        return newString

    def letter_input(self):
        '''user input for letter'''
        failure = True  # assumes user has failed
        while failure:  # loop to prevent further errors in code

            # input for letter
            letter = str(input("LETTER: "))
            # changes input to be lowercase and only one char
            letter = letter.lower()
            try:
                letter = letter[0]
            except IndexError:
                letter = " "
            # checks if letter is in active letter pool
            if letter in self.activePool:
                failure = False
                break
            # checks if letter is in pool of used letters
            elif letter in self.usedPool:
                print("Letter already used")
            # everything else goes here
            else:
                print("invalid character")
        return letter

    def letter_check(self):
        '''check letter against word'''
        letter = self.letter_input()  # first input for letter

        if letter in self.activePool:
            # check if the letter is part of the active pool of letters

            # removes letter from active pool and adds it to used pool
            self.activePool.pop(self.activePool.index(letter))
            self.usedPool.append(letter)
            if letter in self.word:
                # checks if the letter is part of the word
                while letter in self.word:  # goes through the word
                    index = self.word.index(letter)  # finds index for char
                    self.word[index] = letter.upper()  # makes the index upper
                    # adds to list of discovered
                    self.discovered[index] = letter
            else:
                # if the letter is not part of the word
                self.state += 1
        else:
            pass

    def draw_man(self):
        '''draws man according to state'''

        # checks the state and prints the corresponding ascii art
        if self.state == 0:
            self.print_list(self.man0)
        elif self.state == 1:
            self.print_list(self.man1)
        elif self.state == 2:
            self.print_list(self.man2)
        elif self.state == 3:
            self.print_list(self.man3)
        elif self.state == 4:
            self.print_list(self.man4)
        elif self.state == 5:
            self.print_list(self.man5)
        elif self.state == 6:
            self.print_list(self.man6)
        elif self.state == 7:
            self.print_list(self.man7)

    def win_check(self):
        '''checks if player won, returns bool'''
        # checks if there are any unfound letters
        if "_" in self.discovered:  # checks for blanks in finished word
            return False
        else:
            return True

    def gameover_check(self):
        '''checks if game is over'''
        if self.win_check():
            # checks for a win
            self.gameover = True
        elif self.state > 6:
            # checks for a loss
            self.gameover = True
        else:
            pass

    def turn(self):
        '''single game iteration'''
        # prints the characters found
        print(self.list_to_string(self.discovered))
        # prints the guy
        self.draw_man()
        print()
        # prints remaining letters
        print("Letters:")
        print(self.list_to_string(self.activePool))
        print()
        # input for letter
        self.letter_check()

    def play(self):
        '''runs the game'''
        # loop until game finished
        while self.gameover is False:
            # checks for a gameover
            self.gameover_check()
            if self.gameover is True:
                # if the game is over
                if self.win_check():
                    # if the player has won
                    print("YOU WON")
                    print("word was:", self.list_to_string(self.discovered))
                else:
                    # if the player loses
                    self.draw_man()
                    print("you lost")
                    print("word was:")
                    print(self.list_to_string(self.word).lower())
            else:
                # if game isnt over, then repeat turns until game finish
                self.turn()


hangman = Hangman()
hangman.play()
