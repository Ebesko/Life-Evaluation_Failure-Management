import tkinter as tk


class CheckBoxWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Life Evaluation: Failure Management")

        # Set minimum window size (width, height)
        self.root.minsize(500, 500)  # Example minimum size

        # Create a top frame for the title
        self.create_top_frame()

        # Configure rows and columns to expand and fill
        for i in range(2):  # Two rows
            self.root.grid_rowconfigure(i + 1, weight=1)
        for i in range(2):  # Two columns
            self.root.grid_columnconfigure(i, weight=1)

        # Create the four frames
        self.upper_left_frame = self.create_frame(1, 0, "... On a scale of 1 to 100?")
        self.upper_right_frame = self.create_frame(1, 1, "And what's wrong exactly?")
        self.lower_left_frame = self.create_frame(2, 0, "How would you describe your life?")
        self.lower_right_frame = self.create_frame(2, 1, "Options")

        # Create checkboxes for each frame
        self.create_despair(self.upper_left_frame)
        self.create_problems(self.upper_right_frame)
        self.create_low_self_esteem(self.lower_left_frame)
        self.meet_your_end(self.lower_right_frame)


    def create_top_frame(self):
        top_frame = tk.Frame(self.root)
        top_frame.grid(row=0, column=0, columnspan=2)

        label = tk.Label(top_frame, text="How bad is your life right now?", font=("Helvetica", 12))
        label.pack(padx=10, pady=10)


    def create_frame(self, row, column, label_text):
        frame = tk.Frame(self.root, relief=tk.RIDGE, borderwidth=2)
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        label = tk.Label(frame, text=label_text, font=("Helvetica", 12))
        label.pack(side=tk.TOP)

        return frame

    def create_low_self_esteem(self, frame):
        """For low choice radiobuttons"""
        value = tk.StringVar()
        button1 = tk.Radiobutton(frame, text="Ok", variable=value, value=1)
        button2 = tk.Radiobutton(frame, text="Terrible", variable=value, value=2)
        button3 = tk.Radiobutton(frame, text="Awful & I want to die", variable=value, value=3)
        button1.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button2.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button3.pack(side=tk.TOP, padx=10, pady=5, anchor="w")

    def create_problems(self, frame):
        """For checkboxes"""
        button1 = tk.Checkbutton(frame, text="ME")
        button2 = tk.Checkbutton(frame, text="I'm ugly as f*ck")
        button3 = tk.Checkbutton(frame, text="I have no money")
        button4 = tk.Checkbutton(frame, text="I am a lazy bum")
        button5 = tk.Checkbutton(frame, text="I hate humans")
        button6 = tk.Checkbutton(frame, text="Everything is wrong with me")
        button1.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button2.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button3.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button4.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button5.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button6.pack(side=tk.TOP, padx=10, pady=5, anchor="w")

    def create_despair(self, frame):
        """For the level of loser of the user"""
        value = tk.DoubleVar()
        scale_1_to_100 = tk.Scale(frame, variable=value)
        scale_1_to_100.pack()

    def meet_your_end(self, frame):
        """Really just a close button"""
        button_close = tk.Button(frame, text="Close", font=("Helvetica", 11), command=self.root.quit)
        button_close.pack(side=tk.BOTTOM, padx=10, pady=10)

def main():
    root = tk.Tk()
    app = CheckBoxWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()