# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import ttk, messagebox

from models.lease import Lease


class LeaseGUI:

    def __init__(self):

        self.lease_model = Lease()
        self.selected_id = None

        self.root = tk.Tk()
        self.root.title("Paragon Apartment Management System")
        self.root.geometry("1150x720")
        self.root.configure(bg="#F4F6F9")
        self.root.resizable(False, False)

        

        header = tk.Frame(
            self.root,
            bg="#1F4E79",
            height=70
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Paragon Apartment Management System",
            font=("Segoe UI",18,"bold"),
            bg="#1F4E79",
            fg="white"
        )

        title.pack(pady=15)

  

        tk.Label(
            self.root,
            text="Lease Agreement Management",
            font=("Segoe UI",15,"bold"),
            bg="#F4F6F9"
        ).pack(pady=10)

       

        form = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="groove"
        )

        form.pack(
            fill="x",
            padx=20,
            pady=10
        )

        labels=[

            ("Tenant ID",0,0),
            ("Apartment ID",1,0),
            ("Start Date",2,0),

            ("End Date",0,2),
            ("Deposit",1,2),
            ("Monthly Rent",2,2)

        ]

        for text,row,col in labels:

            tk.Label(
                form,
                text=text,
                bg="white",
                font=("Segoe UI",10)
            ).grid(
                row=row,
                column=col,
                padx=10,
                pady=10,
                sticky="w"
            )

        self.tenant_entry = tk.Entry(form,width=30)
        self.tenant_entry.grid(row=0,column=1,padx=5)

        self.apartment_entry = tk.Entry(form,width=30)
        self.apartment_entry.grid(row=1,column=1,padx=5)

        self.start_entry = tk.Entry(form,width=30)
        self.start_entry.grid(row=2,column=1,padx=5)

        self.end_entry = tk.Entry(form,width=30)
        self.end_entry.grid(row=0,column=3,padx=5)

        self.deposit_entry = tk.Entry(form,width=30)
        self.deposit_entry.grid(row=1,column=3,padx=5)

        self.rent_entry = tk.Entry(form,width=30)
        self.rent_entry.grid(row=2,column=3,padx=5)


        button_frame = tk.Frame(
            self.root,
            bg="#F4F6F9"
        )

        button_frame.pack(pady=15)

        tk.Button(
            button_frame,
            text="Add",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.add_lease
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.update_lease
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.delete_lease
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.search_lease
        ).grid(row=0,column=3,padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.clear_fields
        ).grid(row=0,column=4,padx=5)

        tk.Button(
            button_frame,
            text="Back",
            width=12,
            bg="#C00000",
            fg="white",
            command=self.go_back
        ).grid(row=0,column=5,padx=5)

    

        tk.Label(
            self.root,
            text="Lease Records",
            font=("Segoe UI",13,"bold"),
            bg="#F4F6F9"
        ).pack()

        table_frame = tk.Frame(self.root)

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        scrollbar = tk.Scrollbar(table_frame)

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree = ttk.Treeview(

            table_frame,

            columns=(

                "Lease ID",
                "Tenant ID",
                "Apartment ID",
                "Start Date",
                "End Date",
                "Deposit",
                "Monthly Rent"

            ),

            show="headings",

            yscrollcommand=scrollbar.set

        )

        scrollbar.config(command=self.tree.yview)

        headings=[

            ("Lease ID",80),
            ("Tenant ID",100),
            ("Apartment ID",120),
            ("Start Date",120),
            ("End Date",120),
            ("Deposit",120),
            ("Monthly Rent",130)

        ]

        for heading,width in headings:

            self.tree.heading(
                heading,
                text=heading
            )

            self.tree.column(
                heading,
                width=width
            )

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

        self.load_leases()

        self.root.mainloop()

   

    def load_leases(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        leases = self.lease_model.get_all_leases()

        for lease in leases:

            self.tree.insert(
                "",
                tk.END,
                values=lease
            )




    def clear_fields(self):

        self.tenant_entry.delete(0, tk.END)
        self.apartment_entry.delete(0, tk.END)
        self.start_entry.delete(0, tk.END)
        self.end_entry.delete(0, tk.END)
        self.deposit_entry.delete(0, tk.END)
        self.rent_entry.delete(0, tk.END)


  

    def add_lease(self):

        tenant_id = self.tenant_entry.get().strip()
        apartment_id = self.apartment_entry.get().strip()

        if tenant_id == "" or apartment_id == "":

            messagebox.showwarning(
                "Missing Information",
                "Tenant ID and Apartment ID are required."
            )

            return

        self.lease_model.tenant_id = tenant_id
        self.lease_model.apartment_id = apartment_id
        self.lease_model.start_date = self.start_entry.get().strip()
        self.lease_model.end_date = self.end_entry.get().strip()
        self.lease_model.deposit = self.deposit_entry.get().strip()
        self.lease_model.monthly_rent = self.rent_entry.get().strip()

        if self.lease_model.add_lease():

            messagebox.showinfo(
                "Success",
                "Lease agreement added successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_leases()

        else:

            messagebox.showerror(
                "Error",
                "Unable to add lease agreement."
            )
 

    def update_lease(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a lease agreement to update."
            )

            return

        tenant_id = self.tenant_entry.get().strip()
        apartment_id = self.apartment_entry.get().strip()

        if tenant_id == "" or apartment_id == "":

            messagebox.showwarning(
                "Missing Information",
                "Tenant ID and Apartment ID are required."
            )

            return

        self.lease_model.lease_id = self.selected_id
        self.lease_model.tenant_id = tenant_id
        self.lease_model.apartment_id = apartment_id
        self.lease_model.start_date = self.start_entry.get().strip()
        self.lease_model.end_date = self.end_entry.get().strip()
        self.lease_model.deposit = self.deposit_entry.get().strip()
        self.lease_model.monthly_rent = self.rent_entry.get().strip()

        if self.lease_model.update_lease():

            messagebox.showinfo(
                "Success",
                "Lease agreement updated successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_leases()

        else:

            messagebox.showerror(
                "Error",
                "Unable to update lease agreement.")




    def delete_lease(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a lease agreement."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this lease agreement?"
        )

        if not answer:
            return

        if self.lease_model.delete_lease(self.selected_id):

            messagebox.showinfo(
                "Deleted",
                "Lease agreement deleted successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_leases()

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete lease agreement.")


 

    def search_lease(self):

        keyword = self.tenant_entry.get().strip()

        if keyword == "":

            self.load_leases()
            return

        leases = self.lease_model.search_lease(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for lease in leases:

            self.tree.insert(
                "",
                tk.END,
                values=lease
            )


    def select_record(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected)["values"]

        self.clear_fields()

        self.selected_id = values[0]

        self.tenant_entry.insert(0, values[1])
        self.apartment_entry.insert(0, values[2])
        self.start_entry.insert(0, values[3])
        self.end_entry.insert(0, values[4])
        self.deposit_entry.insert(0, values[5])
        self.rent_entry.insert(0, values[6])


 

    def go_back(self):

        answer = messagebox.askyesno(
            "Back",
            "Return to Dashboard?"
        )

        if answer:

            self.root.destroy()



if __name__ == "__main__":

    LeaseGUI()