from tkinter import*
from PIL import Image, ImageTk
import subprocess
Login=Tk()

taskBarHeight = 40

#Configurações da tela
Login.title("Acesso ao QuilOn")
Login.resizable(False, False)

width_screen = Login.winfo_screenwidth()
height_screen = Login.winfo_screenheight() - taskBarHeight

width =990
height = 600

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

Login.maxsize(width, height)
Login.minsize(width, height)

Login.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
Login.configure(bg='#fff')

def entre():
    subprocess.run(["python", "Home.py"])

#titulo bem-vindo
txt_titulo = Label(Login,text="Bem-vindo" ,bg = "#FFF", font=("Helvetica 20"), foreground="#F6AA1C")
txt_titulo.place(relx = .119, rely = .30, anchor = "n")

#Estilização do Login
logo_quilon_origin = Image.open("img/QuilOn.png")
logo_resize = logo_quilon_origin.resize((210, 50), Image.ANTIALIAS)
logoquilon = ImageTk.PhotoImage(logo_resize)
logo_qui = Label(Login, image = logoquilon , bg="#fff")
logo_qui.place(relx = .140, rely = .40, anchor = "n")

#botao acesse sua conta
acesso = Button(Login, text = "Acesso a sua conta", bd = 0, bg = "#FFF", fg = "#777777", font = "Helvetica 10 underline", activebackground = "#FFF", activeforeground = "#777")
acesso.place(relx = .120, rely = .53, anchor = "n")

#titulo entrar
txt_titulo = Label(Login,text="Entrar" ,bg = "#FFF", font=("Helvetica 20"), foreground="#F6AA1C")
txt_titulo.place(relx = .460, rely = .20, anchor = "n")
#faça login
txt_titulo = Label(Login,text="Faça o login na sua conta" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .460, rely = .27, anchor = "n")

#campo nome
txt_nome = Label(Login,text="Nome" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .390, rely = .35, anchor = "n")
lbl_nome = Entry(Login)
lbl_nome.place(relx = .465, rely = .39, anchor = "n" ,  width="190" , height="20")

#campo senha
txt_valor = Label(Login,text="Senha" ,bg = "#FFF", font=("Helvetica 10"))
txt_valor.place(relx = .390, rely = .45, anchor = "n")
lbl_valor = Entry(Login)
lbl_valor.place(relx = .465, rely = .49, anchor = "n",  width="190" , height="20")

#campo tipo de acesso
txt_duracao = Label(Login,text="Tipo de acesso" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .413, rely = .55, anchor = "n")
lbl_duracao = Entry(Login)
lbl_duracao.place(relx = .465, rely = .59, anchor = "n",  width="190" , height="20")

#botões de Entrar
btn_salvar=Button(Login,text="Entrar", bg="#F6AA1C", command=lambda:entre())
btn_salvar.place(relx = .4650, rely = .70, anchor = "n",  width="80" , height="25")

# segunda parte criar contar

#titulo entrar
txt_titulo = Label(Login,text="Crie sua conta" ,bg = "#FFF", font=("Helvetica 20"), foreground="#F6AA1C")
txt_titulo.place(relx = .755, rely = .20, anchor = "n")
#faça login
txt_titulo = Label(Login,text="Faça o login na sua conta" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .755, rely = .27, anchor = "n")

#campo nome
txt_nome = Label(Login,text="Nome" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .690, rely = .35, anchor = "n")
lbl_nome = Entry(Login)
lbl_nome.place(relx = .765, rely = .39, anchor = "n" ,  width="190" , height="20")

#campo email
txt_valor = Label(Login,text="E-mail" ,bg = "#FFF", font=("Helvetica 10"))
txt_valor.place(relx = .690, rely = .45, anchor = "n")
lbl_valor = Entry(Login)
lbl_valor.place(relx = .765, rely = .49, anchor = "n",  width="190" , height="20")

#campo senha
txt_duracao = Label(Login,text="Senha" ,bg = "#FFF", font=("Helvetica 10"))
txt_duracao.place(relx = .690, rely = .55, anchor = "n")
lbl_duracao = Entry(Login)
lbl_duracao.place(relx = .765, rely = .59, anchor = "n",  width="190" , height="20")

#botao cadastre-se
btn_salvar=Button(Login,text="Cadastre-se", bg="#F6AA1C")
btn_salvar.place(relx = .765, rely = .70, anchor = "n",  width="80" , height="25")

Login.mainloop()