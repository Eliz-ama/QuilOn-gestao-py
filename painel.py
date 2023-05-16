from tkinter import*
from PIL import Image, ImageTk
painel=Tk()

taskBarHeight = 40

#Configurações da tela
painel.title("Acesso ao QuilOn")
painel.resizable(False, False)

width_screen = painel.winfo_screenwidth()
height_screen = painel.winfo_screenheight() - taskBarHeight

width =1150
height = 600

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

painel.maxsize(width, height)
painel.minsize(width, height)

painel.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
painel.configure(bg='#fff')

#Estilização do logo
logo_quilon_origin = Image.open("img/QuilOn.png")
logo_resize = logo_quilon_origin.resize((220, 60), Image.ANTIALIAS)
logoquilon = ImageTk.PhotoImage(logo_resize)
logo_qui = Label(painel, image = logoquilon , bg="#fff")
logo_qui.place(relx = .500, rely = .03, anchor = "n")

#links
txt_gra = Label(painel,text="Gráfico de receitas" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_gra.place(relx = .05, rely = .13, anchor = "n")

txt_pe = Label(painel,text="Periodo" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_pe.place(relx = .200, rely = .13, anchor = "n")

txt_re = Label(painel,text="Rentabilidade" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_re.place(relx = .350, rely = .13, anchor = "n")

txt_pro = Label(painel,text="Produtos" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_pro.place(relx = .500, rely = .13, anchor = "n")

txt_sa = Label(painel,text="Saldo" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_sa.place(relx = .650, rely = .13, anchor = "n")

txt_ve = Label(painel,text="Vendas" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_ve.place(relx = .800, rely = .13, anchor = "n")

txt_fe = Label(painel,text="Ferramentas" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_fe.place(relx = .950, rely = .13, anchor = "n")

imagem_origin = Image.open("img/8.png")
imagem_resize = imagem_origin.resize((900, 400), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem_resize)
logo_img = Label(painel, image = imagem , bg="#fff")
logo_img.place(relx = .500, rely = .25, anchor = "n")

painel.mainloop()