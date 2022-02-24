# hangman in python

# maybe i will add a GUI

class Hangman:

    def __init__(self, word):

        self.word = []
        for i in word:
            self.word.append(i)

        self.alphabetStr = "abcdefghijklmnopqrstuvwxyz"
        self.alphabetDict = {}
        self.alphabetList = []

        for i in self.alphabetStr:
            self.alphabetDict[i] = False

        print(self.alphabetDict)
        for i in self.alphabetStr:
            self.alphabetList.append(i)

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

        self.state = 0

        self.gameover = False

        self.activePool = self.alphabetList

        self.usedPool = []

    def string_index_replace(self, string, index, replace):
        newString = string[:index] + replace + string[index+1:]
        return newString

    def letterCheck(self):
        pass

#    def draw(self):
#
#        if self.state == 0:
#            self.state += 1
#            self.man[2] = self.string_index_replace(self.man[2], 5, "O")
#
#        elif self.state == 1:
#            self.state += 1
#            self.man[3] = self.string_index_replace(self.man[3], 5, "|")
#
#        elif self.state == 2:
#            self.state += 1
#            self.man[3] = self.string_index_replace(self.man[3], 3, "-")
#            self.man[3] = self.string_index_replace(self.man[3], 4, "-")
#
#        elif self.state == 3:
#            self.state += 1
#            self.man[3] = self.string_index_replace(self.man[3], 6, "-")
#            self.man[3] = self.string_index_replace(self.man[3], 7, "-")
#
#        elif self.state == 4:
#            self.state += 1
#            self.man[4] = self.string_index_replace(self.man[4], 5, "|")
#
#        for i in self.man:
#            print(i)


hangman = Hangman("apple")
