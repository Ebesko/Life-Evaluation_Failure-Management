from tkinter import *

class MainWindow:
    """Set the main window of Life Evaluation"""
    def __init__(self, window):
        self.window = window

    def main_question(self):
        """Print the main question"""
        txt_main_question = Label(self.window, text="How bad is your life rn?")
        txt_main_question.pack()

    def close_button(self):
        """Print the close button"""
        button_close = Button(self.window, text="Close", command=self.window.quit)
        button_close.pack()

    def scale_of_something(self):
        """Print the message and the scale related"""
        txt_scale = Label(window, text="On a scale of 0 to 100?")
        txt_scale.pack()
        value = DoubleVar()
        scale_1_to_100 = Scale(window, variable=value)
        scale_1_to_100.pack()

    def radio_button(self):
        """Print the message and 1 choice button related"""
        txt_descript = Label(window, text="How would you describe your life?")
        txt_descript.pack()
        value = StringVar()
        button1 = Radiobutton(window, text="Ok", variable=value, value=1)
        button2 = Radiobutton(window, text="Terrible", variable=value, value=2)
        button3 = Radiobutton(window, text="Awful & I want to die", variable=value, value=3)
        button1.pack(side=LEFT, padx=5, pady=5)
        button2.pack(side=LEFT, padx=5, pady=5)
        button3.pack(side=LEFT, padx=5, pady=5)

    def checkbutton(self):
        """Print the message and the checkboxes related"""
        txt_chk_box = Label(window, text="And what's wrong exactly?")
        txt_chk_box.pack()
        button1 = Checkbutton(window, text="ME")
        button2 = Checkbutton(window, text="I'm ugly as f*ck")
        button3 = Checkbutton(window, text="I have no money")
        button4 = Checkbutton(window, text="I am a lazy bum")
        button5 = Checkbutton(window, text="I hate humans")
        button6 = Checkbutton(window, text="Everything is wrong with me")
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()

    def run(self):
        """Run all necessary functions"""
        self.main_question()
        self.scale_of_something()
        self.radio_button()
        self.checkbutton()
        self.close_button()
        self.window.mainloop()


if __name__ == "__main__":
    window = Tk()
    window.title("Failure Management")
    app = MainWindow(window)
    app.run()
