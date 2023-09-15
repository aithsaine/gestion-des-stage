import tkinter as tk
from tkinter import messagebox as ms
from src.Stage import Stage
import re
from tkinter import ttk

MainPage = tk.Tk()
MainPage.attributes('-fullscreen',True)
MainPage.config(width=1000,height=600)
MainPage.title("Gestion Des Stage")
lb = tk.Label(MainPage,text="Made By Ismail Ait Hsaine",font="Times 12 italic bold").place(x=800,y=560)
# MainPage.overrideredirect(True)
MainPage.resizable(False,False)
MainPage.iconbitmap(("icon.ico"))





def FormuleAdd():
    myframe = tk.Frame(MainPage,width=850,height=600,bg="#bef1ff")
    myframe.place(x=150,y=0)
    lb = tk.Label(myframe,text="Made By Ismail Ait Hsaine",font="Times 12 italic bold",bg="#bef1ff").place(x=650,y=560)

    tk.Label(myframe,text="Ajouter Un Stage A la Liste Des Stage",bg="#bef1ff", fg="blue",font="Times 20 italic bold").place(x=200,y=10)
    # id
    tk.Label(myframe,text="Id",font="Times 20 italic bold",bg="#bef1ff").place(x=90,y=100)
    enId = tk.Entry(myframe,font="Times 20 italic bold",bd=3,bg="#bef1ff")
    enId.place(x=300,y=100,width=300,height=30)
    # name
    tk.Label(myframe,text="Name",font="Times 20 italic bold",bg="#bef1ff").place(x=90,y=150)
    enName = tk.Entry(myframe,font="Times 20 italic bold",bd=3,bg="#bef1ff")
    enName.place(x=300,y=150,width=300,height=30)
    # duration
    tk.Label(myframe,text="Duration",font="Times 20 italic bold",bg="#bef1ff").place(x=90,y=200)
    enDuration = tk.Entry(myframe,font="Times 20 italic bold",bd=3,bg="#bef1ff")
    enDuration.place(x=300,y=200,width=300,height=30)
    # price
    tk.Label(myframe,text="Price",font="Times 20 italic bold",bg="#bef1ff").place(x=90,y=250)
    enPrice = tk.Entry(myframe,font="Times 20 italic bold",bd=3,bg="#bef1ff")
    enPrice.place(x=300,y=250,width=300,height=30)
    # Domain
    tk.Label(myframe,text="Domain",font="Times 20 italic bold",bg="#bef1ff").place(x=90,y=300)
    enDomain = tk.Entry(myframe,font="Times 20 italic bold",bd=3,bg="#bef1ff")
    enDomain.place(x=300,y=300,width=300,height=30)


    def addData():
        id = enId.get()
        name  = enName.get()
        duration = enDuration.get()
        price = enPrice.get()
        domain = enDomain.get()
        ids = Stage.GetAllIds()
        if id == "" or name == "" or duration == "" or price == "" or domain == "":
            ms.showerror("error","Fill all Informations!!!!!")
        else:
            clean = True
            if not re.search(r"^\d+$",id) or not re.search(r"^\d+\.?\d+$",price) or not re.search(r"\d+",duration):
                ms.showerror("Error","id and Price and Duration must be numbers")
                clean = False
            if len(name)<5:
                ms.showerror("Error","the  name  must be more than 5 characters")
                clean = False
            if clean:
                if int (id)  in ids:
                    ms.showerror("Error","Id Alrady existe")
                else:
                    obj = Stage(int(id),name,int(duration),float(price),domain)
                    obj.AddToData()
                    enId.delete(0,tk.END)
                    enName.delete(0,tk.END)
                    enDuration.delete(0,tk.END)
                    enPrice.delete(0,tk.END)
                    enDomain.delete(0,tk.END)
                    ms.showinfo("Congrate","Stage Saved with success")      
    


    btn_ajouter = tk.Button(myframe,text="Ajouter",relief="ridge",bg="#7ae2ff",command=addData)
    btn_ajouter.place(x=300,y=400,width=120,height=35)
    btn_annuler = tk.Button(myframe,text="Annuler",relief="ridge",bg="#7ae2ff")
    btn_annuler.place(x=480,y=400,width=120,height=35)


# ********************************************************************************
FormuleAdd()


def FormuleEdit():
    myframe = tk.Frame(MainPage,width=850,height=600,bg="#bef1ff")
    myframe.place(x=150,y=0)
    lb = tk.Label(myframe,text="Made By Ismail Ait Hsaine",font="Times 12 italic bold",bg="#bef1ff").place(x=650,y=560)

    tk.Label(myframe,text="Afficher tout les Stage",bg="#bef1ff", fg="blue",font="Times 20 italic bold").place(x=300,y=10)
    data = Stage.getAllData()
    table = ttk.Treeview(myframe,heigh=15,columns=(1,2,3,4,5),show="headings")
    table.heading(1,text="id")
    table.heading(2,text="Name")
    table.heading(3,text="Duration")
    table.heading(4,text="Price")
    table.heading(5,text="Domain")
    table.column(1,anchor=tk.CENTER,width=120)
    table.column(2,width=200,anchor=tk.CENTER)
    table.column(3,width=130,anchor=tk.CENTER)
    table.column(4,width=150,anchor=tk.CENTER)
    table.column(5,width=220,anchor=tk.CENTER)
    table.place(x=5,y=150)




    def ModifyOrDeleteFormule(id):
        values = table.item(table.focus())["values"]
        if len(values):
            myframe2 = tk.Frame(MainPage,width=850,height=600,bg="#bef1ff")
            myframe2.place(x=150,y=0)
            tk.Label(myframe2,text="Supprimer et Modifier Un Stage",bg="#bef1ff", fg="blue",font="Times 20 italic bold").place(x=200,y=10)
    # id
        
            tk.Label(myframe2,text='id',font="Times 20 italic bold",bg="#bef1ff").place(x=30,y=100)
            lbId = tk.Label(myframe2,text=values[0],font="Times 20 italic bold",bg="#bef1ff")
            lbId.place(x=300,y=100,width=300,height=30)
# name  
            tk.Label(myframe2,text="Name",font="Times 20 italic bold",bg="#bef1ff").place(x=30,y=150)
            enN = tk.Entry(myframe2,font="Times 20 italic bold",bd=3,bg="#bef1ff")
            enN.place(x=300,y=150,width=300,height=30)
            enN.insert(0,values[1])
            # duration
            tk.Label(myframe2,text="Duration",font="Times 20 italic bold",bg="#bef1ff").place(x=30,y=200)
            enDu = tk.Entry(myframe2,font="Times 20 italic bold",bd=3,bg="#bef1ff")
            enDu.place(x=300,y=200,width=300,height=30)
            enDu.insert(0,values[2][0:-5])
            # price
            tk.Label(myframe2,text="Price",font="Times 20 italic bold",bg="#bef1ff").place(x=30,y=250)
            enP = tk.Entry(myframe2,font="Times 20 italic bold",bd=3,bg="#bef1ff")
            enP.place(x=300,y=250,width=300,height=30)
            enP.insert(0,values[3][0:-3])
            # Domain
            tk.Label(myframe2,text="Domain",font="Times 20 italic bold",bg="#bef1ff").place(x=30,y=300)
            enDo = tk.Entry(myframe2,font="Times 20 italic bold",bd=3,bg="#bef1ff")
            enDo.place(x=300,y=300,width=300,height=30)
            enDo.insert(0,values[4].lower())
        else:
            ms.showinfo("Info","click inside row ")



            #commande of delete button 

        def delete():
            if ms.askokcancel("question","are you sure to delete this stage"):
                Stage.deleteById(int(values[0]))
                ms.showinfo("congrate",f"the stage with id = {values[0]} was deleted with success")
                FormuleEdit()


        def Modify():
            accept = ms.askokcancel("question","are you sure to update Stage info")
            if accept:
                new_name = enN.get()
                new_price = enP.get()
                new_duration = enDu.get()
                new_domain = enDo.get()
                if new_domain == "" or new_duration == "" or new_name == "" or new_price =="":
                    ms.showerror("attention","fill all inputs")
                else:
                    ok = True
                    if not re.search(r"^\d+\.?\d$",new_price) or not re.search(r"\d+",new_duration):
                        ms.showerror("Attention","the new price and new duration must be numbers")
                        ok  = False
                    if len(new_name)<5 :
                        ms.showerror("Error","the new name  must be more than 5 characters")
                        ok = False
                    if ok:
                        Stage.UpdateData(int(values[0]),{"name":new_name.capitalize(),"duration":new_duration,"price":float(new_price),"domain":new_domain.upper()})
                        ms.showinfo("congrat",'Stage info updated with success')
                        FormuleEdit()

        btn_Modify = tk.Button(myframe2,text="Modifier",command=Modify,relief="ridge",bg="#7ae2ff")
        btn_Modify.place(x=300,y=400,width=120,height=35)
        btn_Delete = tk.Button(myframe2,text="Supprimer",command=delete,relief="ridge",bg="#7ae2ff")
        btn_Delete.place(x=480,y=400,width=120,height=35)
        



    table.bind("<Double Button-1>",ModifyOrDeleteFormule)
    for item in data:
        table.insert("",tk.END,values=(item["id"],item["name"],f'{item["duration"]} days',f"{item['price']} DH",item["domain"]))  
    


# **************************************************************************************


# Searsh Formulair

def SearshForm():
    myframe3 = tk.Frame(MainPage,width=850,height=600,bg="#bef1ff")
    myframe3.place(x=150,y=0)
    lb = tk.Label(myframe3,text="Made By Ismail Ait Hsaine",font="Times 12 italic bold",bg="#bef1ff").place(x=650,y=560)
    tk.Label(myframe3,text="chercher un Stage",bg="#bef1ff", fg="blue",font="Times 20 italic bold").place(x=300,y=10)
    var = tk.IntVar(myframe3)
    
    def ById():
        lbById = tk.Label(myframe3,text="Id rechercher : ",font="Times 12 italic bold",bg="#bef1ff")
        lbById.place(x=100,y=250)
        ids = Stage.GetAllIds()
        enIdRechercher = tk.Entry(myframe3,font="Times 20 italic bold",bd=3,bg="#bef1ff")
        enIdRechercher.place(x=250,y=250)
        

        def BtnIdSearsh():
            id = enIdRechercher.get()
            if id =="":
                ms.showerror("Error","Fill id Input")
            else:
                if not re.search(r"^\d+$",id):
                    ms.showerror("Error","Id must be number")
                else:
                    if int(id) not in ids:
                        ms.showinfo("Info","No Stage With This Id")
                    else:
                        item = Stage.findById(int(id))
                        itemcolumns = (item["id"],item["name"],item["duration"],item["price"],item["domain"])
                        resTbl = ttk.Treeview(myframe3,columns=(1,2,3,4,5),show="headings",heigh=4)
                        resTbl.heading(1,text="id")
                        resTbl.heading(2,text="Name")
                        resTbl.heading(3,text="Duration")
                        resTbl.heading(4,text="Price")
                        resTbl.heading(5,text="Domain")
                        resTbl.column(1,anchor=tk.CENTER,width=120)
                        resTbl.column(2,width=200,anchor=tk.CENTER)
                        resTbl.column(3,width=130,anchor=tk.CENTER)
                        resTbl.column(4,width=150,anchor=tk.CENTER)
                        resTbl.column(5,width=220,anchor=tk.CENTER)
                        resTbl.insert("",tk.END,values=itemcolumns)
                        resTbl.place(x=2,y=400)
        buttonSearshById = tk.Button(myframe3,text="Chercher",relief="ridge",bg="#7ae2ff",width=15,command=BtnIdSearsh)
        buttonSearshById.place(x=250,y=350)
        buttonSearshByIdAnnuler = tk.Button(myframe3,text="Annuler",relief="ridge",bg="#7ae2ff",width=15,command=SearshForm)
        buttonSearshByIdAnnuler.place(x=400,y=350)
    def ByDomain():
        list_domains = Stage.ListDomains()
        lbBydo = tk.Label(myframe3,text="choisie Domain : ",font="Times 12 italic bold",bg="#bef1ff")
        lbBydo.place(x=100,y=250)
        domain_name = tk.StringVar()
        domain_name.set(list_domains[0])
        list_opts = tk.OptionMenu(myframe3,domain_name,*list_domains)
        list_opts.place(x=250,y=250)




    byId = tk.Radiobutton(myframe3,text="Searsh by id",value=1,variable=var,indicator = 0,
                background = "light blue",width=20,height=2,command=ById)
    byId.place(x=150,y=120)
    byDomain = tk.Radiobutton(myframe3,text="Searsh by Domaine",value=2,variable=var,indicator = 0,
                background = "light blue",width=20,height=2,command=ByDomain)
    byDomain.place(x=400,y=120)








# **************************************************************************************



btnsFrame = tk.Frame(MainPage,width=150,height=600,bg="#000000")
btnsFrame.place(x=0,y=0)


addbtn = tk.Button(btnsFrame,text="Ajouter Un Stage",width=14,height=2,bg="black",fg="white",font="Times 11 italic bold",border=5,command=FormuleAdd)

addbtn.place(x=5,y=10)
deleteBtn = tk.Button(btnsFrame,text="Afficher les stages",width=14,height=2,bg="black",fg="white",font="Times 11 italic bold",border=5,command=FormuleEdit)
deleteBtn.place(x=5,y=80)
deleteBtn = tk.Button(btnsFrame,text="Chercher Un Stage",width=14,height=2,bg="black",fg="white",font="Times 11 italic bold",border=5,command=SearshForm)
deleteBtn.place(x=5,y=150)
















""" addIMG = tk.PhotoImage(file="add.png")
btnAdd = tk.Button(btnsFrame,image=addIMG)
btnAdd.place(x=10,y=10) """


MainPage.mainloop()

    