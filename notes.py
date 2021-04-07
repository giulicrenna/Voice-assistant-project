import sqlite3
import os, sys
import pandas as pd
import time
# def erase_all():
#     conn = sqlite3.connect('notes_db.s3db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM notes")
#     conn.commit()
#     cursor.close()
#     # for row in all:
#     #     print(row)
#     #     cursor.execute("DELETE FROM notes WHERE id= %s" %row)
def error_log2(exception_):
    named = time.localtime() 
    time_string = time.strftime("%m-%d-%Y_%H-%M", named)
    path = r'logs' # to logs folder
    file_name = 'error_log_%s.txt'%time_string
    file = os.path.join(path, file_name)
    file = open(file, "a") # creates the new file if not exists
    file.write(str(exception_))  # write the exception on the new file 
    file.close()

class Notes():
    def __init__(self, note, index, del_id):
        self.note = note
        self.index = index
        self.del_id = del_id
    def add_note(self):
        try:
            conn = sqlite3.connect('notes_db.s3db')
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS notes (index_ text, notas text)")
            cursor.execute("INSERT INTO notes VALUES (NULL,'%s', '%s')" %(self.index, self.note))
            conn.commit()
            cursor.close()
        except AttributeError as error:
            error_log2(error)
    def erase_notes(self):
        try:
            conn = sqlite3.connect('notes_db.s3db')
            cursor = conn.cursor()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE id= %s" %(self.del_id))
            conn.commit()
            cursor.close()
        except AttributeError as error:
            error_log2(error)
    def erase_all(self):
        try:
            conn = sqlite3.connect('notes_db.s3db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes")
            conn.commit()
            cursor.close()
        except AttributeError as error:
            error_log2(error)
    def show_notes(self):
        try:
            conn = sqlite3.connect('notes_db.s3db')
            cursor = conn.cursor()
            db = pd.read_sql("SELECT * from notes", conn)
            print(db)
            cursor.close()
        except AttributeError as error:
            error_log2(error)


conn = sqlite3.connect('notes_db.s3db')
cursor = conn.cursor()
select_ = cursor.execute("SELECT * FROM notes")
count = 1
for i in select_:
    count += 1

del_id_ = 2
