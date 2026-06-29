# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import ttk, messagebox

from models.complaint import Complaint


class ComplaintGUI:

    def __init__(self):

        self.complaint_model = Complaint()
        self.selected_id = None

        self.root = tk.Tk()
        self.root.title("Paragon Apartment Management System")
        self.root.geometry("1200x720")
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
            text="Complaint Management",
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

        labels = [

            ("Tenant ID",0,0),
            ("Description",1,0),

            ("Complaint Date",0,2),
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

        self.tenant_entry = tk.Entry(form,width=30)
        self.tenant_entry.grid(row=0,column=1,padx=5)

        self.description_entry = tk.Entry(form,width=30)
        self.description_entry.grid(row=1,column=1,padx=5)

        self.date_entry = tk.Entry(form,width=30)
        self.date_entry.grid(row=0,column=3,padx=5)

        self.status_combo = ttk.Combobox(

            form,

            width=27,

            state="readonly",

            values=(

                "Open",
                "In Progress",
                "Resolved"

            )

        )

        self.status_combo.grid(row=1,column=3,padx=5)
        self.status_combo.current(0)

        button_frame = tk.Frame(
            self.root,
            bg="#F4F6F9"
        )

        button_frame.pack(pady=15)

        tk.Button(button_frame,text="Add",width=12,bg="#2E75B6",fg="white",command=self.add_complaint).grid(row=0,column=0,padx=5)

        tk.Button(button_frame,text="Update",width=12,bg="#2E75B6",fg="white",command=self.update_complaint).grid(row=0,column=1,padx=5)

        tk.Button(button_frame,text="Delete",width=12,bg="#2E75B6",fg="white",command=self.delete_complaint).grid(row=0,column=2,padx=5)

        tk.Button(button_frame,text="Search",width=12,bg="#2E75B6",fg="white",command=self.search_complaint).grid(row=0,column=3,padx=5)

        tk.Button(button_frame,text="Clear",width=12,bg="#2E75B6",fg="white",command=self.clear_fields).grid(row=0,column=4,padx=5)

        tk.Button(button_frame,text="Back",width=12,bg="#C00000",fg="white",command=self.go_back).grid(row=0,column=5,padx=5)

        tk.Label(
            self.root,
            text="Complaint Records",
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

                "Complaint ID",
                "Tenant ID",
                "Description",
                "Complaint Date",
                "Status"

            ),

            show="headings",

            yscrollcommand=scrollbar.set

        )

        scrollbar.config(command=self.tree.yview)

        headings=[

            ("Complaint ID",100),
            ("Tenant ID",100),
            ("Description",350),
            ("Complaint Date",160),
            ("Status",140)

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

        self.load_complaints()

        self.root.mainloop()
    


    def load_complaints(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        complaints = self.complaint_model.get_all_complaints()

        for complaint in complaints:

            self.tree.insert(
                "",
                tk.END,
                values=complaint
            )




    def clear_fields(self):

        self.tenant_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

        self.status_combo.current(0)




    def add_complaint(self):

        tenant_id = self.tenant_entry.get().strip()
        description = self.description_entry.get().strip()

        if tenant_id == "" or description == "":

            messagebox.showwarning(
                "Missing Information",
                "Tenant ID and Description are required."
            )

            return

        self.complaint_model.tenant_id = tenant_id
        self.complaint_model.description = description
        self.complaint_model.complaint_date = self.date_entry.get().strip()
        self.complaint_model.status = self.status_combo.get()

        if self.complaint_model.add_complaint():

            messagebox.showinfo(
                "Success",
                "Complaint added successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_complaints()

        else:

            messagebox.showerror(
                "Error",
                "Unable to add complaint."
            )


    def update_complaint(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a complaint to update."
            )

            return

        tenant_id = self.tenant_entry.get().strip()
        description = self.description_entry.get().strip()

        if tenant_id == "" or description == "":

            messagebox.showwarning(
                "Missing Information",
                "Tenant ID and Description are required."
            )

            return

        self.complaint_model.complaint_id = self.selected_id
        self.complaint_model.tenant_id = tenant_id
        self.complaint_model.description = description
        self.complaint_model.complaint_date = self.date_entry.get().strip()
        self.complaint_model.status = self.status_combo.get()

        if self.complaint_model.update_complaint():

            messagebox.showinfo(
                "Success",
                "Complaint updated successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_complaints()

        else:

            messagebox.showerror(
                "Error",
                "Unable to update complaint.")




    def delete_complaint(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a complaint."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this complaint?"
        )

        if not answer:
            return

        if self.complaint_model.delete_complaint(self.selected_id):

            messagebox.showinfo(
                "Deleted",
                "Complaint deleted successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_complaints()

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete complaint.")




    def search_complaint(self):

        keyword = self.tenant_entry.get().strip()

        if keyword == "":

            self.load_complaints()
            return

        complaints = self.complaint_model.search_complaint(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for complaint in complaints:

            self.tree.insert(
                "",
                tk.END,
                values=complaint
            )


    def select_record(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected)["values"]

        self.clear_fields()

        self.selected_id = values[0]

        self.tenant_entry.insert(0, values[1])
        self.description_entry.insert(0, values[2])
        self.date_entry.insert(0, values[3])

        self.status_combo.set(values[4])


 

    def go_back(self):

        answer = messagebox.askyesno(
            "Back",
            "Return to Dashboard?"
        )

        if answer:

            self.root.destroy()



if __name__ == "__main__":

    ComplaintGUI()