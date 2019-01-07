#!/usr/bin/env python3
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open("gen1_normal.png")
photo = ImageTk.PhotoImage(image)

text1 = Text(root, height=20, width=30)
#photo = PhotoImage(file='gen1_normal.png')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)

text2 = Text(root, height=20, width=50)
# scroll = Scrollbar(root, command=text2.yview)
# text2.configure(yscrollcommand=scroll.set)
# text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
# text2.tag_configure('big', font=('Verdana', 20, 'bold'))
# text2.tag_configure('color', foreground='#476042', 
# 						font=('Tempus Sans ITC', 12, 'bold'))
# text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
# text2.insert(END,'\nWBIGGO POKEMON TIMES\n', 'big')
# quote = """
# OH LOOK< IT"S A GODDAMN POKEMONE!
# """
# text2.insert(END, quote, 'color')
# text2.insert(END, 'follow-up\n', 'follow')
# text2.pack(side=LEFT)
# scroll.pack(side=RIGHT, fill=Y)

root.mainloop()




# master = Tk()  
# choices = ["Apple", "Orange", "Pear"]
# canceled = BooleanVar()
# def cancelAction(): 
# 	canceled.set(True); master.quit()
# Label(master, text="Choose a fruit:").pack()
# listbox = Listbox(master, selectmode=EXTENDED) # Multiple options can be chosen
# for text in choices: 
# 	listbox.insert(END, text)
# listbox.pack()    
# Button(master, text="OK", command=master.quit).pack(side=LEFT, ipadx=10)
# Button(master, text="Cancel", command=cancelAction).pack(side=RIGHT, ipadx=10)
# mainloop()
# if not canceled.get():
# 	print(listbox.curselection()) # A tuple of choice indices starting with 0
# 	# The above is a tuple even if selectmode=SINGLE
# 	if "0" in listbox.curselection(): print("Apple chosen.")
# 	if "1" in listbox.curselection(): print("Orange chosen.")
# 	if "2" in listbox.curselection(): print("Pear chosen.")
# else:
# 	print("Choice canceled.")