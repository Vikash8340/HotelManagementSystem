from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x500+200+150")
        
        # ======================= variable ===================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        
        # ========================= Title =====================================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        # =========================== logo =====================================
        img2 = Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\logo1.png")
        img2 = img2.resize((125,50), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=130, height=50)
        
        # =========================== label frame====================================
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"))
        Labelframeleft.place(x=0,y=50,width=350,height=420)
        
        # ================labels and entry =====================================
        # cust_ref
        lbl_cust_ref=Label(Labelframeleft,text="Customer Ref",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)       
        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=22,state="readonly")
        entry_ref.grid(row=0,column=1)

        # cust name
        cname=Label(Labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=1,pady=3)
        cname.grid(row=1,column=0,sticky=W)       
        txtcname=ttk.Entry(Labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=22)
        txtcname.grid(row=1,column=1)
        
        # mother name
        lblmname=Label(Labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=1,pady=3)
        lblmname.grid(row=2,column=0,sticky=W)        
        txtmname=ttk.Entry(Labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=22)
        txtmname.grid(row=2,column=1)
        
        # gender combobox
        
        lbl_gender = Label(Labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=1, pady=3)
        lbl_gender.grid(row=3, column=0, sticky=W)

        self.var_gender = StringVar()  # Declare StringVar for gender
        combo_gender = ttk.Combobox(Labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=20, state="readonly")
        combo_gender["value"] = ("Select...", "Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

              
        # postcode
        lbl_cust_ref=Label(Labelframeleft,text="Post Code:",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=4,column=0,sticky=W)        
        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=22)
        entry_ref.grid(row=4,column=1)
        
        # mobile number
        lbl_cust_ref=Label(Labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=5,column=0,sticky=W)        
        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=22)
        entry_ref.grid(row=5,column=1)
        
        # email
        lbl_cust_ref=Label(Labelframeleft,text="Email:",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=6,column=0,sticky=W)       
        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=22)
        entry_ref.grid(row=6,column=1)
        
        # nationality
        lbl_cust_ref = Label(Labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=1, pady=3)
        lbl_cust_ref.grid(row=7, column=0, sticky=W)

        self.var_nationality = StringVar()  # Declare StringVar for nationality
        combo_nationality = ttk.Combobox(Labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=20, state="readonly")
        combo_nationality["value"] = ("Select...", "Indian", "American", "Austrailian", "Britishian", "Others")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        
        # idproof type combobox
        lbl_cust_ref = Label(Labelframeleft, text="Id Proof Type:", font=("arial", 12, "bold"), padx=1, pady=3)
        lbl_cust_ref.grid(row=8, column=0, sticky=W)

        self.var_id_proof = StringVar()  # Declare the variable
        combo_idproof = ttk.Combobox(Labelframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=20, state="readonly")    
        combo_idproof["values"] = ("Select...", "AadharCard", "PanCard", "Driving Licence", "Others")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)

        
        # id number 
        lbl_cust_ref=Label(Labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=9,column=0,sticky=W)       
        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=22)
        entry_ref.grid(row=9,column=1)
        
         # address 
        lbl_cust_ref=Label(Labelframeleft,text="Address:",font=("arial",12,"bold"),padx=1,pady=3)
        lbl_cust_ref.grid(row=10,column=0,sticky=W)       
        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=22)
        entry_ref.grid(row=10,column=1)
        
        # ============================== button =========================================
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=330,width=340,height=40)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=1,padx=2)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=2,padx=2)
        
        btnDelete=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=3,padx=2)
        
        btnReset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=4,padx=2)
        
        
        
        # ================================== table frame search system =============================================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=355,y=50,width=860,height=420)
        
        lblSearchBy=Label(Table_Frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=18,state="readonly")    
        combo_Search["value"]=("Mobile","Ref")
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
        details_table.place(x=0,y=50,width=655,height=320)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        
        self.Cust_Details_Table.heading("ref",text="ref No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=90)
        self.Cust_Details_Table.column("name",width=90)
        self.Cust_Details_Table.column("mother",width=90)
        self.Cust_Details_Table.column("gender",width=90)
        self.Cust_Details_Table.column("post",width=90)
        self.Cust_Details_Table.column("mobile",width=90)
        self.Cust_Details_Table.column("email",width=90)
        self.Cust_Details_Table.column("nationality",width=90)
        self.Cust_Details_Table.column("idproof",width=90)
        self.Cust_Details_Table.column("idnumber",width=90)
        self.Cust_Details_Table.column("address",width=90)       
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
      if self.var_mobile.get() == "" or self.var_mother.get() == "":
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
            my_cursor.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_ref.get(),
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Customer has been added", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
            
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="Vikash@123",database="management")
      my_cursor=conn.cursor()
      my_cursor.execute("Select * from customer")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        for i in rows:
          self.Cust_Details_Table.insert("",END,values=i)
          
        conn.commit()
      conn.close()
      
    def get_cursor(self,event=""):
      cursor_row=self.Cust_Details_Table.focus()
      content=self.Cust_Details_Table.item(cursor_row)
      row=content["values"]
      
      self.var_ref.set(row[0]),
      self.var_cust_name.set(row[1]),
      self.var_mother.set(row[2]),
      self.var_gender.set(row[3]),
      self.var_post.set(row[4]),
      self.var_mobile.set(row[5]),
      self.var_email.set(row[6]),
      self.var_nationality.set(row[7]),
      self.var_id_proof.set(row[8]),
      self.var_id_number.set(row[9]),
      self.var_address.set(row[10])
      
    def update(self):
      if self.var_mobile.get()=="":
        messagebox.showerror("Error","Please enter mobile number",parent=self.root)
      else:
        
       conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vikash@123",
                database="management"
            )
       my_cursor = conn.cursor()
       my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
                )) 
      conn.commit()
      self.fetch_data()
      conn.close()
      messagebox.showinfo("Update","Customer Details has been update successfully",parent=self.root)
      
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
        query="delete from customer where Ref=%s"
        value=(self.var_ref.get(),)
        my_cursor.execute(query,value)
      else:
        if not mDelete:
          return
      conn.commit()
      self.fetch_data()
      conn.close()
      
    def reset(self):
      self.var_ref.set(str(random.randint(1000, 9999)))
      self.var_cust_name.set("")
      self.var_mother.set("")
     # self.var_gender.set("Select...")
      self.var_post.set("")
      self.var_mobile.set("")
      self.var_email.set("")
      #self.var_nationality.set("Select...")
      #self.var_id_proof.set("Select...")
      self.var_id_number.set("")
      self.var_address.set("")
      
      x=random.randint(1000,9999)
      self.var_ref.set(str(x))

    def search(self):
      conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vikash@123",
                database="management"
            )
      my_cursor = conn.cursor()
      
      my_cursor.execute("Select * from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        for i in rows:
          self.Cust_Details_Table.insert("",END,values=i)
        conn.commit() 
      conn.close()
          
      

        
        
        
        
        
        
      
        
      
      

          
        
          
    
         
        
        
if __name__ == '__main__':
  root=Tk()
  obj=Cust_Win(root)
  root.mainloop()
            
          