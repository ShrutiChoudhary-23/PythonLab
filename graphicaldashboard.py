import tkinter as tk
from tkinter import messagebox
import json


class DashboardApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Frame Dashboard")
        self.root.geometry("700x500")

        self.config_data = {"username": "", "theme": "Light"}

        self.create_menu()
        self.create_frames()
        self.show_frame("home")

    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save Configuration",
                             command=self.save_config)
        file_menu.add_command(label="Exit", command=self.root.quit)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Home",
                             command=lambda: self.show_frame("home"))
        view_menu.add_command(label="Settings",
                             command=lambda: self.show_frame("settings"))

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="View", menu=view_menu)

        self.root.config(menu=menubar)

    def create_frames(self):
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.home_frame = tk.Frame(self.container)
        self.settings_frame = tk.Frame(self.container)

        self.create_home()
        self.create_settings()

    def create_home(self):
        tk.Label(self.home_frame, text="Dashboard",
                 font=("Arial", 20, "bold")).pack(pady=20)

        self.welcome_label = tk.Label(
            self.home_frame, text="Welcome to the Dashboard!"
        )
        self.welcome_label.pack(pady=10)

        tk.Button(self.home_frame, text="Go to Settings",
                  command=lambda: self.show_frame("settings")).pack(pady=10)

        tk.Button(self.home_frame, text="Exit",
                 command=self.root.quit).pack(pady=10)

    def create_settings(self):
        tk.Label(self.settings_frame, text="Settings",
                 font=("Arial", 20, "bold")).grid(
                     row=0, column=0, columnspan=2, pady=20
                 )

        tk.Label(self.settings_frame, text="Username:").grid(
            row=1, column=0, padx=10, pady=10
        )

        self.username_entry = tk.Entry(self.settings_frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.settings_frame, text="Theme:").grid(
            row=2, column=0, padx=10, pady=10
        )

        self.theme_var = tk.StringVar(value="Light")

        tk.Radiobutton(self.settings_frame, text="Light",
                      variable=self.theme_var, value="Light").grid(
                          row=2, column=1, sticky="w"
                      )

        tk.Radiobutton(self.settings_frame, text="Dark",
                      variable=self.theme_var, value="Dark").grid(
                          row=3, column=1, sticky="w"
                      )

        tk.Button(self.settings_frame, text="Save Settings",
                 command=self.update_settings).grid(
                     row=4, column=0, columnspan=2, pady=10
                 )

        tk.Button(self.settings_frame, text="Back to Home",
                 command=lambda: self.show_frame("home")).grid(
                     row=5, column=0, columnspan=2, pady=10
                 )

    def show_frame(self, frame_name):
        self.home_frame.pack_forget()
        self.settings_frame.pack_forget()

        if frame_name == "home":
            self.home_frame.pack(fill="both", expand=True)
        elif frame_name == "settings":
            self.settings_frame.pack(fill="both", expand=True)

    def update_settings(self):
        username = self.username_entry.get().strip()
        theme = self.theme_var.get()

        if not username:
            messagebox.showwarning("Warning", "Please enter a username.")
            return

        self.config_data["username"] = username
        self.config_data["theme"] = theme

        self.welcome_label.config(text=f"Welcome, {username}!")

        messagebox.showinfo("Success", "Settings updated successfully!")
        self.show_frame("home")

    def save_config(self):
        try:
            with open("dashboard_config.json", "w") as file:
                json.dump(self.config_data, file, indent=4)

            messagebox.showinfo("Success", "Configuration saved to file.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


root = tk.Tk()
app = DashboardApp(root)
root.mainloop()