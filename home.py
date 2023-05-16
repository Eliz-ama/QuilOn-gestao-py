from tkinter import*
from PIL import Image, ImageTk
home=Tk()

taskBarHeight = 40

#Configurações da tela
home.title("Acesso ao QuilOn")
home.resizable(False, False)

width_screen = home.winfo_screenwidth()
height_screen = home.winfo_screenheight() - taskBarHeight

width =990
height = 600

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

home.maxsize(width, height)
home.minsize(width, height)

home.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
home.configure(bg='#fff')

#Estilização do logo
logo_quilon_origin = Image.open("img/QuilOn.png")
logo_resize = logo_quilon_origin.resize((210, 50), Image.ANTIALIAS)
logoquilon = ImageTk.PhotoImage(logo_resize)
logo_qui = Label(home, image = logoquilon , bg="#fff")
logo_qui.place(relx = .505, rely = .03, anchor = "n")

#Estilização do usuario
usuario_origin = Image.open("img/usuario.png")
logo_resize = usuario_origin.resize((100, 100), Image.ANTIALIAS)
usu = ImageTk.PhotoImage(logo_resize)
usuario = Label(home, image = usu , bg="#fff")
usuario.place(relx = .150, rely = .20, anchor = "n")

#adm
txt_nome = Label(home,text="Administrador(a) Elisângela da silva" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .150, rely = .40, anchor = "n")

#faça cadastro
cadastro_origin = Image.open("img/1.png")
cadastro_resize = cadastro_origin.resize((15, 15), Image.ANTIALIAS)
cad = ImageTk.PhotoImage(cadastro_resize)
cadastro = Label(home, image = cad , bg="#fff")
cadastro.place(relx = .05, rely = .50, anchor = "n")
txt_titulo = Label(home,text="Cadastro" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .09, rely = .50, anchor = "n")

#faça quilombos
quilombos_origin = Image.open("img/2.png")
quilombos_resize = quilombos_origin.resize((15, 15), Image.ANTIALIAS)
qui = ImageTk.PhotoImage(quilombos_resize)
quilombos = Label(home, image = qui , bg="#fff")
quilombos.place(relx = .05, rely = .55, anchor = "n")
txt_titulo = Label(home,text="Quilombos" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .10, rely = .55, anchor = "n")

#faça painel de vendas
painel_origin = Image.open("img/3.png")
painel_resize = painel_origin.resize((20, 20), Image.ANTIALIAS)
pai = ImageTk.PhotoImage(painel_resize)
painel = Label(home, image = pai , bg="#fff")
painel.place(relx = .05, rely = .60, anchor = "n")
txt_titulo = Label(home,text="Painel de vendas" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .12, rely = .60, anchor = "n")

#faça eventos
eventos_origin = Image.open("img/4.png")
eventos_resize = eventos_origin.resize((15, 15), Image.ANTIALIAS)
eve = ImageTk.PhotoImage(eventos_resize)
eventos = Label(home, image = eve , bg="#fff")
eventos.place(relx = .05, rely = .65, anchor = "n")
txt_titulo = Label(home,text="Eventos" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .09, rely = .65, anchor = "n")

#faça chat
chat_origin = Image.open("img/5.png")
chat_resize = chat_origin.resize((15, 15), Image.ANTIALIAS)
cha = ImageTk.PhotoImage(chat_resize)
chat = Label(home, image = cha , bg="#fff")
chat.place(relx = .05, rely = .70, anchor = "n")
txt_titulo = Label(home,text="Chat" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .08, rely = .70, anchor = "n")

#faça configuração
configuracoes_origin = Image.open("img/6.png")
configuracoes_resize = configuracoes_origin.resize((15, 15), Image.ANTIALIAS)
conf = ImageTk.PhotoImage(configuracoes_resize)
configuracoes = Label(home, image = conf , bg="#fff")
configuracoes.place(relx = .05, rely = .75, anchor = "n")
txt_titulo = Label(home,text="Configuração" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .10, rely = .75, anchor = "n")

#imagem
imagem_origin = Image.open("img/7.png")
imagem_resize = imagem_origin.resize((500, 500), Image.ANTIALIAS)
img = ImageTk.PhotoImage(imagem_resize)
imagem = Label(home, image = img , bg="#fff")
imagem.place(relx = .700, rely = .15, anchor = "n")

home.mainloop()