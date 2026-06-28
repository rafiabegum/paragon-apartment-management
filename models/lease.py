# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "pams.db")


class Lease:

    def __init__(self,
                 lease_id=None,
                 tenant_id="",
                 apartment_id="",
                 start_date="",
                 end_date="",
                 deposit=0,
                 monthly_rent=0):

        self.lease_id = lease_id
        self.tenant_id = tenant_id
        self.apartment_id = apartment_id
        self.start_date = start_date
        self.end_date = end_date
        self.deposit = deposit
        self.monthly_rent = monthly_rent


    def get_connection(self):
        return sqlite3.connect(DB_PATH)


    def add_lease(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                INSERT INTO LeaseAgreements
                (
                    tenant_id,
                    apartment_id,
                    start_date,
                    end_date,
                    deposit,
                    monthly_rent
                )

                VALUES(?,?,?,?,?,?)

            """,(

                self.tenant_id,
                self.apartment_id,
                self.start_date,
                self.end_date,
                self.deposit,
                self.monthly_rent

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def update_lease(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                UPDATE LeaseAgreements

                SET

                    tenant_id=?,
                    apartment_id=?,
                    start_date=?,
                    end_date=?,
                    deposit=?,
                    monthly_rent=?

                WHERE lease_id=?

            """,(

                self.tenant_id,
                self.apartment_id,
                self.start_date,
                self.end_date,
                self.deposit,
                self.monthly_rent,
                self.lease_id

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def delete_lease(self, lease_id):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                DELETE FROM LeaseAgreements

                WHERE lease_id=?

            """,(lease_id,))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def search_lease(self, keyword):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM LeaseAgreements

            WHERE

                tenant_id LIKE ?

                OR

                apartment_id LIKE ?

        """,(

            "%" + keyword + "%",
            "%" + keyword + "%"

        ))

        leases = cursor.fetchall()

        connection.close()

        return leases


    def get_all_leases(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM LeaseAgreements

            ORDER BY lease_id

        """)

        leases = cursor.fetchall()

        connection.close()

        return leases


if __name__ == "__main__":

    lease = Lease()

    print("Lease Records\n")

    leases = lease.get_all_leases()

    for record in leases:

        print(record)