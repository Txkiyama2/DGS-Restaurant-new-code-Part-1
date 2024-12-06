from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win



class DGS_RestaurantReservationSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("DGS Restaurant Reservation System")
        self.root.geometry("1550x800+0+0")

        # ===============First image===============
        img1=Image.open(r"C:\Users\Client 04\DGS_Restaurant_Reservation_System\All Image\Restaurant.png")
        img1=img1.resize((1550,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # ===============Logo===============
        img2=Image.open(r"C:\Users\Client 04\DGS_Restaurant_Reservation_System\All Image\DGS.png")
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        # ===============Title===============
        lbl_title=Label(self.root,text="DGS RESTAURANT RESERVATION SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # ===============Main Frame===============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        
        # ===============Menu===============
        lbl_menu=Label(main_frame, text="MENU", font=("times new roman", 20, "bold"),bg="black",fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        # ===============btn Frame===============
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)
        
        Cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22, font=("times new roman",14,"bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        Cust_btn.grid(row=0,column=0,pady=1)

        Table_btn=Button(btn_frame,text="TABLE",width=22, font=("times new roman",14,"bold"),bg="black", fg="gold", bd=0,cursor="hand2")
        Table_btn.grid(row=1,column=0,pady=1)

        Details_btn=Button(btn_frame,text="DETAILS",width=22, font=("times new roman",14,"bold"),bg="black", fg="gold", bd=0,cursor="hand2")
        Details_btn.grid(row=2,column=0,pady=1)

        Report_btn=Button(btn_frame,text="REPORT",width=22, font=("times new roman",14,"bold"),bg="black", fg="gold", bd=0,cursor="hand2")
        Report_btn.grid(row=3,column=0,pady=1)

        Logout_btn=Button(btn_frame,text="LOGOUT",width=22, font=("times new roman",14,"bold"),bg="black", fg="gold", bd=0,cursor="hand2")
        Logout_btn.grid(row=4,column=0,pady=1)

        
        # ===============Right side image===============
        img3=Image.open(r"C:\Users\Client 04\DGS_Restaurant_Reservation_System\All Image\Restaurantfront.png")
        img3=img3.resize((1350,650),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=1,width=1350,height=650)

        # ===============down side image===============
        img4=Image.open(r"C:\Users\Client 04\DGS_Restaurant_Reservation_System\All Image\Table.png")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=225,width=230,height=210)
    
        # ===============down side image===============
        img5=Image.open(r"C:\Users\Client 04\DGS_Restaurant_Reservation_System\All Image\FOOD MENUS.png")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=420,width=230,height=190)
    
    def cust_details(self):
        self.new__window=Toplevel(self.root)
        self.app=Cust_Win(self.new__window)




if __name__ == "__main__":
    root=Tk()
    obj=DGS_RestaurantReservationSystem(root)
    root.mainloop()