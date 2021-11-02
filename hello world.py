from random import random, randint
class card():
    def __init__(self, name , val , suit ):
        self.val = val
        self.suit = suit
        self.name = str(name)
    def displayname(self):
        return self.name + " of " + self.suit +"s"

def cardpicker(listsofint):
    num = randint(0, len(listsofint ) -1)
    cardidx = listsofint.pop(num)
    return Deck[cardidx]

def intcheck(vari):
    try :
        temp = int(vari)
        return True 
    except :
        return False 


c1 = card("Ace" , 11 , "Diamond")# creating cards
c2 = card("Ace" , 11 , "Clover")
c3 = card("Ace" , 11 , "Heart")
c4 = card("Ace" , 11 , "Spade")
c5 = card("Two" , 2 , "Diamond")
c6 = card("Two" , 2 , "Clover")
c7 = card("Two" , 2 , "Heart")
c8 = card("Two" , 2 , "Spade")
c9 = card("Three" , 3 , "Diamond")
c10 = card("Three" ,3 , "Clover")
c11= card("Three" , 3 , "Heart")
c12 =card("Three" , 3 , "Spade")
c13 = card("Four" , 4 , "Diamond")
c14 = card("Four" , 4 , "Clover")
c15 = card("Four" , 4 , "Heart")
c16 = card("Four" , 4 , "Spade")
c17 = card("Five" , 5 , "Diamond")
c18 = card("Five" , 5 , "Clover")
c19 = card("Five" , 5 , "Heart")
c20 = card("Five" , 5 , "Spade")
c21 = card("Six" , 6 , "Diamond")
c22 = card("Six" , 6 , "Clover")
c23 = card("Six" , 6 , "Heart")
c24 = card("Six" , 6 , "Spade")
c25 = card("Seven" , 7 , "Diamond")
c26 = card("Seven" , 7 , "Clover")
c27 = card("Seven" , 7 , "Heart")
c28 = card("Seven" , 7 , "Spade")
c29 = card("Eight" , 8 , "Diamond")
c30 = card("Eight" , 8 , "Clover")
c31 = card("Eight" , 8 , "Heart")
c32 = card("Eight" , 8 , "Spade")
c33 = card("Nine" , 9 , "Diamond")
c34 = card("Nine" , 9 , "Clover")
c35 = card("Nine" , 9 , "Heart")
c36 = card("Nine" , 9 , "Spade")
c37 = card("Ten" , 10, "Diamond")
c38 = card("Ten" , 10 , "Clover")
c39 = card("Ten" , 10 , "Heart")
c40 = card("Ten" , 10 , "Spade")
c41 = card("Jack" , 10 , "Diamond")
c42 = card("Jack" , 10 , "Clover")
c43 = card("Jack" , 10 , "Heart")
c44 = card("Jack" , 10 , "Spade")
c45 = card("Queen" , 10 , "Diamond")
c46 = card("Queen" , 10 , "Clover")
c47 = card("Queen" , 10 , "Heart")
c48 = card("Queen" , 10 , "Spade")
c49 = card("King" , 10 , "Diamond")
c50 = card("King" , 10 , "Clover")
c51 = card("King" , 10 , "Heart")
c52 = card("King" , 10 , "Spade")
# creating the deck
Deck = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12 , c13, c14, c15, c16, c17, c18, c19 , c20 , c21, c22, c23, c24, c25, c26, c27, c28, c29 ,c30, c31 , c32, c33, c34, c35, c36, c37, c38, c39 , c40 ,c41, c42 , c43, c44, c45, c46, c47, c48 ,c49, c50 , c51, c52)
###Main Program
print("++++++++++++++++++++++++++++++++++++++")
print("Welcome To Jun Shengs Blackjack Casino")
print("Blackjack Pays 3 to 2")
print("Dealer hits on soft 17")
print("Insurance pays 2 to 1")
print("++++++++++++++++++++++++++++++++++++++")

capital = input("How much would you like to cash in?  ")
while True:# user cashing in
    try :
        capital = int(capital)
        print("you have cashed in {} dollars".format(str(capital)))
        break
    except:
        print("please input a valid number")
        capital = input("How much would you like to cash in?  ")
while True:# start of new game
    deckofcards = [i for i in list(range(0, 52))]
    bet_amount = input("Please Place your bet  ")
    while True:# type check
        if intcheck(bet_amount) == True:
            if int(bet_amount) <= capital:
                print ("you are betting {}".format(str(bet_amount)))
                break
            else:
                print("bet bigger than capital please input correct bet ")
        bet_amount = input("Please Place your bet  ")
        

    break