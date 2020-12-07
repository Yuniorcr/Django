from tkinter import *
raiz = Tk()
raiz.title("window test")
#raiz.resizable(False,False) #ancho y alto
raiz.iconbitmap("232.ico")
#raiz.geometry("960x540")
#raiz.config(bg="#33CFFF")

MyFrame = Frame()
MyFrame.pack(fill="both", expand="true")
MyFrame.config(bg="red")
MyFrame.config(width="650", height="350")


















raiz.mainloop()