# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "pams.db")


class Maintenance:

    def __init__(self,
                 request_id=None,
                 tenant_id="",
                 apartment_id="",
                 priority="",
                 status="",
                 cost=0,
                 resolution_time=0):

        self.request_id = request_id
        self.tenant_id = tenant_id
        self.apartment_id = apartment_id
        self.priority = priority
        self.status = status
        self.cost = cost
        self.resolution_time = resolution_time

    def get_connection(self):
        return sqlite3.connect(DB_PATH)

    def add_request(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                INSERT INTO MaintenanceRequests
                (
                    tenant_id,
                    apartment_id,
                    priority,
                    status,
                    cost,
                    resolution_time
                )

                VALUES (?,?,?,?,?,?)

            """, (

                self.tenant_id,
                self.apartment_id,
                self.priority,
                self.status,
                self.cost,
                self.resolution_time

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()

    def update_request(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                UPDATE MaintenanceRequests

                SET

                    tenant_id=?,
                    apartment_id=?,
                    priority=?,
                    status=?,
                    cost=?,
                    resolution_time=?

                WHERE request_id=?

            """, (

                self.tenant_id,
                self.apartment_id,
                self.priority,
                self.status,
                self.cost,
                self.resolution_time,
                self.request_id

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()

    def delete_request(self, request_id):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                DELETE FROM MaintenanceRequests

                WHERE request_id=?

            """, (request_id,))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()

    def search_request(self, keyword):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM MaintenanceRequests

            WHERE

                tenant_id LIKE ?

                OR

                apartment_id LIKE ?

        """, (

            "%" + keyword + "%",
            "%" + keyword + "%"

        ))

        requests = cursor.fetchall()

        connection.close()

        return requests

    def get_all_requests(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM MaintenanceRequests

            ORDER BY request_id

        """)

        requests = cursor.fetchall()

        connection.close()

        return requests


if __name__ == "__main__":

    maintenance = Maintenance()

    print("Maintenance Records\n")

    requests = maintenance.get_all_requests()

    for record in requests:

        print(record)