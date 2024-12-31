from tkinter import*
import os
from random import*
from time import*

class Card(Button):
    def __init__(self, match_image):
        super().__init__(image = secret_image)
        self.match_image = match_image
        self.opened = PhotoImage(file = match_image)
        self.stat = False                
        self.bind('<Button-1>', OnClick)
        
pair = []

def OnClick(event):
    global cards, images, pair
    card = event.widget    
    card.config(image = card.opened)
    card.update_idletasks()
    card.stat = True
    pair.append(card)

    counter = 0
    for item in cards:
        if item.stat:
            counter += 1
    
    if counter == 2:
        pair.append(card)        
        if pair[0].match_image == pair[1].match_image:
            pair[0].unbind('<Button-1>')
            pair[1].unbind('<Button-1>')
        else:
            sleep(0.8)
            pair[0].config(image=secret_image)
            pair[1].config(image=secret_image)
                        
        pair = []
        for item in cards:
            item.stat = False


window = Tk()
window.title("Memory")
window.iconbitmap('icons/icon.ico')
window.resizable(width=False,  height=False)

directory = "images/"

secret_image = PhotoImage(file='icons/awesome-memory-icon.gif')
images = []
path = os.listdir(directory)

for i in range(len(path)):
    path[i] = directory + path[i]    
    images.append(path[i])
    images.append(path[i])    

shuffle(images)

cards = []
row = col = 0

for i in range(4):
    for j in range(7):
        card = Card(match_image = images[7*row + col])        
        card.grid(row = row,column = col,padx = 3,pady = 3)
        cards.append(card)
        col+=1
    if col>6:
        col=0
        row+=1

window.mainloop()
