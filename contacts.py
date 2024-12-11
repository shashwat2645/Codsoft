import mysql.connector as c

conn = None
cursor = None

def connectDB():
    global conn, cursor
    try:
        # Connect to the database
        conn = c.connect(host='localhost', user='root', passwd='12345')
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS CONTACT_BOOK")
        cursor.execute("USE CONTACT_BOOK")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS USERS (
                ID INT PRIMARY KEY AUTO_INCREMENT,
                Name VARCHAR(100) NOT NULL,
                Phone_Number VARCHAR(10) UNIQUE NOT NULL,
                Email VARCHAR(100) UNIQUE NOT NULL,
                Address TEXT,
                CHECK (Phone_Number REGEXP '^[0-9]{10}$'),
                CHECK (Email LIKE '%_@_%._%')
            )
        """)
        conn.commit()
        print("Table created...")
    except Exception as e:
        print(f"Error occurred in connecting... {e}")

def closeDB():
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")

def deleteContact():
    id = int(input("Enter contact ID to delete: "))
    sql = "DELETE FROM USERS WHERE ID=%s"
    cursor.execute(sql, (id,))
    conn.commit()
    print("Contact deleted successfully.")

def viewContacts():
    sql = "SELECT ID, Name, Phone_Number FROM USERS"
    cursor.execute(sql)
    results = cursor.fetchall()
    if not results:
        print("No contacts found.")
    else:
        for row in results:
            print("Printing all contacts...")
            print(f"Name: {row[1]}, Phone: {row[2]}")

def updateContactPhone():
    id = int(input("Enter contact ID: "))
    phone = input("Enter new phone number: ")
    validatePhone(phone)
    sql = "UPDATE USERS SET Phone_Number = %s WHERE ID = %s"
    cursor.execute(sql, (phone, id))
    conn.commit()
    print("Phone number updated successfully.")

def updateContactAddress():
    id = int(input("Enter contact ID: "))
    address = input("Enter new address: ")
    sql = "UPDATE USERS SET Address = %s WHERE ID = %s"
    cursor.execute(sql, (address, id))
    conn.commit()
    print("Address updated successfully.")

def searchByPhone():
    phone = input("Enter phone number to search: ")
    validatePhone(phone)
    sql = "SELECT * FROM USERS WHERE Phone_Number = %s"
    cursor.execute(sql, (phone,))
    if cursor.fetchall():
        print(cursor.fetchall())
    else:
        print("No records with phone number ",phone)

def searchByName():
    name = input("Enter name to search: ")
    sql = "SELECT * FROM USERS WHERE Name = %s"
    cursor.execute(sql, (name,))
    if cursor.fetchall():
        print(cursor.fetchall())
    else:
        print("No records with name ",name)

def addContact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phone = validatePhone(phone)
    email = input("Enter email address: ")
    email = validateEmail(email)
    address = input("Enter address: ")
    sql = "INSERT INTO USERS (Name, Phone_Number, Email, Address) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, phone, email, address))
    conn.commit()
    print("Contact added into the contact book...\n")

def validatePhone(phone):
    while not (phone.isdigit() and len(phone) == 10):
        print("Invalid phone number. Please enter again.")
        phone = input("Enter phone number: ")
    return phone

def validateEmail(email):
    while not ("@" in email and "." in email):
        print("Invalid email. Please enter again.")
        email = input("Enter email address: ")
    return email

def menu():
    while True:
        print("\n1. Add a new contact\n2. Update an existing contact\n3. Delete a contact\n4. View all contacts\n5. Search for a contact\n6. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                addContact()
            case 2:
                print("1. Update contact number\n2. Update address")
                sch = int(input("Enter your choice: "))
                match sch:
                    case 1:
                        updateContactPhone()
                    case 2:
                        updateContactAddress()
            case 3:
                deleteContact()
            case 4:
                viewContacts()
            case 5:
                print("1. Search by name\n2. Search by phone")
                sch = int(input("Enter your choice: "))
                match sch:
                    case 1:
                        searchByName()
                    case 2:
                        searchByPhone()
            case 6:
                print("Exiting...")
                closeDB()
                exit()

if __name__ == "__main__":
    print("\tWelcome to Contacts Book...")
    connectDB()
    menu()
