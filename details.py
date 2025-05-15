from tkinter import*
from PIL import Image, ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1050x500+200+150")
        
        # ========================= Title =====================================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1275,height=50)
       
        
        # =========================== logo =====================================
        img2 = Image.open(r"C:\Users\vikas\OneDrive\Documents\Hotel Management System\Images\logo1.png")
        img2 = img2.resize((125,50), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=130, height=50) 
        
        # =========================== label frame====================================
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"))
        Labelframeleft.place(x=5,y=50,width=500,height=350)
        
        
        
        # ================labels and entry =====================================
        # Floor
        lbl_floor=Label(Labelframeleft,text="Floor",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_floor.grid(row=0,column=0,sticky=W)  
         
        self.var_floor=StringVar()   
        entry_floor=ttk.Entry(Labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=17)
        entry_floor.grid(row=0,column=1,sticky=W)
        
        #Room No
        lbl_RoomNo=Label(Labelframeleft,text="Room No",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)   
        
        self.var_roomNo=StringVar()    
        entry_RoomNo=ttk.Entry(Labelframeleft,textvariable=self.var_roomNo,font=("arial",13,"bold"),width=17)
        entry_RoomNo.grid(row=1,column=1,sticky=W)
        
        #Room Type
        lbl_RoomType=Label(Labelframeleft,text="Room Type",font=("arial ",12,"bold"),padx=1,pady=3)
        lbl_RoomType.grid(row=2,column=0,sticky=W)    
        
        self.var_RoomType=StringVar()
           
        entry_RoomType=ttk.Entry(Labelframeleft,textvariable=self.var_RoomType,font=("arial",13,"bold"),width=17)
        entry_RoomType.grid(row=2,column=1,sticky=W)
        
        # ============================== button =========================================
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=340,height=40)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnAdd.grid(row=0,column=0,padx=2)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnUpdate.grid(row=0,column=1,padx=2)
        
        btnDelete=Button(btn_frame,text="DELETE",command=self.mDelete,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnDelete.grid(row=0,column=2,padx=2)
        
      
        btnReset=Button(btn_frame,text="RESET",command=self.reset_data,font=("arial",13,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=2)
        
    # ================================== table frame search system ============================================= 
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=550,y=50,width=460,height=350)
        
   # scroll     
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.room_table=ttk.Treeview(Table_Frame, columns=("floor","roomno","roomType"),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)  
                                 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType", text="Room Type")
        
        
        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
# add data
    def add_data(self):
      if self.var_floor.get() == "" or self.var_RoomType.get() == "":
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
            my_cursor.execute("insert into details values (%s, %s, %s)",(
                                                                        self.var_floor.get(),
                                                                        self.var_roomNo.get(),
                                                                        self.var_RoomType.get()
                                                            
                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "New Room Added Successfully", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
        
        
# fetch data
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Vikash@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from details")
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
      
      self.var_floor.set(row[0]),
      self.var_roomNo.set(row[1]),
      self.var_RoomType.set(row[2])
      
    def update(self):
      if self.var_floor.get()=="":
        messagebox.showerror("Error","Please enter Floor number",parent=self.root)
      else:       
       conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vikash@123",
                database="management"
            )
       my_cursor = conn.cursor()
       my_cursor.execute("update details set Floor=%s,RoomType=%s, where RoomNo=%s",(
                self.var_floor.get(),
                self.var_RoomType.get(),
                self.var_roomNo.get()      
                )) 
      conn.commit()
      self.fetch_data()
      conn.close()
      messagebox.showinfo("Update","Row Details has been updated  successfully",parent=self.root)  
      
    # Delete
    def mDelete(self):
      mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this Room Details",parent=self.root)
      if mDelete>0:
        conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vikash@123",
                database="management"
            )
        my_cursor = conn.cursor()
        query=query = "DELETE FROM details WHERE RoomNo=%s"

        value=(self.var_roomNo.get (),)
        my_cursor.execute(query,value)
      else:
        if not mDelete:
          return
      conn.commit()
      self.fetch_data()
      conn.close()    
      
    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")   
      
          
       
        
        

if __name__ == '__main__':
  root=Tk()
  obj=DetailsRoom(root)
  root.mainloop()