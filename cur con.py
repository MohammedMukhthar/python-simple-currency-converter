from tkinter import*


def d2i(*arg):
    var = float(a.get())
    v.set("%.2f" % (var*65.4)) #change value "65.4" according the daily rate'''

def p2i(*arg):
    var = float(a.get())
    v.set("%.2f" % (var*90.0)) #pond rate'''
    
def dh2i(*arg):
    var = float(a.get())
    v.set("%.2f" % (var*17.6)) #dirham rate'''

def r2i(*arg):
    var = float(a.get())
    v.set("%.2f" % (var*17.0))  #riyal rate'''
    
def e2i(*arg):
    var = float(a.get())
    v.set("%.2f" % (var*70.4))   #euro rate'''
    
root  = Tk()
root.title("Currency Converter")
f = Frame(root)
f.grid(column = 1, row = 3 )

a = StringVar()
v = StringVar()

Label(f,text="Enter the Amount : ").grid(column = 2, row = 0)
Entry(f,textvariable = a).grid(column = 3 ,row =0 )
Button(f,text="Dollar",width = "20",command = d2i).grid(column = 1 , row = 1)
Button(f,text="Pond",width = "20",command = p2i).grid(column =2 , row = 1)
Button(f,text="Dirham",width = "20",command = dh2i).grid(column = 3 , row = 1)
Button(f,text="Riyal",width = "20",command = r2i).grid(column = 4 , row = 1)
Button(f,text="Euro",width = "20",command = e2i).grid(column = 5 , row = 1)
Label(f,text="   INR :", width = "20").grid(column = 2, row = 3)   
Label(f,textvariable = v ,width ="20" ).grid(column =3, row = 3)
root.mainloop()
