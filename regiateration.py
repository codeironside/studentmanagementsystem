from tkinter import *
import sys
import os
from PIL import ImageTk,Image
from tkinter import messagebox
import re
from tkinter import ttk



Reg=Tk()
Reg.title("registeration page")
Reg.iconbitmap("favicon.ico")
Reg.geometry("1000x500+100+50")
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
options2=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28',
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
FNentry =Entry(frame2, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER)# textvariable= first_name)
FNentry.grid(row= 2, padx=1,ipady=3)

LNlabel=Label(frame2, text="last name", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
LNlabel.grid(row= 3, padx=1)
LNentry =Entry(frame2, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER)# textvariable=last_name)
LNentry.grid(row= 5,padx=1,ipady=3)
#=========================================================
clicked1=StringVar()

DOBbox= ttk.Combobox(frame2, value=options2,width=2)
DOBbox.current(0)
DOBbox.place(x=75,y=128)
DOBlabel=Label(frame2, text="date of birth", bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
DOBlabel.grid(row= 6, padx=1)
DOBlabel=Label(frame2, text=" ", bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
DOBlabel.grid(row= 8, padx=1)
#========
clicked2 =StringVar()
DOBbox1=ttk.Combobox(frame2,value=options3,width=10)
DOBbox1.current(0)
DOBbox1.place(x=120,y=128)

#======
clicked3 =StringVar()
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
clicked4 =StringVar()
DOBbox3=ttk.Combobox(frame2,value=options, width=25)
DOBbox3.current(0)
DOBbox3.grid(row=11, column=0)
#===========================================================================

Glabel=Label(frame2, text="Gender", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
Glabel.grid(row= 12, column=0)
clicked5 =StringVar()
DOBbox4=ttk.Combobox(frame2,value=options1, width=25)
DOBbox4.current(0)
DOBbox4.grid(row=14, column=0,pady=5)

#======================================================
#Gentry =Entry(frame2, relief= RIDGE, bd=3, width=20, justify= CENTER,textvariable=Gender)
#Gentry.grid(row= 14, column=0)

#============labelframe2====================================================================
ADDlabel=Label(framer, text="address", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
ADDlabel.grid(row= 15, column=0)
ADDentry =Entry(framer, relief= GROOVE, bd=1, bg='white', width=30, justify= CENTER)# textvariable=address)
ADDentry.grid(row= 17, column=0,ipady=3)
PNlabel=Label(framer, text="phone number", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
PNlabel.grid(row= 18, column=0)
PNentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER)#textvariable=phone_number)
PNentry.grid(row=19, column=0,ipady=3)
UNlabel=Label(framer, text="username", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
UNlabel.grid(row= 20, column=0)
UNentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER)#textvariable=username)
UNentry.grid(row= 23, column=0,ipady=3)
Plabel=Label(framer, text="password", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
Plabel.grid(row= 24, column=0)
Pentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER, show="*")# textvariable=password)
Pentry.grid(row= 26, column=0,ipady=3)
FClabel=Label(framer, text="confirmed password", width=30, bg='#DBDDDA',font=("Arial Rounded MT Bold",13))
FClabel.grid(row= 27, column=0)
FCentry =Entry(framer, relief= GROOVE,bg='white', bd=1, width=30, justify= CENTER, show="*")# textvariable=confirmed_password)
FCentry.grid(row= 29, column=0,pady=3,ipady=2)

#==================buttons===================================

bitt1=Button(framey, width=20, text="submit",bg="#20165B", fg="#EC9787",relief=FLAT,font=("Arial Rounded MT Bold",25))#command=submitReg)
bitt1.pack()#grid(row= 30, column=0)


Reg.mainloop()