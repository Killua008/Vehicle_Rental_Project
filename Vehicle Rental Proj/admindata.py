from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def inserting(id,name,vechtype,fueltype,avail,rent):
    id1=id
    name1=name
    vechtype1=vechtype
    fueltype1=fueltype
    avail1=str(avail)
    rent1=str(rent)

    if(id1== "" or name1=="" or vechtype1=="" or fueltype1=="" or avail1=="" or rent1==""):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",passwd="NewPass",database="admin")
        cursor=con.cursor()

        cursor.execute("Insert into vehicle values('"+ id1 +"','"+ name1 +"','"+ vechtype1+"','" + fueltype1+ "','" + rent1 +"','"+ avail1 +"')")
        cursor.execute("commit")

        
        MessageBox.showinfo("Insert Status","Inserted Successfully")
        con.close()
 
