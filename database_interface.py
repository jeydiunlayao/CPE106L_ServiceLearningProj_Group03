import sqlite3


def confirm_credentials(username, password):
    conn = sqlite3.connect('reservation_information.db')
    cursor = conn.cursor()
    conn.execute("SELECT count(*) FROM USER_INFORMATION WHERE USERNAME = ?", (username, ))
    conn.execute("SELECT count(*) FROM USER_INFORMATION WHERE PASSWORD = ?", (password, ))
    data = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return data


def insert_user_details(name, age, address, contact_number, username, password):
    conn = sqlite3.connect('reservation_information.db')
    conn.execute("INSERT INTO USER_INFORMATION (NAME, AGE, ADDRESS, CONTACT_NUMBER, USERNAME, PASSWORD) \
    VALUES (?, ?, ?, ?, ?, ?)", (name, age, address, contact_number, username, password))
    conn.commit()
    conn.close()


def insert_contact(pax, event,  start, end, duration, date):
    conn = sqlite3.connect('reservation_information.db')
    conn.execute("INSERT INTO RESERVATION_INFORMATION (PAX, EVENT, START, END, DURATION, DATE) \
    VALUES (?, ?, ?, ?, ?, ?)", (pax, event, start, end, duration, date))
    conn.commit()
    conn.close()


def delete_contact_by_name(name):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("DELETE from CONTACT_INFORMATION where name = ?",(name,))
    conn.close()

def edit_address_by_name(name, address):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, address))
    conn.commit()
    conn.close()

def edit_phone_number_by_name(name, phone_number):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set ADDRESS = ? where NAME = ?", (name, phone_number))
    conn.close()


def retrieve_contacts():
    results = []
    conn = sqlite3.connect('reservation_information.db')
    cursor = conn.execute("SELECT RESERVATION_ID, PAX, EVENT, START, END, DURATION, DATE from RESERVATION_INFORMATION ")
    for row in cursor:
        results.append(list(row))
    return results
