from tkinter import *

window=Tk()
window.geometry("700x500")


def calculate():
    Gado_Gado=e1.get()
    Soto=e2.get()
    Es_jeruk=e3.get()
    Es_teh=e4.get()
    print(type(Es_teh))
    total=(int(Gado_Gado)*10)+(int(Soto)*10)+(int(Es_jeruk)*3)+(int(Es_teh)*3)
    label12=Label(window,text=total,font="times 18")
    label12.place(x=100,y=360)


label6=Label(window,text="Cheap Food",font="times 30 bold")
label6.place(x=350,y=20,anchor="center")



#_________menu section_______

label1=Label(window,text="MENU",font="times 28 bold")
label1.place(x=550,y=70)

label2=Label(window,text="Gado Gado    Rp 10", font="times 18")
label2.place(x=450,y=120)


label3=Label(window,text="Soto               Rp 10", font="times 18")
label3.place(x=450,y=147)


label4=Label(window,text="Es jeruk         Rp 3", font="times 18")
label4.place(x=450,y=178)


label5=Label(window,text="Es teh            Rp 3", font="times 18")
label5.place(x=450,y=210)



#____________ billing section __________

label7=Label(window,text="Select the items",font="times 20 bold")
label7.place(x=70,y=70)


label8=Label(window,text="Gado Gado",font="times 18")
label8.place(x=20,y=120)

e1=Entry(window)
e1.place(x=20,y=150)


label9=Label(window,text="Soto",font="times 18")
label9.place(x=250,y=120)

e2=Entry(window)
e2.place(x=250,y=150)


label10=Label(window,text="Es jeruk",font="times 18")
label10.place(x=20,y=200)

e3=Entry(window)
e3.place(x=20,y=230)


label10=Label(window,text="Es teh",font="times 18")
label10.place(x=250,y=200)

e4=Entry(window)
e4.place(x=250,y=230)

b2=Button(window,text='bill' ,width=20,command=calculate)
b2.place(x=100,y=300)

 
window.mainloop()