from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Pannel")

        #-----------Variables-------------------
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()

#     # This part is image labels setting start 
        img=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\banner.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)

        # second header image  
        img1=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\tony.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)


        # third header image  
        img2=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\kids.jpg")
        img2=img2.resize((560,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=560,height=130)

        bg1=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\bg.jpg")
        bg1=bg1.resize((1540,710),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1540,height=710)

        title_lb1 = Label(bg_img,text="STUDENT REGISTRATION SYSTEM",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1650,height=45)

#         # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white")  
        main_frame.place(x=20,y=50,width=1480,height=580)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=540)

       
         # Current Course 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
        current_course_frame.place(x=10,y=5,width=635,height=150)

         #label Department
        dep_label=Label(current_course_frame,text="Department",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

         #combo box 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","CSEAI","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)


         #-------------------------------------------------------------

        #label Year
        year_label=Label(current_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2019-23","2020-24","2021-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)

         #-----------------------------------------------------------------

        #label Semester 
        year_label=Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=2,padx=5,sticky=W)

        #combo box 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)

         #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=10,y=160,width=635,height=200)

        #Student id
        studentId_label = Label(class_Student_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student name
        student_name_label = Label(class_Student_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)


         #Roll No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Gender
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        #combo box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

         #Date of Birth
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

         #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Phone Number
        student_mob_label = Label(class_Student_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Address
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)


         #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=380,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=7,font=("verdana",12,"bold"),fg="white",bg="gray",cursor="hand2")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=7,font=("verdana",12,"bold"),fg="white",bg="gray",cursor="hand2")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

         #delete button
        del_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=7,font=("verdana",12,"bold"),fg="white",bg="gray",cursor="hand2")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=7,font=("verdana",12,"bold"),fg="white",bg="gray",cursor="hand2")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,text="Take Pic",command=self.generate_dataset,width=9,font=("verdana",12,"bold"),fg="white",bg="gray",cursor="hand2")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #update photo button
        update_photo_btn=Button(btn_frame,text="Update Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="gray",cursor="hand2")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)





#         #----------------------------------------------------------------------
#         # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=710,y=10,width=720,height=540)

#         #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=695,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll-No","PHONE-NO","STD-ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="gray")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="gray")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

#         # -----------------------------Table Frame-------------------------------------------------
#         #Table Frame 
#         #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=695,height=360)

#         #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

#         #create table 
        self.student_table = ttk.Treeview(table_frame,column=("dep","year","sem","id","name","roll","gender","dob","email","phone","address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("Photo",text="PhotoSample")
        self.student_table["show"]="headings"


#         # Set Width of Colums 
        self.student_table.column("dep",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("Photo",width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# # ==================Function Decleration==============================
    def add_data(self):
        if self.var_dep.get()=="Select Department"  or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()==""or self.var_std_name.get()=="" or self.var_gender.get()=="Select Gender" or   self.var_roll.get()=="" or self.var_email.get()=="" or self.var_dob.get()==""   or self.var_address.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            
            try:
                conn = mysql.connector.connect(user='root',host='localhost',password="kamil@2003",database='face_recognition',port=3306,auth_plugin = "mysql_native_password")
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

# Fetching data form database to table 

    def fetch_data(self):
        conn=mysql.connector.connect(user='root',host='localhost',password="kamil@2003",database='face_recognition',port=3306,auth_plugin = "mysql_native_password")
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# get cursor function to change data

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_mob.set(data[9]),
        self.var_email.set(data[8]),
        self.var_dob.set(data[7]),
        self.var_address.set(data[10]),
        self.var_radio1.set(data[11])


#   Update data
    def update_data(self):
        if self.var_dep.get()=="Select Department"  or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()==""or self.var_std_name.get()=="" or self.var_gender.get()=="Select Gender" or   self.var_roll.get()=="" or self.var_email.get()=="" or self.var_dob.get()==""   or self.var_address.get()=="" or self.var_mob.get()=="":
    
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn=mysql.connector.connect(user='root',host='localhost',password="kamil@2003",database='face_recognition',port=3306,auth_plugin = "mysql_native_password")
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Dep=%s,Year=%s,Semester=%s, Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",( 
                self.var_dep.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_radio1.get(),   
                self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
#     #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(user='root',host='localhost',password="kamil@2003",database='face_recognition',port=3306,auth_plugin = "mysql_native_password")
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

#     # Reset Function 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_radio1.set("")
    
    # ===========================Search Data===================
    # def search_data(self):
    #     if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
    #         messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
    #             my_cursor = conn.cursor()
    #             sql = "SELECT Student_ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
    #             my_cursor.execute(sql)
    #             # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
    #             rows=my_cursor.fetchall()        
    #             if len(rows)!=0:
    #                 self.student_table.delete(*self.student_table.get_children())
    #                 for i in rows:
    #                     self.student_table.insert("",END,values=i)
    #                 if rows==None:
    #                     messagebox.showerror("Error","Data Not Found",parent=self.root)
    #                     conn.commit()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


# #=====================This part is related to Opencv Camera part=======================
# # ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"  or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()==""or self.var_std_name.get()=="" or self.var_gender.get()=="Select Gender" or   self.var_roll.get()=="" or self.var_email.get()=="" or self.var_dob.get()==""   or self.var_address.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn=mysql.connector.connect(user='root',host='localhost',password="kamil@2003",database='face_recognition',port=3306,auth_plugin = "mysql_native_password")
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Dep=%s,Year=%s,Semester=%s, Name=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",( 
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/stdudent."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  


# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()