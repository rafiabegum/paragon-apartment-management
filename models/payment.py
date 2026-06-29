# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "pams.db")


class Payment:

    def __init__(self,
                 payment_id=None,
                 invoice_id="",
                 amount=0,
                 payment_date="",
                 payment_status=""):

        self.payment_id = payment_id
        self.invoice_id = invoice_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_status = payment_status


    def get_connection(self):
        return sqlite3.connect(DB_PATH)


    def add_payment(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                INSERT INTO Payments
                (
                    invoice_id,
                    amount,
                    payment_date,
                    payment_status
                )

                VALUES (?, ?, ?, ?)

            """, (

                self.invoice_id,
                self.amount,
                self.payment_date,
                self.payment_status

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def update_payment(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                UPDATE Payments

                SET

                    invoice_id=?,
                    amount=?,
                    payment_date=?,
                    payment_status=?

                WHERE payment_id=?

            """, (

                self.invoice_id,
                self.amount,
                self.payment_date,
                self.payment_status,
                self.payment_id

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def delete_payment(self, payment_id):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                DELETE FROM Payments

                WHERE payment_id=?

            """, (payment_id,))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def search_payment(self, keyword):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Payments

            WHERE

                invoice_id LIKE ?

                OR

                payment_status LIKE ?

        """, (

            "%" + keyword + "%",
            "%" + keyword + "%"

        ))

        payments = cursor.fetchall()

        connection.close()

        return payments


    def get_all_payments(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Payments

            ORDER BY payment_id

        """)

        payments = cursor.fetchall()

        connection.close()

        return payments


if __name__ == "__main__":

    payment = Payment()

    print("Payment Records\n")

    payments = payment.get_all_payments()

    for record in payments:

        print(record)