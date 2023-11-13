from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# # This part is image labels setting start 
        # first header image  
        title_lb1 = Label(self.root,text="Help Desk",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1650,height=45)
#         # backgorund image 
        bg1=Image.open(r"college_images\help.jpeg")
        bg1=bg1.resize((1540,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        f_lbl = Label(self.root,image=self.photobg1)
        f_lbl.place(x=0,y=55,width=1540,height=768)

        dev_lbl=Label(f_lbl,text="Email:kamilhayat27@gmail.com",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        dev_lbl.place(x=400,y=60)

       


      

        


        






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()