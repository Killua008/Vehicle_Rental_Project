from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def booking(id,name,vechtype,fueltype,FromDate,ToDate,Email):
    id1=id
    name1=name
    vechtype1=vechtype
    fueltype1=fueltype
    FromDate1=FromDate
    ToDate1=ToDate
    Email_id=Email
    

    if(id1== "" or name1=="" or vechtype1=="" or fueltype1=="" or FromDate1=="" or ToDate=="" or Email_id==""):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",passwd="NewPass",database="admin")
        cursor=con.cursor()
        
        cursor.execute("Insert into booking values('"+ id1 +"','"+ name1 +"','"+ vechtype1+"','" + fueltype1+ "','" + FromDate1 +"','"+ ToDate1 +"','"+ Email_id + "')")
        cursor.execute("commit")

        
        MessageBox.showinfo("Insert Status","Inserted Successfully")
        MessageBox.showinfo("Bill for "+ Email_id +" be Generated : "," Bill : From " +FromDate1+ " to " + ToDate1 + " as per day rent ")
                  
        
        availibility(id1)
        i=1
        con.close()
        
            
def availibility(id):
    id1=id
    i=0
    con=mysql.connect(host="localhost",user="root",passwd="NewPass",database="admin")
    cursor=con.cursor()
        
    sql="Update Vehicle Set Avail=%s where id=%s"
    val=(i,id)
    cursor.execute(sql,val)
    cursor.execute("commit")
    
    
