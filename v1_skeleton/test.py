from tkinter import *
root = Tk()

root.title("wellcome to GeekForGeeks")
root.geometry('350x200')

label = Label(root, text="GeeksForGeeks.org!")
label.pack()

IbI = Label(root,text="are you a geek?")
IbI.pack()

root.title("Counting Seconds")

button = Button(root, text="Stop", width=25, command=root.destroy)
button.pack()


Label(root, text="First Name").pack()
Label(root, text="Last Name").pack()

entry1 = Entry(root)
entry2 = Entry(root)

entry1.pack()
entry2.pack()


root.mainloop()