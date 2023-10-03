from tkinter import *


class MainWindow:
    """Set the main window of Life Evaluation: Failure Management"""
    def __init__(self, window):

        #Set up name, size and min size of the window
        self.window = window
        self.window.title("Life Evaluation: Failure Management")
        self.window.geometry("600x500")
        #self.window.minsize(400, 300)

        # Create a top frame for the title
        self.create_top_frame()

        # Configure rows and columns to expand and fill
        for i in range(2):  # Two rows
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(2):  # Two columns
            self.window.grid_columnconfigure(i, weight=1)

        # Create the four frames
        self.upper_left_frame = self.create_frame(0, 0, "Upper Left")
        self.upper_right_frame = self.create_frame(0, 1, "Upper Right")
        self.lower_left_frame = self.create_frame(1, 0, "Lower Left")
        self.lower_right_frame = self.create_frame(1, 1, "Lower Right")

    def create_top_frame(self):
        top_frame = Frame(self.window)
        top_frame.grid(row=0, column=0, columnspan=2)

        label = Label(top_frame, text="Main question", font=("Helvetica", 12))
        label.pack(padx=10, pady=10)

        return top_frame

    def create_frame(self, row, column, label_text):
        frame = Frame(self.window, relief=RIDGE, borderwidth=2)
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        label = Label(frame, text=label_text, font=("Helvetica", 12))
        label.pack(side=TOP)

        return frame

    def frame(self):
        left_frame = Frame(window, width=200, height=300, bg='white')
        left_frame.place(x=0, y=0)
        #left_frame.pack(side=LEFT, anchor=NW)
        #txt_scale = Label(left_frame, text="On a scale of 0 to 100?")
        #txt_scale.pack()

    def close_button(self):
        """Print the close button"""
        button_close = Button(self.window, text="Close", command=self.window.quit)
        #button_close.pack()

    def scale_of_something(self):
        """Print the message and the scale related"""
        txt_scale = Label(window, text="On a scale of 0 to 100?")
        #txt_scale.pack()
        value = DoubleVar()
        scale_1_to_100 = Scale(window, variable=value)
        #scale_1_to_100.pack()

    def radio_button(self):
        """Print the message and 1 choice button related"""
        txt_descript = Label(window, text="How would you describe your life?")
        #txt_descript.pack(side="left")
        value = StringVar()
        button1 = Radiobutton(window, text="Ok", variable=value, value=1)
        button2 = Radiobutton(window, text="Terrible", variable=value, value=2)
        button3 = Radiobutton(window, text="Awful & I want to die", variable=value, value=3)
        #button1.pack(side=LEFT)
        #button2.pack(side=LEFT)
        #button3.pack(side=LEFT)

    def check_button(self):
        """Print the message and the checkboxes related"""
        txt_chk_box = Label(window, text="And what's wrong exactly?")
        txt_chk_box.pack()
        button1 = Checkbutton(window, text="ME")
        button2 = Checkbutton(window, text="I'm ugly as f*ck")
        button3 = Checkbutton(window, text="I have no money")
        button4 = Checkbutton(window, text="I am a lazy bum")
        button5 = Checkbutton(window, text="I hate humans")
        button6 = Checkbutton(window, text="Everything is wrong with me")
        #button1.pack()
        #button2.pack()
        #button3.pack()
        #button4.pack()
        #button5.pack()
        #button6.pack()

    def run(self):
        """Run all necessary functions"""
        #self.main_question()
        #self.scale_of_something()
        #self.radio_button()
        #self.check_button()
        #self.close_button()
        self.window.mainloop()


if __name__ == "__main__":
    window = Tk()
    #window.title("Life Evaluation: Failure Management")
    #window.geometry("1000x800")
    app = MainWindow(window)
    app.run()
