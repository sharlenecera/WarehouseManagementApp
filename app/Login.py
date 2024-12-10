import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import bcrypt

class LoginWindow(tk.Frame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.__users = {
            "test": self.hash_password("test")
        }
        self.on_login_success = on_login_success
        self.create_widgets()
    
    def create_widgets(self):
        # UI for Username Field
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # UI for Password Field
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # UI for Login Button
        self.login_button = tk.Button(self, text="Login", command=self.process_login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        # UI for Sign Up Button        
        self.sign_up_button = tk.Button(self, text="Sign Up", command=self.open_sign_up_window)
        self.sign_up_button.grid(row=4, columnspan=2, pady=10)

    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
    
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
        if username in self.__users:
            return self.check_hashed_password(password, self.__users[username])
        return False
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
    
    def check_hashed_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    def process_login(self):
        is_validated = self.validate_login_details(self.get_login())
        if is_validated:
            self.on_login_success()
        else:
            messagebox.showerror("Login Failed", "Invalid details.")
            self.clear_fields()

    def sign_up(self, username, password, confirm_password, window):
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
        
        if username in self.__users:
            messagebox.showerror("Error", "Username already exists.")
            self.clear_fields()
        else:
            self.__users[username] = self.hash_password(password)
            messagebox.showinfo("Success", f"Successfully created an account for user {username}.")
            window.destroy()

    
    def open_sign_up_window(self):
        sign_up_window = tk.Toplevel(self)
        sign_up_window.title("Register")
        sign_up_window.geometry("400x200")
        
        tk.Label(sign_up_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
        username_entry = tk.Entry(sign_up_window)
        username_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(sign_up_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
        password_entry = tk.Entry(sign_up_window, show="*")
        password_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(sign_up_window, text="Confirm Password:").grid(row=2, column=0, padx=10, pady=5)
        confirm_password_entry = tk.Entry(sign_up_window, show="*")
        confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        sign_up_button = tk.Button(sign_up_window, text="Sign Up", command=lambda: self.sign_up(username_entry.get(), password_entry.get(), confirm_password_entry.get(), sign_up_window))
        sign_up_button.grid(row=3, columnspan=2, pady=10)