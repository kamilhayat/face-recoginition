from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# # This part is image labels setting start 
#         # title section
        title_lb1 = Label(self.root,text="Developer",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1650,height=45)
#         # backgorund image 
        bg1=Image.open(r"college_images\dev.jpg")
        bg1=bg1.resize((1540,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        f_lbl = Label(self.root,image=self.photobg1)
        f_lbl.place(x=0,y=55,width=1430,height=768)


        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=500,height=500)

        bg1_1=Image.open(r"college_images\developer.jpg")
        bg1_1=bg1_1.resize((200,200),Image.ANTIALIAS)
        self.photobg1_1=ImageTk.PhotoImage(bg1_1)

        f_lbl_1 = Label(self.root,image=self.photobg1_1)
        f_lbl_1.place(x=0,y=55,width=150,height=150)



        std_b1_1 = Label(f_lbl,text="Hi My name is, Kamil Hayat",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1.place(x=155,y=0)

        std_b1_1 = Label(f_lbl,text="I'm a Full Stack Web Developer",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1.place(x=150,y=30)
        
        std_b1_1_1 = Label(f_lbl,text="and a passonaite web developer ",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1_1.place(x=150,y=60)

        std_b1_1_1_1 = Label(f_lbl,text="with more than 1 year of",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1_1_1.place(x=150,y=90)

        std_b1_1_1 = Label(f_lbl,text="experience.",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1_1.place(x=150,y=120)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()