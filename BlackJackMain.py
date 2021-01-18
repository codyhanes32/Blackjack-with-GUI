import tkinter as tk
from PIL import Image, ImageTk
from tkmacosx import Button
from PlayGame import Game

HEIGHT = 500
WIDTH = 1250

root = tk.Tk()
root.title("BlackJack")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def loadHome():
    frame = tk.Frame(root, bg="green")
    frame.place(relwidth=1, relheight=1)

    image = Image.open("BlackJackMain.jpg")
    render = ImageTk.PhotoImage(image)
    img = tk.Label(frame, image=render, bg='green')
    img.image = render
    img.place(relx=0, rely=.01, relheight=.987, relwidth=.726)
    BlackJackLabel = tk.Label(frame, text="BlackJack", fg='#811111', bg='green',
                                   font=('times', 37, 'bold'))
    BlackJackLabel.place(relx=.79, rely=.12)
    playButton = Button(frame, text="Start", fg='white', bg='blue', command=lambda: playGame(frame))
    playButton.place(relx=.825, rely=.25)

def playGame(frame):
    frame.destroy()
    playGame = Game(root)
    playGame.dealCards()


if __name__ == '__main__':
    loadHome()
    root.mainloop()