# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "pams.db")


class Tenant:

    def __init__(self,
                 tenant_id=None,
                 ni_number="",
                 name="",
                 phone="",
                 email="",
                 occupation="",
                 reference=""):

        self.tenant_id = tenant_id
        self.ni_number = ni_number
        self.name = name
        self.phone = phone
        self.email = email
        self.occupation = occupation
        self.reference = reference

    

    def get_connection(self):
        return sqlite3.connect(DB_PATH)

    

    def add_tenant(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""
                INSERT INTO Tenants
                (
                    ni_number,
                    name,
                    phone,
                    email,
                    occupation,
                    reference
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (

                self.ni_number,
                self.name,
                self.phone,
                self.email,
                self.occupation,
                self.reference

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()

    

    def update_tenant(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                UPDATE Tenants

                SET

                    ni_number=?,
                    name=?,
                    phone=?,
                    email=?,
                    occupation=?,
                    reference=?

                WHERE tenant_id=?

            """, (

                self.ni_number,
                self.name,
                self.phone,
                self.email,
                self.occupation,
                self.reference,
                self.tenant_id

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()

    

    def delete_tenant(self, tenant_id):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                DELETE FROM Tenants

                WHERE tenant_id=?

            """, (tenant_id,))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()

   

    def search_tenant(self, keyword):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Tenants

            WHERE
                name LIKE ?
                OR
                ni_number LIKE ?

        """, (

            "%" + keyword + "%",
            "%" + keyword + "%"

        ))

        tenants = cursor.fetchall()

        connection.close()

        return tenants

   

    def get_all_tenants(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Tenants

            ORDER BY tenant_id

        """)

        tenants = cursor.fetchall()

        connection.close()

        return tenants



if __name__ == "__main__":

    tenant = Tenant()

    print("Tenant Records\n")

    tenants = tenant.get_all_tenants()

    for record in tenants:
        print(record)