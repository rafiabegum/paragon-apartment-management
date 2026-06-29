# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "pams.db")


class Complaint:

    def __init__(self,
                 complaint_id=None,
                 tenant_id="",
                 description="",
                 complaint_date="",
                 status=""):

        self.complaint_id = complaint_id
        self.tenant_id = tenant_id
        self.description = description
        self.complaint_date = complaint_date
        self.status = status


    def get_connection(self):
        return sqlite3.connect(DB_PATH)


    def add_complaint(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                INSERT INTO Complaints
                (
                    tenant_id,
                    description,
                    complaint_date,
                    status
                )

                VALUES(?,?,?,?)

            """,(

                self.tenant_id,
                self.description,
                self.complaint_date,
                self.status

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def update_complaint(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                UPDATE Complaints

                SET

                    tenant_id=?,
                    description=?,
                    complaint_date=?,
                    status=?

                WHERE complaint_id=?

            """,(

                self.tenant_id,
                self.description,
                self.complaint_date,
                self.status,
                self.complaint_id

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def delete_complaint(self, complaint_id):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                DELETE FROM Complaints

                WHERE complaint_id=?

            """,(complaint_id,))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def search_complaint(self, keyword):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Complaints

            WHERE

                tenant_id LIKE ?

                OR

                status LIKE ?

        """,(

            "%" + keyword + "%",
            "%" + keyword + "%"

        ))

        complaints = cursor.fetchall()

        connection.close()

        return complaints


    def get_all_complaints(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Complaints

            ORDER BY complaint_id

        """)

        complaints = cursor.fetchall()

        connection.close()

        return complaints


if __name__ == "__main__":

    complaint = Complaint()

    print("Complaint Records\n")

    complaints = complaint.get_all_complaints()

    for record in complaints:

        print(record)