# Rafia Begum
# 24043914

import sqlite3
import os

# Database file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "pams.db")


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    def create_tables(self):

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tenants(
                tenant_id INTEGER PRIMARY KEY AUTOINCREMENT,
                ni_number TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                occupation TEXT,
                reference TEXT
            )
        """)

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Apartments(
                apartment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                location TEXT NOT NULL,
                apartment_type TEXT NOT NULL,
                monthly_rent REAL NOT NULL,
                number_of_rooms INTEGER,
                status TEXT NOT NULL
            )
        """)

       
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS LeaseAgreements(
                lease_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_id INTEGER,
                apartment_id INTEGER,
                start_date TEXT,
                end_date TEXT,
                deposit REAL,
                monthly_rent REAL,
                FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id),
                FOREIGN KEY (apartment_id) REFERENCES Apartments(apartment_id)
            )
        """)

       
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Invoices(
                invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_id INTEGER,
                amount REAL,
                issue_date TEXT,
                due_date TEXT,
                status TEXT,
                FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
            )
        """)

       
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Payments(
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_id INTEGER,
                amount REAL,
                payment_date TEXT,
                payment_status TEXT,
                FOREIGN KEY (invoice_id) REFERENCES Invoices(invoice_id)
            )
        """)

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Complaints(
                complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_id INTEGER,
                description TEXT,
                complaint_date TEXT,
                status TEXT,
                FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id)
            )
        """)

        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS MaintenanceRequests(
                request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tenant_id INTEGER,
                apartment_id INTEGER,
                priority TEXT,
                status TEXT,
                cost REAL,
                resolution_time INTEGER,
                FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id),
                FOREIGN KEY (apartment_id) REFERENCES Apartments(apartment_id)
            )
        """)

        self.connection.commit()

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    db = Database()
    db.create_tables()
    print("Database and tables created successfully.")
    db.close_connection()