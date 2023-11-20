import tkinter

import customtkinter as ctk


class FailureManagement(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Life Evaluation: Failure Management")
        self.geometry("500x500+700+300")

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        label = ctk.CTkLabel(self, text="How bad is your life right now?", font=("Helvetica", 16))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Scale Frame
        self.upper_left = MyFrameTest(self, "...On a scale of 1 to 100?")
        self.upper_left.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.upper_left.scale()

        # Chkbox Frame
        self.upper_right = MyFrameTest(self, "And what's wrong exactly?")
        self.upper_right.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.upper_right.chkboxes()

        # Radiobutton Frame
        self.lower_left = MyFrameTest(self, "How would you describe your life?")
        self.lower_left.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.lower_left.radiobuttons()

        # Options Frame
        self.lower_right = MyFrameTest(self, "Options")
        self.lower_right.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.lower_right.buttons()

    def button_callback(self):
        print("button pressed")


class MyFrameTest(ctk.CTkFrame):

    def __init__(self, master, title):
        super().__init__(master)
        self.title = title
        self.title = ctk.CTkLabel(self, text=self.title, fg_color="transparent", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        self.grid(row=0, column=0, columnspan=2)
        self.grid_columnconfigure((0, 1), weight=1)

    def scale(self):
        scaleforce = tkinter.IntVar()
        slider = ctk.CTkSlider(self, from_=1, to=100, variable=scaleforce, orientation="vertical",
                               height=100)
        slider.grid()
        # slider_value = slider.cget()
        scale_label = ctk.CTkLabel(self, text="Test")
        scale_label.grid()

    def buttons(self):
        button = ctk.CTkButton(self, text="Score")
        button.grid()
        button1 = ctk.CTkButton(self, text="Options")
        button1.grid()
        button2 = ctk.CTkButton(self, text="Exit")
        button2.grid()

    def chkboxes(self):
        chkbox_names = ["ME", "I'm ugly as f*ck", "I have no money", "I am a lazy bum",
                 "I hate humans", "Everything is wrong with me"]
        for name in chkbox_names:
            check_var = ctk.StringVar(value="off")
            checkbox = ctk.CTkCheckBox(self, text=name, variable=check_var, onvalue="on", offvalue="off",
                                       checkbox_height=17, checkbox_width=17)
            checkbox.grid(sticky="nsew")

    def radiobuttons(self):
        radionames =["Ok", "Terrible", "Awful and I want to die"]
        for named in radionames:
            radio_var = tkinter.IntVar(value=0)
            radiobutton = ctk.CTkRadioButton(self, text=named, variable=radio_var, value=1)
            radiobutton.grid(sticky="nsew")



app = FailureManagement()
app.mainloop()
