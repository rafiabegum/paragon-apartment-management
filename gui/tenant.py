# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import ttk, messagebox

from models.tenant import Tenant


class TenantGUI:

    def __init__(self):

        self.tenant_model = Tenant()
        self.selected_id = None

        self.root = tk.Tk()
        self.root.title("Paragon Apartment Management System")
        self.root.geometry("1100x700")
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
            font=("Segoe UI", 18, "bold"),
            bg="#1F4E79",
            fg="white"
        )

        title.pack(pady=15)



        tk.Label(
            self.root,
            text="Tenant Management",
            font=("Segoe UI", 15, "bold"),
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

        labels = [

            ("NI Number",0,0),
            ("Name",1,0),
            ("Phone",2,0),

            ("Email",0,2),
            ("Occupation",1,2),
            ("Reference",2,2)

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

        self.ni_entry = tk.Entry(form,width=30)
        self.ni_entry.grid(row=0,column=1,padx=5)

        self.name_entry = tk.Entry(form,width=30)
        self.name_entry.grid(row=1,column=1,padx=5)

        self.phone_entry = tk.Entry(form,width=30)
        self.phone_entry.grid(row=2,column=1,padx=5)

        self.email_entry = tk.Entry(form,width=30)
        self.email_entry.grid(row=0,column=3,padx=5)

        self.occupation_entry = tk.Entry(form,width=30)
        self.occupation_entry.grid(row=1,column=3,padx=5)

        self.reference_entry = tk.Entry(form,width=30)
        self.reference_entry.grid(row=2,column=3,padx=5)



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
            command=self.add_tenant
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.update_tenant
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.delete_tenant
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.search_tenant
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

            text="Tenant Records",

            bg="#F4F6F9",

            font=("Segoe UI",13,"bold")

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

                "ID",

                "NI",

                "Name",

                "Phone",

                "Email",

                "Occupation",

                "Reference"

            ),

            show="headings",

            yscrollcommand=scrollbar.set

        )

        scrollbar.config(command=self.tree.yview)

        headings=[

            ("ID",50),

            ("NI",120),

            ("Name",150),

            ("Phone",120),

            ("Email",180),

            ("Occupation",140),

            ("Reference",150)

        ]

        for heading,width in headings:

            if heading == "ID":
                text = "Tenant ID"

            elif heading == "NI":
                text = "NI Number"

            else:
                text = heading

            self.tree.heading(
                heading,
                text=text
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

        self.load_tenants()

        self.root.mainloop()


    def load_tenants(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        tenants = self.tenant_model.get_all_tenants()

        for tenant in tenants:
            self.tree.insert("", tk.END, values=tenant)




    def clear_fields(self):

        self.ni_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.occupation_entry.delete(0, tk.END)
        self.reference_entry.delete(0, tk.END)



    def add_tenant(self):

        ni_number = self.ni_entry.get().strip()
        name = self.name_entry.get().strip()

        if ni_number == "" or name == "":

            messagebox.showwarning(
                "Missing Information",
                "NI Number and Name are required."
            )

            return

        self.tenant_model.ni_number = ni_number
        self.tenant_model.name = name
        self.tenant_model.phone = self.phone_entry.get().strip()
        self.tenant_model.email = self.email_entry.get().strip()
        self.tenant_model.occupation = self.occupation_entry.get().strip()
        self.tenant_model.reference = self.reference_entry.get().strip()

        if self.tenant_model.add_tenant():

            messagebox.showinfo(
                "Success",
                "Tenant added successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_tenants()

        else:

            messagebox.showerror(
                "Error",
                "Unable to add tenant."
            )
    

    def update_tenant(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a tenant to update."
            )

            return

        ni_number = self.ni_entry.get().strip()
        name = self.name_entry.get().strip()

        if ni_number == "" or name == "":

            messagebox.showwarning(
                "Missing Information",
                "NI Number and Name are required."
            )

            return

        self.tenant_model.tenant_id = self.selected_id
        self.tenant_model.ni_number = ni_number
        self.tenant_model.name = name
        self.tenant_model.phone = self.phone_entry.get().strip()
        self.tenant_model.email = self.email_entry.get().strip()
        self.tenant_model.occupation = self.occupation_entry.get().strip()
        self.tenant_model.reference = self.reference_entry.get().strip()

        if self.tenant_model.update_tenant():

            messagebox.showinfo(
                "Success",
                "Tenant updated successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_tenants()

        else:

            messagebox.showerror(
                "Error",
                "Unable to update tenant.")



    def delete_tenant(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a tenant."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this tenant?"
        )

        if not answer:
            return

        if self.tenant_model.delete_tenant(self.selected_id):

            messagebox.showinfo(
                "Deleted",
                "Tenant deleted successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_tenants()

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete tenant.")



    def search_tenant(self):

        keyword = self.name_entry.get().strip()

        if keyword == "":

            self.load_tenants()
            return

        tenants = self.tenant_model.search_tenant(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for tenant in tenants:

            self.tree.insert(
                "",
                tk.END,
                values=tenant
            )
    
        

    def select_record(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected)["values"]


        self.clear_fields()

        self.selected_id = values[0]

        self.ni_entry.insert(0, values[1])
        self.name_entry.insert(0, values[2])
        self.phone_entry.insert(0, values[3])
        self.email_entry.insert(0, values[4])
        self.occupation_entry.insert(0, values[5])
        self.reference_entry.insert(0, values[6])


    

    def go_back(self):

        answer = messagebox.askyesno(
            "Back",
            "Return to Dashboard?"
        )

        if answer:

            self.root.destroy()



if __name__ == "__main__":

    TenantGUI()