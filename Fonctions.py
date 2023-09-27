from tkinter import *
window = Tk()

def label():
    label = Label(window, text="Texte par défaut", bg="blue")
    label.pack()

def entrée():
    value = StringVar()
    value.set("texte par défaut")
    entree = Entry(window, textvariable=value, width=30)
    entree.pack()

def checkbutton():
    Blu = Label(window, text="And what's wrong exactly?")
    Blu.pack()
    bouton = Checkbutton(window, text="ME")
    bouton2 = Checkbutton(window, text="I'm ugly as f*ck")
    bouton3 = Checkbutton(window, text="I have no money")
    bouton4 = Checkbutton(window, text="I am a lazy bum")
    bouton5 = Checkbutton(window, text="I hate humans")
    bouton6 = Checkbutton(window, text="Everything is wrong with me")
    bouton.pack()
    bouton2.pack()
    bouton3.pack()
    bouton4.pack()
    bouton5.pack()
    bouton6.pack()

def radiobutton():
    Bla = Label(window, text="How would you describe your life?")
    Bla.pack()
    value = StringVar()
    bouton1 = Radiobutton(window, text="Ok", variable=value, value=1)
    bouton2 = Radiobutton(window, text="Terrible", variable=value, value=2)
    bouton3 = Radiobutton(window, text="Awful & I want to die", variable=value, value=3)
    bouton1.pack(side=LEFT, padx=5, pady=5)
    bouton2.pack(side=LEFT, padx=5, pady=5)
    bouton3.pack(side=LEFT, padx=5, pady=5)

def liste():
    liste = Listbox(window)
    liste.insert(1, "Python")
    liste.insert(2, "PHP")
    liste.insert(3, "jQuery")
    liste.insert(4, "CSS")
    liste.insert(5, "Javascript")
    liste.pack()

def canvas():
    canvas = Canvas(window, width=150, height=120, background='yellow')
    ligne1 = canvas.create_line(75, 0, 75, 120)
    ligne2 = canvas.create_line(0, 60, 150, 60)
    ligne3 = canvas.create_oval()
    txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
    canvas.pack()

def scaleOfSomething():
    label = Label(window, text="On a scale of 0 to 100?")
    label.pack()
    value = DoubleVar()
    scale = Scale(window, variable=value)
    scale.pack()

def Frames():
    window['bg'] = 'white'
    # frame 1
    Frame1 = Frame(window, borderwidth=2, relief=GROOVE)
    Frame1.pack(side=LEFT, padx=30, pady=30)
    radiobutton()

    # frame 2
    Frame2 = Frame(window, borderwidth=2, relief=GROOVE)
    Frame2.pack(side=LEFT, padx=10, pady=10)
    scaleOfSomething()

    # frame 3 dans frame 2
    #Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
    #Frame3.pack(side=RIGHT, padx=5, pady=5)

    # Ajout de labels
    Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
    Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
    #Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)