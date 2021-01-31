from tkinter import *
from tkinter import filedialog 
import os
from pathlib import Path

#Global Variable
DIR_PATH=''
DIR_NAME={1:"Photos",2:"Videos",3:"PDF",4:"Word",5:"Excel",6:"RAR",7:"ZIP",8:"Softwares",9:"PPT",10:"TextFile"}
CWD=os.getcwd()
LIST=[1,1,1,1,1,1,1,1,1,1]

class Infra_S:
    def __init__(self,root):
        self.root=root
        self.root.title("File Arranger")
        self.root.geometry("800x600+0+0")
        self.root.configure(background='sky blue')

        #Internal Functions
        def select_dir():
            global DIR_PATH,LIST,CWD
            DIR_PATH=filedialog.askdirectory()
            self.dirname.set(DIR_PATH)
            CWD=DIR_PATH
            self.en_var1.set(f"{DIR_PATH}/Photos")
            self.en_var2.set(f"{DIR_PATH}/Videos")
            self.en_var3.set(f"{DIR_PATH}/PDF")
            self.en_var4.set(f"{DIR_PATH}/Word")
            self.en_var5.set(f"{DIR_PATH}/Excel")
            self.en_var6.set(f"{DIR_PATH}/RAR")
            self.en_var7.set(f"{DIR_PATH}/ZIP")
            self.en_var8.set(f"{DIR_PATH}/Softwares")
            self.en_var9.set(f"{DIR_PATH}/PPT")
            self.en_var10.set(f"{DIR_PATH}/TextFile")
            if any(File.endswith(".img") or File.endswith(".jpg") or File.endswith(".jpeg") or File.endswith(".png") for File in os.listdir(DIR_PATH)):
                self.chk1.configure(state='normal')
                self.chk1a.configure(state='normal')
                LIST[0]=1
            else:
                self.chk1.config(state=DISABLED)
                self.chk1a.config(state=DISABLED)
                LIST[0]=0
            if any(File.endswith(".mp4") or File.endswith(".mkv") for File in os.listdir(DIR_PATH)):
                self.chk2.configure(state='normal')
                self.chk2a.configure(state='normal')
                LIST[1]=1
            else:
                self.chk2.config(state=DISABLED)
                self.chk2a.config(state=DISABLED)
                LIST[1]=0
            if any(File.endswith(".pdf") for File in os.listdir(DIR_PATH)):
                self.chk3.configure(state='normal')
                self.chk3a.configure(state='normal')
                LIST[2]=1
            else:
                self.chk3.config(state=DISABLED)
                self.chk3a.config(state=DISABLED)
                LIST[2]=0
            if any(File.endswith(".doc") or File.endswith(".docx") for File in os.listdir(DIR_PATH)):
                self.chk4.configure(state='normal')
                self.chk4a.configure(state='normal')
                LIST[3]=1
            else:
                self.chk4.config(state=DISABLED)
                self.chk4a.config(state=DISABLED)
                LIST[3]=0
            if any(File.endswith(".xlsx") or File.endswith(".csv") for File in os.listdir(DIR_PATH)):
                self.chk5.configure(state='normal')
                self.chk5a.configure(state='normal')
                LIST[4]=1
            else:
                self.chk5.config(state=DISABLED)
                self.chk5a.config(state=DISABLED)
                LIST[4]=0
            if any(File.endswith(".rar") or File.endswith(".rar4") for File in os.listdir(DIR_PATH)):
                self.chk6.configure(state='normal')
                self.chk6a.configure(state='normal')
                LIST[5]=1
            else:
                self.chk6.config(state=DISABLED)
                self.chk6a.config(state=DISABLED)
                LIST[5]=0
            if any(File.endswith(".zip") for File in os.listdir(DIR_PATH)):
                self.chk7.configure(state='normal')
                self.chk7a.configure(state='normal')
                LIST[6]=1
            else:
                self.chk7.config(state=DISABLED)
                self.chk7a.config(state=DISABLED)
                LIST[6]=0
            if any(File.endswith(".exe") for File in os.listdir(DIR_PATH)):
                self.chk8.configure(state='normal')
                self.chk8a.configure(state='normal')
                LIST[7]=1
            else:
                self.chk8.config(state=DISABLED)
                self.chk8a.config(state=DISABLED)
                LIST[7]=0
            if any(File.endswith(".ppt") or File.endswith(".pptx") for File in os.listdir(DIR_PATH)):
                self.chk9.configure(state='normal')
                self.chk9a.configure(state='normal')
                LIST[8]=1
            else:
                self.chk9.config(state=DISABLED)
                self.chk9a.config(state=DISABLED)
                LIST[8]=0
            if any(File.endswith(".txt") for File in os.listdir(DIR_PATH)):
                self.chk10.configure(state='normal')
                self.chk10a.configure(state='normal')
                LIST[9]=1
            else:
                self.chk10.config(state=DISABLED)
                self.chk10a.config(state=DISABLED)
                LIST[9]=0
            if 1 in LIST:
                self.chka.configure(state='normal')
            else:
                self.chka.config(state=DISABLED)
                
        def Exit():
            exit()

        def custom_folder_name():
            if self.varb.get() == 1:
                self.en1.configure(state='normal')
                self.en2.configure(state='normal')
                self.en3.configure(state='normal')
                self.en4.configure(state='normal')
                self.en5.configure(state='normal')
                self.en6.configure(state='normal')
                self.en7.configure(state='normal')
                self.en8.configure(state='normal')
                self.en9.configure(state='normal')
                self.en10.configure(state='normal')
                self.en_var1.set('')
                self.en_var2.set('')
                self.en_var3.set('')
                self.en_var4.set('')
                self.en_var5.set('')
                self.en_var6.set('')
                self.en_var7.set('')
                self.en_var8.set('')
                self.en_var9.set('')
                self.en_var10.set('')
            else:
                self.en1.config(state=DISABLED)
                self.en2.config(state=DISABLED)
                self.en3.config(state=DISABLED)
                self.en4.config(state=DISABLED)
                self.en5.config(state=DISABLED)
                self.en6.config(state=DISABLED)
                self.en7.config(state=DISABLED)
                self.en8.config(state=DISABLED)
                self.en9.config(state=DISABLED)
                self.en10.config(state=DISABLED)
                self.en_var1.set(f"{CWD}/Photos")
                self.en_var2.set(f"{CWD}/Videos")
                self.en_var3.set(f"{CWD}/PDF")
                self.en_var4.set(f"{CWD}/Word")
                self.en_var5.set(f"{CWD}/Excel")
                self.en_var6.set(f"{CWD}/RAR")
                self.en_var7.set(f"{CWD}/ZIP")
                self.en_var8.set(f"{CWD}/Softwares")
                self.en_var9.set(f"{CWD}/PPT")
                self.en_var10.set(f"{CWD}/TextFile")

            if self.var1a.get() == 1:
                self.en1.configure(state='normal')
                self.en_var1.set('')
                LIST[0]=1
            else:
                self.en1.config(state=DISABLED)
                self.en_var1.set(f"{CWD}/Photos")
                LIST[0]=0
            if self.var2a.get() == 1:
                self.en2.configure(state='normal')
                self.en_var2.set('')
                LIST[1]=1
            else:
                self.en2.config(state=DISABLED)
                self.en_var2.set(f"{CWD}/Videos")
                LIST[1]=0
            if self.var3a.get() == 1:
                self.en3.configure(state='normal')
                self.en_var3.set('')
                LIST[2]=1
            else:
                self.en3.config(state=DISABLED)
                self.en_var3.set(f"{CWD}/PDF")
                LIST[2]=0
            if self.var4a.get() == 1:
                self.en4.configure(state='normal')
                self.en_var4.set('')
                LIST[3]=1
            else:
                self.en4.config(state=DISABLED)
                self.en_var4.set(f"{CWD}/Word")
                LIST[3]=0
            if self.var5a.get() == 1:
                self.en5.configure(state='normal')
                self.en_var5.set('')
                LIST[4]=1
            else:
                self.en5.config(state=DISABLED)
                self.en_var5.set(f"{CWD}/Excel")
                LIST[4]=0
            if self.var6a.get() == 1:
                self.en6.configure(state='normal')
                self.en_var6.set('')
                LIST[5]=1
            else:
                self.en6.config(state=DISABLED)
                self.en_var6.set(f"{CWD}/RAR")
                LIST[5]=0
            if self.var7a.get() == 1:
                self.en7.configure(state='normal')
                self.en_var7.set('')
                LIST[6]=1
            else:
                self.en7.config(state=DISABLED)
                self.en_var7.set(f"{CWD}/ZIP")
                LIST[6]=0
            if self.var8a.get() == 1:
                self.en8.configure(state='normal')
                self.en_var8.set('')
                LIST[7]=1
            else:
                self.en8.config(state=DISABLED)
                self.en_var8.set(f"{CWD}/Softwares")
                LIST[7]=0
            if self.var9a.get() == 1:
                self.en9.configure(state='normal')
                self.en_var9.set('')
                LIST[8]=1
            else:
                self.en9.config(state=DISABLED)
                self.en_var9.set(f"{CWD}/PPT")
                LIST[8]=0
            if self.var10a.get() == 1:
                self.en10.configure(state='normal')
                self.en_var10.set('')
                LIST[9]=1
            else:
                self.en10.config(state=DISABLED)
                self.en_var10.set(f"{CWD}/TextFile")
                LIST[9]=0
            


        def select_all():
            if self.vara.get() == 1:
                if LIST[0] == 1:
                    self.var1.set(1)
                if LIST[1] == 1:
                    self.var2.set(1)
                if LIST[2] == 1:
                    self.var3.set(1)
                if LIST[3] == 1:
                    self.var4.set(1)
                if LIST[4] == 1:
                    self.var5.set(1)
                if LIST[5] == 1:
                    self.var6.set(1)
                if LIST[6] == 1:
                    self.var7.set(1)
                if LIST[7] == 1:
                    self.var8.set(1)
                if LIST[8] == 1:
                    self.var9.set(1)
                if LIST[9] == 1:
                    self.var10.set(1)
            else:
                self.var1.set(0)
                self.var2.set(0)
                self.var3.set(0)
                self.var4.set(0)
                self.var5.set(0)
                self.var6.set(0)
                self.var7.set(0)
                self.var8.set(0)
                self.var9.set(0)
                self.var10.set(0)

        def check_all_select():
            if self.var1.get()==0 or self.var2.get()==0 or self.var3.get()==0 or self.var4.get()==0 or self.var5.get()==0 or self.var6.get()==0 or self.var7.get()==0 or self.var8.get()==0 or self.var9.get()==0 or self.var10.get()==0:
                self.vara.set(0)
                #btn1["state"] = "DISABLED"

        # def run():
        #     global DIR_NAME

        #     #Directory_Custom_Name_Updation
        #     if(var1a.get()==1): DIR_NAME[1]==en_var1.get()
        #     if(var2a.get()==1): DIR_NAME[2]==en_var2.get()
        #     if(var3a.get()==1): DIR_NAME[3]==en_var3.get()
        #     if(var4a.get()==1): DIR_NAME[4]==en_var4.get()
        #     if(var5a.get()==1): DIR_NAME[5]==en_var5.get()
        #     if(var6a.get()==1): DIR_NAME[6]==en_var6.get()
        #     if(var7a.get()==1): DIR_NAME[7]==en_var7.get()
        #     if(var8a.get()==1): DIR_NAME[8]==en_var8.get()
        #     if(var9a.get()==1): DIR_NAME[9]==en_var9.get()
        #     if(var10a.get()==1): DIR_NAME[10]==en_var10.get()

        #     #Function calling with diretory name parameter
        #     #{MOVE}
        #     if(var_rad.get()==1):
        #         if(var1.get()==1): main_C.PICTURES_M(DIR_NAME.get(1))
        #         if(var2.get()==1): main_C.VIDEOS_M(DIR_NAME.get(2))
        #         if(var3.get()==1): main_C.PDF_M(DIR_NAME.get(3))
        #         if(var4.get()==1): main_C.DOCX_M(DIR_NAME.get(4))
        #         if(var5.get()==1): main_C.EXCEL_M(DIR_NAME.get(5))
        #         if(var6.get()==1): main_C.RAR_M(DIR_NAME.get(6))
        #         if(var7.get()==1): main_C.ZIP_M(DIR_NAME.get(7))
        #         if(var8.get()==1): main_C.SOFTWARES_M(DIR_NAME.get(8))
        #         if(var9.get()==1): main_C.PPT_M(DIR_NAME.get(9))
        #         if(var10.get()==1): main_C.TEXTFILE_M(DIR_NAME.get(10))
        #     #{COPY}
        #     elif(var_rad.get()==2):
        #         if(var1.get()==1): main_C.PICTURES_C(DIR_NAME.get(1))
        #         if(var2.get()==1): main_C.VIDEOS_C(DIR_NAME.get(2))
        #         if(var3.get()==1): main_C.PDF_C(DIR_NAME.get(3))
        #         if(var4.get()==1): main_C.DOCX_C(DIR_NAME.get(4))
        #         if(var5.get()==1): main_C.EXCEL_C(DIR_NAME.get(5))
        #         if(var6.get()==1): main_C.RAR_C(DIR_NAME.get(6))
        #         if(var7.get()==1): main_C.ZIP_C(DIR_NAME.get(7))
        #         if(var8.get()==1): main_C.SOFTWARES_C(DIR_NAME.get(8))
        #         if(var9.get()==1): main_C.PPT_C(DIR_NAME.get(9))
        #         if(var10.get()==1): main_C.TEXTFILE_C(DIR_NAME.get(10))
        #     else: pass

        #Frame-1
        frame1=Frame(self.root,padx=9,pady=9)
        frame1.place(x=0,y=10,width=660,height=50)
        lb1=Label(frame1,text="Selected Folder",bg='#2c2c2c',fg="white",font=("",15,"bold"))
        lb1.pack(side=LEFT)
        self.dirname=StringVar()
        #global CWD
        self.dirname.set(CWD)
        self.lb2=Label(frame1,bg='#2c2c2c',text="",fg="white",textvariable=self.dirname,font=("",15,"bold"))
        self.lb2.pack(side=LEFT,padx=(10,0))

        bt1=Button(frame1,text="Browse",command=select_dir)
        bt1.pack(side=LEFT,padx=(10,0))


        #Frame-2
        frame2=Frame(self.root,padx=9,pady=9)
        frame2.place(x=1,y=70,width=580,height=260)
        self.var1=IntVar(frame2)
        self.var2=IntVar(frame2)
        self.var3=IntVar(frame2)
        self.var4=IntVar(frame2)
        self.var5=IntVar(frame2)
        self.var6=IntVar(frame2)
        self.var7=IntVar(frame2)
        self.var8=IntVar(frame2)
        self.var9=IntVar(frame2)
        self.var10=IntVar(frame2)
        self.chk1=Checkbutton(frame2,text="Photos",variable=self.var1,command=check_all_select)
        self.chk2=Checkbutton(frame2,text="Videos",variable=self.var2,command=check_all_select)
        self.chk3=Checkbutton(frame2,text="PDF",variable=self.var3,command=check_all_select)
        self.chk4=Checkbutton(frame2,text="Word",variable=self.var4,command=check_all_select)
        self.chk5=Checkbutton(frame2,text="Excel",variable=self.var5,command=check_all_select)
        self.chk6=Checkbutton(frame2,text="RAR",variable=self.var6,command=check_all_select)
        self.chk7=Checkbutton(frame2,text="ZIP",variable=self.var7,command=check_all_select)
        self.chk8=Checkbutton(frame2,text="Softwares",variable=self.var8,command=check_all_select)
        self.chk9=Checkbutton(frame2,text="PPT",variable=self.var9,command=check_all_select)
        self.chk10=Checkbutton(frame2,text="TextFile",variable=self.var10,command=check_all_select)
        self.chk1.grid(column=0, row=1, sticky=W)
        self.chk2.grid(column=0, row=2, sticky=W)
        self.chk3.grid(column=0, row=3, sticky=W)
        self.chk4.grid(column=0, row=4, sticky=W)
        self.chk5.grid(column=0, row=5, sticky=W)
        self.chk6.grid(column=0, row=6, sticky=W)
        self.chk7.grid(column=0, row=7, sticky=W)
        self.chk8.grid(column=0, row=8, sticky=W)
        self.chk9.grid(column=0, row=9, sticky=W)
        self.chk10.grid(column=0, row=10, sticky=W)
        
        self.var1a=IntVar(frame2)
        self.var2a=IntVar(frame2)
        self.var3a=IntVar(frame2)
        self.var4a=IntVar(frame2)
        self.var5a=IntVar(frame2)
        self.var6a=IntVar(frame2)
        self.var7a=IntVar(frame2)
        self.var8a=IntVar(frame2)
        self.var9a=IntVar(frame2)
        self.var10a=IntVar(frame2)
        self.chk1a=Checkbutton(frame2,text='',variable=self.var1a,command=custom_folder_name)
        self.chk2a=Checkbutton(frame2,text='',variable=self.var2a,command=custom_folder_name)
        self.chk3a=Checkbutton(frame2,text='',variable=self.var3a,command=custom_folder_name)
        self.chk4a=Checkbutton(frame2,text='',variable=self.var4a,command=custom_folder_name)
        self.chk5a=Checkbutton(frame2,text='',variable=self.var5a,command=custom_folder_name)
        self.chk6a=Checkbutton(frame2,text='',variable=self.var6a,command=custom_folder_name)
        self.chk7a=Checkbutton(frame2,text='',variable=self.var7a,command=custom_folder_name)
        self.chk8a=Checkbutton(frame2,text='',variable=self.var8a,command=custom_folder_name)
        self.chk9a=Checkbutton(frame2,text='',variable=self.var9a,command=custom_folder_name)
        self.chk10a=Checkbutton(frame2,text='',variable=self.var10a,command=custom_folder_name)
        self.chk1a.grid(column=8, row=1, sticky=W)
        self.chk2a.grid(column=8, row=2, sticky=W)
        self.chk3a.grid(column=8, row=3, sticky=W)
        self.chk4a.grid(column=8, row=4, sticky=W)
        self.chk5a.grid(column=8, row=5, sticky=W)
        self.chk6a.grid(column=8, row=6, sticky=W)
        self.chk7a.grid(column=8, row=7, sticky=W)
        self.chk8a.grid(column=8, row=8, sticky=W)
        self.chk9a.grid(column=8, row=9, sticky=W)
        self.chk10a.grid(column=8, row=10, sticky=W)

        self.en_var1=StringVar(frame2)
        self.en_var2=StringVar(frame2)
        self.en_var3=StringVar(frame2)
        self.en_var4=StringVar(frame2)
        self.en_var5=StringVar(frame2)
        self.en_var6=StringVar(frame2)
        self.en_var7=StringVar(frame2)
        self.en_var8=StringVar(frame2)
        self.en_var9=StringVar(frame2)
        self.en_var10=StringVar(frame2)
        self.en_var1.set(f"{CWD}\Photos")
        self.en_var2.set(f"{CWD}\Videos")
        self.en_var3.set(f"{CWD}\PDF")
        self.en_var4.set(f"{CWD}\Word")
        self.en_var5.set(f"{CWD}\Excel")
        self.en_var6.set(f"{CWD}\RAR")
        self.en_var7.set(f"{CWD}\ZIP")
        self.en_var8.set(f"{CWD}\Softwares")
        self.en_var9.set(f"{CWD}\PPT")
        self.en_var10.set(f"{CWD}\TextFile")
        self.en1=Entry(frame2,state=DISABLED,textvariable=self.en_var1,width=50)
        self.en2=Entry(frame2,state=DISABLED,textvariable=self.en_var2,width=50)
        self.en3=Entry(frame2,state=DISABLED,textvariable=self.en_var3,width=50)
        self.en4=Entry(frame2,state=DISABLED,textvariable=self.en_var4,width=50)
        self.en5=Entry(frame2,state=DISABLED,textvariable=self.en_var5,width=50)
        self.en6=Entry(frame2,state=DISABLED,textvariable=self.en_var6,width=50)
        self.en7=Entry(frame2,state=DISABLED,textvariable=self.en_var7,width=50)
        self.en8=Entry(frame2,state=DISABLED,textvariable=self.en_var8,width=50)
        self.en9=Entry(frame2,state=DISABLED,textvariable=self.en_var9,width=50)
        self.en10=Entry(frame2,state=DISABLED,textvariable=self.en_var10,width=50)
        self.en1.grid(column=10, row=1, sticky=W)
        self.en2.grid(column=10, row=2, sticky=W)
        self.en3.grid(column=10, row=3, sticky=W)
        self.en4.grid(column=10, row=4, sticky=W)
        self.en5.grid(column=10, row=5, sticky=W)
        self.en6.grid(column=10, row=6, sticky=W)
        self.en7.grid(column=10, row=7, sticky=W)
        self.en8.grid(column=10, row=8, sticky=W)
        self.en9.grid(column=10, row=9, sticky=W)
        self.en10.grid(column=10, row=10, sticky=W)


        #Frame-3
        frame3=Frame(self.root,padx=9,pady=9)
        frame3.place(x=1,y=340,width=480,height=130)
        self.vara=IntVar(frame3)
        self.varb=IntVar(frame3)
        self.var_rad=IntVar(frame3, 1)
        self.chka=Checkbutton(frame3,text="Select All",variable=self.vara,command=select_all)
        self.chkb=Checkbutton(frame3,text="Choose Custom Folder Name",variable=self.varb,command=custom_folder_name)
        self.rada=Radiobutton(frame3,text="Move",variable=self.var_rad,value=1)
        self.radb=Radiobutton(frame3,text="Copy",variable=self.var_rad,value=2)
        self.chka.grid(column=0,row=0,sticky=W)
        self.chkb.grid(column=2,row=0,sticky=W)
        self.rada.grid(column=0,row=1,sticky=W)
        self.radb.grid(column=2,row=1,sticky=W)

        btn1=Button(frame3,text="Proceed",bg="#000000",fg="white",font=("",15,"bold"),command=self.run).grid(column=0, row=7, sticky=W)
        btn2=Button(frame3,text="Exit",bg="#000000",fg="white",command=Exit,font=("",15,"bold")).grid(column=1, row=7, sticky=W)


        #Checking filetype that exist on the     selected Folder
        if not any(File.endswith(".img") or File.endswith(".jpg") or File.endswith(".jpeg") or File.endswith(".png") for File in os.listdir(".")):
            self.chk1.config(state=DISABLED)
            self.chk1a.config(state=DISABLED)
            LIST[0]=0
        if not any(File.endswith(".mp4") or File.endswith(".mkv") for File in os.listdir(".")):
            self.chk2.config(state=DISABLED)
            self.chk2a.config(state=DISABLED)
            LIST[1]=0
        if not any(File.endswith(".pdf") for File in os.listdir(".")):
            self.chk3.config(state=DISABLED)
            self.chk3a.config(state=DISABLED)
            LIST[2]=0
        if not any(File.endswith(".doc") or File.endswith(".docx") for File in os.listdir(".")):
            self.chk4.config(state=DISABLED)
            self.chk4a.config(state=DISABLED)
            LIST[3]=0
        if not any(File.endswith(".xlsx") or File.endswith(".csv") for File in os.listdir(".")):
            self.chk5.config(state=DISABLED)
            self.chk5a.config(state=DISABLED)
            LIST[4]=0
        if not any(File.endswith(".rar") or File.endswith(".rar4") for File in os.listdir(".")):
            self.chk6.config(state=DISABLED)
            self.chk6a.config(state=DISABLED)
            LIST[5]=0
        if not any(File.endswith(".zip") for File in os.listdir(".")):
            self.chk7.config(state=DISABLED)
            self.chk7a.config(state=DISABLED)
            LIST[6]=0
        if not any(File.endswith(".exe") for File in os.listdir(".")):
            self.chk8.config(state=DISABLED)
            self.chk8a.config(state=DISABLED)
            LIST[7]=0
        if not any(File.endswith(".pptx") or File.endswith(".ppt") for File in os.listdir(".")):
            self.chk9.config(state=DISABLED)
            self.chk9a.config(state=DISABLED)
            LIST[8]=0
        if not any(File.endswith(".txt") for File in os.listdir(".")):
            self.chk10.config(state=DISABLED)
            self.chk10a.config(state=DISABLED)
            LIST[9]=0
        if not 1 in LIST:
            self.chka.config(state=DISABLED)

        mainloop()

    def run(self):
            global DIR_NAME

            #Directory_Custom_Name_Updation
            if(self.var1a.get()==1): DIR_NAME[1]=self.en_var1.get()
            if(self.var2a.get()==1): DIR_NAME[2]=self.en_var2.get()
            if(self.var3a.get()==1): DIR_NAME[3]=self.en_var3.get()
            if(self.var4a.get()==1): DIR_NAME[4]=self.en_var4.get()
            if(self.var5a.get()==1): DIR_NAME[5]=self.en_var5.get()
            if(self.var6a.get()==1): DIR_NAME[6]=self.en_var6.get()
            if(self.var7a.get()==1): DIR_NAME[7]=self.en_var7.get()
            if(self.var8a.get()==1): DIR_NAME[8]=self.en_var8.get()
            if(self.var9a.get()==1): DIR_NAME[9]=self.en_var9.get()
            if(self.var10a.get()==1): DIR_NAME[10]=self.en_var10.get()

            #Function calling with diretory name parameter
            #{MOVE}
            if(self.var_rad.get()==1):
                if(self.var1.get()==1): main_C.PICTURES_M(DIR_NAME.get(1))
                if(self.var2.get()==1): main_C.VIDEOS_M(DIR_NAME.get(2))
                if(self.var3.get()==1): main_C.PDF_M(DIR_NAME.get(3))
                if(self.var4.get()==1): main_C.DOCX_M(DIR_NAME.get(4))
                if(self.var5.get()==1): main_C.EXCEL_M(DIR_NAME.get(5))
                if(self.var6.get()==1): main_C.RAR_M(DIR_NAME.get(6))
                if(self.var7.get()==1): main_C.ZIP_M(DIR_NAME.get(7))
                if(self.var8.get()==1): main_C.SOFTWARES_M(DIR_NAME.get(8))
                if(self.var9.get()==1): main_C.PPT_M(DIR_NAME.get(9))
                if(self.var10.get()==1): main_C.TEXTFILE_M(DIR_NAME.get(10))
            #{COPY}
            elif(self.var_rad.get()==2):
                if(self.var1.get()==1): main_C.PICTURES_C(DIR_NAME.get(1))
                if(self.var2.get()==1): main_C.VIDEOS_C(DIR_NAME.get(2))
                if(self.var3.get()==1): main_C.PDF_C(DIR_NAME.get(3))
                if(self.var4.get()==1): main_C.DOCX_C(DIR_NAME.get(4))
                if(self.var5.get()==1): main_C.EXCEL_C(DIR_NAME.get(5))
                if(self.var6.get()==1): main_C.RAR_C(DIR_NAME.get(6))
                if(self.var7.get()==1): main_C.ZIP_C(DIR_NAME.get(7))
                if(self.var8.get()==1): main_C.SOFTWARES_C(DIR_NAME.get(8))
                if(self.var9.get()==1): main_C.PPT_C(DIR_NAME.get(9))
                if(self.var10.get()==1): main_C.TEXTFILE_C(DIR_NAME.get(10))
            else: pass



class MAIN_CODE:
    global DIR_PATH
    def __init__(self,root):
        self.path=Path()
    
    def DOCX_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.docx {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.docx {DIR_PATH}/{dir_name}"')
    
    def EXCEL_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.xls {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.csv {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.xls {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.csv {DIR_PATH}/{dir_name}"')
    
    def RAR_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.rar4 {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.rar {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.rar4 {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.rar {DIR_PATH}/{dir_name}"')
    
    def ZIP_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.zip {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.zip {DIR_PATH}/{dir_name}"')
    
    def SOFTWARES_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.exe {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.exe {DIR_PATH}/{dir_name}"')
    
    def PPT_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.ppt {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.pptx {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.ppt {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.pptx {DIR_PATH}/{dir_name}"')
    
    def PICTURES_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.jpg {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.jpeg {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.png {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.jpg {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.jpeg {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.png {DIR_PATH}/{dir_name}"')
    
    def TEXTFILE_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.txt {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.txt {DIR_PATH}/{dir_name}"')
    
    def PDF_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.pdf {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.pdf {DIR_PATH}/{dir_name}"')
    
    def VIDEOS_M(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "move {DIR_PATH}/*.mkv {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.mp4 {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.mkv {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "move {DIR_PATH}/*.mp4 {DIR_PATH}/{dir_name}"')
    
    
    def DOCX_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.docx {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.docx {DIR_PATH}/{dir_name}"')
    
    def EXCEL_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.csv {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.xls {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.csv {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.xls{DIR_PATH}/{dir_name}"')
    
    def RAR_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.rar4 {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.rar {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.rar4 {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.rar {DIR_PATH}/{dir_name}"')
    
    def ZIP_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.zip {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.zip {DIR_PATH}/{dir_name}"')
    
    def SOFTWARES_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.exe {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.exe {DIR_PATH}/{dir_name}"')
    
    def PPT_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.ppt {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.pptx {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.ppt {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.pptx {DIR_PATH}/{dir_name}"')
    
    def PICTURES_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.jpg  {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.jpeg {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.png {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.jpg  {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.jpeg {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.png {DIR_PATH}/{dir_name}"')
    
    def TEXTFILE_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.txt {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.txt {DIR_PATH}/{dir_name}"')
    
    def PDF_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.pdf {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.pdf {DIR_PATH}/{dir_name}"')
    
    def VIDEOS_C(self,dir_name):
        file_path=list(self.path.glob(f'{DIR_PATH}'))
        if not len(file_path)==0:
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.mp4 {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.mkv {DIR_PATH}/{dir_name}"')
        else:
            os.system(f'cmd /c "mkdir {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.mp4 {DIR_PATH}/{dir_name}"')
            os.system(f'cmd /c "xcopy {DIR_PATH}/*.mkv {DIR_PATH}/{dir_name}"')



#Classes & Objects
root=Tk()
main_C=MAIN_CODE(root)
infra=Infra_S(root)