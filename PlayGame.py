import tkinter as tk
from tkmacosx import Button
from random import randint
from PIL import Image, ImageTk
from time import time

class Game:
    def __init__(self, root):
        self.money=1000
        self.userBusted = False
        self.dealerBusted = False
        self.cardList = list()
        self.outterFrame = tk.Frame(root, bg="#03C04A")
        self.outterFrame.place(relwidth=1, relheight=1)
        self.middleFrame = tk.Frame(self.outterFrame, bg='black')
        self.middleFrame.place(relx=.03, rely=.03, relheight=.85, relwidth=.94)
        self.innerFrame = tk.Frame(self.middleFrame, bg='green')
        self.innerFrame.place(relx=.01, rely=.02, relheight=.95, relwidth=.98)

    def dealCards(self):
        self.dealButton = Button(self.outterFrame, text='Deal', bg='blue', fg='white',
                                 font=('times', 15), command=self.deal)
        self.dealButton.place(relx=.4, rely=.92)
        self.moneyLabel = tk.Label(self.outterFrame, text="Cash:", bg='#03C04A', fg='#234F1E',
                                   font=('times', 20))
        self.moneyLabel.place(relx=.25, rely=.91)
        self.moneyAmount = tk.Label(self.outterFrame, text= "$" + str(self.money), bg='#03C04A',
                                    font=('times', 20, 'bold'), fg='black')
        self.moneyAmount.place(relx=.29, rely=.91)

    def deal(self):
        self.userVal = 0
        self.dealerVal = 0
        self.dealButton.destroy()
        self.userX=.15
        self.userY=.61
        self.dealerX =.15
        self.dealerY =.05

        self.card1 = self.getCards()
        self.card2 = self.getCards()
        self.loadCard(self.card1, "User", self.userX, self.userY)
        self.loadCard(self.card2, "User", self.userX, self.userY)

        self.cardList.clear()

        self.dealerCard1 = self.getCards()
        self.dealerCard2 = self.getCards()
        self.loadCard(self.dealerCard1, "Dealer", self.dealerX, self.dealerY)
        self.loadCard(self.dealerCard2, "Dealer", self.dealerX, self.dealerY)

        self.stayButton = Button(self.outterFrame, text="Stay", bg='blue', fg='white',
                                 font=('times',15), command=self.stay)
        self.stayButton.place(relx=.45, rely=.92)
        self.hitButton = Button(self.outterFrame, text="Hit", bg='blue', fg='white',
                                 font=('times', 15), command=self.hit)
        self.hitButton.place(relx=.37, rely=.92)

    def hit(self):
        card=self.getCards()
        self.loadCard(card, "User", self.userX, self.userY)

    def stay(self):
        cardFrame = tk.Frame(self.innerFrame, bg='white', highlightbackground="black", highlightthickness=2)
        cardFrame.place(relx=.15, rely=.05, relwidth=.09, relheight=.37)
        self.cardLabel1 = tk.Label(cardFrame, text=self.dealerBlankVal, bg='white', fg='black', font=('times', 20))
        self.cardLabel1.place(relx=.08, rely=.03)
        self.cardLabel2 = tk.Label(cardFrame, text=self.dealerBlankVal, bg='white', fg='black', font=('times', 20))
        self.cardLabel2.place(relx=.7, rely=.77)
        if self.dealerSuite == "Clubs":
            imageName = "club.png"
        elif self.dealerSuite == "Hearts":
            imageName = "heart.png"
        elif self.dealerSuite == "Diamonds":
            imageName = "diamond.png"
        elif self.dealerSuite == "Spades":
            imageName = "spade.png"

        image = Image.open(imageName)
        render = ImageTk.PhotoImage(image)
        img = tk.Label(cardFrame, image=render, bg='white')
        img.image = render
        img.place(relx=.25, rely=.25, relwidth=.5, relheight=.5)

        self.hitButton.destroy()
        self.stayButton.destroy()

        while self.dealerVal < 17:
            card = self.getCards()
            self.loadCard(card, "Dealer", self.dealerX, self.dealerY)
            self.getDealerValue()
        self.getDealerValue()
        self.getResults()


    def getCards(self):
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "1", "J", "Q", "K"]
        suits = ["Clubs", "Hearts", "Diamonds", "Spades"]


        cardVal = randint(0, len(cards)-1)
        suitVal = randint(0, len(suits)-1)
        card = cards[cardVal] + suits[suitVal]

        return card

    def loadCard(self, card, player, x, y):

        cardNum = card[0]
        cardSuit = card[1:]
        if cardNum == "1":
            cardNum = "10"

        self.cardFrame = tk.Frame(self.innerFrame, bg='white', highlightbackground="black", highlightthickness=2)
        self.cardFrame.place(relx=x, rely=y, relwidth=.09, relheight=.37)

        if self.dealerVal == 0 and player == "Dealer":
            image = Image.open("backside.jpg")
            render = ImageTk.PhotoImage(image)
            img = tk.Label(self.cardFrame, image=render, bg='white')
            img.image = render
            img.place(relx=.01, rely=.01, relwidth=.98, relheight=.98)
            self.dealerBlankVal = cardNum
            self.dealerSuite = cardSuit

        else:
            self.cardLabel1 = tk.Label(self.cardFrame, text=cardNum, bg='white', fg='black', font=('times',20))
            self.cardLabel1.place(relx=.08, rely=.03)
            self.cardLabel2 = tk.Label(self.cardFrame, text=cardNum, bg='white', fg='black', font=('times',20))
            self.cardLabel2.place(relx=.7, rely=.77)

            if cardSuit == "Clubs":
                imageName = "club.png"
            elif cardSuit == "Hearts":
                imageName = "heart.png"
            elif cardSuit == "Diamonds":
                imageName = "diamond.png"
            elif cardSuit == "Spades":
                imageName = "spade.png"

            image = Image.open(imageName)
            render = ImageTk.PhotoImage(image)
            img = tk.Label(self.cardFrame, image=render, bg='white')
            img.image = render
            img.place(relx=.25, rely=.25, relwidth=.5, relheight=.5)

        if player == "User":
            if cardNum == "J" or cardNum == "Q" or cardNum == "K":
                self.userVal += 10
            elif cardNum == "A":
                self.userVal += 11
            else:
                self.userVal += int(cardNum)

            self.cardList.append(cardNum)
            busted=False
            if self.userVal > 21:
                for crd in self.cardList:
                    if crd != "A":
                        busted=True
                    else:
                        self.userVal -= 10
                        self.cardList.remove("A")
                        busted=False
                        break

            self.userValLabel = tk.Label(self.innerFrame, text="User - " + str(self.userVal), bg='green', fg='white',
                                         font=('times',25))
            self.userValLabel.place(relx=.03, rely=.75)

            if busted:
                self.bustedLabel = tk.Label(self.innerFrame, text="You Busted!", bg='green', fg='#811111', font=('times',30))
                self.bustedLabel.place(relx=.4, rely=.45)
                self.userBusted = True
                self.dealerWin = tk.Label(self.innerFrame, text="Dealer Wins", bg='green', fg='black', font=('times', 30))
                self.dealerWin.place(relx=.7, rely=.45)
                self.money -= 100
                self.hitButton.destroy()
                self.stayButton.destroy()
                self.getResults()

            self.userX += .1

        else:
            if cardNum == "J" or cardNum == "Q" or cardNum == "K":
                self.dealerVal += 10
            elif cardNum == "A":
                self.dealerVal += 11
            else:
                self.dealerVal += int(cardNum)

            self.cardList.append(cardNum)
            busted = False
            if self.dealerVal > 21:
                for crd in self.cardList:
                    if crd != "A":
                        busted = True
                    else:
                        self.dealerVal -= 10
                        self.cardList.remove("A")
                        busted = False
                        break

            if busted:
                self.dealerBustedLabel = tk.Label(self.innerFrame, text="Dealer Busted!", bg='green', fg='#811111',
                                            font=('times', 30))
                self.dealerBustedLabel.place(relx=.4, rely=.45)
                self.dealerBusted = True
                self.youWin = tk.Label(self.innerFrame, text="You Win", bg='green', fg ='black', font=('times', 30))
                self.youWin.place(relx=.7, rely=.45)
                self.money += 100

            self.dealerX += .1

    def getDealerValue(self):
        self.dealerValLabel = tk.Label(self.innerFrame, text="Dealer - " + str(self.dealerVal), bg='green',
                                        fg='white', font=('times', 25))
        self.dealerValLabel.place(relx=.03, rely=.15)

    def getResults(self):
        self.moneyAmount.destroy()
        if self.dealerBusted:
            self.wonMoney()
        elif self.userBusted:
            self.lostMoney()

        if not self.dealerBusted and not self.userBusted:
            if self.dealerVal == self.userVal:
                self.drawLabel = tk.Label(self.innerFrame, text="Push", bg='green', fg='white', font=('times',30))
                self.drawLabel.place(relx=.45, rely=.45)
                self.noMoney()
            elif self.dealerVal > self.userVal:
                self.dealerWinLabel = tk.Label(self.innerFrame, text="Dealer Wins", bg='green', fg='black', font=('times',30))
                self.dealerWinLabel.place(relx=.45, rely=.45)
                self.lostMoney()
                self.money -= 100
            else:
                self.userWinLabel = tk.Label(self.innerFrame, text="User Wins", bg='green', fg='black', font=('times',30))
                self.userWinLabel.place(relx=.45, rely=.45)
                self.wonMoney()
                self.money += 100

        self.dealerBusted=False
        self.userBusted=False
        self.shuffleButton = Button(self.outterFrame, text='Shuffle', bg='blue', fg='white',
                                 font=('times', 15), command=self.newGame)
        self.shuffleButton.place(relx=.12, rely=.92)

    def wonMoney(self):
        self.wonMoneyLabel = tk.Label(self.outterFrame, text="+ $100", bg='#03C04A', fg='#234F1E', font=('times', 20, 'bold'))
        self.wonMoneyLabel.place(relx=.295, rely=.91)
        self.lost = False

    def lostMoney(self):
        self.lostMoneyLabel = tk.Label(self.outterFrame, text="- $100", bg='#03C04A', fg='#811111',
                                      font=('times', 20, 'bold'))
        self.lostMoneyLabel.place(relx=.295, rely=.91)
        self.lost = True

    def noMoney(self):
        self.noMoneyLabel = tk.Label(self.outterFrame, text="+ $0", bg='#03C04A', fg='white',
                                      font=('times', 20, 'bold'))
        self.noMoneyLabel.place(relx=.295, rely=.91)
        self.draw = True

    def newGame(self):
        self.shuffleButton.destroy()
        self.innerFrame.destroy()
        if self.lost:
            self.lostMoneyLabel.destroy()
        elif not self.lost:
            self.wonMoneyLabel.destroy()
        elif self.draw:
            self.noMoneyLabel.destroy()
        self.innerFrame = tk.Frame(self.middleFrame, bg='green')
        self.innerFrame.place(relx=.01, rely=.02, relheight=.95, relwidth=.98)
        self.dealCards()



