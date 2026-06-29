# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import ttk, messagebox

from models.maintenance import Maintenance


class MaintenanceGUI:

    def __init__(self):

        self.maintenance_model = Maintenance()
        self.selected_id = None

        self.root = tk.Tk()
        self.root.title("Paragon Apartment Management System")
        self.root.geometry("1200x740")
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
            text="Maintenance Management",
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

            ("Tenant ID",0,0),
            ("Apartment ID",1,0),
            ("Priority",2,0),

            ("Status",0,2),
            ("Cost",1,2),
            ("Resolution Time",2,2)

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

        self.priority_combo = ttk.Combobox(
            form,
            width=27,
            state="readonly",
            values=("Low","Medium","High")
        )
        self.priority_combo.grid(row=2,column=1,padx=5)
        self.priority_combo.current(0)

        self.status_combo = ttk.Combobox(
            form,
            width=27,
            state="readonly",
            values=("Pending","In Progress","Completed")
        )
        self.status_combo.grid(row=0,column=3,padx=5)
        self.status_combo.current(0)

        self.cost_entry = tk.Entry(form,width=30)
        self.cost_entry.grid(row=1,column=3,padx=5)

        self.time_entry = tk.Entry(form,width=30)
        self.time_entry.grid(row=2,column=3,padx=5)



        button_frame = tk.Frame(
            self.root,
            bg="#F4F6F9"
        )

        button_frame.pack(pady=15)

        tk.Button(button_frame,text="Add",width=12,bg="#2E75B6",fg="white",command=self.add_request).grid(row=0,column=0,padx=5)

        tk.Button(button_frame,text="Update",width=12,bg="#2E75B6",fg="white",command=self.update_request).grid(row=0,column=1,padx=5)

        tk.Button(button_frame,text="Delete",width=12,bg="#2E75B6",fg="white",command=self.delete_request).grid(row=0,column=2,padx=5)

        tk.Button(button_frame,text="Search",width=12,bg="#2E75B6",fg="white",command=self.search_request).grid(row=0,column=3,padx=5)

        tk.Button(button_frame,text="Clear",width=12,bg="#2E75B6",fg="white",command=self.clear_fields).grid(row=0,column=4,padx=5)

        tk.Button(button_frame,text="Back",width=12,bg="#C00000",fg="white",command=self.go_back).grid(row=0,column=5,padx=5)

    

        tk.Label(
            self.root,
            text="Maintenance Records",
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
        scrollbar.pack(side="right",fill="y")

        self.tree = ttk.Treeview(

            table_frame,

            columns=(

                "Request ID",
                "Tenant ID",
                "Apartment ID",
                "Priority",
                "Status",
                "Cost",
                "Resolution Time"

            ),

            show="headings",

            yscrollcommand=scrollbar.set

        )

        scrollbar.config(command=self.tree.yview)

        headings=[

            ("Request ID",90),
            ("Tenant ID",90),
            ("Apartment ID",100),
            ("Priority",100),
            ("Status",130),
            ("Cost",100),
            ("Resolution Time",150)

        ]

        for heading,width in headings:

            self.tree.heading(heading,text=heading)
            self.tree.column(heading,width=width)

        self.tree.pack(fill="both",expand=True)

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

        self.load_requests()

        self.root.mainloop()



    def load_requests(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        requests = self.maintenance_model.get_all_requests()

        for request in requests:

            self.tree.insert(
                "",
                tk.END,
                values=request
            )




    def clear_fields(self):

        self.tenant_entry.delete(0, tk.END)
        self.apartment_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

        self.priority_combo.current(0)
        self.status_combo.current(0)


  

    def add_request(self):

        tenant_id = self.tenant_entry.get().strip()
        apartment_id = self.apartment_entry.get().strip()

        if tenant_id == "" or apartment_id == "":

            messagebox.showwarning(
                "Missing Information",
                "Tenant ID and Apartment ID are required."
            )

            return

        self.maintenance_model.tenant_id = tenant_id
        self.maintenance_model.apartment_id = apartment_id
        self.maintenance_model.priority = self.priority_combo.get()
        self.maintenance_model.status = self.status_combo.get()
        self.maintenance_model.cost = self.cost_entry.get().strip()
        self.maintenance_model.resolution_time = self.time_entry.get().strip()

        if self.maintenance_model.add_request():

            messagebox.showinfo(
                "Success",
                "Maintenance request added successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_requests()

        else:

            messagebox.showerror(
                "Error",
                "Unable to add maintenance request."
            )


    def update_request(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a maintenance request to update."
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

        self.maintenance_model.request_id = self.selected_id
        self.maintenance_model.tenant_id = tenant_id
        self.maintenance_model.apartment_id = apartment_id
        self.maintenance_model.priority = self.priority_combo.get()
        self.maintenance_model.status = self.status_combo.get()
        self.maintenance_model.cost = self.cost_entry.get().strip()
        self.maintenance_model.resolution_time = self.time_entry.get().strip()

        if self.maintenance_model.update_request():

            messagebox.showinfo(
                "Success",
                "Maintenance request updated successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_requests()

        else:

            messagebox.showerror(
                "Error",
                "Unable to update maintenance request.")



    def delete_request(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a maintenance request."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this maintenance request?"
        )

        if not answer:
            return

        if self.maintenance_model.delete_request(self.selected_id):

            messagebox.showinfo(
                "Deleted",
                "Maintenance request deleted successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_requests()

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete maintenance request.")




    def search_request(self):

        keyword = self.tenant_entry.get().strip()

        if keyword == "":

            self.load_requests()
            return

        requests = self.maintenance_model.search_request(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for request in requests:

            self.tree.insert(
                "",
                tk.END,
                values=request
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

        self.priority_combo.set(values[3])
        self.status_combo.set(values[4])

        self.cost_entry.insert(0, values[5])
        self.time_entry.insert(0, values[6])




    def go_back(self):

        answer = messagebox.askyesno(
            "Back",
            "Return to Dashboard?"
        )

        if answer:

            self.root.destroy()



if __name__ == "__main__":

    MaintenanceGUI()