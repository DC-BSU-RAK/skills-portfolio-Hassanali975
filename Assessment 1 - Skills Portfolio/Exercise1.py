import tkinter as tk
from tkinter import messagebox
import random

# ---------------------- FUNCTIONS ----------------------

def displayMenu():
    menu_frame.pack(fill="both", expand=True)
    quiz_frame.pack_forget()
    result_frame.pack_forget()

def start_quiz(level):
    global difficulty, score, question_count, attempt
    difficulty = level
    score = 0
    question_count = 0
    attempt = 1
    menu_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)
    next_question()

def randomInt(level):
    if level == "Easy":
        return random.randint(1, 9)
    elif level == "Moderate":
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(["+", "-"])

def next_question():
    global num1, num2, op, question_count, attempt
    if question_count >= 10:
        displayResults()
        return

    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    op = decideOperation()

    question_count += 1
    attempt = 1

    problem_label.config(text=f"Question {question_count}:  {num1} {op} {num2} = ?")
    answer_entry.delete(0, tk.END)
    feedback_label.config(text="")

def isCorrect():
    global score, attempt
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    correct_answer = num1 + num2 if op == "+" else num1 - num2

    if user_answer == correct_answer:
        if attempt == 1:
            score += 10
            feedback_label.config(text="Correct! +10 points", fg="green")
        else:
            score += 5
            feedback_label.config(text="Correct! +5 points", fg="blue")

        root.after(700, next_question)

    else:
        if attempt == 1:
            attempt = 2
            feedback_label.config(text="Incorrect! Try again.", fg="red")
            answer_entry.delete(0, tk.END)
        else:
            feedback_label.config(text=f"Wrong! Correct answer: {correct_answer}", fg="red")
            root.after(700, next_question)

def displayResults():
    quiz_frame.pack_forget()
    result_frame.pack(fill="both", expand=True)

    if score >= 90: grade = "A+"
    elif score >= 80: grade = "A"
    elif score >= 70: grade = "B"
    elif score >= 60: grade = "C"
    else: grade = "D"

    result_label.config(text=f"Your Score: {score}/100\nGrade: {grade}")

# ---------------------- GUI SETUP ----------------------

root = tk.Tk()
root.title("Maths Quiz")
root.geometry("450x400")

menu_frame = tk.Frame(root)
quiz_frame = tk.Frame(root)
result_frame = tk.Frame(root)

# ---------------------- MENU ----------------------

tk.Label(menu_frame, text="Select Difficulty Level", font=("Arial", 18)).pack(pady=20)

tk.Button(menu_frame, text="Easy", width=20, command=lambda: start_quiz("Easy")).pack(pady=8)
tk.Button(menu_frame, text="Moderate", width=20, command=lambda: start_quiz("Moderate")).pack(pady=8)
tk.Button(menu_frame, text="Advanced", width=20, command=lambda: start_quiz("Advanced")).pack(pady=8)

# ---------------------- QUIZ ----------------------

problem_label = tk.Label(quiz_frame, text="", font=("Arial", 16))
problem_label.pack(pady=20)

answer_entry = tk.Entry(quiz_frame, font=("Arial", 14))
answer_entry.pack()

tk.Button(quiz_frame, text="Submit", command=isCorrect).pack(pady=10)

feedback_label = tk.Label(quiz_frame, text="", font=("Arial", 12))
feedback_label.pack(pady=5)

# ---------------------- RESULTS ----------------------

result_label = tk.Label(result_frame, text="", font=("Arial", 18))
result_label.pack(pady=25)

tk.Button(result_frame, text="Play Again", command=displayMenu).pack(pady=10)
tk.Button(result_frame, text="Exit", command=root.quit).pack()

# Start on menu
displayMenu()

root.mainloop()
