import tkinter as tk
import random

class JokeApp:
    def __init__(self, master):
        self.master = master
        master.title("Alexa Joke Assistant")
        master.geometry("500x450")
        master.configure(bg="#c9e8ff")  # soft blue background

        # -------------------------------
        # JOKES BUILT INTO THE CODE
        # -------------------------------
        self.jokes = [
            ("Why did the chicken cross the road?", "To get to the other side."),
            ("What happens if you boil a clown?", "You get a laughing stock."),
            ("Why don’t scientists trust atoms?", "Because they make up everything!"),
            ("Why did the scarecrow win an award?", "Because he was outstanding in his field."),
            ("Why don’t skeletons fight each other?", "Because they don’t have the guts."),
            ("What do you call fake spaghetti?", "An impasta."),
            ("Why was the math book sad?", "Because it had too many problems."),
            ("Why did the bicycle fall over?", "Because it was two-tired."),
            ("What do you call cheese that isn’t yours?", "Nacho cheese."),
            ("Why can’t you give Elsa a balloon?", "Because she will let it go.")
        ]

        self.current_setup = ""
        self.current_punchline = ""

        # Title Label
        tk.Label(
            master,
            text="🤖 Alexa Joke Assistant",
            font=("Comic Sans MS", 20, "bold"),
            bg="#c9e8ff",
            fg="#003d66"
        ).pack(pady=10)

        # Frame for the joke display
        self.joke_frame = tk.Frame(master, bg="#ffffff", bd=3, relief="ridge")
        self.joke_frame.pack(pady=15, padx=20, fill="both", expand=True)

        # Setup text
        self.setup_label = tk.Label(
            self.joke_frame,
            text="Click a button to hear a joke!",
            font=("Arial", 14),
            bg="#ffffff",
            wraplength=400,
            justify="center"
        )
        self.setup_label.pack(pady=15)

        # Punchline text
        self.punchline_label = tk.Label(
            self.joke_frame,
            text="",
            font=("Arial", 12, "italic"),
            bg="#ffffff",
            fg="#444444",
            wraplength=380,
            justify="center"
        )
        self.punchline_label.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(master, bg="#c9e8ff")
        button_frame.pack(pady=10)

        # Create styled buttons
        self.create_button(button_frame, "Alexa tell me a Joke", self.show_joke).pack(pady=5)
        self.create_button(button_frame, "Show Punchline", self.show_punchline).pack(pady=5)
        self.create_button(button_frame, "Next Joke", self.show_joke).pack(pady=5)
        self.create_button(button_frame, "Quit", master.quit, danger=True).pack(pady=8)

    def create_button(self, master, text, command, danger=False):
        """Creates a consistently styled button with hover effects."""
        bg_color = "#ffffff" if not danger else "#ffcccc"
        hover_color = "#e6f7ff" if not danger else "#ffb3b3"

        btn = tk.Button(
            master,
            text=text,
            command=command,
            width=25,
            height=1,
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#003d66",
            activebackground=hover_color,
            relief="raised",
            bd=3,
            cursor="hand2"
        )

        # Hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))

        return btn

    def show_joke(self):
        """Select a random joke and display the setup."""
        self.current_setup, self.current_punchline = random.choice(self.jokes)
        self.setup_label.config(text=self.current_setup)
        self.punchline_label.config(text="")

    def show_punchline(self):
        """Show punchline."""
        self.punchline_label.config(text=self.current_punchline)


root = tk.Tk()
app = JokeApp(root)
root.mainloop()
