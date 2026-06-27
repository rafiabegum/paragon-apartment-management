# Rafia Begum
# 24043914

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "pams.db")


def insert_mock_data():

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    
    users = [
        ("Administrator", "admin@pams.com", "admin123", "Administrator"),
        ("Front Desk Staff", "frontdesk@pams.com", "front123", "Front Desk Staff"),
        ("Finance Manager", "finance@pams.com", "finance123", "Finance Manager"),
        ("Maintenance Staff", "maintenance@pams.com", "maint123", "Maintenance Staff"),
        ("Manager", "manager@pams.com", "manager123", "Manager")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Users(name,email,password,role)
        VALUES(?,?,?,?)
    """, users)

    
    apartments = [
        ("Bristol","Studio",650,1,"Available"),
        ("Bristol","Two Bedroom",900,2,"Occupied"),
        ("London","One Bedroom",1200,1,"Available"),
        ("London","Two Bedroom",1700,2,"Occupied"),
        ("Cardiff","Studio",600,1,"Available"),
        ("Cardiff","Three Bedroom",1100,3,"Occupied"),
        ("Manchester","One Bedroom",800,1,"Available"),
        ("Manchester","Two Bedroom",1000,2,"Occupied")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Apartments(
            location,
            apartment_type,
            monthly_rent,
            number_of_rooms,
            status)
        VALUES(?,?,?,?,?)
    """, apartments)

    
    tenants = [
        ("NI10001","John Smith","07111111111","john@gmail.com","Engineer","ABC Ltd"),
        ("NI10002","Emily Brown","07222222222","emily@gmail.com","Teacher","XYZ School"),
        ("NI10003","David Wilson","07333333333","david@gmail.com","Doctor","City Hospital"),
        ("NI10004","Sophia Jones","07444444444","sophia@gmail.com","Designer","Creative Ltd"),
        ("NI10005","Michael Taylor","07555555555","michael@gmail.com","Developer","Tech Ltd")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Tenants(
            ni_number,
            name,
            phone,
            email,
            occupation,
            reference)
        VALUES(?,?,?,?,?,?)
    """, tenants)

    
    leases = [
        (1,2,"2026-01-01","2026-12-31",900,900),
        (2,4,"2026-02-01","2027-01-31",1700,1700),
        (3,6,"2026-03-01","2027-02-28",1100,1100)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO LeaseAgreements(
            tenant_id,
            apartment_id,
            start_date,
            end_date,
            deposit,
            monthly_rent)
        VALUES(?,?,?,?,?,?)
    """, leases)

    
    invoices = [
        (1,900,"2026-06-01","2026-06-10","Paid"),
        (2,1700,"2026-06-01","2026-06-10","Pending"),
        (3,1100,"2026-06-01","2026-06-10","Paid")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Invoices(
            tenant_id,
            amount,
            issue_date,
            due_date,
            status)
        VALUES(?,?,?,?,?)
    """, invoices)

    
    payments = [
        (1,900,"2026-06-05","Completed"),
        (3,1100,"2026-06-06","Completed")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Payments(
            invoice_id,
            amount,
            payment_date,
            payment_status)
        VALUES(?,?,?,?)
    """, payments)

    
    complaints = [
        (1,"Water leakage","2026-06-10","Open"),
        (2,"Broken window","2026-06-11","Resolved"),
        (3,"Heating issue","2026-06-12","Open")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Complaints(
            tenant_id,
            description,
            complaint_date,
            status)
        VALUES(?,?,?,?)
    """, complaints)

    
    maintenance = [
        (1,2,"High","Open",0,0),
        (2,4,"Medium","Resolved",120,3),
        (3,6,"Low","Open",0,0)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO MaintenanceRequests(
            tenant_id,
            apartment_id,
            priority,
            status,
            cost,
            resolution_time)
        VALUES(?,?,?,?,?,?)
    """, maintenance)

    connection.commit()
    connection.close()

    print("Mock data inserted successfully.")


if __name__ == "__main__":
    insert_mock_data()