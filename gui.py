import tkinter

historyfile = open(r"Voice-main\text files\history.txt" , 'r+')
root = tkinter.Tk()


contents = historyfile.readlines()
histlabel = tkinter.Label(text= "History: ")
histlabel.pack()
for x in contents:
    hislabel = tkinter.Label(text = x, padx=122 ,pady=10 )
    print(x)
    hislabel.pack()
    







root.mainloop()