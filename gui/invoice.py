# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import ttk, messagebox

from models.invoice import Invoice


class InvoiceGUI:

    def __init__(self):

        self.invoice_model = Invoice()
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
            text="Invoice Management",
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
            ("Amount",1,0),
            ("Issue Date",2,0),

            ("Due Date",0,2),
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

        self.tenant_entry=tk.Entry(form,width=30)
        self.tenant_entry.grid(row=0,column=1,padx=5)

        self.amount_entry=tk.Entry(form,width=30)
        self.amount_entry.grid(row=1,column=1,padx=5)

        self.issue_entry=tk.Entry(form,width=30)
        self.issue_entry.grid(row=2,column=1,padx=5)

        self.due_entry=tk.Entry(form,width=30)
        self.due_entry.grid(row=0,column=3,padx=5)

        self.status_combo=ttk.Combobox(

            form,

            width=27,

            state="readonly",

            values=(

                "Pending",
                "Paid",
                "Overdue"

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
            command=self.add_invoice
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.update_invoice
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.delete_invoice
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.search_invoice
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

            text="Invoice Records",

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

                "Invoice ID",
                "Tenant ID",
                "Amount",
                "Issue Date",
                "Due Date",
                "Status"

            ),

            show="headings",

            yscrollcommand=scrollbar.set

        )

        scrollbar.config(command=self.tree.yview)

        headings=[

            ("Invoice ID",90),
            ("Tenant ID",100),
            ("Amount",120),
            ("Issue Date",140),
            ("Due Date",140),
            ("Status",120)

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

        self.load_invoices()

        self.root.mainloop()


    def load_invoices(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        invoices = self.invoice_model.get_all_invoices()

        for invoice in invoices:

            self.tree.insert(
                "",
                tk.END,
                values=invoice
            )




    def clear_fields(self):

        self.tenant_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.issue_entry.delete(0, tk.END)
        self.due_entry.delete(0, tk.END)

        self.status_combo.current(0)




    def add_invoice(self):

        tenant_id = self.tenant_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if tenant_id == "" or amount == "":

            messagebox.showwarning(
                "Missing Information",
                "Tenant ID and Amount are required."
            )

            return

        self.invoice_model.tenant_id = tenant_id
        self.invoice_model.amount = amount
        self.invoice_model.issue_date = self.issue_entry.get().strip()
        self.invoice_model.due_date = self.due_entry.get().strip()
        self.invoice_model.status = self.status_combo.get()

        if self.invoice_model.add_invoice():

            messagebox.showinfo(
                "Success",
                "Invoice added successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_invoices()

        else:

            messagebox.showerror(
                "Error",
                "Unable to add invoice."
            )


    def update_invoice(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select an invoice to update."
            )

            return

        tenant_id = self.tenant_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if tenant_id == "" or amount == "":

            messagebox.showwarning(
                "Missing Information",
                "Tenant ID and Amount are required."
            )

            return

        self.invoice_model.invoice_id = self.selected_id
        self.invoice_model.tenant_id = tenant_id
        self.invoice_model.amount = amount
        self.invoice_model.issue_date = self.issue_entry.get().strip()
        self.invoice_model.due_date = self.due_entry.get().strip()
        self.invoice_model.status = self.status_combo.get()

        if self.invoice_model.update_invoice():

            messagebox.showinfo(
                "Success",
                "Invoice updated successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_invoices()

        else:

            messagebox.showerror(
                "Error",
                "Unable to update invoice.")



    def delete_invoice(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select an invoice."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this invoice?"
        )

        if not answer:
            return

        if self.invoice_model.delete_invoice(self.selected_id):

            messagebox.showinfo(
                "Deleted",
                "Invoice deleted successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_invoices()

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete invoice.")



    def search_invoice(self):

        keyword = self.tenant_entry.get().strip()

        if keyword == "":

            self.load_invoices()
            return

        invoices = self.invoice_model.search_invoice(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for invoice in invoices:

            self.tree.insert(
                "",
                tk.END,
                values=invoice
            )


    def select_record(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected)["values"]

        self.clear_fields()

        self.selected_id = values[0]

        self.tenant_entry.insert(0, values[1])
        self.amount_entry.insert(0, values[2])
        self.issue_entry.insert(0, values[3])
        self.due_entry.insert(0, values[4])

        self.status_combo.set(values[5])


   

    def go_back(self):

        answer = messagebox.askyesno(
            "Back",
            "Return to Dashboard?"
        )

        if answer:

            self.root.destroy()



if __name__ == "__main__":

    InvoiceGUI()