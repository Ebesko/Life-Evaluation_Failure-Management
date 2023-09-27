from Fonctions import *


def mainQuestion():
    question = Label(window, text="How bad is your life rn?")
    question.pack()


def closeButton():
    buttonClose = Button(window, text="Close", command=window.quit)
    buttonClose.pack()

mainQuestion()
scaleOfSomething()
radiobutton()
closeButton()
checkbutton()

window.mainloop()

