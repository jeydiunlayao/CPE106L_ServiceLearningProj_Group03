import sqlite3


conn = sqlite3.connect('reservation_information.db')
query = (''' CREATE TABLE USER_INFORMATION
            (USER_ID INTEGER PRIMARY KEY,
            NAME TEXT,
            AGE INTEGER,
            ADDRESS TEXT,
            CONTACT_NUMBER INTEGER,
            USERNAME TEXT,
            PASSWORD TEXT)'''
         )
conn.execute(query)
conn.close()
