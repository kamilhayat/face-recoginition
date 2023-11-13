from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Pannel")

#         # This part is image labels setting start 
#         # first header image  
     


        #title section
        title_lb1 = Label(self.root,text="Welcome to Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"college_images\facialrecognition.png")
        img_top = img_top.resize((1540, 300), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1540,height=300)

#         # Create buttons below the section 
#         # ------------------------------------------------------------------------------------------------------------------- 
#         # Training button 1
        

        b1_1 = Button(self.root,text="Train Dataset",cursor="hand2",command=self.train_classifier,font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=0,y=355,width=1530,height=45)

        img_bottom=Image.open(r"college_images\ai.jpeg")
        img_bottom=img_bottom.resize((1530,380),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=400,width=1530,height=380)

#     # ==================Create Function of Traing===================
#   using lbph alogo(local binary pattern histogram )
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()