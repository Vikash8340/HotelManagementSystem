from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
import random
import time 
import datetime
from register import Register
from Hotel import HotelManagementSystem 


def main():
  win=Tk()
  app=Login_Window(win)
  win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\img3.png")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Image and title
        img1 = Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\loginlogo.png")
        img1 = img1.resize((90, 90), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        Label(image=self.photoimage1, bg="black", borderwidth=0).place(x=730, y=170, width=90, height=90)
        get_str=Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=85)
# ================================= label ==================
        # Username
        Username=lbl=Label(frame, text="Username", font=("times new roman", 12, "bold"), fg="white", bg="black")
        Username.place(x=70, y=125)
        
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        
        self.txtuser.place(x=40, y=150, width=270)

        # Password
        Password=lbl=Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="black")
        
        Password.place(x=70, y=195)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=220, width=270)
        
        # ===============Icon Iamges=======
        img2=Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\loginlogo.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=294,width=25,height=25)
      
        img3=Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\logipwd.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=364,width=25,height=25)

        # Login Button
        loginbtn=Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"),
               bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=270, width=120, height=35)

        # Register Button (not implemented)
        register=Button(frame, text="New User Register",command=self.register_window ,font=("times new roman", 10, "bold"),
               borderwidth=0, fg="white", bg="black")
        register.place(x=15, y=320, width=160)

        # Forget Password Button (not implemented)
        forgetpssbtn=Button(frame, text="Forget Password", command=self.forgot_password_window,font=("times new roman", 10, "bold"),
               borderwidth=0, fg="white", bg="black")
        forgetpssbtn.place(x=10, y=350, width=160)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to our hotel")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Vikash@123",
                    database="management"
                )
            cur = conn.cursor()
            cur.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()  
        
   # ======================== reset pswd================
   
    def reset_pass(self):
      if self.combo_security_Q.get()=="Select":
        messagebox.showerror("Error","Select security Question")
      elif self.txt_security.get()=="":
        messagebox.showerror("Error","Please enter the answer")
      elif self.txt_newpass.get()=="":
        messagebox.showerror("Error","Please enter the new password")
      else:
        conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Vikash@123",
                    database="management"
                )
        cur = conn.cursor()
        qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
        vlue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
        cur.execute(qury,vlue)
        row=cur.fetchone()
        if row==None:
          messagebox.showerror("Error","Please enter correct Answer")
        else:
          query=("update register set password=%s where email=%s")
          value=(self.txt_newpass.get(),self.txtuser.get())
          cur.execute(query,value)
          
          conn.commit()
          conn.close()
          messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
          self.root2.destroy()
          
          
   
   #==================== forget password ==========         
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Vikash@123",
                    database="management"
                )
            cur = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)
        
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Pet School Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)
                
                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                
                      
                    
                    
                    
                
    class Register:
      def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # ======== Variables ======
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        
        # background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\image1.png")
        
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0,y=0,width=1475,height=650)
        
        # Leftimage
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\register (2).png")
        
        LEFT_lbl = Label(self.root, image=self.bg1)
        LEFT_lbl.place(x=50, y=100, width=470, height=500)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=670,height=500)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        
        # ========== label and entry ======
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)
        
        
        # row 2
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        # row 3
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)
        
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Pet Name","Your Pet School Name","Your Favourite Place")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)
        
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
               
        # row 4
        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)
        
        # ======== check ========
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        # ========== button ========
        img = Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\regi.png")
        img = img.resize((140, 70), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        btn_register=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        btn_register.place(x=10,y=420,width=200) 
        
        
        img1 = Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\regis1.png")
        img1 = img1.resize((100, 70), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1=Button(frame,image=self.photoimg1,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=340,y=420,width=300)
        
  # ============= Fuctio declaratio ======
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & condition")
        else:
            conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="Vikash@123",
                    database="management"
                )
            cur = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),
                                                                                 self.var_lname.get(),
                                                                                 self.var_contact.get(),
                                                                                 self.var_email.get(),
                                                                                 self.var_securityQ.get(),
                                                                                 self.var_securityA.get(),
                                                                                 self.var_pass.get()
                                                                                 ))
                
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

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
        
  
  
  
      


if __name__ == "__main__":
    main()
