# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "pams.db")


class User:

    def __init__(self, user_id=None, name="", email="", password="", role=""):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    

    def get_connection(self):
        return sqlite3.connect(DB_PATH)

   

    def login(self, email, password):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT user_id, name, email, password, role
            FROM Users
            WHERE email=? AND password=?
        """, (email, password))

        user = cursor.fetchone()

        connection.close()

        return user

   

    def add_user(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO Users(name, email, password, role)
            VALUES(?,?,?,?)
        """, (
            self.name,
            self.email,
            self.password,
            self.role
        ))

        connection.commit()
        connection.close()

 

    def get_all_users(self):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM Users
            ORDER BY user_id
        """)

        users = cursor.fetchall()

        connection.close()

        return users

 

    def delete_user(self, user_id):

        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM Users
            WHERE user_id=?
        """, (user_id,))

        connection.commit()
        connection.close()



if __name__ == "__main__":

    user = User()

    print("Users in Database\n")

    users = user.get_all_users()

    for record in users:
        print(record)