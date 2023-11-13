from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport
import tkinter
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogonition System")

# This part is image labels setting start 
        # first header image  
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

        # backgorund image 
        bg1=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\bg.jpg")
        bg1=bg1.resize((1540,710),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1540,height=710)


        # title section
        title_lb1 = Label(bg_img,text="Attendence Managment System Using Facial Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1650,height=45)

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text= string)
            lbl.after(1000, time)

        lbl=Label(title_lb1,font=("verdana",10,"bold"),bg="white",fg="navyblue")
        lbl.place(x=0,y=0,width=110, height=50)
        time()
        # Create buttons below the section 
         
        # student button 1
        std_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\student.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.photostd_img_btn=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.photostd_img_btn,command=self.student_pannels, cursor="hand2")
        std_b1.place(x=200,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,text="Student Details",command=self.student_pannels, cursor="hand2",font=("verdana",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=200,y=280,width=180,height=45)

        # Detect Face  button 
        det_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\face.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.photodet_img_btn=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,image=self.photodet_img_btn, cursor="hand2",command=self.face_rec)
        det_b1.place(x=500,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Face Detector", cursor="hand2",command=self.face_rec,font=("verdana",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=500,y=280,width=180,height=45)

         # Attendence System  button 3
        att_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.photoatt_img_btn=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.photoatt_img_btn,cursor="hand2",command=self.attendence_pannel)
        att_b1.place(x=800,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Attendence",cursor="hand2",command=self.attendence_pannel,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=800,y=280,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\help.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.photohlp_img_btn=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.photohlp_img_btn,cursor="hand2",command=self.helpSupport)
        hlp_b1.place(x=1100,y=100,width=180,height=180)

        hlp_b1_1 = Button(bg_img,text="Help Support",cursor="hand2",command=self.helpSupport,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1100,y=280,width=180,height=45)

#         # Top 4 buttons end.......
#         # ---------------------------------------------------------------------------------------------------------------------------
#         # Start below buttons.........
#          # Train   button 5
        tra_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\di.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        self.phototra_img_btn=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,image=self.phototra_img_btn,cursor="hand2",command=self.train_pannels)
        tra_b1.place(x=200,y=380,width=180,height=180)

        tra_b1_1 = Button(bg_img,text="Data Train",cursor="hand2",command=self.train_pannels,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=200,y=560,width=180,height=45)

#         # Photo   button 6
        pho_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\phots.jpg")
        pho_img_btn=pho_img_btn.resize((180,180),Image.LANCZOS)
        self.photopho_img_btn=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,image=self.photopho_img_btn,cursor="hand2",command=self.open_img)
        pho_b1.place(x=500,y=380,width=180,height=180)

        pho_b1_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=500,y=560,width=180,height=45)

# #         # Developers   button 7
        dev_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\developerk.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.LANCZOS)
        self.photodev_img_btn=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,image=self.photodev_img_btn,cursor="hand2",command=self.developer)
        dev_b1.place(x=800,y=380,width=180,height=180)

        dev_b1_1 = Button(bg_img,text="Developers",cursor="hand2",command=self.developer,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=800,y=560,width=180,height=45)

# # #         # exit   button 8
        exi_img_btn=Image.open(r"C:\Users\kamil\Desktop\attendence_using_face\college_images\exit.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
        self.photoexi_img_btn=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,image=self.photoexi_img_btn,cursor="hand2",command=self.iExit)
        exi_b1.place(x=1100,y=380,width=180,height=180)

        exi_b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=1100,y=560,width=180,height=45)

# # ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Are you sure want to exit",parent=self.root)
        if self.iExit > 0 :
            self.root.destroy()
        else:
            return
# # ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendence_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

 
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
