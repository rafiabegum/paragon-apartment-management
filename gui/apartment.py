# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import ttk, messagebox

from models.apartment import Apartment


class ApartmentGUI:

    def __init__(self):

        self.apartment_model = Apartment()
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
            font=("Segoe UI",18,"bold"),
            bg="#1F4E79",
            fg="white"
        )

        title.pack(pady=15)


        tk.Label(
            self.root,
            text="Apartment Management",
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

            ("Location",0,0),
            ("Apartment Type",1,0),
            ("Monthly Rent",2,0),

            ("Rooms",0,2),
            ("Status",1,2)

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

        self.location_entry=tk.Entry(form,width=30)
        self.location_entry.grid(row=0,column=1,padx=5)

        self.type_entry=tk.Entry(form,width=30)
        self.type_entry.grid(row=1,column=1,padx=5)

        self.rent_entry=tk.Entry(form,width=30)
        self.rent_entry.grid(row=2,column=1,padx=5)

        self.rooms_entry=tk.Entry(form,width=30)
        self.rooms_entry.grid(row=0,column=3,padx=5)

        self.status_combo=ttk.Combobox(

            form,

            width=27,

            state="readonly",

            values=(

                "Available",
                "Occupied",
                "Under Maintenance"

            )

        )

        self.status_combo.grid(row=1,column=3,padx=5)
        self.status_combo.current(0)

  

        button_frame=tk.Frame(
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
            command=self.add_apartment
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.update_apartment
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.delete_apartment
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.search_apartment
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

            text="Apartment Records",

            font=("Segoe UI",13,"bold"),

            bg="#F4F6F9"

        ).pack()

        table_frame=tk.Frame(self.root)

        table_frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10

        )

        scrollbar=tk.Scrollbar(table_frame)

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree=ttk.Treeview(

            table_frame,

            columns=(

                "ID",
                "Location",
                "Type",
                "Rent",
                "Rooms",
                "Status"

            ),

            show="headings",

            yscrollcommand=scrollbar.set

        )

        scrollbar.config(command=self.tree.yview)

        headings=[

            ("ID",70),
            ("Location",200),
            ("Type",180),
            ("Rent",120),
            ("Rooms",100),
            ("Status",180)

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

        self.load_apartments()

        self.root.mainloop()
   

    def load_apartments(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        apartments = self.apartment_model.get_all_apartments()

        for apartment in apartments:

            self.tree.insert(
                "",
                tk.END,
                values=apartment
            )



    def clear_fields(self):

        self.location_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.rent_entry.delete(0, tk.END)
        self.rooms_entry.delete(0, tk.END)

        self.status_combo.current(0)



    def add_apartment(self):

        location = self.location_entry.get().strip()
        apartment_type = self.type_entry.get().strip()

        if location == "" or apartment_type == "":

            messagebox.showwarning(
                "Missing Information",
                "Location and Apartment Type are required."
            )

            return

        self.apartment_model.location = location
        self.apartment_model.apartment_type = apartment_type
        self.apartment_model.monthly_rent = self.rent_entry.get().strip()
        self.apartment_model.number_of_rooms = self.rooms_entry.get().strip()
        self.apartment_model.status = self.status_combo.get()

        if self.apartment_model.add_apartment():

            messagebox.showinfo(
                "Success",
                "Apartment added successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_apartments()

        else:

            messagebox.showerror(
                "Error",
                "Unable to add apartment."
            )


    def update_apartment(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select an apartment to update."
            )

            return

        location = self.location_entry.get().strip()
        apartment_type = self.type_entry.get().strip()

        if location == "" or apartment_type == "":

            messagebox.showwarning(
                "Missing Information",
                "Location and Apartment Type are required."
            )

            return

        self.apartment_model.apartment_id = self.selected_id
        self.apartment_model.location = location
        self.apartment_model.apartment_type = apartment_type
        self.apartment_model.monthly_rent = self.rent_entry.get().strip()
        self.apartment_model.number_of_rooms = self.rooms_entry.get().strip()
        self.apartment_model.status = self.status_combo.get()

        if self.apartment_model.update_apartment():

            messagebox.showinfo(
                "Success",
                "Apartment updated successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_apartments()

        else:

            messagebox.showerror(
                "Error",
                "Unable to update apartment.")


    def delete_apartment(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select an apartment."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this apartment?"
        )

        if not answer:
            return

        if self.apartment_model.delete_apartment(self.selected_id):

            messagebox.showinfo(
                "Deleted",
                "Apartment deleted successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_apartments()

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete apartment.")



    def search_apartment(self):

        keyword = self.location_entry.get().strip()

        if keyword == "":

            self.load_apartments()
            return

        apartments = self.apartment_model.search_apartment(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for apartment in apartments:

            self.tree.insert(
                "",
                tk.END,
                values=apartment
            )



    def select_record(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected)["values"]

        self.clear_fields()

        self.selected_id = values[0]

        self.location_entry.insert(0, values[1])
        self.type_entry.insert(0, values[2])
        self.rent_entry.insert(0, values[3])
        self.rooms_entry.insert(0, values[4])

        self.status_combo.set(values[5])



    def go_back(self):

        answer = messagebox.askyesno(
            "Back",
            "Return to Dashboard?"
        )

        if answer:

            self.root.destroy()



if __name__ == "__main__":

    ApartmentGUI()