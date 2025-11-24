import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.students = []

        # Background Image
        try:
            bg_img = Image.open("lexus.jpg").resize((900, 600))
            self.bg = ImageTk.PhotoImage(bg_img)
            bg_label = tk.Label(root, image=self.bg)
            bg_label.place(relwidth=1, relheight=1)
        except:
            root.configure(bg="#d9e6f2")

        # Menus
        menubar = tk.Menu(root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Load Student File", command=self.load_file)
        file_menu.add_command(label="Load Sample Records", command=self.load_default_students)
        menubar.add_cascade(label="File", menu=file_menu)

        actions_menu = tk.Menu(menubar, tearoff=0)
        actions_menu.add_command(label="View All Records", command=self.view_all)
        actions_menu.add_command(label="View Individual Record", command=self.view_individual)
        actions_menu.add_command(label="Highest Score", command=self.show_highest)
        actions_menu.add_command(label="Lowest Score", command=self.show_lowest)
        menubar.add_cascade(label="Actions", menu=actions_menu)
        root.config(menu=menubar)

        # Table for data
        self.table = ttk.Treeview(root, columns=("id","name","cw","exam","percent","grade"), show="headings", height=15)
        for col in ("id","name","cw","exam","percent","grade"):
            self.table.heading(col, text=col.title())
            self.table.column(col, width=120)
        self.table.pack(pady=20)

        # Auto-load sample students
        self.load_default_students()

    # Load file
    def load_file(self):
        filepath = filedialog.askopenfilename(title="Select studentMarks.txt")
        if not filepath: return
        try:
            with open(filepath, "r") as file:
                lines = file.readlines()

            self.parse_students(lines[1:])
            messagebox.showinfo("Loaded", "Student data loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Parse students
    def parse_students(self, lines):
        self.students.clear()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) != 6: continue
            stu_id, name, m1, m2, m3, exam = parts
            coursework = int(m1)+int(m2)+int(m3)
            total = coursework + int(exam)
            percent = (total/160)*100
            grade = self.get_grade(percent)
            self.students.append({"id":stu_id, "name":name, "coursework":coursework, "exam":int(exam), "percent":percent, "grade":grade})
        self.update_table()

    # Sample students
    def load_default_students(self):
        sample = [
            "1345,John Curry,8,15,7,45",
            "2345,Sam Sturtivant,14,15,14,77",
            "9876,Lee Scott,17,11,16,99",
            "3724,Matt Thompson,19,11,15,81",
            "1212,Ron Herrema,14,17,18,66",
            "8439,Jake Hobbs,10,11,10,43",
            "2344,Jo Hyde,6,15,10,55",
            "9384,Gareth Southgate,5,6,8,33",
            "8327,Alan Shearer,20,20,20,100",
            "2983,Les Ferdinand,15,17,18,92"
        ]  # Updated student list
        self.parse_students(sample)
        messagebox.showinfo("Loaded", "Sample students loaded!")

    # Update table
    def update_table(self):
        for row in self.table.get_children(): self.table.delete(row)
        for s in self.students:
            self.table.insert("", "end", values=(s["id"], s["name"], s["coursework"], s["exam"], f"{s['percent']:.2f}%", s["grade"]))

    # Grade
    def get_grade(self, percent):
        if percent>=70:return "A"
        if percent>=60:return "B"
        if percent>=50:return "C"
        if percent>=40:return "D"
        return "F"

    # Actions
    def view_all(self):
        self.update_table()

    def view_individual(self):
        top=tk.Toplevel(self.root)
        top.title("Find Student")
        tk.Label(top, text="Enter Student ID or Name:").pack(pady=5)
        entry=tk.Entry(top); entry.pack(pady=5)
        def search():
            q=entry.get().lower()
            result=[s for s in self.students if q in s['id'].lower() or q in s['name'].lower()]
            if result:
                self.students=result
                self.update_table()
                top.destroy()
            else:
                messagebox.showinfo("Not Found","Student not found")
        tk.Button(top,text="Search",command=search).pack(pady=10)

    def show_highest(self):
        stu=max(self.students,key=lambda s:s['percent'])
        self.students=[stu]
        self.update_table()

    def show_lowest(self):
        stu=min(self.students,key=lambda s:s['percent'])
        self.students=[stu]
        self.update_table()

# Run the app
if __name__ == "__main__":
    root=tk.Tk()
    root.geometry("900x600")
    app=StudentManager(root)
    root.mainloop()
