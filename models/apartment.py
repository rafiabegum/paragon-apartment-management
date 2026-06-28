# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "pams.db")


class Apartment:

    def __init__(self,
                 apartment_id=None,
                 location="",
                 apartment_type="",
                 monthly_rent=0,
                 number_of_rooms=0,
                 status=""):

        self.apartment_id = apartment_id
        self.location = location
        self.apartment_type = apartment_type
        self.monthly_rent = monthly_rent
        self.number_of_rooms = number_of_rooms
        self.status = status


    def get_connection(self):
        return sqlite3.connect(DB_PATH)


    def add_apartment(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                INSERT INTO Apartments
                (
                    location,
                    apartment_type,
                    monthly_rent,
                    number_of_rooms,
                    status
                )

                VALUES (?, ?, ?, ?, ?)

            """, (

                self.location,
                self.apartment_type,
                self.monthly_rent,
                self.number_of_rooms,
                self.status

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def update_apartment(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                UPDATE Apartments

                SET

                    location=?,
                    apartment_type=?,
                    monthly_rent=?,
                    number_of_rooms=?,
                    status=?

                WHERE apartment_id=?

            """, (

                self.location,
                self.apartment_type,
                self.monthly_rent,
                self.number_of_rooms,
                self.status,
                self.apartment_id

            ))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def delete_apartment(self, apartment_id):

        connection = self.get_connection()
        cursor = connection.cursor()

        try:

            cursor.execute("""

                DELETE FROM Apartments

                WHERE apartment_id=?

            """, (apartment_id,))

            connection.commit()
            return True

        except sqlite3.Error as error:

            print("Database Error:", error)
            return False

        finally:

            connection.close()


    def search_apartment(self, keyword):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Apartments

            WHERE

                location LIKE ?

                OR

                apartment_type LIKE ?

        """, (

            "%" + keyword + "%",
            "%" + keyword + "%"

        ))

        apartments = cursor.fetchall()

        connection.close()

        return apartments


    def get_all_apartments(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM Apartments

            ORDER BY apartment_id

        """)

        apartments = cursor.fetchall()

        connection.close()

        return apartments


if __name__ == "__main__":

    apartment = Apartment()

    print("Apartment Records\n")

    apartments = apartment.get_all_apartments()

    for record in apartments:

        print(record)