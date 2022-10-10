from tkinter import *
import sys
import time;
import random
import datetime
import os
from PIL import ImageTk,Image
from tkinter import messagebox
import re
from tkinter import ttk
import tkinter.messagebox

#set theme=[waldorf $: : argv 0]

def okp():
    RegCP.destroy()
    Window1()

def confirmPN():
    global RegCP
    usernamei=username.get()
    list_of_files=os.listdir('C:/Users/CODEIRONSIDE/OneDrive/project1')
    data = open(usernamei,"r")
    data1=data.read()
    RegCP=Toplevel()
    RegCP.title("recover password page")
    RegCP.iconbitmap("favico.ico")
    RegCP.resizable(width=False, height=False)
    RegCP.config(bg="brown")
    labelCPt=Label(RegCP, text="this is your details",bg="brown")
    labelCPt.pack()
    labelCP=Label(RegCP, text=data1,bg="brown")
    labelCP.pack()
    pas=LabelFrame(RegCP,bg="brown")
    BtnCP=Button(pas, text="ok", command=Window1,bg="brown")
    
    btnCp.pack()
    data.close()
    RegCP.mainloop()

def forgetpass():
    global username
    username=StringVar()
    Reg1=Toplevel()
    Reg1.title("recover password page")
    Reg1.iconbitmap("favico.ico")
    Reg1.resizable(width=False, height=False)
    Reg1.config(bg="brown")

    frame12=Frame(Reg1, bg ="#BFBFBF", relief=FLAT)
    frame12.pack()
    frameFP=LabelFrame(frame12,bg ="white", relief=RIDGE, bd=3)
    frameFP.pack()
    labelf=Label(frameFP, justify=LEFT,width=27, text="please confirm" + "\n" + "username" +  "\n"  + 
    "by entering your number below", bg='#BFBFBF',
    font=("Arial Rounded MT Bold",13))
    labelf.pack()

    logo2 = ImageTk.PhotoImage(Image.open("qm.jpg"))



    fp=Label(frame12, image=logo2)
    fp.pack()

    #
    #labelf=Label(frame12, justify=LEFT, text="please confirm" + "\n" + "your phone number" +  "\n"  + 
    #"by entering your number below", bg='#BFBFBF',
    #font=("Arial Rounded MT Bold",8))
    #labelf.place(x=7,y=7)
    frameFQ=LabelFrame(frame12,bg ="#BFBFBF", relief=RIDGE, bd=3)
    frameFQ.pack()

    FNlabelw=Label(frameFQ,width=42, text="username*",  bg='#BFBFBF',font=("Arial Rounded MT Bold",8),pady=10)
    FNlabelw.pack()
    FNentryw =Entry(frameFQ, relief= RIDGE,width=30,bd=1,bg ="white", show="*", justify= CENTER, textvariable=username)
    FNentryw.pack(ipady=8) 
    bitt2=Button(frameFQ,width=20, text="submit",bg ="#BFBFBF", relief=FLAT,command=confirmPN)
    bitt2.pack()
    Reg1.mainloop()

def rad3(value):
    if r==1:
        Window4()
    else:
        Window3()   
def cancel():
    global cancel
    response=messagebox.askokcancel()
#def slide(var):
 #   txtdisplay.configure(height=horiz.get(), width=vert.get())




def button_click(number):
    #caE.delete(0, END)
    current = caE.get()
    caE.delete(0, END)
    caE.insert(0, str(current) + str(number))
def button_equals():
    second_number=caE.get()
    caE.delete(0, END)
    try:
        if smath=="addition":
            result =f_num + int(second_number)
            caE.insert(0, result)
        if smath=="divide":
            result =f_num / int(second_number)
            caE.insert(0, result)
        if smath=="multiply":
            result = f_num * int(second_number)
            caE.insert(0,result)
        if smath=="substraction":
            result = f_num - int(second_number)
            caE.insert(0, result)
    except ValueError and NameError:
        caE.insert(0, "syntax error")

def checkca1():
    if var1.get()==1:
        ca1E.configure(state=NORMAL)
        ca1E.focus()
        ca1E.delete(0, END)
    elif var1.get()==0:
        ca1E.configure(state=DISABLED)
def checkca2():
    if var2.get()==1:
        ca2E.configure(state=NORMAL)
        ca2E.focus()
        ca2E.delete(0, END)
    elif var2.get()==0:
        ca2E.configure(state=DISABLED)
def checkca3():
    if var3.get()==1:
        ca3E.configure(state=NORMAL)
        ca3E.focus()
        ca3E.delete(0, END)
    elif var3.get()==0:
        ca3E.configure(state=DISABLED)
def checkca4():
    if var4.get()==1:
        ca4E.configure(state=NORMAL)
        ca4E.focus()
        ca4E.delete(0, END)
    elif var4.get()==0:
        ca4E.configure(state=DISABLED)
def checkca5():
    if var5.get()==1:
        ca5E.configure(state=NORMAL)
        ca5E.focus()
        ca5E.delete(0, END)
    elif var5.get()==0:
        ca5E.configure(state=DISABLED)



def button_add():
    first_number=caE.get()
    global f_num
    global smath
    smath="addition"
    f_num = int(first_number)
    caE.delete(0, END)
def button_substract():
    first_number=caE.get()
    global f_num
    global smath
    smath="substraction"
    f_num = int(first_number)
    caE.delete(0, END)
def button_multiply():
    first_number=caE.get()
    global f_num
    global  smath
    smath="multiply"
    f_num = int(first_number)
    caE.delete(0, END)
def button_divide():
    first_number=caE.get()
    global f_num
    global smath
    smath="divide"
    f_num = int(first_number)
    caE.delete(0, END)
def button_clears():
    caE.delete(0, END)
    caE.insert(0, "0")

def reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    ca11.set("0")
    ca22.set("0")
    ca33.set("0")
    ca44.set("0")
    ex1.set("0")
    caE.delete(0, END)
    ca1E.configure(state=DISABLED)
    ca2E.configure(state=DISABLED)
    ca3E.configure(state=DISABLED)
    ca4E.configure(state=DISABLED)
    ca5E.configure(state=DISABLED)
    LBfn.delete(0, END)
    LBln.delete(0, END)
    #f_name.set("0")
    #L_name.set("0")
    #ca_ttl.set("0")
    #exm_ttl.set("0")
    #avg.set("0")
    #cle_ttl.set("0")
    pos2.current(0)
    term4.current(0)
    LBCT.delete(0, END)
    LBET.delete(0, END)
    LBCAT.delete(0, END)
    LBremark.delete(0,END)
    #txtdisplay.delete(1.0, END)
    #txtdisplay.insert(1.0, "FIRST NAME\t\t" + "LAST NAME\t\t\t" + "1st C.A\t\t"+ "2nd C.A\t\t"+ "3rd C.A\t\t"+ "4th C.A\t\t"+ "C.A total\t\t"+ "Exam total\t\t"+ "average\t\t")


def finish():
    f_name1=f_name.get()
    L_name1=L_name.get()
    avge1=avge.get()
    tex1=(ca5E.get())
    tca44=(ca4E.get())   
    tca33=(ca3E.get())
    tca11=(ca1E.get())
    tca22=(ca2E.get())
    sub_n=subject_name.get()
    gd= LBET.get()
    txtdisplay.insert(1.0, "\n\n" + str(f_name1) + "\t\t" + str(L_name1)  + "\t\t\t" + str(tca11) + "\t\t" + str(tca22) + "\t\t" + 
    str(tca33) + "\t\t" + str(tca44) + "\t\t\t\t" + str(tex1) +  "\t\t" +  str(total1) + "\t\t" + str(total2) + "\t\t" + str(gd) + "\t\t" +str(avge1))
    txtdisplay.insert(1.0, "\nFIRST NAME\t\t" + "LAST NAME\t\t\t" + "1st C.A\t\t"+ "2nd C.A\t\t"+ "3rd C.A\t\t"+ "4th C.A\t\t\t\t" +  "Examination\t\t" + "C.A total\t\t" + "total\t\t"
    + "grade\t\t" + "remark\t\t" + "\n")
    txtdisplay.insert(1.0, "\nSUBJECT :" + str(sub_n) + "\n")
    
   
    #txtdisplay.insert(1.0, + str(L_name1))
    #txtdisplay.insert(1.0, str(tca11) + "\t\t")
    #txtdisplay.insert(1.0, str(tca22) + "\t\t")
    #txtdisplay.insert(1.0, str(tca33) + "\t\t")
    #txtdisplay.insert(1.0, str(tca44) + "\t\t")
    #txtdisplay.insert(1.0, str(tex1) + "\t\t")
    #txtdisplay.insert(1.0, str(total1) + "\t\t")
    #txtdisplay.insert(1.0, str(total2) + "\t\t")
    #txtdisplay.insert(1.0, str(avge1))

def total():
    tca111=int(ca1E.get())
    tca222=int(ca2E.get())
    tca333=int(ca3E.get())
    tca444=int(ca4E.get())
    tex11=int(ca5E.get())
    tex1=(ca5E.get())
    tca44=(ca4E.get())   
    tca33=(ca3E.get())
    tca11=(ca1E.get())
    tca22=(ca2E.get())

    if  re.search('[a-z]', tex1) and re.search('[A-Z]', tex1):
        response=messagebox.showerror("...","input contains an alphabet")
        ca5E.delete(0, END)
    if re.search('[a-z]', tca44) and re.search('[A-Z]', tca44):
        response=messagebox.showerror("...","input contains an alphabet")
        ca4E.delete(0, END)
    if re.search('[a-z]', tca33) and re.search('[A-Z]', tca33):
        response=messagebox.showerror("...","input contains an alphabet")
        ca3E.delete(0, END)
    if re.search('[a-z]', tca11) and re.search('[A-Z]', tca11):
        response=messagebox.showerror("...","input contains an alphabet")
        ca1E.delete(0, END)
    if re.search('[a-z]', tca22) and re.search('[A-Z]', tca22):
        response=messagebox.showerror("...","input contains am alpha")
        ca2E.delete(0, END)
    else:
        global total1
        total1=(tca444 + tca333 + tca222 + tca111)
        global total2
        total2= int(total1) + int(tex1)
        LBCT.insert(0, str(total1))
        #LBET.insert(0, str(tex1))
        LBCAT.insert(0, str(total2))
        #t1 = [74, 75,76,77,78,7,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,07,98,99,]

        #for total2 in range(74-100):
        #   LBremark.insert(0, 'EXCELLENT')
       #else:
       #    pass
        if total2 in list(range(74,101)):
            LBremark.insert(0, " EXCELLENT")
        elif total2 in list(range(69,75)):
            LBremark.insert(0, 'V.GOOD')
        elif total2 in list(range(64,70)):
            LBremark.insert(0, "GOOD")
        elif  total2 in list(range(50,65)):
            LBremark.insert(0, 'CREDIT')
        elif total2 in list(range(39,50)):
            LBremark.insert(0,'PASS')
        elif total2 in list(range(17,40)):
            LBremark.insert(0, 'WEAK PASS')
        elif total2 < 17:
            LBremark.insert(0, 'FAIL')
        elif total2 > 100:
            response=messagebox.showinfo('OOPS', 'values dont correspond')
        else:
            response=messagebox.showinfo('OOPS', 'SCORE IS OVER')
            #avge.set("EXCELLENT")




    if total2 in list(range(69,101)):
        LBET.insert(0, "A1")
    elif total2 in list(range(60,70)):
        LBET.insert(0, 'B2')  
    elif total2 in list(range(60,65)):
        LBET.insert(0, "B3")
    elif  total2 in list(range(54,60)):
        LBET.insert(0, 'C4')
    elif total2 in list(range(49,55)):
        LBET.insert(0,'C5')
    elif total2 in list(range(45,50)):
        LBET.insert(0, 'C6')
    elif total2 in list(range(39,45)):
        LBET.insert(0, 'D7')
    elif total2 in list(range(17,40)):
        LBET.insert(0, 'E8')
    elif total2 < 17:
        LBET.insert(0, 'F9')
   
    else:
        response=messagebox.showinfo('OOPS', 'SCORE IS OVER')

    
def Window3():
    Reg4.destroy()
    root.withdraw()
    global Window3
    global Reg3
    global caE
    Reg5=Toplevel()
    Reg5.title("SUBJECT TEACHER")
    Reg5.iconbitmap("favico.ico")
    Reg5.resizable(width=False, height=False)
    Reg5.geometry("1270x650+0+0")
    #Reg2.overrideredirect(True)
    #Reg2.transient(1)
    #Reg2.protocol("WM_DELETE_WINDOW", CancelCommand)
    Reg5.config(bg="#77c593")
    #===========sliders====================
    global my_canvas
    main_frame= Frame(Reg5,)
    main_frame.pack(side=RIGHT,fill=BOTH, expand=1)#pady=20
    my_canvas= Canvas(main_frame,width=200,height=400)
    my_canvas.pack(side=LEFT,fill=BOTH, expand =1)
    my_scrollbar=Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT ,fill=Y)
   
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    student_info1=Frame(my_canvas, pady=5,bg="#EDEBFF")
    my_canvas.create_window((0,0), window=student_info1, anchor="nw")
    my_scrollbar1=Scrollbar(student_info1, orient=HORIZONTAL,command=my_canvas.xview)
    my_scrollbar1.pack(side=BOTTOM ,fill=X)#place(x=2, y=410, fill=X)place(x=2, y=410)
    my_canvas.configure(xscrollcommand=my_scrollbar1.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    #==========================slider down=================================================
    #main_frame1= Frame(Reg5)
    #main_frame1.place(x=1, y=1)
    #my_canvas1= Canvas(main_frame1,width=873,height=406)
    #my_canvas1.pack(side=TOP,fill=BOTH, expand =1)
    #my_scrollbar1.pack(side=BOTTOM ,fill=X)#place(x=2, y=410)#pack(side=BOTTOM ,fill=Y)
    #my_canvas1.configure(yscrollcommand=my_scrollbar1.set)
    #my_canvas1.bind('<Configure>', lambda e:my_canvas1.configure(scrollregion=my_canvas1.bbox("all")))
    #student_info11=Frame(my_canvas1, pady=5,bg="#FFF8DC")
    #my_canvas1.create_window((0,0), window=student_info1, anchor="nw")
    #=========================top===================================
    student_info=Frame(student_info1, pady=5,bg="#EDEBFF", relief=FLAT,bd=12)
    #student_info111=Frame(student_info11, pady=5,bg="#FFF8DC", relief=FLAT,bd=12)
  
    student_info.pack(side= TOP)
   # student_info111.pack()

    #my_canvas.create_window((0,0), window=student_info, anchor="nw")
    my_menu=Menu(Reg5)
    Reg5.config(menu=my_menu)


    file_menu=Menu(my_menu)
    my_menu.add_cascade(label="file",menu=file_menu)
    file_menu.add_command(label="New")
    file_menu.add_separator()
    file_menu.add_command(label="open")


    
    tool_menu=Menu(my_menu)
    my_menu.add_cascade(label="tools",menu=file_menu)
    tool_menu.add_command(label="copy")
    tool_menu.add_separator()
    tool_menu.add_command(label="cut")
    fil_img1=PhotoImage(file="studentsss.png")
    fil_img2= Label(student_info, image=fil_img1)
    fil_img2.pack(side=LEFT)
    lblTitle1= Label(student_info,width=30,height=1, text="student grade mangement system",fg="#3B3434",bg="#EDEBFF", relief=FLAT,
    font=("chiller",75,"bold"),justify=CENTER)    
    lblTitle1.pack(side=RIGHT)


    #++++++++++++++++++++++++++++++++++++
    global subject_name

    subject_name=StringVar()
    subject_info2=Frame(Reg5,bg="#38ACC0", relief=RIDGE, bd=2)

    student_info3=Frame(subject_info2,relief=FLAT, bd=1, borderwidth=0)
    social_lb1=Frame(student_info3, relief=FLAT,bd=2)
    fil_img=PhotoImage(file="file.png")
    fil_btn=Button(social_lb1, image=fil_img,borderwidth=0)
    fil_btn.grid(row=0, column=0)
 
    lbl1=Label(social_lb1,width=10, text="new",font=("chiller", 25,'bold'))
    lbl1.grid(row=0, column=1)

    open_img=PhotoImage(file="file.png")
    open_btn=Button(social_lb1, image=fil_img,borderwidth=0)
    open_btn.grid(row=1, column=0)
 
    lbl11=Label(social_lb1,width=10, text="open",font=("chiller", 25,'bold'))
    lbl11.grid(row=1, column=1)

    social_lb1.pack(side=TOP)
   
    social_lb3 = Frame(student_info3)
    lbl3=Label(social_lb3,width=10, text="subject",font=("chiller", 25,'bold'))
    lbl3.pack()
    sub3 = Entry(social_lb3 , textvariable=subject_name)
    sub3.pack()

    lbl4=Label(social_lb3,width=10, text="student no.",font=("chiller", 25,'bold'))
    lbl4.pack(padx=3)
    sub4 = Entry(social_lb3 )
    sub4.pack()

    social_lb3.pack()




    #sub11.pack(pady=10,ipady=13)
    social_lb11=Frame(student_info3)
    sub1 = Label(social_lb11, text="for more enquires, \ncomplaints", font=("chiller", 25,'bold'))
    sub1.pack()
    fb_img=PhotoImage(file="iconfinder_facebook_834722.png")
    fb_btn=Button(social_lb11, image=fb_img,borderwidth=0)
    fb_btn.pack(side=LEFT, padx=12)
    fb_im=PhotoImage(file="tw2.png")
    fb_btn1=Button(social_lb11, image=fb_im,borderwidth=0)
    fb_btn1.pack(side=LEFT, padx=12)
    tw_im=PhotoImage(file="iconfinder_11-linkedin_104493.png")
    tw_btn1=Button(social_lb11, image=tw_im,borderwidth=0)
    tw_btn1.pack(side=LEFT, padx=12)
    social_lb11.pack(pady=85)

   
    

    social_lb=Frame(student_info3)
    sub2 = Label(social_lb, text="Screen Copyright©", font=("chiller", 25,'bold'))
    sub2.pack(side=BOTTOM)
    
    social_lb.pack(side=BOTTOM, pady=85)




    student_info3.pack()
    subject_info2.pack(side=LEFT)

    #====================== left(subject info)===================================
    subject_info=Frame(student_info1,bg="#38ACC0", relief=FLAT,bd=2)
    subject_info.pack(side=LEFT)
    #---------------------------------
    pos1 =["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th",
    "21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st","32nd","33rd","34th","35th","36th","37th","38th","39th","40th",
    "41st","42nd","43rd","44th","45th","46th","47th","48th","49th","50th","51st","52nd","53rd","54th","55th","56th","57th","58th","59th","60th"]
    term2=["1st","2nd","3rd"]
    position1=StringVar()
    term1=StringVar()
    student_F=Frame(subject_info,bd=6,bg="#38ACC0")
    student_F.configure(height=260, width=100)
    student_F.pack(side=TOP)
    #subject_f.place
    txtfn=Label(student_F,height=1,relief=FLAT,bg="#38ACC0", width=12,text="First name ",font=("Harlow Solid Italic", 20,'bold'))
    txtfn.grid(row=0,column=0,sticky=W)
    txtln=Label(student_F,height=1,width=12,relief=FLAT,bg="#38ACC0",text="Other name",font=("Harlow Solid Italic", 20,'bold'))
    txtln.grid(row=1,column=0,sticky=W)
    
    #pos3=Label(student_f,relief=RIDGE, width=12,text="position", bd=4,font=("helvetica", 20,'bold'))
    #pos3.grid(row=2,column=0)
    global f_name
    global L_name
    global ca_ttl

    global avg
    global cle_ttl
    global pos2
    global term4

    f_name=StringVar()
    L_name=StringVar()
    ca_ttl=StringVar()
   
    avg=StringVar()
    cle_ttl=StringVar()

    global LBfn
    global LBln
    global LBET

    LBfn=Entry(student_F, width=25, bg ="#E9DBDB",font=("helvetica", 15,'bold'),textvariable=f_name)
    LBfn.grid(row=0,column=1,ipady=3)
    LBln=Entry(student_F, width=25, bg ="#E9DBDB" ,font=("helvetica", 15,'bold'),textvariable=L_name)
    LBln.grid(row=1,column=1,ipady=3)
   
    
    global LBCT
    
    global click6
    global click7
    global pos2
    global term4
    click6 =StringVar()
    click7= StringVar()
    
    
    #pos2= ttk.Combobox(student_F, value=pos1,width=23,font=("helvetica", 10,'bold'))
    #pos2.current(0)
    #pos2.grid(row=4,column=1,ipady=5)
    term3=Label(student_F,relief=FLAT, width=12,text="Term",bg="#38ACC0",font=("Harlow Solid Italic", 20,'bold'))
    #term3=Label(student_F,relief=RIDGE, width=12,text="term",bg="#38ACC0",font=("helvetica", 20,'bold'))
    term3.grid(row=3,column=0,sticky=W)
    term4= ttk.Combobox(student_F, value=term2,width=23,font=("helvetica", 14,'bold'))
    term4.current(0)
    term4.grid(row=3,column=1,ipady=5)
   
     
    global LBremark
    global avge
    avge = StringVar()
   
    
    global LBCAT
    
   
    

    
    #==========================================================================
    global var1
    global var2
    global var3
    global var4
    global var5
    global ca1
    global ca2
    global ca3
    global ca4
    global exams
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    scores=Frame(subject_info,bd=10,bg="#38ACC0", relief=FLAT)
    scores.pack(side=LEFT)
    
    ca1=Checkbutton(scores, text="First C.A", bg="#38ACC0",variable=var1, onvalue=1,offvalue=0,font=("Arial Rounded MT Bold",20,"bold"), command=checkca1)
    ca1.grid(row=0,sticky=W)
    ca2=Checkbutton(scores, text="Second  C.A",bg="#38ACC0", variable=var2, onvalue=1,offvalue=0,font=("Arial Rounded MT Bold",20,"bold"), command=checkca2)
    ca2.grid(row=1,sticky=W)
    ca3=Checkbutton(scores, text="Third C.A", bg="#38ACC0",variable=var3, onvalue=1,offvalue=0,font=("Arial Rounded MT Bold",20,"bold"), command=checkca3)
    ca3.grid(row=2,sticky=W)
    ca4=Checkbutton(scores, text="Fourth C.A",bg="#38ACC0", variable=var4, onvalue=1,offvalue=0,font=("Arial Rounded MT Bold",20,"bold"), command=checkca4)
    ca4.grid(row=3,sticky=W)
    exams=Checkbutton(scores, text="Examination",bg="#38ACC0", variable=var5, onvalue=1,offvalue=0,font=("Arial Rounded MT Bold",20,"bold"), command=checkca5)
    exams.grid(row=4,sticky=W)
    txtCT=Label(scores,relief=FLAT,height=1, width=12,bg="#38ACC0",text="CA total",justify=RIGHT, font=("Arial Rounded MT Bold", 20,'bold'))
    txtCT.grid(row=5,sticky=W)
    
    pos3=Label(scores,relief=FLAT, width=12,height=1,bg="#38ACC0",text="Position",font=("Arial Rounded MT Bold", 20,'bold'))
    pos3.grid(row=7,sticky=W)
    CATlb=Label(scores,relief=FLAT, width=12,bg="#38ACC0",text="Total scores", bd=4,font=("Arial Rounded MT Bold", 20,'bold'))
    CATlb.grid(row=8,sticky=W)

    txtET=Label(scores, width=12,relief=FLAT,height=1,bg="#38ACC0",text="grade", font=("Arial Rounded MT Bold", 20,'bold'))
    txtET.grid(row=9,column=0,sticky=W)
    avelb=Label(scores,relief=FLAT, width=12,bg="#38ACC0",text="Remark", bd=4,font=("Arial Rounded MT Bold", 20,'bold'))
    avelb.grid(row=10,sticky=W,pady=11)
    #=========================================
    global ca11
    global ca22
    global ca33
    global ca44
    global ex1
    global ca1E
    global ca2E
    global ca3E
    global ca4E
    global ca5E
    ex1=IntVar()
    ca44=IntVar()
    ca33=IntVar()
    ca11=IntVar()
    ca22=IntVar()
    grades=Frame(subject_info,bd=10,relief=FLAT,bg="#38ACC0")
    grades.pack(side=RIGHT)
    
    ca1E=Entry(grades, relief =FLAT, bd=3,bg="#E9DBDB" ,justify="center",font=("helvetica", 20,'bold'), state=DISABLED,textvariable=ca11)
    ca1E.grid(row=0, sticky=W,ipady=5)
    ca2E=Entry(grades, relief =FLAT, bd=3,bg="#E9DBDB", justify="center",font=("helvetica", 20,'bold'), state=DISABLED,textvariable=ca22)
    ca2E.grid(row=1, sticky=W,ipady=2)
    ca3E=Entry(grades, relief =FLAT, bd=3,bg="#E9DBDB", justify="center",font=("helvetica", 20,'bold'), state=DISABLED,textvariable=ca33)
    ca3E.grid(row=2, sticky=W,ipady=2)
    ca4E=Entry(grades, relief =FLAT, bd=3,bg="#E9DBDB", justify="center",font=("helvetica", 20,'bold'), state=DISABLED,textvariable=ca44)
    ca4E.grid(row=3, sticky=W,ipady=2)
    ca5E=Entry(grades, relief =FLAT, bd=3,bg="#E9DBDB", justify="center",font=("helvetica", 20,'bold'), state=DISABLED,textvariable=ex1)
    ca5E.grid(row=4, sticky=W,ipady=3)
    LBCT=Entry(grades, bg ="#E9DBDB",width=19,font=("helvetica", 21,'bold'),textvariable=ca_ttl)
    LBCT.grid(row=5,sticky=W,ipady=2)
   
    pos2= ttk.Combobox(grades, value=pos1,width=41,font=("helvetica", 9,'bold'))
    pos2.current(0)
    pos2.grid(row=7,sticky=W,ipady=5,pady=2)
    LBCAT=Entry(grades, bg ="#E9DBDB",width=19,font=("helvetica", 21,'bold'),textvariable=cle_ttl)
    global LBET
    LBCAT.grid(row=8,sticky=W,ipady=2)
    LBET=Entry(grades, bg ="#E9DBDB",width=19,font=("helvetica", 21,'bold'))
    LBET.grid(row=9,sticky=W,ipady=2, pady=2)#column=1,
    LBremark=Entry(grades, bg ="#E9DBDB",width=19,font=("helvetica", 21,'bold'),textvariable=avge)
    LBremark.grid(row=10,sticky=W,ipady=2,pady=8)

    #````````````````````````````````

    #pos1 =["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th",
    #"21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st","32nd","33rd","34th","35th","36th","37th","38th","39th","40th",
    #"41st","42nd","43rd","44th","45th","46th","47th","48th","49th","50th","51st","52nd","53rd","54th","55th","56th","57th","58th","59th","60th"]
    #position1=StringVar()

    
    subject_f=Frame(student_info1, relief=FLAT, bd=1)
    subject_f.place(x=5,y=585)

    #============================right(display options)=============================
    display=Frame(student_info1, relief=FLAT,bd=1,bg="#7a2048")
    display.pack(side= RIGHT)
    
    #-------------buttons frame---------------------------------------
    Button_f=Frame(display,relief=FLAT,bd=5, bg="#7a2048")
    Button_f.pack(side=BOTTOM)
    Button_ff=Frame(Button_f, bd=1 ,height =1,bg="#7a2048")
    Button_ff.pack()
    Button_fff=LabelFrame(Button_f,bd=4,bg="#7a2048")
    Button_fff.pack()
    global horiz
    global vert
    global txtdisplay
    txtdisplay=Text(Button_ff, bg ="#E9DBDB", bd=1,font=("helvetica", 8,'bold'),wrap="none" )
    txt_scrollbar=Scrollbar(Button_ff, orient=VERTICAL,command=txtdisplay.yview)
    txt_scrollbar.pack(side=RIGHT ,fill=Y)
   
    txtdisplay.configure(yscrollcommand=txt_scrollbar.set)
    txt1_scrollbar1=Scrollbar(Button_ff, orient=HORIZONTAL,command=txtdisplay.xview)
    txt1_scrollbar1.pack(side=BOTTOM ,fill=X)
   
    txtdisplay.configure(xscrollcommand=txt1_scrollbar1.set)
    #horiz=Scrollbar(txtdisplay,height=25)
    #horiz.config(command=txtdisplay.yview)
    #horiz.pack(anchor=E, fill=Y)
    #vert=Scale(txtdisplay, from_=0, to=100000,width=125, command=slide)
    #txtdisplay.insert(1.0, "\nFIRST NAME\t\t" + "LAST NAME\t\t\t" + "1st C.A\t\t"+ "2nd C.A\t\t"+ "3rd C.A\t\t"+ "4th C.A\t\t"+ "C.A total\t\t"+ "Exam total\t\t"+ "average\t\t")
    txtdisplay.configure(height=21,width=125)
    txtdisplay.pack()#grid(row=0,column=0,sticky=W)
    btntotal=Button(Button_fff,bg="#ecc19c",relief=RIDGE, text="reset", bd=3,font=("helvetica", 20,'bold'),command=reset)
    btntotal.grid(row=1,column=0)
    btntotal=Button(Button_fff,relief =RIDGE,bg="#1e847f", text="save", bd=3,font=("helvetica", 20,'bold'))
    btntotal.grid(row=1,column=1)
    btntotal=Button(Button_fff,relief =RIDGE,bg="#d9a5b3",  text="total",bd=3,font=("helvetica", 20,'bold'), command=total) 
    btntotal.grid(row=1,column=2)
    btntotal=Button(Button_fff,relief =RIDGE,bg="#d9a5b3",  text="print",bd=3,font=("helvetica", 20,'bold'))
    btntotal.grid(row=1,column=4)
    btnfinish=Button(Button_fff,bg="#ecc19c",relief=RIDGE, text="finish", bd=3,font=("helvetica", 20,'bold'),command= finish)
    btnfinish.grid(row=1,column=3)
    #````````````````````````````````````````````
    global text_Input
    text_Input=StringVar()
    calf=Frame(display,relief=RIDGE,bg="#7a2048")
    calf.pack(side=TOP)
    caE=Entry(calf,width=55,bg="#E9DBDB",bd=4, font=("arial",12,"bold"),justify=RIGHT,textvariable=text_Input)
    caE.grid(row=0,column=0,columnspan=4,ipady=3,pady=1)
    caE.insert(0,"0")
    #============calculator buttons===================
    global btn7
    btn7=Button(calf,text="7",relief=RIDGE,bd=3,width=12,pady=1,fg="black",bg="#CEA642", font=("arial",15,"bold"), command=lambda:button_click(7))
    btn7.grid(row=2,column=0)
    btn8=Button(calf,text="8",pady=1,width=12,relief=RIDGE,bd=3,fg="black",bg="#CEA642", font=("arial",15,"bold"), command=lambda:button_click(8))
    btn8.grid(row=2,column=1)
    btn9=Button(calf,text="9",pady=1,fg="black",width=12,relief=RIDGE,bd=3,bg="#CEA642", font=("arial",15,"bold"), command=lambda:button_click(9))
    btn9.grid(row=2,column=2)
    btnadd=Button(calf,text="+",pady=1,fg="black",width=12,relief=RIDGE,bd=3,bg="#CEA642", font=("arial",15,"bold"),command=button_add)
    btnadd.grid(row=2,column=3)


    btn4=Button(calf,text="4",relief=RIDGE,bd=3,pady=1,fg="black", width=12,bg="#E9DBDB",font=("arial",15,"bold"), command=lambda:button_click(4))
    btn4.grid(row=3,column=0)
    btn5=Button(calf,text="5",pady=1,fg="black",relief=RIDGE,bd=3, width=12,bg="#E9DBDB",font=("arial",15,"bold"), command=lambda:button_click(5))
    btn5.grid(row=3,column=1)
    btn6=Button(calf,text="6",pady=1,fg="black",relief=RIDGE,bd=3, width=12,bg="#E9DBDB",font=("arial",15,"bold"), command=lambda:button_click(6))
    btn6.grid(row=3,column=2)
    btnsub=Button(calf,text="-",pady=1,fg="black",width=12,relief=RIDGE,bd=3,bg="#CEA642", font=("arial",15,"bold"),command=button_substract)
    btnsub.grid(row=3,column=3)


    btn1=Button(calf,text="1",pady=1,fg="black",relief=RIDGE,bd=3,bg="#E9DBDB", width=12,font=("arial",15,"bold"), command=lambda:button_click(1))
    btn1.grid(row=4,column=0)
    btn2=Button(calf,text="2",pady=1,fg="black", relief=RIDGE,bd=3,bg="#E9DBDB",width=12,font=("arial",15,"bold"), command=lambda:button_click(2))
    btn2.grid(row=4,column=1)
    btn3=Button(calf,text="3",pady=1,fg="black",width=12,relief=RIDGE,bd=3,bg="#E9DBDB", font=("arial",15,"bold"), command=lambda:button_click(3))
    btn3.grid(row=4,column=2)
    btnmul=Button(calf,text="*",pady=1,fg="black",relief=RIDGE,bd=3, width=12,bg="#CEA642",font=("arial",15,"bold"), command=button_multiply)
    btnmul.grid(row=4,column=3)


    btndiv=Button(calf,text="/",pady=1,fg="black",relief=RIDGE,bd=3,width=12,bg="#CEA642", font=("arial",15,"bold"), command=button_divide)
    btndiv.grid(row=5,column=0)
    btnz=Button(calf,text="0",pady=1,fg="black",relief=RIDGE,bd=3,width=12,bg="#CEA642", font=("arial",15,"bold"), command=lambda:button_click(0))
    btnz.grid(row=5,column=1)
    btne=Button(calf,text="=",width=12,pady=1,relief=RIDGE,bd=3,fg="black",bg="#CEA642", font=("arial",15,"bold"),command=button_equals)
    btne.grid(row=5,column=2)
    btnclr=Button(calf,text="clr",width=12,pady=1,relief=RIDGE,bd=3,fg="black", bg="#CEA642",font=("arial",15,"bold"),command=button_clears)
    btnclr.grid(row=5,column=3)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #regf=Frame(display,relief=RIDGE,bd=4)
    #regf.pack(side=BOTTOM)
    Reg5.mainloop() 

def Window4():
    Reg4.destroy()
    root.withdraw()
    global Window4
    global Reg6
    Reg6=Toplevel()
    Reg6.title("FORM-MASTER/MISTRESS")
    Reg6.iconbitmap("favico.ico")
    Reg6.resizable(width=False, height=False)
    Reg6.geometry("300x300")
    #Reg2.overrideredirect(True)
    #Reg2.transient(1)
    #Reg2.protocol("WM_DELETE_WINDOW", CancelCommand)
    Reg6.config(bg="white")
    Reg6.mainloop()
def options():
    global Reg4
    global options
    global clicked
    global r
    global Variable
    Reg4=Toplevel(root)
    Reg4.title("WELCOME")
    Reg4.iconbitmap("favico.ico")
    Reg4.resizable(width=False, height=False)
    #Reg4.geometry("350x150")
    #Reg2.overrideredirect(True)
    #Reg2.transient(1)
    #Reg2.protocol("WM_DELETE_WINDOW", CancelCommand)
    Reg4.config(bg="#B0E0E6")
    r = IntVar()
    r.get()
    rad1=Radiobutton(Reg4, text="formmaster/mistress",bg="#B0E0E6",font=("arial", 8,"bold"),variable=r, value=1,command=lambda:(1))
    rad2=Radiobutton(Reg4, text="subject teacher",bg="#B0E0E6", font=("arial", 8,"bold"),variable=r, value=2,command=lambda:(2))
    rad1.pack(anchor=W)
    rad2.pack(anchor=W)
    btnRAD= Button(Reg4, text="next>>>",bg="#B0E0E6",bd=1,command=lambda: rad3(r.get()))# 
    btnRAD.pack(anchor=W)

    btncancel= Button(Reg4, text="cancel",bg="#B0E0E6",bd=1,command=cancel)#bg="white", 
    btncancel.pack(anchor=W)
    


def reg3():
    Reg2.destroy()
    #frame1.config(state='enabled')
    txtUsername.configure(state='normal')            
    txtPassword.configure(state='normal')
    

    #========================buuttons=====================================

    btnReg.configure(state='normal')
    btnLgn.configure(state='normal')
    btnCp.configure(state='normal')
    
clock=30    
def clock1():
    global clock
    clock=int(clock)-1
    my_label.config(text="YOU HAVE ATTEMPTD THREE TIME \n sorry you have to wait " + str(clock) + " secs")
    my_label.after(1000, clock1)
    my_label.after(30000, reg3)

times = 5
def loginchecker():

    
    username1=username_verify.get()
    password1=password_verify.get()


    list_of_files=os.listdir('C:/Users/CODEIRONSIDE/OneDrive/project1')
    def submit():
            global  my2
            global Reg2
            global my_label
            global times
            times=int(times)-1
            if username1 in list_of_files:
                file1 = open(username1, 'r')
                verify =file1.read().splitlines()
                
                if password1 in verify:
                    response=messagebox.showinfo("LOGIN SUCESSFUL", "you are going to the main page")
                    if response=="ok":
                        options()
            elif times==2:
                #frame1.disabled()
                Reg2=Toplevel(root)
                Reg2.title("please wait")
                Reg2.iconbitmap("favico.ico")
                Reg2.resizable(width=False, height=False)
                Reg2.overrideredirect(True)
                #Reg2.transient(1)
                #Reg2.protocol("WM_DELETE_WINDOW", CancelCommand)
                Reg2.config(bg="white")
                #Reg2.geometry("250x80+0+0")
                txtUsername.configure(state='disabled')
                
                
                txtPassword.configure(state='disabled')
                

                #========================buuttons=====================================

                btnReg.configure(state='disabled')
                btnLgn.configure(state='disabled')
                btnCp.configure(state='disabled')
                
                my2= Frame(Reg2, relief=RIDGE,bg="white",bd=3)
                my_label=Label(my2, text="", bg="white")
                clock1()
                my_label.pack(pady=20)
                my2.pack()
                
                

                

                    
            elif times==0:
                response=messagebox.askokcancel("OOPS", 'sorry you have exceeded the number of trials \n would you like to register')
                if response==1:
                    Window2()
                else:
                    root.destroy()
            else:
                response=messagebox.askokcancel('OOPS', 'you have ' + str(times) + " attempts" )
                if response==1:
                    txtUsername.delete(0,'end')
                    txtPassword.delete(0, 'end')
                else:
                    root.destroy()


    submit()            
        
       





def Window1():
    global btnReg
    global btnLgn
    global btnCp
    global frame1
    global root
    root = Tk()
    global username_verify
    global password_verify
    global txtUsername
    global txtPassword

    
    #RegCP.destroy()
    username_verify= StringVar()
    password_verify=StringVar()
    root.title("login screen")
    root.iconbitmap("favico.ico")
    root.resizable(width=False, height=False)
    root.config(bg="white")
    #root.wm_attributes("-topmost", True)
    #root.wm_attributes("-disabled", True)
    #root.wm_attributes("-transparentcolor", "white")
    #====================================================================

    
    frame1=Frame(root, bg ="white", relief=RAISED)
    frame1.pack()

    logo2 = ImageTk.PhotoImage(Image.open("ndass2.jpg"))



    lblTitle=Label(frame1, image=logo2)
    lblTitle.grid(row=0,column=0,columnspan=3, pady =20)
     
    
    
    #==========================================================
    Loginframe1= LabelFrame(frame1,width=2000,height=400,pady=5, font=("arial", 11,"bold"), relief=RIDGE, bg="#9EF489", bd=2)
    Loginframe1.grid(row=1,column=0)

    Loginframe2= LabelFrame(frame1,width=3000,height=600,pady=5, font=("arial", 11,"bold"), relief=RIDGE, bg="#9EF489", bd=2)
    Loginframe2.grid(row=2,column=0)
    #===================label and entry===============================

    lblUsername = Label(Loginframe1,width=31, text="username* ", bg="#9EF489",font=("helvetica", 10,'bold'))
    lblUsername.grid(row=0,column=0)
    txtUsername = Entry(Loginframe1, relief =RIDGE, bd=3, justify="center",font=("helvetica", 10,'bold'),textvariable =username_verify)
    txtUsername.grid(row=1,column=0)
    lblPassword = Label(Loginframe1, text="password* ",width=31,justify="center", bg="#9EF489", font=("helvetica", 10, 'bold'))
    lblPassword.grid(row=2,column=0)
    txtPassword = Entry(Loginframe1,width=23, justify="center", show="*", textvariable =password_verify)
    txtPassword.grid(row=3,column=0)

    #========================buuttons=====================================
    
    btnReg = Button(Loginframe2, text="register",relief=RAISED, bg='#EE1D99',padx=10,pady=10,font=("Arial Rounded MT Bold",8),command= Window2)
    btnReg.grid(row=0,column=0)
    btnLgn = Button(Loginframe2, text="login",relief=RAISED, bg='yellow',font=("Arial Rounded MT Bold",8),padx=10,pady=10,command = loginchecker)
    #btnLgn.bind("<Return>", loginchecker)
    btnLgn.grid(row=0,column=1)
    btnCp= Button(Loginframe2, text="forget password?",relief=RAISED,font=("Arial Rounded MT Bold",8),padx=9,pady=9, bg='#B61DEE', command=forgetpass)
    btnCp.grid(row=0,column=2)
    label4 = Label(Loginframe2, width=31, text="login screen copyright ©", bg="#9EF489", font=("helvetica", 10))
    label4.grid(row=4,column=0,columnspan=3)
    
    #root.withdraw()
    root.mainloop()




    

    
def ok():
    response=messagebox.askokcancel("confirm", "do you want to continue")
    if response==1:
        submitReg()


    

def submitReg():
    #===============================
        #i=info
    first_nameI=first_name.get()
    last_nameI=last_name.get()
    DOBI=click1.get()
    DOBI1=click2.get()
    DOBI2=click3.get()
    SOGi=click4.get()
    Genderi=click5.get()
    addressi= address.get()
    phone_numberi=phone_number.get()
    usernamei=username.get()
    passwordi=password.get()
    confirmed_passwordi=confirmed_password.get()

    
    
    
    try:
        if len(first_nameI)==0 or first_nameI.isdigit():
            response=messagebox.showinfo("HELP", "invalid input")
            if response =="ok":
                FNentry.delete(0, 'end')
        if len(last_nameI)==0 or last_nameI.isdigit():
            response=messagebox.showinfo("HELP", "invalid input")
            if response =="ok":
                LNentry.delete(0, 'end')
                    
        
        
        
        if  len(addressi)==0:
            response=messagebox.showinfo("HELP", "invalid input")
            if response =="ok":
                ADDentry.delete(0, 'end')

        if len(phone_numberi)==0 or phone_numberi.isalpha():
            response=messagebox.showinfo("HELP", "invalid input")
            if response =="ok":    
                PNentry.delete(0, 'end')

        if len(usernamei)==0 or usernamei.isdigit():
            response=messagebox.showinfo("HELP", "invalid input")
            if response =="ok":    
                UNentry.delete(0, 'end')
        
        if confirmed_passwordi == passwordi and re.search("[a-z]", passwordi) and re.search("[a-z]", confirmed_passwordi) and re.search("[A-Z]",passwordi) and re.search("[A-Z]", confirmed_passwordi)  and confirmed_passwordi.isalnum and passwordi.isalnum() and len(confirmed_passwordi)>8 and len(passwordi) >8:
            file= open(usernamei, "w")
            file.write(usernamei + "\n")
            file.write(confirmed_passwordi + "\n")
            file.write(phone_numberi + "\n")    
            file.write(first_nameI + "\n")
            file.write(last_nameI + "\n")
            file.write(addressi + "\n")
            file.write(Genderi + "\n")
            file.write(SOGi + "\n")
            file.write(DOBI + "\n")
            file.write(DOBI1 + "\n")
            file.write(DOBI2 + "\n")
            
            file.close() 
            Reg.destroy()
            
                                            
         


        else:
            response=messagebox.showinfo("HELP", "invalid input")
            if response =="ok":
                Pentry.delete(0, 'end')
                FCentry.delete(0, 'end')
                       

               
    except FileNotFoundError and FileExistsError:
        response=messagebox.askokcancel("HELP", "do you want to quit the registeration process")
        if response =="ok":
            Reg.destroy()
        else:
            messagebox.showinfo("RETURN", "you are going back to the registeration page")

    




def Window2():
    global Reg
    global Window2
    global frame2
    global framer

    global first_name
    global last_name
    global DOB
    global SOG
    global Gender
    global address
    global phone_number
    global username
    global password
    global confirmed_password

    #=========global entry============
    global label5
    global FNentry
    global LNentry
    global ADDentry
    global click1
    global click2
    global click3
    global click4
    global click5
    global PNentry
    global UNentry
    global Pentry
    global FCentry
    global lblTitle

    root.deiconify()

    first_name=StringVar()
    last_name=StringVar()
    DOB= StringVar()
    SOG=StringVar()
    Gender=StringVar()
    address=StringVar()
    phone_number=StringVar()
    username= StringVar()
    password=StringVar()
    confirmed_password=StringVar()

    Reg=Toplevel()
    Reg.title("registeration page")
    Reg.iconbitmap("favico.ico")
    Reg.geometry("1000x450+100+50")
    bgf= ImageTk.PhotoImage(Image.open("bgfor1.jpg"))
    lblTitle=Label(Reg, image=bgf)
    lblTitle.place(x=0,y=0, relwidth=1,relheight=1)

    Reg.resizable(width=False, height=False)
    Reg.config(bg="brown")

    frame4=Frame(Reg, bg ="#DBDDDA", relief=FLAT,bd=2)
    frame4.place(x=150,y=100, width=689,height=270)

    #============combobox details for  states==========='
    options=['abia',"adamawa","akwa-ibom", 'anambra', 'Bauchi','Bayelsa','Benue','Borno','Cross River','Delta',
    'Ebonyi','Edo','Ekiti','Enugu','Gombe','Imo','Jigawa','Kaduna','Kano','Katsina','Kebbi','Kogi','Kwara','Lagos','Nasarawa',
    'Niger','Ogun','Ondo','Osun','Oyo','Plateau','Rivers','Sokoto','Taraba','Yobe','Zamfara','F.C.T']
    options1=['male','female','others']
    options2=['1','2','3','4','5','6','7','8','9','10','11','12','13','12','12','10','17','18','19','20','21','22','23','24','25','26','27','28',
    '29','30','31']
    options3=['January','February','March','April','May','June','July','August','September', 'October','November','December']
    #options4=['Monday','Tuesday','Wednessday','Thursday','Friday','Sarturday']
    options5=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
    '1975', '1976','1977','1978','1979','1980','1981','1982','1983','1984','1984','1985','1986','1987','1988','1989','1990',
    '1991','1992','1992','1993','1994','1995','1996','1997','1998']


    #=============registerion details========
    framet=LabelFrame(frame4, bg ="white", relief=RIDGE, bd =2)
    framet.grid(row=0,column=0)
    frame2=LabelFrame(framet, bg ="#DBDDDA",width=200, height=2000, relief=FLAT, bd =1)
    frame2.grid(row=0,column=0)
    framer=LabelFrame(framet, bg ="#DBDDDA",width=600, height=150, relief=FLAT, bd =1)
    framer.grid(row=0,column=1)
    frameb=LabelFrame(Reg, bg ="#20165B",width=30, height=20, relief=FLAT, bd =1)
    frameb.place(x=430,y=350, width=130,height=58)
    
    framey=LabelFrame(frameb, bg ="white", relief=RIDGE, bd =2)
    framey.pack()
    
    #===============================================================================
    label5=Label(frame2, text="first name", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    label5.grid(row=1,padx=1,sticky=W)
    FNentry =Entry(frame2, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER, textvariable= first_name)
    FNentry.grid(row= 2, padx=1,ipady=3)

    LNlabel=Label(frame2, text="last name", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    LNlabel.grid(row= 3, padx=1)
    LNentry =Entry(frame2, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER, textvariable=last_name)
    LNentry.grid(row= 5,padx=1,ipady=3)
    #=========================================================
    click1=StringVar()

    DOBbox= ttk.Combobox(frame2, value=options2,width=2)
    DOBbox.current(0)
    DOBbox.place(x=75,y=128)
    DOBlabel=Label(frame2, text="date of birth", bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    DOBlabel.grid(row= 6, padx=1)
    DOBlabel=Label(frame2, text=" ", bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    DOBlabel.grid(row= 8, padx=1)
    #========
    click2 =StringVar()
    DOBbox1=ttk.Combobox(frame2,value=options3,width=10)
    DOBbox1.current(0)
    DOBbox1.place(x=120,y=128)

    #======
    click3 =StringVar()
    DOBbox2=ttk.Combobox(frame2,value=options5, width=4)
    DOBbox2.current(0)
    DOBbox2.place(x=210,y=128)
    #DOBentry =Entry(frame2, ef= RIDGE, bd=3, width=20, justify= CENTER, textvariable=DOB)
    #DOBentry.grid(row= 8, column=0)

   #=========================================================
    SOGlabel=Label(frame2, text="state of origin", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    SOGlabel.grid(row= 9, column=0)
    #SOGentry =Entry(frame2, relief= RIDGE, bd=3, width=20, justify= CENTER, textvariable=SOG)
    #SOGentry.grid(row= 11, column=0)
    click4 =StringVar()
    DOBbox3=ttk.Combobox(frame2,value=options, width=25)
    DOBbox3.current(0)
    DOBbox3.grid(row=11, column=0)
    #===========================================================================

    Glabel=Label(frame2, text="Gender", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    Glabel.grid(row= 12, column=0)


    click5 =StringVar()
    DOBbox4=ttk.Combobox(frame2,value=options1, width=25)
    DOBbox4.current(0)
    DOBbox4.grid(row=13, column=0,pady=5)

    #======================================================
    #Gentry =Entry(frame2, relief= RIDGE, bd=3, width=20, justify= CENTER,textvariable=Gender)
    #Gentry.grid(row= 12, column=0)

    #============labelframe2====================================================================
    ADDlabel=Label(framer, text="address", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    ADDlabel.grid(row= 12, column=0)
    ADDentry =Entry(framer, relief= GROOVE, bd=1, bg='white', width=30, justify= CENTER, textvariable=address)
    ADDentry.grid(row= 17, column=0,ipady=3)
    PNlabel=Label(framer, text="phone number", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    PNlabel.grid(row= 18, column=0)
    PNentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER,textvariable=phone_number)
    PNentry.grid(row=19, column=0,ipady=3)
    UNlabel=Label(framer, text="username", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    UNlabel.grid(row= 20, column=0)
    UNentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER, textvariable=username)
    UNentry.grid(row= 23, column=0,ipady=3)
    Plabel=Label(framer, text="password", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    Plabel.grid(row= 24, column=0)
    Pentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER, show="*", textvariable=password)
    Pentry.grid(row= 26, column=0,ipady=3)
    FClabel=Label(framer, text="confirmed password", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
    FClabel.grid(row= 27, column=0)
    FCentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER, show="*", textvariable=confirmed_password)
    FCentry.grid(row= 29, column=0,pady=3,ipady=2)
    
    #==================buttons===================================

    bitt1=Button(framey, width=20, text="submit",bg="#20165B", fg="#EC9787",relief=FLAT,font=("Arial Rounded MT Bold",25),command=submitReg)
    bitt1.pack()#grid(row= 30, column=0)

    Reg.mainloop()






Window1()
 