from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x500+200+150")
        
# =================== variables ==================================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtaxt=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
# ========================= Title =====================================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

              
        # =========================== logo =====================================
        img2 = Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\logo1.png")
        img2 = img2.resize((125,50), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=130, height=50) 
        
        # =========================== label frame====================================
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("times new roman",12,"bold"))
        Labelframeleft.place(x=0,y=50,width=350,height=420)   
        
        # ================labels and entry =====================================
        # customer contact
        lbl_cust_contact=Label(Labelframeleft,text="Cust. contact:",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)   
            
        entry_contact=ttk.Entry(Labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=17)
        entry_contact.grid(row=0,column=1,sticky=W)
        
        # fetch data button
        btnFetchData=Button(Labelframeleft,command=self.fetch_contact,text="Fetch Data ",font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=263,y=2)
        
        # Check_in Date
        Check_in_Date=Label(Labelframeleft,text="Check_In Date:",font=("arial ",12,"bold"),padx=1,pady=3)
        Check_in_Date.grid(row=1,column=0,sticky=W)       
        txtCheck_in_Date=ttk.Entry(Labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=22)
        txtCheck_in_Date.grid(row=1,column=1)
        
        # Check_out Date
        Check_out_Date=Label(Labelframeleft,text="Check_Out Date:",font=("arial ",12,"bold"),padx=1,pady=3)
        Check_out_Date.grid(row=2,column=0,sticky=W)       
        txtCheck_out=ttk.Entry(Labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=22)
        txtCheck_out.grid(row=2,column=1)
        
        # Room Type
        lbl_RoomType=Label(Labelframeleft,text="Room Type",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_RoomType.grid(row=3,column=0,sticky=W)  
      
        conn=mysql.connector.connect(host="localhost",username="root",password="Vikash@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomType from details")
        ide=my_cursor.fetchall()
             
        combo_RoomType = ttk.Combobox(Labelframeleft,textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=20, state="readonly")
        combo_RoomType["value"] =ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1) 
        
        # Available Room
        AvailableRoom=Label(Labelframeleft,text="Available Room:",font=("arial ",12,"bold"),padx=1,pady=3)
        AvailableRoom.grid(row=4,column=0,sticky=W)       
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Vikash@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("Select RoomNo from details")
        rows=my_cursor.fetchall()
        
        combo_RoomNo = ttk.Combobox(Labelframeleft,textvariable=self.var_roomavailable,font=("arial", 12, "bold"), width=20, state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)
               
        # Meal
        lbl_Meal=Label(Labelframeleft,text="Meal:",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_Meal.grid(row=5,column=0,sticky=W)       
        txtMeal=ttk.Entry(Labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=22)
        txtMeal.grid(row=5,column=1)
        
        # No Of Days
        lbl_NoOfDays=Label(Labelframeleft,text="No Of Days:",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_NoOfDays.grid(row=6,column=0,sticky=W)       
        txtNoOfDays=ttk.Entry(Labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=22)
        txtNoOfDays.grid(row=6,column=1)   
        
        # Paid Tax
        lbl_Paid=Label(Labelframeleft,text="Paid Tax:",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_Paid.grid(row=7,column=0,sticky=W)       
        txtPaid=ttk.Entry(Labelframeleft,textvariable=self.var_paidtaxt,font=("arial",13,"bold"),width=22)
        txtPaid.grid(row=7,column=1)   
        
        # Sub Total
        lbl_NoOfTotal=Label(Labelframeleft,text="Sub Total:",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_NoOfTotal.grid(row=8,column=0,sticky=W)       
        txtNoOfTotal=ttk.Entry(Labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=22)
        txtNoOfTotal.grid(row=8,column=1)   
        
        # Total Cost
        lbl_TotalCost=Label(Labelframeleft,text="No Of Days:",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_TotalCost.grid(row=9,column=0,sticky=W)       
        txtTotalCost=ttk.Entry(Labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=22)
        txtTotalCost.grid(row=9,column=1)   
             
        # ====================Bill Button================================================
        btn_Bill=Button(Labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold")
        btn_Bill.grid(row=10,column=0,padx=1,sticky=W)
                
        # ============================== button =========================================
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=330,width=340,height=40)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=0,padx=2)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=1,padx=2)
        
        btnDelete=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=2,padx=2)
        
        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=2)
        
        # ======================== Right Side Image =================
        img6 = Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\img6.png")
        img6 = img6.resize((490,250), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        lblimg = Label(self.root, image=self.photoimg6, bd=0, relief=RIDGE)
        lblimg.place(x=660, y=50, width=500, height=250)
           
        # ================================== table frame search system =============================================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=355,y=250,width=870,height=220)
        
        lblSearchBy=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=18,state="readonly")    
        combo_Search["value"]=("contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",12,"bold"),width=18)
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=2)
        
        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=2)
        
        # =============================== Show Data all ========================================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=40,width=866,height=156)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(details_table, columns=("Contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
   
        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout", text="Check-Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Roomavailable")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("Contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
# add data
    def add_data(self):
      if self.var_contact.get() == "" or self.var_checkin.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vikash@123",
                database="management"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("insert into row values (%s, %s, %s, %s, %s, %s, %s)",(
                                                                        self.var_contact.get(),
                                                                        self.var_checkin.get(),
                                                                        self.var_checkout.get(),
                                                                        self.var_roomtype.get(),
                                                                        self.var_roomavailable.get(),
                                                                        self.var_meal.get(),
                                                                        self.var_noofdays.get()
                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Room Booked ", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

        
# =============================== All Data Fetch ====================
     # fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Vikash@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from row")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                      
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                 self.room_table.insert("",END,values=i)
          
                 conn.commit()
            conn.close()  
            
    #get_cursor   
    def get_cursor(self,event=""):
      cursor_row=self.room_table.focus()
      content=self.room_table.item(cursor_row)
      row=content["values"]
      
      self.var_contact.set(row[0]),
      self.var_checkin.set(row[1]),
      self.var_checkout.set(row[2]),
      self.var_roomtype.set(row[3]),
      self.var_roomavailable.set(row[4]),
      self.var_meal.set(row[5]),
      self.var_noofdays.set(row[6])
       
   # update function   
    def update(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","Please enter mobile number",parent=self.root)
      else:
        
       conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vikash@123",
                database="management"
            )
       my_cursor = conn.cursor()
       my_cursor.execute("update row set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()               
                )) 
      conn.commit()
      self.fetch_data()
      conn.close()
      messagebox.showinfo("Update","Row Details has been updated  successfully",parent=self.root)  
      
    # Delete
    def mDelete(self):
      mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
      if mDelete>0:
        conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vikash@123",
                database="management"
            )
        my_cursor = conn.cursor()
        query=query = "DELETE FROM row WHERE Contact=%s"

        value=(self.var_contact.get (),)
        my_cursor.execute(query,value)
      else:
        if not mDelete:
          return
      conn.commit()
      self.fetch_data()
      conn.close()           
    
    def reset(self):
      self.var_contact.set(""),
      self.var_checkin.set(""),
      self.var_checkout.set(""),
      self.var_roomtype.set(""),
      self.var_roomavailable.set(""),
      self.var_meal.set(""),
      self.var_noofdays.set(""),
      self.var_paidtaxt.set(""),
      self.var_actualtotal.set(""),
      self.var_total.set("")
      
             
#=========================== All Data fetch ==============================        
    def fetch_contact(self):
            if self.var_contact.get()=="":
                    messagebox.showerror("Error","Please enter contact Number",parent=self.root)
            else:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Vikash@123",database="management")
                    my_cursor=conn.cursor()  
                    query=("Select Name from customer where mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)  
                    row=my_cursor.fetchone()
                    
                    if row==None:
                            messagebox.showerror("Error","This number not found",parent=self.root)
                    else:
                            conn.commit()
                            conn.close()
                            
                            showDataframe=Frame(self.root,bd=3,relief=RIDGE,padx=2)
                            showDataframe.place(x=350,y=55,width=300,height=190)
                            
                            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                            lblName.place(x=0,y=0)
                            
                            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                            lbl.place(x=75,y=0)
                            
                            conn=mysql.connector.connect(host="localhost",username="root",password="Vikash@123",database="management")
                            
# ===================================== Gender =============
                    my_cursor=conn.cursor()  
                    query=("Select Gender from customer where mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)  
                    row=my_cursor.fetchone()
                    
                    lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                    lblGender.place(x=0,y=25)
                            
                    lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                    lbl.place(x=75,y=25)
                    
# ======================================= Email =========================
                    my_cursor=conn.cursor()  
                    query=("Select Email from customer where mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)  
                    row=my_cursor.fetchone()
                    
                    lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                    lblEmail.place(x=0,y=50)
                            
                    lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                    lbl.place(x=75,y=50)
                    
# ======================================== Nationality ================

                    my_cursor=conn.cursor()  
                    query=("Select Nationality from customer where mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)  
                    row=my_cursor.fetchone()
                    
                    lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                    lblNationality.place(x=0,y=75)
                            
                    lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                    lbl.place(x=85,y=75)
                    self.room_table.pack(fill=BOTH,expand=1)                    
                    
# ======================== Address =======================
                    my_cursor=conn.cursor()  
                    query=("Select Address from customer where mobile=%s")
                    value=(self.var_contact.get(),)
                    my_cursor.execute(query,value)  
                    row=my_cursor.fetchone()
                    
                    lblAddress=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                    lblAddress.place(x=1,y=100)
                            
                    lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                    lbl.place(x=75,y=100)
                    
    # search system
    def search(self):
      conn = mysql.connector.connect(host="localhost", username="root", password="Vikash@123", database="management")
      my_cursor = conn.cursor()
      
      my_cursor.execute("select * from row where"+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
      rows=my_cursor.fetchall()
      if len(rows) != 0:
        self.room_table.delete(*self.room_table.get_children())
        for i in rows:
            self.room_table.insert("", END, values=i)
        conn.commit()
      conn.close()
                                       
    def total(self):
     inDate = self.var_checkin.get()
     outDate = self.var_checkout.get()
     inDate=datetime.strptime(inDate,"%d/%m/%Y")
     outDate=datetime.strptime(outDate,"%d/%m/%Y")
     self.var_noofdays.set(abs(outDate-inDate).days)
     
     if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxary"):
       q1=float(300)
       q2=float(700)
       q3=float(self.var_noofdays.get())
       q4=float(q1+q2)
       q5=float(q3+q4)
       Tax="Rs."+str("%.2f"%((q5)*0.1))
       ST="Rs."+str("%.2f"%((q5)))
       TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
       self.var_paidtaxt.set(Tax)
       self.var_actualtotal.set(ST)
       self.var_total.set(TT)
       
     elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
       q1=float(300)
       q2=float(700)
       q3=float(self.var_noofdays.get())
       q4=float(q1+q2)
       q5=float(q3+q4)
       Tax="Rs."+str("%.2f"%((q5)*0.1))
       ST="Rs."+str("%.2f"%((q5)))
       TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
       self.var_paidtaxt.set(Tax)
       self.var_actualtotal.set(ST)
       self.var_total.set(TT)
       
     elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
       q1=float(300)
       q2=float(700)
       q3=float(self.var_noofdays.get())
       q4=float(q1+q2)
       q5=float(q3+q4)
       Tax="Rs."+str("%.2f"%((q5)*0.1))
       ST="Rs."+str("%.2f"%((q5)))
       TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
       self.var_paidtaxt.set(Tax)
       self.var_actualtotal.set(ST)
       self.var_total.set(TT)
      
     elif(self.var_meal.get()=="Lunch" and self. var_roomtype.get()=="Double"):
       q1=float(300)
       q2=float(700)
       q3=float(self.var_noofdays.get())
       q4=float(q1+q2)
       q5=float(q3+q4)
       Tax="Rs."+str("%.2f"%((q5)*0.1))
       ST="Rs."+str("%.2f"%((q5)))
       TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
       self.var_paidtaxt.set(Tax)
       self.var_actualtotal.set(ST)
       self.var_total.set(TT) 
       
     elif(self.var_meal.get()=="Lunch" and self. var_roomtype.get()=="Luxary"):
       q1=float(300)
       q2=float(700)
       q3=float(self.var_noofdays.get())
       q4=float(q1+q2)
       q5=float(q3+q4)
       Tax="Rs."+str("%.2f"%((q5)*0.1))
       ST="Rs."+str("%.2f"%((q5)))
       TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
       self.var_paidtaxt.set(Tax)
       self.var_actualtotal.set(ST)
       self.var_total.set(TT)
       
     elif(self.var_meal.get()=="Lunch" and self. var_roomtype.get()=="Single"):
       q1=float(300)
       q2=float(700)
       q3=float(self.var_noofdays.get())
       q4=float(q1+q2)
       q5=float(q3+q4)
       Tax="Rs."+str("%.2f"%((q5)*0.1))
       ST="Rs."+str("%.2f"%((q5)))
       TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
       self.var_paidtaxt.set(Tax)
       self.var_actualtotal.set(ST)
       self.var_total.set(TT)
       
     elif(self.var_meal.get()=="Single" and self. var_roomtype.get()=="Dinner"):
       q1=float(500)
       q2=float(1000)
       q3=float(self.var_noofdays.get())
       q4=float(q1+q2)
       q5=float(q3+q4)
       Tax="Rs."+str("%.2f"%((q5)*0.1))
       ST="Rs."+str("%.2f"%((q5)))
       TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
       self.var_paidtaxt.set(Tax)
       self.var_actualtotal.set(ST)
       self.var_total.set(TT)    
              
        
if __name__ == '__main__':
  root=Tk()
  obj=Roombooking(root)
  root.mainloop()