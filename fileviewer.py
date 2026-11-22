import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from PIL import Image, ImageTk

def open_file():
    global photo

    file = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if file:
        try:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                img = Image.open(file)
                img.thumbnail((400, 300))

                photo = ImageTk.PhotoImage(img)
                canvas.delete("all")
                canvas.create_image(200, 150, image=photo)

                label.config(text="Image Opened Successfully")

            elif file.lower().endswith(".txt"):
                with open(file, "r") as f:
                    content = f.read()

                canvas.delete("all")
                text_area.delete("1.0", tk.END)
                text_area.insert(tk.END, content)

                label.config(text="Text File Opened Successfully")

            else:
                messagebox.showerror("Error", "Unsupported File Type")

        except Exception as e:
            messagebox.showerror("Error", str(e))


def change_color():
    color = colorchooser.askcolor(title="Choose Background Color")

    if color[1]:
        root.config(bg=color[1])
        label.config(bg=color[1])


def clear_screen():
    canvas.delete("all")
    text_area.delete("1.0", tk.END)
    label.config(text="No File Selected")


def on_enter(event):
    open_file()


# Main window
root = tk.Tk()
root.title("Image and File Viewer")
root.geometry("550x550")

photo = None

# Heading
label = tk.Label(
    root,
    text="Dynamic Image/File Viewer",
    font=("Arial", 16, "bold")
)
label.pack(pady=10)

# Buttons
tk.Button(root, text="Open File",
          command=open_file).pack(pady=5)

tk.Button(root, text="Choose Color",
          command=change_color).pack(pady=5)

tk.Button(root, text="Clear Screen",
          command=clear_screen).pack(pady=5)

# Canvas for displaying images
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=10)

# Text area for displaying text files
text_area = tk.Text(root, height=8, width=55)
text_area.pack(pady=5)

# Keyboard event binding
root.bind("<Return>", on_enter)

# Mouse click binding
canvas.bind("<Button-1>", lambda event: label.config(
    text="Canvas Clicked at: " + str(event.x) + ", " + str(event.y)
))

root.mainloop()