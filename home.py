from tkinter import*
from PIL import Image, ImageTk
Login=Tk()

taskBarHeight = 40

#Configurações da tela
Login.title("Acesso ao Petshop Dogin's")
Login.resizable(False, False)

width_screen = Login.winfo_screenwidth()
height_screen = Login.winfo_screenheight() - taskBarHeight

width = 1240
height = 790

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

Login.maxsize(width, height)
Login.minsize(width, height)

Login.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
Login.configure(bg='#fff')

#Estilização do Login
logo_quilon_origin = Image.open("img/QuilOn.png")
logo_resize = logo_quilon_origin.resize((140, 50), Image.ANTIALIAS)
logoquilon = ImageTk.PhotoImage(logo_resize)
logo_qui = Label(Login, image = logoquilon , bg="#fff")
logo_qui.place(relx = .150, rely = .10, anchor = "n")


Login.mainloop()