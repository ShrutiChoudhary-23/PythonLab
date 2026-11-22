import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pickle


class StudentRecordManager:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Manager")
        self.root.geometry("750x650")

        self.students = {}

        tk.Label(root, text="Student Record Manager",
                font=("Arial", 18, "bold")).pack(pady=10)

        form = tk.Frame(root)
        form.pack(pady=10)

        tk.Label(form, text="Student ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(form)
        self.id_entry.grid(row=0, column=1)

        tk.Label(form, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form)
        self.name_entry.grid(row=1, column=1)

        tk.Label(form, text="Course:").grid(row=2, column=0, padx=5, pady=5)
        self.course_entry = tk.Entry(form)
        self.course_entry.grid(row=2, column=1)

        tk.Label(form, text="Gender:").grid(row=3, column=0, padx=5, pady=5)
        self.gender = tk.StringVar(value="Not Selected")

        tk.Radiobutton(form, text="Male", variable=self.gender,
                      value="Male").grid(row=3, column=1, sticky="w")

        tk.Radiobutton(form, text="Female", variable=self.gender,
                      value="Female").grid(row=4, column=1, sticky="w")

        tk.Label(form, text="Hobbies:").grid(row=5, column=0, padx=5, pady=5)

        self.reading = tk.BooleanVar()
        self.sports = tk.BooleanVar()
        self.music = tk.BooleanVar()

        tk.Checkbutton(form, text="Reading", variable=self.reading).grid(
            row=5, column=1, sticky="w")

        tk.Checkbutton(form, text="Sports", variable=self.sports).grid(
            row=6, column=1, sticky="w")

        tk.Checkbutton(form, text="Music", variable=self.music).grid(
            row=7, column=1, sticky="w")

        tk.Label(form, text="Address:").grid(row=8, column=0, padx=5, pady=5)
        self.address_text = tk.Text(form, width=30, height=4)
        self.address_text.grid(row=8, column=1, pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Record",
                 command=self.add_record).grid(row=0, column=0, padx=5)

        tk.Button(button_frame, text="Delete Record",
                 command=self.delete_record).grid(row=0, column=1, padx=5)

        tk.Button(button_frame, text="Save to File",
                 command=self.save_file).grid(row=0, column=2, padx=5)

        tk.Button(button_frame, text="Load from File",
                 command=self.load_file).grid(row=0, column=3, padx=5)

        tk.Button(button_frame, text="Clear Fields",
                 command=self.clear_fields).grid(row=0, column=4, padx=5)

        tk.Label(root, text="Student Records",
                font=("Arial", 12, "bold")).pack(pady=5)

        self.tree = ttk.Treeview(
            root,
            columns=("ID", "Name", "Course", "Gender", "Hobbies"),
            show="headings"
        )

        for col in ("ID", "Name", "Course", "Gender", "Hobbies"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def add_record(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        course = self.course_entry.get().strip()
        gender = self.gender.get()

        hobbies = []

        if self.reading.get():
            hobbies.append("Reading")
        if self.sports.get():
            hobbies.append("Sports")
        if self.music.get():
            hobbies.append("Music")

        address = self.address_text.get("1.0", tk.END).strip()

        if not student_id or not name or not course:
            messagebox.showwarning(
                "Input Error", "Please enter ID, Name and Course."
            )
            return

        if student_id in self.students:
            messagebox.showwarning(
                "Duplicate ID", "Student ID already exists."
            )
            return

        record = {
            "ID": student_id,
            "Name": name,
            "Course": course,
            "Gender": gender,
            "Hobbies": hobbies,
            "Address": address
        }

        self.students[student_id] = record
        self.display_records()
        self.clear_fields()

        messagebox.showinfo("Success", "Student record added successfully!")

    def display_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for student in self.students.values():
            self.tree.insert(
                "",
                tk.END,
                values=(
                    student["ID"],
                    student["Name"],
                    student["Course"],
                    student["Gender"],
                    ", ".join(student["Hobbies"])
                )
            )

    def delete_record(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Selection Error", "Please select a record to delete."
            )
            return

        item = self.tree.item(selected[0])
        student_id = item["values"][0]

        if student_id in self.students:
            del self.students[student_id]

        self.display_records()
        messagebox.showinfo("Success", "Student record deleted.")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".dat",
            filetypes=[("Data Files", "*.dat"), ("All Files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, "wb") as file:
                    pickle.dump(self.students, file)

                messagebox.showinfo(
                    "Success", "Student records saved successfully!"
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Data Files", "*.dat"), ("All Files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, "rb") as file:
                    self.students = pickle.load(file)

                self.display_records()

                messagebox.showinfo(
                    "Success", "Student records loaded successfully!"
                )

            except Exception as e:
                messagebox.showerror("Error", str(e))

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)

        self.gender.set("Not Selected")
        self.reading.set(False)
        self.sports.set(False)
        self.music.set(False)

        self.address_text.delete("1.0", tk.END)


root = tk.Tk()
app = StudentRecordManager(root)
root.mainloop()