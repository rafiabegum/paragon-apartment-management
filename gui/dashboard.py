# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import messagebox

from gui.tenant import TenantGUI
from gui.apartment import ApartmentGUI
from gui.lease import LeaseGUI
from gui.invoice import InvoiceGUI
from gui.payment import PaymentGUI
from gui.complaint import ComplaintGUI
from gui.maintenance import MaintenanceGUI


class Dashboard:

    def __init__(self, user_name, user_role):

        self.root = tk.Tk()

        self.root.title("Paragon Apartment Management System")
        self.root.geometry("1000x650")
        self.root.configure(bg="#F4F6F9")
        self.root.resizable(False, False)

        # ===========================
        # Header
        # ===========================

        header = tk.Frame(
            self.root,
            bg="#1F4E79",
            height=80
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Paragon Apartment Management System",
            font=("Segoe UI", 22, "bold"),
            bg="#1F4E79",
            fg="white"
        )

        title.pack(pady=10)

        subtitle = tk.Label(
            header,
            text=f"Welcome: {user_name}    |    Role: {user_role}",
            font=("Segoe UI", 11),
            bg="#1F4E79",
            fg="white"
        )

        subtitle.pack()

      

        main_frame = tk.Frame(
            self.root,
            bg="#F4F6F9"
        )

        main_frame.pack(fill="both", expand=True, padx=40, pady=30)

      

        buttons = [

            ("Tenant Management", self.open_tenant),

            ("Apartment Management", self.open_apartment),

            ("Lease Management", self.open_lease),

            ("Invoice Management", self.open_invoice),

            ("Payment Management", self.open_payment),

            ("Complaint Management", self.open_complaint),

            ("Maintenance Management", self.open_maintenance),

            ("Logout", self.logout)

        ]
        
        row = 0
        col = 0

        for text, command in buttons:

            button = tk.Button(

                main_frame,

                text=text,

                width=25,

                height=2,

                font=("Segoe UI", 11, "bold"),

                bg="#2E75B6",

                fg="white",

                activebackground="#1F4E79",

                cursor="hand2",

                command=command

            )

            button.grid(
                row=row,
                column=col,
                padx=25,
                pady=20
            )

            col += 1

            if col == 2:
                row += 1
                col = 0

        self.root.mainloop()

    # =======================================

    def tenant(self):
        messagebox.showinfo(
            "Tenant",
            "Tenant Management Module"
        )

    def apartment(self):
        messagebox.showinfo(
            "Apartment",
            "Apartment Management Module"
        )

    def payment(self):
        messagebox.showinfo(
            "Payment",
            "Payment & Billing Module"
        )

    def maintenance(self):
        messagebox.showinfo(
            "Maintenance",
            "Maintenance Module"
        )

    def reports(self):
        messagebox.showinfo(
            "Reports",
            "Reporting Module"
        )

    def users(self):
        messagebox.showinfo(
            "Users",
            "User Management Module"
        )

    def logout(self):

        if messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        ):

            self.root.destroy()
    

    def open_tenant(self):
        TenantGUI()

    def open_apartment(self):
        ApartmentGUI()

    def open_lease(self):
        LeaseGUI()

    def open_invoice(self):
        InvoiceGUI()

    def open_payment(self):
        PaymentGUI()

    def open_complaint(self):
        ComplaintGUI()

    def open_maintenance(self):
        MaintenanceGUI()


if __name__ == "__main__":

    Dashboard(
        "Administrator",
        "Administrator"
    )