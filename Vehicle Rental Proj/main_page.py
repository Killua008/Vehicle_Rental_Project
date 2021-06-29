from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from admindata import*
from loginuser import*


def admins():
    top=Toplevel()
    top.title("ADMIN PAGE")

    id=Label(top,text="Enter ID :",font=('bold',10))
    id.grid(row=1,column=1)

    name=Label(top,text="Enter Vehicle name:",font=('bold',10))
    name.grid(row=2,column=1)

    vehicle_type=Label(top,text="Enter VehicleType :",font=('bold',10))
    vehicle_type.grid(row=3,column=1)

    Fuel_type=Label(top,text="Enter Fuel Type :",font=('bold',10))
    Fuel_type.grid(row=4,column=1)

    avail=Label(top,text="Enter avail :",font=('bold',10))
    avail.grid(row=5,column=1)
    
    rent=Label(top,text="Enter RENT :",font=('bold',10))
    rent.grid(row=6,column=1)

    e_id=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_id.grid(row=1,column=2)

    e_name=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_name.grid(row=2,column=2)

    e_vechtype=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_vechtype.grid(row=3,column=2)

    e_fueltype=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_fueltype.grid(row=4,column=2)

    e_avail=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_avail.grid(row=5,column=2)

    e_rent=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_rent.grid(row=6,column=2)
    

    def insert():
        inserting(e_id.get(),e_name.get(),e_vechtype.get(),e_fueltype.get(),int(e_avail.get()),int(e_rent.get()))
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_vechtype.delete(0,'end')
        e_fueltype.delete(0,'end')
        e_avail.delete(0,'end')
        e_rent.delete(0,'end')
        


    def booked():
        #Enter the host,user,password,database name that you are using
        con=mysql.connect(host="**",user="**",passwd="**",database="**")
        cursor=con.cursor()
        top=Toplevel()
        top.title("REntED Customers")

        cursor.execute("SELECT * FROM Booking limit 0,10")
        i=0 
        for Booking in cursor: 
            for j in range(len(Booking)):
                e = Entry(top, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, Booking[j])
            i=i+1
    def vehicles():
        #Enter the host,user,password,database name that you are using
        con=mysql.connect(host="**",user="**",passwd="**",database="**")
        cursor=con.cursor()

        top=Toplevel()
        top.title("Vehicles Present in data")


        cursor.execute("SELECT * FROM vehicle limit 0,10")
        i=0 
        for vehicle in cursor: 
            for j in range(len(vehicle)):
                e = Entry(top, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, vehicle[j])
            i=i+1

    def deleteVehicles(e_ID):
        ID=int(e_ID)

        if(ID==""):
            MessageBox.showinfo("Delete Status","Email_ID Required")
        else:
            #Enter the host,user,password,database name that you are using
            con=mysql.connect(host="**",user="**",passwd="**",database="**")
            cursor=con.cursor()
            cursor.execute("Delete from  vehicle where id = '%d'" %(ID))
            cursor.execute("commit")

            
            MessageBox.showinfo("Delete Vehicle Data","Vehicle Data Deleted Successfully")
            con.close()

    def vehicle_deletes():
        top=Toplevel()
        top.title("Delete Vehicle")
        e_ID=Label(top,text="Enter Id of the vehicle :",font=('bold',10))
        e_ID.grid(row=2,column=1)
        e_ID=Entry(top)
        e_ID.grid(row=2,column=2)
        
        vehdelete=Button(top,text="Delete Vehicles",font=("italic",10),bg="light blue",command=lambda:deleteVehicles(e_ID.get()))
        vehdelete.grid(row=8,column=2,padx=10,pady=10)

        
        

    deleteveh=Button(top,text="Remove Vehicle",font=("italic",10),bg="light blue",command=vehicle_deletes)
    deleteveh.grid(row=0,column=2,padx=10,pady=10)



    def admin_delete(e_email):
        if(e_email==""):
            MessageBox.showinfo("Delete Status","Email_ID Required")
        else:
            #Enter the host,user,password,database name that you are using
            con=mysql.connect(host="**",user="**",passwd="**",database="**")
            cursor=con.cursor()
            cursor.execute("Delete from  loginusers where Email_id = '%s'" %(e_email))
            cursor.execute("commit")

            
            MessageBox.showinfo("Delete Loginusers Data","LoginUsers Data Deleted Successfully")
            con.close()

    def admin_deletes():
        top=Toplevel()
        top.title("Delete User")
        Email=Label(top,text="Enter Email Id of the user :",font=('bold',10))
        Email.grid(row=2,column=1)
        e_email=Entry(top)
        e_email.grid(row=2,column=2)
        
        admin_deleteb=Button(top,text="Delete LoginUsers",font=("italic",10),bg="light blue",command=lambda:admin_delete(e_email.get()))
        admin_deleteb.grid(row=8,column=2,padx=10,pady=10)
       
        
    

    insert=Button(top,text="Insert",font=("italic",10),bg="light blue",command=insert)
    insert.grid(row=7,column=1,padx=10,pady=10)

    booked=Button(top,text="Booked Customers",font=("italic",10),bg="light blue",command=booked)
    booked.grid(row=7,column=2,padx=10,pady=10)

    Vehicles=Button(top,text="Vehicles In Data",font=("italic",10),bg="light blue",command=vehicles)
    Vehicles.grid(row=7,column=3,padx=10,pady=10)

    delete_users=Button(top,text="Delete USERS",font=("italic",10),bg="light blue",command=admin_deletes)
    delete_users.grid(row=7,column=4,padx=10,pady=10)


    


def adminusers():
    #Enter the host,user,password,database name that you are using
        con=mysql.connect(host="**",user="**",passwd="**",database="**")
    cursor=con.cursor()
    user_verification=e_name.get()
    email=e_email.get()
    pass_verification=e_password.get()
    sql = "select * from adminlist where name = %s or code = %s"
    cursor.execute(sql,[(user_verification),(pass_verification)])
    results = cursor.fetchall()
    if results:
        for i in results:
            MessageBox.showinfo("Login Status","Logged in Successfully")
            e_name.delete(0,'end')
            e_email.delete(0,'end')
            e_password.delete(0,'end')
            admins()
            break
    else:
        MessageBox.showinfo("Login Status","Login Failed")



    
    
def users():
    
    top=Toplevel()
    top.title("Booking Page")
    

    id=Label(top,text="Enter ID :",font=('bold',10))
    id.grid(row=1,column=1)

    name=Label(top,text="Enter name:",font=('bold',10))
    name.grid(row=2,column=1)

    vehicle_type=Label(top,text="Enter VehicleType :",font=('bold',10))
    vehicle_type.grid(row=3,column=1)

    Fuel_type=Label(top,text="Enter Fuel Type :",font=('bold',10))
    Fuel_type.grid(row=4,column=1)

    FromDate=Label(top,text="From Date :",font=('bold',10))
    FromDate.grid(row=5,column=1)

    ToDate=Label(top,text="To Date :",font=('bold',10))
    ToDate.grid(row=6,column=1)
    
    email=Label(top,text="Email_id *:",font=('bold',10))
    email.grid(row=7,column=1)


    e_id=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_id.grid(row=1,column=2)

    e_name=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_name.grid(row=2,column=2)

    e_vechtype=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_vechtype.grid(row=3,column=2)

    e_fueltype=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_fueltype.grid(row=4,column=2)

    e_FromDate=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_FromDate.grid(row=5,column=2)
    
    e_ToDate=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_ToDate.grid(row=6,column=2)

    e_email=Entry(top,width=40,fg="blue",bg="white",borderwidth=10)
    e_email.grid(row=7,column=2)


    

    def check():
        booking(e_id.get(),e_name.get(),e_vechtype.get(),e_fueltype.get(),e_FromDate.get(),e_ToDate.get(),e_email.get())

        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_vechtype.delete(0,'end')
        e_fueltype.delete(0,'end')
        e_FromDate.delete(0,'end')
        e_ToDate.delete(0,'end')
        e_email.delete(0,'end')

    insert=Button(top,text="Insert",font=("italic",10),bg="light blue",command=check)
    insert.grid(row=8,column=1,padx=10,pady=10)

    def data():
        #Enter the host,user,password,database name that you are using
        con=mysql.connect(host="**",user="**",passwd="**",database="**")
        cursor=con.cursor()

        top=Toplevel()
        top.title("AVAILABLE VEhicLES")


        cursor.execute("SELECT * FROM vehicle limit 0,10")
        i=0 
        for vehicle in cursor: 
            for j in range(len(vehicle)):
                e = Entry(top, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, vehicle[j])
            i=i+1

    def user_delete(e_email):
        if(e_email==""):
            MessageBox.showinfo("Delete Status","Email_ID Required")
        else:
            #Enter the host,user,password,database name that you are using
            con=mysql.connect(host="**",user="**",passwd="**",database="**")
            cursor=con.cursor()
            cursor.execute("Delete from  loginusers where Email_id = '%s'" %(e_email))
            cursor.execute("commit")

            
            MessageBox.showinfo("Delete Loginusers Data","LoginUsers Data Deleted Successfully")
            con.close()

    def user_deletes():
        top=Toplevel()
        top.title("Delete User")
        Email=Label(top,text="Enter Email Id of the user :",font=('bold',10))
        Email.grid(row=2,column=1)
        e_email=Entry(top)
        e_email.grid(row=2,column=2)
        
        
        user_deleteb=Button(top,text="Delete LoginUsers",font=("italic",10),bg="light blue",command=lambda:user_delete(e_email.get()))
        user_deleteb.grid(row=8,column=2)
        e_email.delete(0,'end')
        


    def delete_bookings(e_email):
        if(e_email==""):
            MessageBox.showinfo("Delete Status","Email_ID Required")
        else:
            def change_avail(e_email):
                #Enter the host,user,password,database name that you are using
                con=mysql.connect(host="**",user="**",passwd="**",database="**")
                cursor=con.cursor()
                cursor.execute("Select id from booking where Email_id='%s'" %e_email)
                id=cursor.fetchone()
                cursor.execute("commit")
                con.close

            #Enter the host,user,password,database name that you are using
            con=mysql.connect(host="**",user="**",passwd="**",database="**")
            cursor=con.cursor()
            cursor.execute("Delete from  booking where Email_id = '%s'" %(e_email))
            cursor.execute("commit")
            

            
            MessageBox.showinfo("Booking Deleteing Status","Booking Data Deleted Successfully")
            con.close()
            

            def availibility_1(id):
                
                i=1
                #Enter the host,user,password,database name that you are using
                con=mysql.connect(host="**",user="**",passwd="**",database="**")
                cursor=con.cursor()
        
                sql="Update Vehicle Set Avail=%s where id=%s"
                val=(i,id)
                cursor.execute(sql,val)
                cursor.execute("commit")
            
        



            

    def delete_booking():
        top=Toplevel()
        top.title("Delete Booking")
        Email=Label(top,text="Enter Email Id of the user :",font=('bold',10))
        Email.grid(row=2,column=1)
        e_email=Entry(top)
        e_email.grid(row=2,column=2)
        
        user_deleteb=Button(top,text="Delete Booking",font=("italic",10),bg="light blue",command=lambda:delete_bookings(e_email.get()))
        user_deleteb.grid(row=8,column=2,padx=10,pady=10)



    data=Button(top,text="Available Vehicles",font=("italic",10),bg="light blue",command=data)
    data.grid(row=8,column=2,padx=10,pady=10)

    deleteuser=Button(top,text="Delete Your Account",font=("italic",10),bg="light blue",command=user_deletes)
    deleteuser.grid(row=0,column=1,padx=10,pady=10)

    deleteBooking=Button(top,text="Delete Your Booking",font=("italic",10),bg="light blue",command=delete_booking)
    deleteBooking.grid(row=0,column=2,padx=10,pady=10)


    
    

def loginusers():
    #Enter the host,user,password,database name that you are using
    con=mysql.connect(host="**",user="**",passwd="**",database="**")    
    cursor=con.cursor()
    user_verification=e_name.get()
    email=e_email.get()
    pass_verification=e_password.get()
    sql = "select * from loginusers where name = %s or password = %s"
    cursor.execute(sql,[(user_verification),(pass_verification)])
    results = cursor.fetchall()
    if results:
        for i in results:
            MessageBox.showinfo("Login Status","Logged in Successfully")
            e_name.delete(0,'end')
            e_email.delete(0,'end')
            e_password.delete(0,'end')
            users()
            break
    else:
        MessageBox.showinfo("Login Status","Login Failed")

    


    

def signin():
    
    name=e_name.get()
    email=e_email.get()
    password=e_password.get()
    

    if(  name=="" or email=="" or password==""):
        MessageBox.showinfo("Insert Status","All Fields are required")
    else:
        #Enter the host,user,password,database name that you are using
        con=mysql.connect(host="**",user="**",passwd="**",database="**")
        cursor=con.cursor()
        
        cursor.execute("Insert into Loginusers values('"+ name +"','"+ email+"','" + password+ "')")
        cursor.execute("commit")
        
        
        e_name.delete(0,'end')
        e_email.delete(0,'end')
        e_password.delete(0,'end')


        

        
        MessageBox.showinfo("Signing Status","Signing in Successfully")







root=Tk()
root.geometry("600x300")
root.title("Luxury At Rent ")

title=Label(root,text="**********Welcome to Luxury At ReNT ..\n\t \t \t Luxury for each and one***********",font="italic",fg='green')
title.place(x=20,y=0)


name=Label(root,text="Enter Name :",font=('bold',10))
name.place(x=20,y=60)
email=Label(root,text="Enter Email_id :",font=('bold',10))
email.place(x=20,y=90)

password=Label(root,text="Enter Password :",font=('bold',10))
password.place(x=20,y=120)


e_name=Entry()
e_name.place(x=150,y=60)

e_email=Entry()
e_email.place(x=150,y=90)

e_password=Entry(show="*")
e_password.place(x=150,y=120)

admin=Button(root,text="Admin",font=("italic",10),bg="light blue",command=adminusers)
admin.place(x=20,y=140)

Login=Button(root,text="Login",font=("italic",10),bg="light blue",command=loginusers)
Login.place(x=70,y=140)

signin=Button(root,text="Sign in IF NOT!",font=("italic",10),bg="light blue",command=signin)
signin.place(x=130,y=140)
"""
get=Button(root,text="Get",font=("italic",10),bg="white",command=get)
get.place(x=190,y=140) """

root.mainloop()

