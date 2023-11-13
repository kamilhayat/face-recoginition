# import re
import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        
        self.var_attend_id=StringVar()
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"college_images\attend.jpeg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=800,height=200)

        img1=Image.open(r"college_images\attend2.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        # set image as lable
        f_lb1_1 = Label(self.root,image=self.photoimg1)
        f_lb1_1.place(x=800,y=0,width=800,height=200)

        # backgorund image 
        bg1=Image.open(r"college_images\bg.jpg")
        bg1=bg1.resize((1540,710),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=200,width=1540,height=710)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white")  
        main_frame.place(x=20,y=50,width=1480,height=540)

    #     # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=710,height=400)

        

    #     # ==================================Text boxes and Combo Boxes====================
        #Attendence id
        Attendence_label = Label(left_frame,text="Attendence-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        Attendence_label.grid(row=0,column=0,padx=5)

        Attendence_label = ttk.Entry(left_frame,width=15,textvariable=self.var_attend_id,font=("verdana",12,"bold"))
        Attendence_label.grid(row=0,column=1)

        #Studnet Name
        student_name_label = Label(left_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2)

        student_name_entry = ttk.Entry(left_frame,width=15,textvariable=self.var_name,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3)
        
         #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=1,column=0,padx=5,sticky=W)

        date_entry = ttk.Entry(left_frame,width=15,textvariable=self.var_date,font=("verdana",12,"bold"))
        date_entry.grid(row=1,column=1,pady=8)

        # Department
        dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        dep_label.grid(row=1,column=2,padx=5)

        dep_entry = ttk.Entry(left_frame,width=15,textvariable=self.var_dep,font=("verdana",12,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)

        #time
        time_label = Label(left_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=2,column=0,)

        time_entry = ttk.Entry(left_frame,width=15,textvariable=self.var_time,font=("verdana",12,"bold"))
        time_entry.grid(row=2,column=1)
       

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll.No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,width=15,textvariable=self.var_roll,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        

        

        

       

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        self.attend_combo=ttk.Combobox(left_frame,text="Attendence Status",width=13,textvariable=self.var_attend,font=("verdana",12,"bold"),state="readonly")
        self.attend_combo["values"]=("Status","Present","Absent")
        self.attend_combo.grid(row=3,column=1,pady=8)
        self.attend_combo.current(0)

    #     # =========================button section========================

    #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=200,width=630,height=60)

        #import button
        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #export button
        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #update button
        del_btn=Button(btn_frame,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=12,command=self.reset_data,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)


        # ===============================Table Sql Data View==========================
        # table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        # table_frame.place(x=10,y=100,width=635,height=310)

        #scroll bar 
        # scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        # scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        # self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    #     scroll_x.pack(side=BOTTOM,fill=X)
    #     scroll_y.pack(side=RIGHT,fill=Y)
    #     scroll_x.config(command=self.attendanceReport_left.xview)
    #     scroll_y.config(command=self.attendanceReport_left.yview)

    #     self.attendanceReport_left.heading("ID",text="Std-ID")
    #     self.attendanceReport_left.heading("Roll_No",text="Roll.No")
    #     self.attendanceReport_left.heading("Name",text="Std-Name")
    #     self.attendanceReport_left.heading("Time",text="Time")
    #     self.attendanceReport_left.heading("Date",text="Date")
    #     self.attendanceReport_left.heading("Attend",text="Attend-status")
    #     self.attendanceReport_left["show"]="headings"


    #     # Set Width of Colums 
    #     self.attendanceReport_left.column("ID",width=100)
    #     self.attendanceReport_left.column("Roll_No",width=100)
    #     self.attendanceReport_left.column("Name",width=100)
    #     self.attendanceReport_left.column("Time",width=100)
    #     self.attendanceReport_left.column("Date",width=100)
    #     self.attendanceReport_left.column("Attend",width=100)
        
    #     self.attendanceReport_left.pack(fill=BOTH,expand=1)
    #     self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    


    #     



         # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=400)


         # -----------------------------Table Frame------------------------------------------------- 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=0,width=640,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReportTable = ttk.Treeview(table_frame,column=("id","department","name","roll", "time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id",text="Attendence-ID")
        self.attendanceReportTable.heading("department",text="Department")
        self.attendanceReportTable.heading("name",text="Std-Name")
        self.attendanceReportTable.heading("roll",text="Roll.No")
        self.attendanceReportTable.heading("time",text="Time")
        self.attendanceReportTable.heading("date",text="Date")
        self.attendanceReportTable.heading("attendence",text="Attend-status")
        self.attendanceReportTable["show"]="headings"


    #     # Set Width of Colums 
        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("roll",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendence",width=100)
        
        self.attendanceReportTable.pack(fill=BOTH,expand=1)
        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor_left)
    #     self.fetch_data()


    def fetchData(self,rows):
    #     mydata = rows
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    # #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
    # # =================================update for mysql button================
    # #Update button
    #     del_btn=Button(right_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
    #     del_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    # #Update button
    #     del_btn=Button(right_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
    #     del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
    # # ===============================update function for mysql database=================
    # def update_data(self):
    #     if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
    #         messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
    #     else:
    #         try:
    #             Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
    #             if Update > 0:
    #                 conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
    #                 mycursor = conn.cursor()
    #                 mycursor.execute("update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
    #                 self.var_id.get(),
    #                 self.var_roll.get(),
    #                 self.var_name.get(),
    #                 self.var_time.get(),
    #                 self.var_date.get(),
    #                 self.var_attend.get(),
    #                 self.var_id.get()  
    #                 ))
    #             else:
    #                 if not Update:
    #                     return
    #             messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # # =============================Delete Attendance form my sql============================
    # def delete_data(self):
    #     if self.var_id.get()=="":
    #         messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
    #     else:
    #         try:
    #             delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
    #             if delete>0:
    #                 conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
    #                 mycursor = conn.cursor() 
    #                 sql="delete from stdattendance where std_id=%s"
    #                 val=(self.var_id.get(),)
    #                 mycursor.execute(sql,val)
    #             else:
    #                 if not delete:
    #                     return

    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    # # ===========================fatch data form mysql attendance===========

    # def fetch_data(self):
    #     conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
    #     mycursor = conn.cursor()

    #     mycursor.execute("select * from stdattendance")
    #     data=mycursor.fetchall()

    #     if len(data)!= 0:
    #         self.attendanceReport.delete(*self.attendanceReport.get_children())
    #         for i in data:
    #             self.attendanceReport.insert("",END,values=i)
    #         conn.commit()
    #     conn.close()

    # #============================Reset Data======================
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # # =========================Fetch Data Import data ===============

    #    

    # #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReportTable.focus()
        content = self.attendanceReportTable.item(cursor_focus)
        data = content["values"]

        self.var_attend_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_name.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_attend.set(data[6])  
       
# reset data
    
     #=============Cursur Function for mysql========================

    # def get_cursor_right(self,event=""):
    #     cursor_focus = self.attendanceReport.focus()
    #     content = self.attendanceReport.item(cursor_focus)
    #     data = content["values"]

    #     self.var_id.set(data[0]),
    #     self.var_roll.set(data[1]),
    #     self.var_name.set(data[2]),
    #     self.var_time.set(data[3]),
    #     self.var_date.set(data[4]),
    #     self.var_attend.set(data[5])    
    # #=========================================Update CSV============================

    # # export upadte
    # def action(self):
    #     if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
    #         messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(user='root',host='localhost',password="kamil@2003",database='face_recognition',port=3306,auth_plugin = "mysql_native_password")
    #             mycursor = conn.cursor()
    #             mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s)",(
    #             self.var_id.get(),
    #             self.var_roll.get(),
    #             self.var_name.get(),
    #             self.var_time.get(),
    #             self.var_date.get(),
    #             self.var_attend.get()
    #             ))

    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)






    #     conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
    #     mycursor = conn.cursor()
    #     if messagebox.askyesno("Confirmation","Are you sure you want to save attendance on database?"):
    #         for i in mydata:
    #             uid = i[0]
    #             uroll = i[1]
    #             uname = i[2]
    #             utime = i[3]
    #             udate = i[4]
    #             uattend = i[5]
    #             qury = "INSERT INTO stdattendance(std_id, std_roll_no, std_name, std_time, std_date, std_attendance) VALUES(%s,%s,%s,%s,%s,%s)"
    #             mycursor.execute(qury,(uid,uroll,uname,utime,udate,uattend))
    #         conn.commit()
    #         conn.close()
    #         messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
    #     else:
    #         return False




        # 









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()