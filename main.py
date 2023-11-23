import customtkinter
import sqlite3
from CTkTable import *

root = customtkinter.CTk()
root.geometry("1000x500")
root.resizable(False, False)

findp = customtkinter.CTkEntry(root)
findp.place(relx = 0.01, rely = 0.03)

searchp = customtkinter.CTkButton(root, text= "search", width= 50, command=lambda: show_patients())
searchp.place(relx = 0.16, rely = 0.03)

hframe = customtkinter.CTkFrame(root, width= 450)

pframe = customtkinter.CTkScrollableFrame(root, 800)
pframe.place(relx = 0.01, rely = 0.20)

btnframe = customtkinter.CTkFrame(root)
btnframe.place(relx = 0.84, rely = 0.20)

con = sqlite3.connect('db.db')
cur = con.cursor()

def sql_database():

    createingtable = """
        create table if not exists patient(
        name text, age int, gender text,
        illness text, medication text, dosage int)
    """

    patients = """
        insert into patient values 
        ("Michael", 23, "Male", "Conjunctivitis","Antihistamines", 3),
        ("Leonardo", 21, "Male", "Diarrhea", "Imodium", 2),
        ("Sabel", 12, "Female", "Mononucleosis", "Penicilin", 3),
        ("Criza", 24, "Female", "Diabetes", "Sulfonylureas", 1)
    """

    cur.execute(createingtable)
    cur.execute(patients)

    con.commit()
    con.close()

def show_patients():

    pname = findp.get()
    squery = f"select * from patient where name = '{pname}'"

    allp = f"select * from patient"

    cur.execute(allp)
    ncur = cur.fetchall()

    tap = CTkTable(pframe, row = 6, column = 6, values= ncur)       #table of all patients
    tap.pack()

cm = customtkinter.CTkButton(btnframe, text= "Current Medication")
cm.grid(row = 0, column = 0, padx = 5, pady = 21)

nm = customtkinter.CTkButton(btnframe, text= "New Medication")
nm.grid(row = 1, column = 0, padx = 5, pady = 21)

form = customtkinter.CTkButton(btnframe, text= "Formulary")
form.grid(row = 2, column = 0, padx = 5, pady = 21)




root.mainloop()