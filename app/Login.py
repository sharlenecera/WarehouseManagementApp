import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class LoginWindow(tk.Frame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.on_login_success = on_login_success
        self.create_widgets()
    
    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.login_button = tk.Button(self, text="Login", command=self.process_login)
        self.login_button.grid(row=2, columnspan=2, pady=10)
    
    def get_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        return {
            "username": username,
            "password": password
        }
        
    def validate_login_details(self, login_details_dict):
        username = login_details_dict["username"]
        password = login_details_dict["password"]
        if username == "test" and password == "test":
            return True
        return False
    
    def process_login(self):
        is_validated = self.validate_login_details(self.get_login())
        if is_validated:
            self.on_login_success()
        else:
            messagebox.showerror("Login Failed", "Invalid details.")