import tkinter
import customtkinter as ctk

# FONT = ("Helvetica", 14)
FONT_TITLE = ("Helvetica", 16)


class FailureManagement(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Life Evaluation: Failure Management")
        self.geometry("500x500+700+300")

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Main Frame
        self.upper_upper = CreateTopFrame(self, "How bad is your life right now?", fg_color="transparent")
        self.upper_upper.grid(column=0, row=0, columnspan=3, sticky="nsew")

        # Scale Frame
        self.upper_left = CreateFrame(self, "...On a scale of 1 to 100?")
        self.upper_left.scale()
        self.upper_left.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Chkbox Frame
        self.upper_right = CreateFrame(self, "And what's wrong exactly?")
        self.upper_right.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.upper_right.chkboxes()

        # Radiobutton Frame
        self.lower_left = CreateFrame(self, "How would you describe your life?")
        self.lower_left.radiobuttons()
        self.lower_left.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Options Frame
        self.lower_right = CreateFrame(self, "Options")
        self.lower_right.buttons()
        self.lower_right.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")


class CreateTopFrame(ctk.CTkFrame):

    def __init__(self, master, title, **kwargs):
        super().__init__(master, **kwargs)
        self.title = title
        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color="transparent",
                                        corner_radius=6, font=FONT_TITLE)
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)


class CreateFrame(ctk.CTkFrame):

    def __init__(self, master, title):
        super().__init__(master)
        self.title = title
        self.title_label = ctk.CTkLabel(self, text=self.title, fg_color="transparent",
                                        corner_radius=6)
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)

        self.chkbox_list = []
        self.toggle_var = tkinter.BooleanVar()

    def scale(self):
        scaleforce = tkinter.IntVar()
        slider = ctk.CTkSlider(self, from_=1, to=100, variable=scaleforce, orientation="vertical",
                               height=100)
        slider.grid()

    def buttons(self):
        button = ctk.CTkButton(self, text="Score")
        button.grid(padx=10, pady=10)
        button1 = ctk.CTkButton(self, text="Options")
        button1.grid(padx=10, pady=10)
        button2 = ctk.CTkButton(self, text="Exit")
        button2.grid(padx=10, pady=10)

    def chkboxes(self):
        # On va plutot creer une classe de chkbox
        # Quoique....
        chkbox_names = ["ME", "I'm ugly as f*ck", "I have no money", "I am a lazy bum",
                        "I hate humans"]

        for name in chkbox_names:
            check_var = tkinter.BooleanVar(value=False)
            self.chkbox_list.append(check_var)
            chkbox = ctk.CTkCheckBox(self, text=name, variable=check_var,
                                     checkbox_height=17, checkbox_width=17)
            chkbox.grid(padx=10, pady=0, sticky="nsew")

        checkbox_all = ctk.CTkCheckBox(self, text="Everything is wrong with me", variable=self.toggle_var,
                                       command=self.toggle_checkboxes(),
                                       checkbox_height=17, checkbox_width=17)
        checkbox_all.grid(padx=10, pady=0, sticky="nsew")

    def toggle_checkboxes(self):
        # Get the state of the toggle checkbox
        toggle_state = self.toggle_var.get()
        print(toggle_state)

        # Set the state of all other checkboxes to match the toggle checkbox
        for checkbox_var in self.chkbox_list:
            checkbox_var.set(toggle_state)

    def radiobuttons(self):
        radionames = ["Ok", "Terrible", "Awful and I want to die"]
        radio_var = tkinter.IntVar(value=0)
        for i, named in enumerate(radionames):
            radiobutton = ctk.CTkRadioButton(self, text=named, variable=radio_var, value=i + 1)
            radiobutton.grid(padx=10, pady=5, sticky="nsew")


class CustomCheckbox(ctk.CTkCheckBox):
    def __init__(self, master, name, **kwargs):
        super().__init__(master, **kwargs)
        self.name = name

        self.check_var = ctk.StringVar(value="off")
        checkbox = ctk.CTkCheckBox(self, text=name, variable=self.check_var, onvalue="on", offvalue="off",
                                   checkbox_height=17, checkbox_width=17)
        checkbox.grid(padx=10, pady=0, sticky="nsew")

    def activate(self):
        self.check_var = "on"

    def deactivate(self):
        self.check_var = "off"


app = FailureManagement()
app.mainloop()
