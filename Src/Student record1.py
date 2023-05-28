from Tkinter import *
import os
import sqlite3
from tkMessageBox import *
import pandas as pd
con=sqlite3.Connection('student_record')
cur=con.cursor()


dtarray1=[]
dtarray2=[]
dtarray3=[]
dtarray4=[]
dtarray5=[]
dtarray6=[]
dtarray7=[]
dtarray8=[]
dtarray9=[]
dtarray10=[]
dtarray11=[]
dtarray12=[]
dtarray13=[]
dtarray14=[]
dtarray15=[]
dtarray16=[]
dtarray17=[]
dtarrayA=[]
dtarrayB=[]
dtarrayC=[]
dtarrayD=[]



window=Tk()
window.geometry('1280x600')
window.title('Start Window')

a=PhotoImage(file='pic 1.gif')
Label(window,image=a).place(x=1,y=0)


def start():
    window=Toplevel()
    window.geometry('1080x600')
    window.title('Login Window')
    Label(window,text='Username  ',font=("Times New",20)).grid(row=1,column=1)                                 #v=id
    v=Entry(window,width=25,font=("Times New",18),bd=5,bg="light grey")
    v.grid(row=1,column=2)
    Label(window,text='Password  ',font=("Times n=New",20)).grid(row=2,column=1)
    vv=Entry(window,show='*',width=25,font=("Times New",18),bd=5,bg="light grey")                                                                                       #vv=password
    vv.grid(row=2,column=2)

    mode=StringVar(window)                                                       #mode=mode of login.
    mode.set("Select Mode") # default value
    var = OptionMenu(window,mode, "Faculty Mode", "Student Mode")
    var.grid(row=2,column=4)

    def login():
        if(((int(v.get())!=123) or (int(vv.get())!=123)) and (mode.get()!="Select Mode")):                     #make for mode
            showwarning('Login Failed','wrong Password Used Or Mode Not Selected')
        else:
            menu = Toplevel()
            menu.geometry('1080x600')
            menu.title('Menu Window')

            l=Label(menu,text='Dashboard :',font='Times 20 bold')
            l.grid(row=0,column=0)
            apx=PhotoImage(file='p2.gif')
            Label(menu,image=apx).grid(row=1,column=100,rowspan=30)
###############################################################################################################################################
            if(mode.get()=="Faculty Mode"):
                showinfo('Notice','Teachers please Update Marks of Students before -----')
            else:
                showinfo('Notice','Students Results will be Uploaded on ------')
            def option1():
                if(mode.get()=="Faculty Mode"):
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('Register Students Details')
                    l=Label(root,text='Register Student Details :',font='Times 20 bold')
                    l.grid(row=0,column=3)
                    
                    l=Label(root,text=' ')
                    l.grid(row=1,column=0)

                    l=Label(root,text='Enter Student ID : ')
                    l.grid(row=2,column=0)
                    
                    c=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                      #c=sid
                    c.grid(row=2,column=1)
                    xp=c.get()
                    
                    l=Label(root,text='Enter first name : ')
                    l.grid(row=3,column=0)
                    d=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                         #d=fname
                    d.grid(row=3,column=1)
                    l=Label(root,text='Enter last name : ')
                    l.grid(row=4,column=0)
                    e=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                      #e=lname
                    e.grid(row=4,column=1)
                    l=Label(root,text='Enter class : ')
                    l.grid(row=5,column=0)

                    f=StringVar(root)                                                       #f=class no.
                    f.set("Select class") # default value
                    w = OptionMenu(root,f, "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12")
                    w.grid(row=5,column=1)

                    l=Label(root,text='Enter total marks : ')
                    l.grid(row=6,column=0)
                    q=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                            #q=total marks
                    q.grid(row=6,column=1)
                    
                    
                    cur.execute("create table if not exists student(sid number primary key, fname varchar(20), lname varchar(20), clno number(4), yearduemarks number(6), eng_at number(4), hin_at number(4), mat_at number(4), sc_at number(4), ssc_at number(4), san_at number(4), eng_m number(4), hin_m number(4), mat_m number(4), sc_m number(4), ssc_m number(4), san_m number(4))")
                    def insertinstudent():
                        cur.execute("select * from student where sid=?",(int(c.get()),))
                        cpy=cur.fetchone()
                        try:
                            cur.execute("insert into student values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(int(c.get()),d.get(),e.get(),f.get(),int(q.get()),0,0,0,0,0,0,0,0,0,0,0,0))
                            con.commit()
                            showinfo('Information','Student Insertion Successful')
###################################################     PANDAS            ####################################################
                            dtarray1.append(int(c.get()))
                            dtarray2.append(d.get())
                            dtarray3.append(e.get())
                            dtarray4.append(f.get())
                            dtarray5.append(int(q.get()))
                            

                            df1 = pd.DataFrame({'Student Id': dtarray1,'First Name':dtarray2,'Last Name':dtarray3,'Class':dtarray4,'Yearly Due marks':dtarray5})#,'Attendance In English':dtarray6,'Attendance In Hindi':dtarray7,'Attendance In Math':dtarray8,'Attendance In Science':dtarray9,'Attendance In SST':dtarray10,'Attendance In Sanskrit':dtarray11,'Marks In English':dtarray12,'Marks In Hindi':dtarray13,'Marks In Math':dtarray14,'Marks In Science':dtarray15,'Marks In SSt':dtarray16,'Marks In Sanskrit':dtarray17})
                            writer = pd.ExcelWriter('C:\\Users\\ASUS\\Desktop\\Project\\Student_Details.xlsx', engine='xlsxwriter')
                            df1.to_excel(writer, sheet_name='Sheet1')
                            writer.save()
                            
###################################################     PANDAS            #############################################################                                                        
                        except sqlite3.IntegrityError as error:
                            showwarning('Error','Already exists!')
            

                    
                    Button(root,text='Insert Data Of Student',command=insertinstudent,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column =0,sticky=N+S+E+W)
                    
                    def logout():
                         ans=askyesno('Confirmation', 'Do You Want To Exit?')
                         if(ans==True):
                             root.destroy()
                    Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0,sticky=N+S+E+W)
                    root.mainloop()
                else:
                      showerror('Information','Access Denied')
            
            Button(menu,text='Register Student details',command=option1,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=1,column=0,sticky=N+S+E+W)
##############################################################################################################################################
            def option2():
                root = Toplevel()
                root.geometry('1080x600')
                root.title('Student Details View')
                l=Label(root,text='View Student Details :',font='Times 20 bold')
                l.grid(row=0,column=3)
                l=Label(root,text=' ')
                l.grid(row=1,column=0)

                l=Label(root,text='Enter Student Id : ')
                l.grid(row=2,column=0)
                ui=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                    #ui=sid
                ui.grid(row=2,column=1)
                
                l=Label(root,text='Enter class : ')
                l.grid(row=4,column=0)
                f=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                        #f=clno.
                f.grid(row=4,column=1)
                def show1():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    val=[(int(ui.get()))]
                    row_number=0
                    Label(root, text = "Student ID").grid(column=1,row = row_number)
                    Label(root, text = "First Name").grid(column=2,row = row_number)
                    Label(root, text = "Last Name").grid(column=3,row = row_number)
                    Label(root, text = "Class No.").grid(column=4,row = row_number)
                    Label(root, text = "Year Due marks").grid(column=5,row = row_number)
                    

                    z=cur.execute("select *from student where sid=?",val)
                    for row_number,row in enumerate(z):
                        Label(root, text = "" + str(row[0])).grid(column=1,row = row_number+1)
                        Label(root, text = "" + str(row[1])).grid(column=2,row = row_number+1)
                        Label(root, text = "" + str(row[2])).grid(column=3,row = row_number+1)
                        Label(root, text = "" + str(row[3])).grid(column=4,row = row_number+1)
                        Label(root, text = "" + str(row[4])).grid(column=5,row = row_number+1)
                        
                    root.mainloop()
                Button(root,text='Show Student Data',command=show1,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column =2,sticky=N+S+E+W)
####
                def show2():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    v=[(f.get())]
                    z=cur.execute("select *from student where clno=?",v)
                    Label(root, text = "Student ID").grid(column=0,row=0)
                    Label(root, text = "First Name").grid(column=1,row=0)
                    Label(root, text = "Last Name").grid(column=2,row=0)
                    Label(root, text = "Class No.").grid(column=3,row=0)
                    Label(root, text = "Year Due marks").grid(column=4,row=0)
                   
                    y=-1
                    for row_number,row in enumerate(z):
                        y=y+1
                        Label(root, text = "" + str(row[0])).grid(column=0,row = row_number+1+y)
                        Label(root, text = "" + str(row[1])).grid(column=1,row = row_number+1+y)
                        Label(root, text = "" + str(row[2])).grid(column=2,row = row_number+1+y)
                        Label(root, text = "" + str(row[3])).grid(column=3,row = row_number+1+y)
                        Label(root, text = "" + str(row[4])).grid(column=4,row = row_number+1+y)
                        
                    root.mainloop()
                Button(root,text='Show All Student Data Of Class',command=show2,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=4,column =2,sticky=N+S+E+W)
                
####
                def delete2():
                    if(mode.get()=="Faculty Mode"):
                        cur.execute("drop table student")
                        showinfo('Information','Student Deletion Successful')
                    else:
                        showerror('Information','Access Denied')
                Button(root,text='Delete All Student Data',command=delete2,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column =0,sticky=N+S+E+W)
                def logout():
                    ans=askyesno('Confirmation', 'Do You Want To Exit?')
                    if(ans==True):
                        root.destroy()
                Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0,sticky=N+S+E+W)
                root.mainloop()
            Button(menu,text='View Student details',command=option2,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column=0,sticky=N+S+E+W)
###############################################################################################################################################
            def option3():
                if(mode.get()=="Faculty Mode"):
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('Student marks Updation')
                    l=Label(root,text='Student marks Updation :',font='Times 20 bold')
                    l.grid(row=0,column=3)
                    
                    l=Label(root,text=' ')
                    l.grid(row=1,column=0)

                    l=Label(root,text='Enter Student ID : ')
                    l.grid(row=2,column=0)
                    g=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                             #g=sid
                    g.grid(row=2,column=1)
                    l=Label(root,text='Enter marks paid : ')
                    l.grid(row=3,column=0)
                    h=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                                              #h=marks paid
                    h.grid(row=3,column=1)
                    def update1():
                        p=int(g.get())
                        cur.execute("update student set yearduemarks=yearduemarks-? where sid=?",(int(h.get()),p))
                        con.commit()
                        showinfo('Information','marks Updation Successful')

                     
                    Button(root,text='Update marks',command=update1,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=4,column =0,sticky=N+S+E+W)

                    l=Label(root,text=' ')
                    l.grid(row=5,column=0)

                    l=Label(root,text='Enter Student ID to see details : ')
                    l.grid(row=6,column=0)
                    i=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                                              #i=sid
                    i.grid(row=6,column=1)
                    def show3():
                        w=[(int(i.get()))]
                        cur.execute("select yearduemarks from student where sid=?",w)
                        x=cur.fetchall()
                        showinfo('Result',x)
                    Button(root,text='Show Student due marks ',command=show3,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column =0,sticky=N+S+E+W)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            root.destroy()
                    Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0)
                    root.mainloop()
                else:
                    showerror('Information','Access Denied')
            Button(menu,text='Student marks Updation',command=option3,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=3,column=0,sticky=N+S+E+W)
######################################################################################################################################################################

            def option4():
                if(mode.get()=="Faculty Mode"):
                    win = Toplevel()
                    win.geometry('1080x600')
                    win.title('Update Attendance')
                    #l=Label(win,text='Student Attendance Keeping System :',font='Times 20 bold')
                    #l.grid(row=0,column=0)
                    l=Label(win,text='Enter Student Id : ')
                    l.grid(row=2,column=0)
                    f=Entry(win,font=("Times New",10),bd=5,bg="light grey")                                                        #f=sid.
                    f.grid(row=2,column=1)

                    def fill():
                        v=[(f.get())]
                        
                        
                        Label(win, text = "English").grid(column=1,row = 3,sticky=N+S+E+W)
                        eng=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        eng.grid(row=4,column=1,sticky=N+S+E+W)
                            
                        Label(win, text = "Hindi").grid(column=2,row = 3,sticky=N+S+E+W)
                        hin=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        hin.grid(row=4,column=2,sticky=N+S+E+W)
                        
                        Label(win, text = "Mathematics").grid(column=3,row = 3,sticky=N+S+E+W)
                        mat=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        mat.grid(row=4,column=3,sticky=N+S+E+W)
                            
                        Label(win, text = "Science").grid(column=4,row = 3)
                        sc=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        sc.grid(row=4,column=4,sticky=N+S+E+W)
                         
                        Label(win, text = "Social Science").grid(column=5,row = 3,sticky=N+S+E+W)
                        ssc=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        ssc.grid(row=4,column=5,sticky=N+S+E+W)
                     
                        Label(win, text = "Sanskrit").grid(column=6,row = 3,sticky=N+S+E+W)
                        san=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        san.grid(row=4,column=6,sticky=N+S+E+W)
                            
                        def regist():
                            cur.execute("update student set eng_at=? where sid=?",(eng.get(),f.get()))
                            con.commit()
                            cur.execute("update student set hin_at=? where sid=?",(hin.get(),f.get()))
                            con.commit()
                            cur.execute("update student set mat_at=? where sid=?",(mat.get(),f.get()))
                            con.commit()
                            cur.execute("update student set sc_at=? where sid=?",(sc.get(),f.get()))
                            con.commit()
                            cur.execute("update student set ssc_at=? where sid=?",(ssc.get(),f.get()))
                            con.commit()
                            cur.execute("update student set san_at=? where sid=?",(san.get(),f.get()))
                            con.commit()
                            cur.execute("select fname from student where sid=?",(f.get()))
                            new=cur.fetchone()
                            showinfo('Information','Attendance Locked')

##############################################          PANDAS         #########################################################
                            dtarrayA.append(int(f.get()))
                            dtarray6.append(int(eng.get()))
                            dtarray7.append(int(hin.get()))
                            dtarray8.append(int(mat.get()))
                            dtarray9.append(int(sc.get()))
                            dtarray10.append(int(ssc.get()))
                            dtarray11.append(int(san.get()))
                            dtarrayC.append(str(new))
                            df2 = pd.DataFrame({'Student ID':dtarrayA,'Name':dtarrayC,'Attendance In English':dtarray6,'Attendance In Hindi':dtarray7,'Attendance In Math':dtarray8,'Attendance In Science':dtarray9,'Attendance In SST':dtarray10,'Attendance In Sanskrit':dtarray11})
                            writer = pd.ExcelWriter('C:\\Users\\ASUS\\Desktop\\Project\\Student_Attendance.xlsx', engine='xlsxwriter')
                            df2.to_excel(writer, sheet_name='Sheet1')
                            writer.save()

##############################################          PANDAS         #########################################################
                        Button(win,text='Submit',command=regist,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column =0)
                    Button(win,text='Show',command=fill,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column =2)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            win.destroy()
                    Button(win,text='Exit',command=logout,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column=3)
                    
                    win.mainloop()
                else:
                    showerror('Information','Access Denied')
            Button(menu,text='Update Attendance',command=option4,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=4,column=0,sticky=N+S+E+W)
#########################################################################################################################################
            def option5():
                root=Toplevel()
                root.geometry('1080x600')
                root.title('Attandence View')
                l=Label(root,text='Student Attendance View',font='Times 20 bold')
                l.grid(row=0,column=3)
                
                l=Label(root,text='')
                l.grid(row=1,column=0)

                l=Label(root,text='Enter Student ID : ')
                l.grid(row=2,column=0)
                stid=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")
                stid.grid(row=2,column=1)
                def show4():
                    root = Toplevel()
                    root.geometry('1080x600')
                    root.title('View Window')
                    row_number=0
                    Label(root, text = "English").grid(column=1,row = row_number)
                    Label(root, text = "Hindi").grid(column=2,row = row_number)
                    Label(root, text = "Mathematics").grid(column=3,row = row_number)
                    Label(root, text = "Science").grid(column=4,row = row_number)
                    Label(root, text = "Social Science").grid(column=5,row = row_number)
                    Label(root, text = "Sanskrit").grid(column=6,row = row_number)
                    
                    w=[(int(stid.get()))]
                    z=cur.execute("select eng_at,hin_at,mat_at,sc_at,ssc_at,san_at from student where sid=?",w)
                    for row_number,row in enumerate(z):
                        Label(root, text = "" + str(row[0])).grid(column=1,row = row_number+1)
                        Label(root, text = "" + str(row[1])).grid(column=2,row = row_number+1)
                        Label(root, text = "" + str(row[2])).grid(column=3,row = row_number+1)
                        Label(root, text = "" + str(row[3])).grid(column=4,row = row_number+1)
                        Label(root, text = "" + str(row[4])).grid(column=5,row = row_number+1)
                        Label(root, text = "" + str(row[5])).grid(column=6,row = row_number+1)
                    root.mainloop()
                Button(root,text='Show Student Attendance ',command=show4,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column =0,sticky=N+S+E+W)
                def logout():
                    ans=askyesno('Confirmation', 'Do You Want To Exit?')
                    if(ans==True):
                        root.destroy()
                Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0)
                root.mainloop()
            Button(menu,text='View Attendance',command=option5,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column=0,sticky=N+S+E+W)

#########################################################################################################################################
            def option6():
                if(mode.get()=="Faculty Mode"):
                    win=Toplevel()
                    win.geometry('1080x600')
                    win.title('Register Student Marks')
                    #l=Label(root,text='Student Marks Updation',font='Times 20 bold')
                    #l.grid(row=0,column=3)
                    l=Label(win,text='Enter Student Id : ')
                    l.grid(row=2,column=0)
                    f=Entry(win,font=("Times New",10),bd=5,bg="light grey")                                                        #f=sid.
                    f.grid(row=2,column=1)

                    def fill():
                        v=[(f.get())]

                        Label(win, text = "English").grid(column=1,row = 3,sticky=N+S+E+W)
                        eng=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        eng.grid(row=4,column=1,sticky=N+S+E+W)
                            
                        Label(win, text = "Hindi").grid(column=2,row = 3,sticky=N+S+E+W)
                        hin=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        hin.grid(row=4,column=2,sticky=N+S+E+W)
                        
                        Label(win, text = "Mathematics").grid(column=3,row = 3,sticky=N+S+E+W)
                        mat=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        mat.grid(row=4,column=3,sticky=N+S+E+W)
                            
                        Label(win, text = "Science").grid(column=4,row = 3)
                        sc=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        sc.grid(row=4,column=4,sticky=N+S+E+W)
                         
                        Label(win, text = "Social Science").grid(column=5,row = 3,sticky=N+S+E+W)
                        ssc=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        ssc.grid(row=4,column=5,sticky=N+S+E+W)
                     
                        Label(win, text = "Sanskrit").grid(column=6,row = 3,sticky=N+S+E+W)
                        san=Entry(win,width=15,font=("Times New",10),bd=5,bg="light grey")
                        san.grid(row=4,column=6,sticky=N+S+E+W)
                            
                        def regist():
                            cur.execute("update student set eng_m=? where sid=?",(eng.get(),f.get()))
                            con.commit()
                            cur.execute("update student set hin_m=? where sid=?",(hin.get(),f.get()))
                            con.commit()
                            cur.execute("update student set mat_m=? where sid=?",(mat.get(),f.get()))
                            con.commit()
                            cur.execute("update student set sc_m=? where sid=?",(sc.get(),f.get()))
                            con.commit()
                            cur.execute("update student set ssc_m=? where sid=?",(ssc.get(),f.get()))
                            con.commit()
                            cur.execute("update student set san_m=? where sid=?",(san.get(),f.get()))
                            con.commit()
                            cur.execute("select fname from student where sid=?",(f.get()))
                            new=cur.fetchone()
                            showinfo('Information','Attendance Locked')


##############################################          PANDAS         #########################################################
                            dtarrayB.append(int(f.get()))
                            dtarray12.append(int(eng.get()))
                            dtarray13.append(int(hin.get()))
                            dtarray14.append(int(mat.get()))
                            dtarray15.append(int(sc.get()))
                            dtarray16.append(int(ssc.get()))
                            dtarray17.append(int(san.get()))
                            dtarrayD.append(str(new))
                            df2 = pd.DataFrame({'Student ID':dtarrayA,'Name':dtarrayD,'Marks In English':dtarray12,'Marks In Hindi':dtarray13,'Marks In Math':dtarray14,'Marks In Science':dtarray15,'Marks In SST':dtarray16,'Marks In Sanskrit':dtarray17})
                            writer = pd.ExcelWriter('C:\\Users\\ASUS\\Desktop\\Project\\Student_Marks.xlsx', engine='xlsxwriter')
                            df2.to_excel(writer, sheet_name='Sheet1')
                            writer.save()

##############################################          PANDAS         #########################################################
                            
                        Button(win,text='Submit',command=regist,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=5,column =0)
                    Button(win,text='Show',command=fill,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column =2)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            win.destroy()
                    Button(win,text='Exit',command=logout,width=15,font=("Times New",10),bd=5,bg="light grey").grid(row=2,column=3)
                    
                    win.mainloop()
                else:
                    showerror('Information','Access Denied')
            Button(menu,text='Update Student Marks',command=option6,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=6,column=0,sticky=N+S+E+W)
#########################################################################################################################################
            def option7():
                    root=Toplevel()
                    root.geometry('1080x600')
                    root.title('Marks View')
                    #l=Label(root,text='Student Marks View',font='Times 20 bold')
                    #l.grid(row=0,column=3)

                    l=Label(root,text='Enter Student ID : ')
                    l.grid(row=2,column=0)
                    stid=Entry(root,width=25,font=("Times New",10),bd=5,bg="light grey")                   #stid=sid;
                    stid.grid(row=2,column=1)

                    def show4():
                        root = Toplevel()
                        root.geometry('1080x600')
                        root.title('View Window')
                        row_number=0
                        Label(root, text = "English").grid(column=1,row = row_number)
                        Label(root, text = "Hindi").grid(column=2,row = row_number)
                        Label(root, text = "Mathematics").grid(column=3,row = row_number)
                        Label(root, text = "Science").grid(column=4,row = row_number)
                        Label(root, text = "Social Science").grid(column=5,row = row_number)
                        Label(root, text = "Sanskrit").grid(column=6,row = row_number)
                        w=[(int(stid.get()))]
                        z=cur.execute("select eng_m,hin_m,mat_m,sc_m,ssc_m,san_m from student where sid=?",w)
                        for row_number,row in enumerate(z):
                            Label(root, text = "" + str(row[0])).grid(column=1,row = row_number+1)
                            Label(root, text = "" + str(row[1])).grid(column=2,row = row_number+1)
                            Label(root, text = "" + str(row[2])).grid(column=3,row = row_number+1)
                            Label(root, text = "" + str(row[3])).grid(column=4,row = row_number+1)
                            Label(root, text = "" + str(row[4])).grid(column=5,row = row_number+1)
                            Label(root, text = "" + str(row[5])).grid(column=6,row = row_number+1)
                        root.mainloop()
                    Button(root,text='Show Student Marks ',command=show4,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column =0,sticky=N+S+E+W)
                    def logout():
                        ans=askyesno('Confirmation', 'Do You Want To Exit?')
                        if(ans==True):
                            root.destroy()
                    Button(root,text='Exit',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=8,column=0)
                    root.mainloop()                  
        
            Button(menu,text='View Marks',command=option7,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=7,column=0,sticky=N+S+E+W)

            def logout():
                ans=askyesno('Confirmation', 'Do You Want To Logout?')
                if(ans==True):
                    menu.destroy()
            Button(menu,text='Logout',command=logout,width=25,font=("Times New",10),bd=5,bg="light grey").grid(row=10,column=0,sticky=N+S+E+W)

            menu.mainloop()
    Button(window,text='Login',command=login,width=20,font=("Times New",15),bd=5,bg="light grey").grid(row=3,column=2,sticky=N+S+E+W)

    def gallery():
        root2=Toplevel()
        root2.geometry('1080x600')
        root2.title('Gallery')

        p1=PhotoImage(file='mypic1.gif')
        def pic1():
            root3=Toplevel()
            root3.title('Photo')
            photo=PhotoImage(file='mypic1.gif')
            Label(root3,image=photo).grid(row=0,column=0)
            root3.mainloop()
        Button(root2,image=p1,command=pic1,bd=-5).grid(row=0,column=0,sticky=N+S+E+W)

        p2=PhotoImage(file='mypic2.gif')
        def pic2():
            root3=Toplevel()
            root3.title('Photo')
            photo=PhotoImage(file='mypic2.gif')
            Label(root3,image=photo).grid(row=0,column=0)
            root3.mainloop()
        Button(root2,image=p2,command=pic2,bd=-5).grid(row=0,column=1,sticky=N+S+E+W)

        p3=PhotoImage(file='mypic3.gif')
        def pic3():
            root3=Toplevel()
            root3.title('Photo')
            photo=PhotoImage(file='mypic3.gif')
            Label(root3,image=photo).grid(row=0,column=0)
            root3.mainloop()
        Button(root2,image=p3,command=pic3,bd=-5).grid(row=0,column=2,sticky=N+S+E+W)

        p4=PhotoImage(file='mypic6.gif')
        def pic4():
            root3=Toplevel()
            root3.title('Photo')
            photo=PhotoImage(file='mypic5.gif')
            Label(root3,image=photo).grid(row=0,column=0)
            root3.mainloop()
        Button(root2,image=p4,command=pic4,bd=-5).grid(row=1,column=0,sticky=N+S+E+W)

        p5=PhotoImage(file='mypic5.gif')
        def pic5():
            root3=Toplevel()
            root3.title('Photo')
            photo=PhotoImage(file='mypic5.gif')
            Label(root3,image=photo).grid(row=0,column=0)
            root3.mainloop()
        Button(root2,image=p5,command=pic5,bd=-5).grid(row=1,column=1,sticky=N+S+E+W)

        p6=PhotoImage(file='mypic6.gif')
        def pic6():
            root3=Toplevel()
            root3.title('Photo')
            photo=PhotoImage(file='\mypic6.gif')
            Label(root3,image=photo).grid(row=0,column=0)
            root3.mainloop()
        Button(root2,image=p6,command=pic6,bd=-5).grid(row=1,column=1,sticky=N+S+E+W)
        

        root2.mainloop()
    

    Button(window,text='View Photo Gallery',command=gallery,width=20,font=("Times New",15),bd=5,bg="light grey").grid(row=4,column=2,sticky=N+S+E+W)
    
    window.mainloop()

###############################################################################################################################################################

b=PhotoImage(file='Start Button.gif')

Button(window,image=b,command=start,bd=-5).place(x=410,y=490)

Label(window,text='Contact Us\n Developer:\Deepika Kendole',font=("Times New",15)).place(x=1090,y=0)
window.mainloop()