import tkinter as tk


class FailureManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Life Evaluation: Failure Management")

        # Checkboxes attribute's
        self.Chk_1 = tk.IntVar()
        self.Chk_2 = tk.IntVar()
        self.Chk_3 = tk.IntVar()
        self.Chk_4 = tk.IntVar()
        self.Chk_5 = tk.IntVar()
        # Checkboxes for all
        self.Chk_6 = tk.IntVar()

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
        self.upper_left_frame = self.create_frame(1, 0, "... On a scale of 0 to 100?")
        self.upper_right_frame = self.create_frame(1, 1, "And what's wrong exactly?")
        self.lower_left_frame = self.create_frame(2, 0, "How would you describe your life?")
        self.lower_right_frame = self.create_frame(2, 1, "Options")

        # Create checkboxes for each frame
        self.create_despair(self.upper_left_frame)
        self.create_problems(self.upper_right_frame)
        self.create_low_self_esteem(self.lower_left_frame)
        self.more_buttons(self.lower_right_frame)
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
        """For low choice radiobutton"""
        value = tk.IntVar()
        button1 = tk.Radiobutton(frame, text="Ok", variable=value, value=1)
        button2 = tk.Radiobutton(frame, text="Terrible", variable=value, value=2)
        button3 = tk.Radiobutton(frame, text="Awful & I want to die", variable=value, value=3)
        button1.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button2.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button3.pack(side=tk.TOP, padx=10, pady=5, anchor="w")

    def toggle_all(self):
        """Toggle all boxes when we toggle 'everything is wrong' """
        # And now I regret not having done a loop from beginning...
        if self.Chk_6.get() == 1:
            self.Chk_1.set(1)
            self.Chk_2.set(1)
            self.Chk_3.set(1)
            self.Chk_4.set(1)
            self.Chk_5.set(1)
        else:
            self.Chk_1.set(0)
            self.Chk_2.set(0)
            self.Chk_3.set(0)
            self.Chk_4.set(0)
            self.Chk_5.set(0)

    def create_problems(self, frame):
        """For checkboxes"""
        # Create Checkboxes
        button1 = tk.Checkbutton(frame, text="ME", variable=self.Chk_1)
        button2 = tk.Checkbutton(frame, text="I'm ugly as f*ck", variable=self.Chk_2)
        button3 = tk.Checkbutton(frame, text="I have no money", variable=self.Chk_3)
        button4 = tk.Checkbutton(frame, text="I am a lazy bum", variable=self.Chk_4)
        button5 = tk.Checkbutton(frame, text="I hate humans", variable=self.Chk_5)
        button6 = tk.Checkbutton(frame, text="Everything is wrong with me", variable=self.Chk_6,
                                 command=lambda: self.toggle_all())

        # Design
        button1.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button2.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button3.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button4.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button5.pack(side=tk.TOP, padx=10, pady=5, anchor="w")
        button6.pack(side=tk.TOP, padx=10, pady=5, anchor="w")

    def create_despair(self, frame):
        """Scale of the Loserness"""
        # Create a scale from 0 to 100
        value = tk.DoubleVar()
        scale_0_to_100 = tk.Scale(frame, variable=value, from_=100, to=0)
        scale_0_to_100.pack()

    def screwing(self):
        """Score the Luser"""
        loserness = 0


    def more_buttons(self, frame):
        """Button of screwing and options to escape"""
        # To screw the user
        button_score = tk.Button(frame, text="Score", font=("Helvetica", 11), command=lambda: self.screwing())
        button_score.pack(side=tk.TOP, padx=10, pady=5)

        # Button More Options (MOVE IT)
        button_options = tk.Button(frame, text="Options", font=("Helvetica", 11))
        button_options.pack(side=tk.TOP, padx=10, pady=5)

    def meet_your_end(self, frame):
        """Really just a close button"""
        # I confirm, it's a close button
        button_close = tk.Button(frame, text="Close", font=("Helvetica", 11), command=self.root.quit)
        button_close.pack(side=tk.TOP, padx=10, pady=10)


def main():
    root = tk.Tk()
    FailureManagement(root)
    root.mainloop()


if __name__ == "__main__":
    main()
