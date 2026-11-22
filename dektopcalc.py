import tkinter as tk

def click(value):
    current = entry.get()

    if value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif value == "C":
        entry.delete(0, tk.END)

    elif value == "DEL":
        entry.delete(len(current) - 1, tk.END)

    else:
        entry.insert(tk.END, value)


root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("350x450")
root.resizable(False, False)

# Display field
entry = tk.Entry(root, font=("Arial", 22), justify="right",
                 borderwidth=5)
entry.grid(row=0, column=0, columnspan=4,
           padx=10, pady=20, ipadx=5, ipady=10)

# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["DEL", ".", "(", ")"]
]

# Create buttons using grid geometry manager
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        value = buttons[i][j]

        btn = tk.Button(
            root,
            text=value,
            font=("Arial", 16),
            width=6,
            height=2,
            command=lambda v=value: click(v)
        )

        btn.grid(row=i + 1, column=j,
                 padx=5, pady=5)

root.mainloop()
