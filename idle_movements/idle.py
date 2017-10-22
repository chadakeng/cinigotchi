import time
from tkinter import *

#root = Tk()

list1=["idle_movements\cinigatchi_sprites\ciniidle2.PNG","idle_movements\cinigatchi_sprites\ciniidle1.PNG"]
"""while (n <= lenlist1):
photo = PhotoImage(file=list1[n])
label = Label(root, image=photo)
label.pack()
time.sleep(3)
n++"""

def idleMove(list1):
    for i in list1:
        root = Tk()
        print(i)
        photo = PhotoImage(file=i)
        label = Label(root, image=photo)
        label.pack()
        root.mainloop()

    return

while True:
    idleMove(list1)
