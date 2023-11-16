from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk,Image
window=Tk()
window.geometry("600x600")
window.title("Banking system GUI App of Nyan Linn Htet")
window.configure(bg='light blue')
class BankMain():
    def __init__(Na,Am,Ad,pi):
        db=len(Userlist)
        to_insert={db:{'name':Na,'amount':Am,'address':Ad,'pin':pi}}
        Userlist.update(to_insert)
        messagebox.showinfo('Registerlist','New Account created successful!\n'"______Please attention______\nDon't forget Name or Pin!.Have a nice day!{}".format(Userlist))
        window.deiconify()
        second.withdraw()

class Withdraw:
    def __init__(self):
        signal2=0
        for x in range(len(Userlist)):
            if Userlist[x]['name']==dewname.get():
                if Userlist[x]['amount']>int(dewithdraw.get()):
                    Userlist[x]['amount']-=int(dewithdraw.get())
                    messagebox.showinfo('Withdrawlist','Thank you for your withdraw!\n {}:{}'.format(Userlist[x]['name'],Userlist[x]['amount']))
                    Forth.withdraw()
                    window.deiconify()
                    signal2=1
                    break     
                elif Userlist[x]['amount']<int(dewithdraw.get()):
                    messagebox.showerror('Error','Your bank account have not enough for withdraw!\n __Please check up!')
                    break
        if signal2==0:
            messagebox.showerror('Error','Something wrong!\n ')
            Forth.deiconify()

class Deposit:
    def __init__(self):
        signal3=0
        for x in range(len(Userlist)):
                if Userlist[x]['name']==dename.get():
                    Userlist[x]['amount']+=int(deamount.get()) 
                    messagebox.showinfo('Depositlist','Thank you for your deposit \n {}:{}'.format(Userlist[x]['name'],Userlist[x]['amount']))
                    Third.withdraw()
                    window.deiconify()
                    signal3=1
                    break
        if signal3==0:
            messagebox.showerror('Error','This name have not in this list!')
            Third.deiconify()

class Removelist(Withdraw):
    def __init__(self):
        # if deremove.get() == name.get():
        signal1=0
        for x in range(len(Userlist)):
                if Userlist[x]['name']==deremove.get():
                    Userlist.pop(x)
                    messagebox.showinfo('Removelist','We have been remove your register account!')
                    Fiveth.withdraw()
                    window.deiconify()
                    signal1=1
                    break
        if signal1 == 0:
            messagebox.showerror('Error',"This '{}' name have not in program!".format(deremove.get()))
            Fiveth.withdraw()
            window.deiconify()
       
class Checklist(Removelist):
    def __init__(self):
        signal=0
        for i in range(len(Userlist)):
            if decheck.get() == Userlist[i]['name'] and int(decheckpin.get()) == Userlist[i]['pin']:
                messagebox.showinfo('Checkinglist','{}\n "This is your Register list!"'.format(Userlist[i]))
                Sixth.withdraw()
                window.deiconify()
                signal=1
                break
        if signal == 0:
            messagebox.showerror('Error',"You are wrong something name or pin!")
            Sixth.deiconify()
            
class Controlpin:
        def user():
            BankMain.__init__(listName.get(),int(listAmount.get()),listAddress.get(),int(listPin.get()))
        
        def backacc():
            second.withdraw()
            window.deiconify()   

        def username():
            global listName,listAmount,listAddress,listPin,second
            second=Tk()
            window.withdraw()
            second.geometry("600x600")
            second.configure(bg='light blue')
            lbl1=Label(second,text="•♥•.¸¸.•♥•.¸¸.•♥•Register•♥•.¸¸.•♥•.¸¸.•♥•",font=('Ariel',10),background='light blue')
            lbl1.place(x=190, y=80)
            lbl2=Label(second,text='Customer_name:',font=('Ariel',10),background='light blue')
            lbl2.place(x=150,y=150)
            listName=Entry(second,width=30)
            listName.place(x=300,y=150)
            lbl3=Label(second,text='Customer_amount:',font=('Ariel',10),background='light blue')
            lbl3.place(x=150,y=250)
            listAmount=Entry(second,width=30)
            listAmount.place(x=300,y=250)
            lbl4=Label(second,text='Customer_address:',font=('Ariel',10),background='light blue')
            lbl4.place(x=150,y=350)
            listAddress=Entry(second,width=30)
            listAddress.place(x=300,y=350)
            lbl5=Label(second,text='Customer_pin:',font=('Ariel',10),background='light blue')
            lbl5.place(x=150,y=450)
            listPin=Entry(second,width=30)
            listPin.place(x=300,y=450)
            userallbtn=Button(second,text='Send',command=Controlpin.user)
            userallbtn.place(x=250,y=500,height=50,width=50)
            userbackbtn=Button(second,text='Back',command=Controlpin.backacc)
            userbackbtn.place(x=350,y=500,height=50,width=50)

class Checkpin:
        def userwamount():
            Checklist.__init__(Checklist)
        
        def backacc():
            Sixth.withdraw()
            window.deiconify()    

            
        def usercheck():
            global decheck,decheckpin,Sixth
            Sixth=Tk()
            window.withdraw()
            Sixth.geometry("600x600")
            Sixth.configure(bg='light blue')
            lbl1=Label(Sixth,text="•♥•.¸¸.•♥•.¸¸.•♥•Check•♥•.¸¸.•♥•.¸¸.•♥•",font=('Ariel',10),background='light blue')
            lbl1.place(x=190, y=80)
            # lbl1=Label(Sixth,text="If you are leave this program,you type 'end'!",font=('Ariel',10),background='light blue')
            # lbl1.place(x=190, y=120)
            lbl3=Label(Sixth,text='Customer_Name:',font=('Ariel',10),background='light blue')
            lbl3.place(x=150,y=200)
            decheck=Entry(Sixth,width=30)
            decheck.place(x=300,y=200)
            lbl3=Label(Sixth,text='Customer_pin:',font=('Ariel',10),background='light blue')
            lbl3.place(x=150,y=250)
            decheckpin=Entry(Sixth,width=30)
            decheckpin.place(x=300,y=250)
            usercheckbtn=Button(Sixth,text='Send',command=Checkpin.userwamount)
            usercheckbtn.place(x=250,y=300,height=50,width=50)
            userbackbtn=Button(Sixth,text='Back',command=Checkpin.backacc)
            userbackbtn.place(x=250,y=500,height=50,width=50)
class Removepin:
        def userwamount():
                Removelist.__init__(Removelist)
    
        def backacc():
            Fiveth.withdraw()
            window.deiconify()    

        def userremove():
            global deremove,Fiveth
            Fiveth=Tk()
            window.withdraw()
            Fiveth.geometry("600x600")
            Fiveth.configure(bg='light blue')
            lbl1=Label(Fiveth,text="•♥•.¸¸.•♥•.¸¸.•♥•Remove•♥•.¸¸.•♥•.¸¸.•♥•",font=('Ariel',10),background='light blue')
            lbl1.place(x=190, y=80)
            lbl3=Label(Fiveth,text='Customer_Name:',font=('Ariel',10),background='light blue')
            lbl3.place(x=150,y=200)
            deremove=Entry(Fiveth,width=30)
            deremove.place(x=300,y=200)
            userremovebtn=Button(Fiveth,text='Send',command=Removepin.userwamount)
            userremovebtn.place(x=250,y=300,height=50,width=50)
            userbackbtn=Button(Fiveth,text='Back',command=Removepin.backacc)
            userbackbtn.place(x=250,y=500,height=50,width=50)
            
class Withdrawpin:
        def userwamount():
                Withdraw.__init__(Withdraw)
            
        def backacc():
            Forth.withdraw()
            window.deiconify()  

        def userwithdraw():
            global dewithdraw,Forth,dewname
            Forth=Tk()
            window.withdraw()
            Forth.geometry("600x600")
            Forth.configure(bg='light blue')
            lbl1=Label(Forth,text="•♥•.¸¸.•♥•.¸¸.•♥•Withdraw•♥•.¸¸.•♥•.¸¸.•♥•",font=('Ariel',10),background='light blue')
            lbl1.place(x=190, y=80)
            lbl2=Label(Forth,text='Customer_name:',font=('Ariel',10),background='light blue')
            lbl2.place(x=150,y=150)
            dewname=Entry(Forth,width=30)
            dewname.place(x=300,y=150)
            lbl3=Label(Forth,text='Customer_withdraw:',font=('Ariel',10),background='light blue')
            lbl3.place(x=150,y=200)
            dewithdraw=Entry(Forth,width=30)
            dewithdraw.place(x=300,y=200)
            userwithbtn=Button(Forth,text='Send',command=Withdrawpin.userwamount)
            userwithbtn.place(x=250,y=300,height=50,width=50)
            userbackbtn=Button(Forth,text='Back',command=Withdrawpin.backacc)
            userbackbtn.place(x=250,y=500,height=50,width=50)

class Depositpin:
        def useramount():
            Deposit.__init__(Deposit)

        def backacc():
            Third.withdraw()
            window.deiconify()

        def userdeposit():
            global deamount,Third,dename
            Third=Tk()
            window.withdraw()
            Third.geometry("600x600")
            Third.configure(bg='light blue')
            lbl1=Label(Third,text="•♥•.¸¸.•♥•.¸¸.•♥•Deposit•♥•.¸¸.•♥•.¸¸.•♥•",font=('Ariel',10),background='light blue')
            lbl1.place(x=190, y=80)
            lbl2=Label(Third,text='Customer_name:',font=('Ariel',10),background='light blue')
            lbl2.place(x=150,y=150)
            dename=Entry(Third,width=30)
            dename.place(x=300,y=150)
            lbl3=Label(Third,text='Customer_deposit:',font=('Ariel',10),background='light blue')
            lbl3.place(x=150,y=200)
            deamount=Entry(Third,width=30)
            deamount.place(x=300,y=200)
            userdepobtn=Button(Third,text='Send',command=Depositpin.useramount)
            userdepobtn.place(x=250,y=300,height=50,width=50)
            userbackbtn=Button(Third,text='Back',command=Depositpin.backacc)
            userbackbtn.place(x=250,y=500,height=50,width=50)

class Main:
        def ending():
            messagebox.showinfo('Banking system info','Good Bye Guys!\n Have a nice day!')
            window.withdraw()
        lbl=Label(text= "                   '______Welcome our banking system!________'\n"
                            "                      1.If you wanna create new account!\n"
                            "                      2.If you wanna deposit bank account!\n"
                            "                      3.If you wanna withdraw from bank account!\n"
                            "                      4.If you wanna delete your bank account!\n"
                            "                      5.If you wanna checking  your Register account!\n"
                            "                      6.If you wanna end this banking system program!\n"
                            "                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n"
                            "                       •♥•.¸¸.•♥•.¸¸.•♥•Main Menu•♥•.¸¸.•♥•.¸¸.•♥•\n",font=('Ariel',11),background='light blue')
        
        lbl.place(x=70, y=140)
        userbtn=Button(text=1,command=Controlpin.username)
        userbtn.place(x=60,y=330,height=35,width=35)
        userbtn=Button(text=2,command=Depositpin.userdeposit)
        userbtn.place(x=150,y=330,height=35,width=35)
        userbtn=Button(text=3,command=Withdrawpin.userwithdraw)
        userbtn.place(x=240,y=330,height=35,width=35)
        userbtn=Button(text=4,command=Removepin.userremove)
        userbtn.place(x=330,y=330,height=35,width=35)
        userbtn=Button(text=5,command=Checkpin.usercheck)
        userbtn.place(x=420,y=330,height=35,width=35)
        userbtn=Button(text=6,command=ending)
        userbtn.place(x=510,y=330,height=35,width=35)
        my_img=ImageTk.PhotoImage(Image.open('image.png'))
        lbl=Label(image=my_img,background='light blue')
        lbl.place(x=280, y=400)
        lbl=Label(text="Please attention : Next new features will come to this banking system.\n Coming soon we will come back the best."
                  ,font=('Ariel',10),background='light blue')
        lbl.place(x=80, y=450)
        
Userlist={}
Userpin={}
window.mainloop()
