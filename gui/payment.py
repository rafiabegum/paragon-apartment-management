# Rafia Begum
# 24043914

import tkinter as tk
from tkinter import ttk, messagebox

from models.payment import Payment


class PaymentGUI:

    def __init__(self):

        self.payment_model = Payment()
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
            text="Payment Management",
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

            ("Invoice ID",0,0),
            ("Amount",1,0),

            ("Payment Date",0,2),
            ("Payment Status",1,2)

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

        self.invoice_entry = tk.Entry(form,width=30)
        self.invoice_entry.grid(row=0,column=1,padx=5)

        self.amount_entry = tk.Entry(form,width=30)
        self.amount_entry.grid(row=1,column=1,padx=5)

        self.date_entry = tk.Entry(form,width=30)
        self.date_entry.grid(row=0,column=3,padx=5)

        self.status_combo = ttk.Combobox(

            form,

            width=27,

            state="readonly",

            values=(

                "Pending",
                "Completed",
                "Failed"

            )

        )

        self.status_combo.grid(row=1,column=3,padx=5)
        self.status_combo.current(0)

     

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
            command=self.add_payment
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            button_frame,
            text="Update",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.update_payment
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            button_frame,
            text="Delete",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.delete_payment
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            button_frame,
            text="Search",
            width=12,
            bg="#2E75B6",
            fg="white",
            command=self.search_payment
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

            text="Payment Records",

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

                "Payment ID",
                "Invoice ID",
                "Amount",
                "Payment Date",
                "Payment Status"

            ),

            show="headings",

            yscrollcommand=scrollbar.set

        )

        scrollbar.config(command=self.tree.yview)

        headings=[

            ("Payment ID",90),
            ("Invoice ID",100),
            ("Amount",120),
            ("Payment Date",150),
            ("Payment Status",150)

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

        self.load_payments()

        self.root.mainloop()
    


    def load_payments(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        payments = self.payment_model.get_all_payments()

        for payment in payments:

            self.tree.insert(
                "",
                tk.END,
                values=payment
            )



    def clear_fields(self):

        self.invoice_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

        self.status_combo.current(0)




    def add_payment(self):

        invoice_id = self.invoice_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if invoice_id == "" or amount == "":

            messagebox.showwarning(
                "Missing Information",
                "Invoice ID and Amount are required."
            )

            return

        self.payment_model.invoice_id = invoice_id
        self.payment_model.amount = amount
        self.payment_model.payment_date = self.date_entry.get().strip()
        self.payment_model.payment_status = self.status_combo.get()

        if self.payment_model.add_payment():

            messagebox.showinfo(
                "Success",
                "Payment added successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_payments()

        else:

            messagebox.showerror(
                "Error",
                "Unable to add payment."
            )


        # =====================================================
    # Update Payment
    # =====================================================

    def update_payment(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a payment to update."
            )

            return

        invoice_id = self.invoice_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if invoice_id == "" or amount == "":

            messagebox.showwarning(
                "Missing Information",
                "Invoice ID and Amount are required."
            )

            return

        self.payment_model.payment_id = self.selected_id
        self.payment_model.invoice_id = invoice_id
        self.payment_model.amount = amount
        self.payment_model.payment_date = self.date_entry.get().strip()
        self.payment_model.payment_status = self.status_combo.get()

        if self.payment_model.update_payment():

            messagebox.showinfo(
                "Success",
                "Payment updated successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_payments()

        else:

            messagebox.showerror(
                "Error",
                "Unable to update payment.")


    # =====================================================
    # Delete Payment
    # =====================================================

    def delete_payment(self):

        if self.selected_id is None:

            messagebox.showwarning(
                "Warning",
                "Please select a payment."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this payment?"
        )

        if not answer:
            return

        if self.payment_model.delete_payment(self.selected_id):

            messagebox.showinfo(
                "Deleted",
                "Payment deleted successfully."
            )

            self.clear_fields()
            self.selected_id = None
            self.load_payments()

        else:

            messagebox.showerror(
                "Error",
                "Unable to delete payment.")


    # =====================================================
    # Search Payment
    # =====================================================

    def search_payment(self):

        keyword = self.invoice_entry.get().strip()

        if keyword == "":

            self.load_payments()
            return

        payments = self.payment_model.search_payment(keyword)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for payment in payments:

            self.tree.insert(
                "",
                tk.END,
                values=payment
            )

    def select_record(self, event):

        selected = self.tree.focus()

        if not selected:
            return

        values = self.tree.item(selected)["values"]

        self.clear_fields()

        self.selected_id = values[0]

        self.invoice_entry.insert(0, values[1])
        self.amount_entry.insert(0, values[2])
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

    PaymentGUI()