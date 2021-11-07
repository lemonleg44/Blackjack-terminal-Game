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

class player :
    
    def __init__(self) -> None:
        self.hand = []
    def blackjack(self):
        total = 0
        for card in self.hand:
            total += card.val
        if total == 21:
            return True
        else:
            return False
    def deal(self):
        self.hand.append(cardpicker(deckofcards))
        self.hand.append(cardpicker(deckofcards))
        
    def hit(self):
        self.hand.append(cardpicker(deckofcards))
        

    def showhand(self):
        print("PLayers Cards:")
        for card in self.hand:
            print (card.displayname())
    def calchand(self):
        total_val = 0
        a_counter = 0
        for card in self.hand :
            if card.val == 11:
                a_counter += 1
            total_val +=  card.val
        while a_counter != 0  and total_val> 21:
            a_counter -= 1
            total_val -= 10
        if total_val <= 21:
            return(True, total_val) 
        else:
            return (False, total_val)
        

        
class dealer(player):
    def __init__(self) -> None:
        super().__init__()
    def showone(self):
        print("Dealers Faceup Card")
        print(self.hand[0].displayname())
    def soft17(self):
        total = 0
        a_counter = 0
        for card in self.hand:
            if card.val == 11:
                a_counter +=1
            total += card.val
        if total == 17 and a_counter == 1:
            return True
        else:
            return False
    def dealershowhand(self):
        print("Dealers Cards:")
        for card in self.hand:
            print (card.displayname())

    def dealerai(self):
        
        if self.soft17() == True:
            self.hit()
            while self.calchand()[1] < 18:
                self.hit()
        else:
            while self.calchand()[1] < 17:
                self.hit()

def game(yesorno):
    global capital
    if yesorno == "1":
        print ("games has ended")
        return None
    
    elif yesorno == "2":
        global deckofcards
        deckofcards = [i for i in list(range(0, 52))]
        bet_amount = input("Please Place your bet  ")

        while True:# type check
            if intcheck(bet_amount) == True:
                if int(bet_amount) <= capital:
                    print ("you are betting {}".format(str(bet_amount)))
                    break
                elif capital == 0:
                    game("1")
                else:
                    print("bet bigger than capital please input correct bet ")
            bet_amount = input("Please Place your bet  ")
        bet_amount = int(bet_amount)
        dealer1 = dealer()
        player1 = player()  
        player1.deal()
        dealer1.deal()
        dealer1.showone()
        player1.showhand()
        if player1.blackjack() == True and dealer1.blackjack() == False:
            print("you Blackjacked!")
            print("you win!")
            value_won = bet_amount * 1.5
            capital += value_won
            print("your new capital is {}".format(str(capital)))
            inputbool = input("press 1 to continue and press 2 to end game ")
            game(inputbool)
        elif player1.blackjack() == False and dealer1.blackjack() == True:
            capital -= bet_amount
            print("dealer Blackjack")
            print("you lost better luck next time!")
            print("your new capital is {}".format(str(capital)))
            inputbool = input("press 1 to continue and press 2 to end game ")
            game(inputbool)
        elif player1.blackjack() == True and dealer1.blackjack() == True:
            print("bet is pushed")
            print("your new capital is {}".format(str(capital)))
            inputbool = input("press 1 to continue and press 2 to end game ")
            game(inputbool)
        bust = False
        while True and bust == False:
            sorh = input("stand or hit press 1 to stand 2 to hit:   ")
            if sorh == "1":
                print("++++++++++++++")
                player1.showhand()
                print("your hand value is {}".format(str(player1.calchand()[1])))
                print("+++++++++++++++++")
                break
            else:
                player1.hit()
                player1.showhand()
                if player1.calchand()[0] == False:
                    
                    capital -= bet_amount
                    bust = True
        print("------------------------")
        
        print("your hand value is {}".format(str(player1.calchand()[1])))
        if bust == False:
            dealer1.dealerai()
        print("--------------------------")
        dealer1.dealershowhand()
        print("dealers hand value is {}".format(str(dealer1.calchand()[1])))
        if player1.calchand()[1] > 21:
            print ("bust lah u greedy bastard")
            print("your new capital is {}".format(str(capital)))
            inputbool = input("press 1 to end and press 2 to continue ")
            game(inputbool)

        elif dealer1.calchand()[0] == False or dealer1.calchand()[1] < player1.calchand()[1]:
            capital += bet_amount
            print("You won!")
            print("your new capital is {}".format(str(capital)))
            inputbool = input("press 1 to end and press 2 continue ")
            game(inputbool)
        elif  dealer1.calchand()[1] == player1.calchand()[1]:
            print("bet is pushed")
            print("your new capital is {}".format(str(capital)))
            inputbool = input("press 1 to end and press 2 to continue ")
            game(inputbool)
        else:
            capital -= bet_amount
            print("you lost better luck next time!")
            print("your new capital is {}".format(str(capital)))
            inputbool = input("press 1 to end and press 2 to continue ")
            game(inputbool)
    else:
        print ("invalid input please input correctly")        
         

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
print(game("2"))
# while True:# start of new game
#     deckofcards = [i for i in list(range(0, 52))]
#     bet_amount = input("Please Place your bet  ")
#     while True:# type check
#         if intcheck(bet_amount) == True:
#             if int(bet_amount) <= capital:
#                 print ("you are betting {}".format(str(bet_amount)))
#                 break
#             else:
#                 print("bet bigger than capital please input correct bet ")
#         bet_amount = input("Please Place your bet  ")
#     bet_amount = int(bet_amount)
#     dealer1 = dealer()
#     player1 = player()  
#     player1.deal()
#     dealer1.deal()
#     dealer1.showone()
#     player1.showhand()
#     if player1.blackjack() == True and dealer1.blackjack() == False:
#         print("you Blackjacked!")
#         print("you win!")
#         value_won = bet_amount * 1.5
#         capital += value_won
#         print("your new capital is {}".format(str(capital)))
#         break #game end
#     elif player1.blackjack() == False and dealer1.blackjack() == True:
#         capital -= bet_amount
#         print("dealer Blackjack")
#         print("you lost better luck next time!")
#         print("your new capital is {}".format(str(capital)))
#         break # game end
#     elif player1.blackjack() == True and dealer1.blackjack() == True:
#         print("bet is pushed")
#         print("your new capital is {}".format(str(capital)))
#         break #game end
#     bust = False
#     while True and bust == False:
#         sorh = input("stand or hit press 1 to stand 2 to hit:   ")
#         if sorh == "1":
#             print("++++++++++++++")
#             player1.showhand()
#             print("your hand value is {}".format(str(player1.calchand()[1])))
#             print("+++++++++++++++++")
#             break
#         else:
#             player1.hit()
#             player1.showhand()
#             if player1.calchand()[0] == False:
                
#                 capital -= bet_amount
#                 bust = True
#     print("------------------------")
    
#     print("your hand value is {}".format(str(player1.calchand()[1])))
#     dealer1.dealerai()
#     print("--------------------------")
#     dealer1.dealershowhand()
#     print("dealers hand value is {}".format(str(dealer1.calchand()[1])))
#     if player1.calchand()[1] > 21:
#         print ("bust lah u greedy bastard")
#         print("your new capital is {}".format(str(capital)))
#         break #game end

#     elif dealer1.calchand()[0] == False or dealer1.calchand()[1] < player1.calchand()[1]:
#         capital += bet_amount
#         print("You won!")
#         print("your new capital is {}".format(str(capital)))
#         break #game end
#     elif  dealer1.calchand()[1] == player1.calchand()[1]:
#         print("bet is pushed")
#         print("your new capital is {}".format(str(capital)))
#         break # gameend
#     else:
#         capital -= bet_amount
#         print("you lost better luck next time!")
#         print("your new capital is {}".format(str(capital)))
#         break #game end
        
    