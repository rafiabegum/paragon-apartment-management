# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import messagebox

from streamlit import user
from gui.dashboard import Dashboard
from models.user import User


class LoginWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Paragon Apartment Management System")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        

        heading = tk.Label(
            self.root,
            text="Paragon Apartment Management System",
            font=("Arial", 16, "bold")
        )

        heading.pack(pady=20)

       

        tk.Label(
            self.root,
            text="Email",
            font=("Arial", 11)
        ).pack()

        self.email_entry = tk.Entry(
            self.root,
            width=35
        )

        self.email_entry.pack(pady=5)

       

        tk.Label(
            self.root,
            text="Password",
            font=("Arial", 11)
        ).pack()

        self.password_entry = tk.Entry(
            self.root,
            show="*",
            width=35
        )

        self.password_entry.pack(pady=5)

       

        login_button = tk.Button(
            self.root,
            text="Login",
            width=20,
            bg="#1E90FF",
            fg="white",
            command=self.login
        )

        login_button.pack(pady=20)

        self.root.mainloop()

   

    def login(self):

        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if email == "" or password == "":

            messagebox.showerror(
                "Error",
                "Please enter email and password."
            )

            return

        user_model = User()
        user = user_model.login(email, password)

        if user:

            messagebox.showinfo(
                "Success",
                f"Welcome {user[1]}\nRole: {user[4]}"
            )

            self.root.destroy()

           
            Dashboard(user[1], user[4])

            

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid email or password."
            )


if __name__ == "__main__":

    LoginWindow()