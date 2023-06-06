from pymongo import MongoClient
from tkinter import *
from tkinter import ttk

import subprocess
import os

client = MongoClient("mongodb://localhost:27017")
db = client["QuilOn"]
collection = db["usuario"]

ca = Tk()

def criarUsuario(nome, sexo, data, rg, cpf , endereco, numero, bairro, cidade, estado, complemento, telefone, celular, nq, cq, ll, quilometro, email, senha):
    findemail = collection.count_documents({'email': email})

    if findemail == 0:
        collection.insert_one({
            'nome': nome,
            'sexo': sexo,
            'data': data,
            'rg': rg,
            'cpf': cpf,
            'endereco': endereco,
            'numero': numero,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'complemento': complemento,
            'telefone': telefone,
            'celular': celular,
            'nq': nq,
            'cq': cq,
            'll': ll,
            'quilometro': quilometro,
            'email': email,
            'senha': senha
        })

        subprocess.run(['python', 'rotateImg.py'])

def updateUsuario(nome, sexo, data, rg, cpf , endereco, numero, bairro, cidade, estado, complemento, telefone, celular, nq, cq, ll, quilometro, email, senha):
    collection.update_one({'email': email}, {'$set': {
           'nome': nome,
            'sexo': sexo,
            'data': data,
            'rg': rg,
            'cpf': cpf,
            'endereco': endereco,
            'numero': numero,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'complemento': complemento,
            'telefone': telefone,
            'celular': celular,
            'nq': nq,
            'cq': cq,
            'll': ll,
            'quilometro': quilometro,
            'email': email,
            'senha': senha
    }})

def excluirUsuario(email):
    collection.delete_one({'email': email})

taskBarHeight = 40

#Configurações da tela
ca.title("Acesso ao QuilOn")
ca.resizable(False, False)

width_screen = ca.winfo_screenwidth()
height_screen = ca.winfo_screenheight() - taskBarHeight

width =980
height = 600

posx = (width_screen / 2) - (width / 2)
posy = (height_screen / 2) - (height / 2)

ca.maxsize(width, height)
ca.minsize(width, height)

ca.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
ca.configure(bg='#fff')

def entre():
    subprocess.run(["python", "home.py"])

#titulo entrar
txt_titulo = Label(ca,text="Cadastre seu Quilombo" ,bg = "#FFF", font=("Helvetica 20"), foreground="#F6AA1C")
txt_titulo.place(relx = .50, rely = .05, anchor = "n")
#faça login
txt_titulo = Label(ca,text="Faça o login na sua conta" ,bg = "#FFF", font=("Helvetica 10 underline"), foreground="#777777")
txt_titulo.place(relx = .49, rely = .11, anchor = "n")

#campo nome
txt_nome = Label(ca,text="Nome" ,bg = "#FFF", font=("Helvetica 10"))
txt_nome.place(relx = .10, rely = .22, anchor = "n")
lbl_nome = Entry(ca)
lbl_nome.place(relx = .18, rely = .26, anchor = "n" ,  width="190" , height="20")

#campo sexo
txt_sexo = Label(ca,text="Sexo" ,bg = "#FFF", font=("Helvetica 10"))
txt_sexo.place(relx = .34, rely = .22, anchor = "n")
lbl_sexo = Entry(ca)
lbl_sexo.place(relx = .37, rely = .26, anchor = "n" ,  width="100" , height="20")

#campo data
txt_data = Label(ca,text="Data de nascimento" ,bg = "#FFF", font=("Helvetica 10"))
txt_data.place(relx = .53, rely = .22, anchor = "n")
lbl_data = Entry(ca)
lbl_data.place(relx = .53, rely = .26, anchor = "n" ,  width="120" , height="20")

#campo rg
txt_rg = Label(ca,text="Rg" ,bg = "#FFF", font=("Helvetica 10"))
txt_rg.place(relx = .66, rely = .22, anchor = "n")
lbl_rg = Entry(ca)
lbl_rg.place(relx = .70, rely = .26, anchor = "n" ,  width="100" , height="20")

#campo cpf
txt_cpf = Label(ca,text="CPF" ,bg = "#FFF", font=("Helvetica 10"))
txt_cpf.place(relx = .80, rely = .22, anchor = "n")
lbl_cpf = Entry(ca)
lbl_cpf.place(relx = .84, rely = .26, anchor = "n" ,  width="100" , height="20")

#campo endereço
txt_endereço = Label(ca,text="Endereço" ,bg = "#FFF", font=("Helvetica 10"))
txt_endereço.place(relx = .11, rely = .33, anchor = "n")
lbl_endereço = Entry(ca)
lbl_endereço.place(relx = .18, rely = .37, anchor = "n" ,  width="190" , height="20")

#campo numero
txt_numero = Label(ca,text="Numero" ,bg = "#FFF", font=("Helvetica 10"))
txt_numero.place(relx = .34, rely = .33, anchor = "n")
lbl_numero = Entry(ca)
lbl_numero.place(relx = .36, rely = .37, anchor = "n" ,  width="90" , height="20")

#campo bairro
txt_bairro = Label(ca,text="Bairro" ,bg = "#FFF", font=("Helvetica 10"))
txt_bairro.place(relx = .49, rely = .33, anchor = "n")
lbl_bairro = Entry(ca)
lbl_bairro.place(relx = .52, rely = .37, anchor = "n" ,  width="100" , height="20")

#campo cidade
txt_cidade = Label(ca,text="Cidade" ,bg = "#FFF", font=("Helvetica 10"))
txt_cidade.place(relx = .67, rely = .33, anchor = "n")
lbl_cidade = Entry(ca)
lbl_cidade.place(relx = .72, rely = .37, anchor = "n" ,  width="140" , height="20")

#campo estado
txt_estado = Label(ca,text="Estado" ,bg = "#FFF", font=("Helvetica 10"))
txt_estado.place(relx = .83, rely = .33, anchor = "n")
lbl_estado = Entry(ca)
lbl_estado.place(relx = .84, rely = .37, anchor = "n" ,  width="60" , height="20")

#campo complemento
txt_complemento = Label(ca,text="Complemento" ,bg = "#FFF", font=("Helvetica 10"))
txt_complemento.place(relx = .12, rely = .44, anchor = "n")
lbl_complemento = Entry(ca)
lbl_complemento.place(relx = .15, rely = .48, anchor = "n" ,  width="130" , height="20")

#campo telefone
txt_telefone = Label(ca,text="Telefone" ,bg = "#FFF", font=("Helvetica 10"))
txt_telefone.place(relx = .34, rely = .44, anchor = "n")
lbl_telefone = Entry(ca)
lbl_telefone.place(relx = .36, rely = .48, anchor = "n" ,  width="100" , height="20")

#campo celular
txt_celular = Label(ca,text="Celular" ,bg = "#FFF", font=("Helvetica 10"))
txt_celular.place(relx = .49, rely = .44, anchor = "n")
lbl_celular = Entry(ca)
lbl_celular.place(relx = .52, rely = .48, anchor = "n" ,  width="100" , height="20")

#campo nome do quilombo
txt_nq = Label(ca,text="Nome do quilombo" ,bg = "#FFF", font=("Helvetica 10"))
txt_nq.place(relx = .66, rely = .44, anchor = "n")
lbl_nq = Entry(ca)
lbl_nq.place(relx = .68, rely = .48, anchor = "n" ,  width="150" , height="20")

#campo certificação quilombola
txt_cq = Label(ca,text="Certificação Quilombola" ,bg = "#FFF", font=("Helvetica 10"))
txt_cq.place(relx = .86, rely = .44, anchor = "n")
lbl_cq = Entry(ca)
lbl_cq.place(relx = .87, rely = .48, anchor = "n" ,  width="170" , height="20")

#campo longitude e latitude
txt_ll = Label(ca,text="Longitude e Latitude" ,bg = "#FFF", font=("Helvetica 10"))
txt_ll.place(relx = .14, rely = .55, anchor = "n")
lbl_ll = Entry(ca)
lbl_ll.place(relx = .15, rely = .59, anchor = "n" ,  width="150" , height="20")

#campo quilometro
txt_quilometro = Label(ca,text="Quilometro" ,bg = "#FFF", font=("Helvetica 10"))
txt_quilometro.place(relx = .34, rely = .55, anchor = "n")
lbl_quilometro = Entry(ca)
lbl_quilometro.place(relx = .38, rely = .59, anchor = "n" ,  width="140" , height="20")

#campo email
txt_email = Label(ca,text="E-mail" ,bg = "#FFF", font=("Helvetica 10"))
txt_email.place(relx = .52, rely = .55, anchor = "n")
lbl_email = Entry(ca)
lbl_email.place(relx = .57, rely = .59, anchor = "n",  width="150" , height="20")

#campo senha
txt_senha = Label(ca,text="Senha" ,bg = "#FFF", font=("Helvetica 10"))
txt_senha.place(relx = .71, rely = .55, anchor = "n")
lbl_senha = Entry(ca)
lbl_senha.place(relx = .74, rely = .59, anchor = "n",  width="100" , height="20")

#botao 
btn_salvar=Button(ca,text="Cadastre-se", bg="#F6AA1C", command=lambda:criarUsuario(lbl_nome.get(),lbl_sexo.get(),lbl_data.get(),lbl_rg.get(),lbl_cpf.get(),lbl_endereço.get(),lbl_numero.get(),lbl_bairro.get(),lbl_cidade.get(),lbl_estado.get(),lbl_complemento.get(),lbl_telefone.get(),lbl_celular.get(),lbl_nq.get(),lbl_cq.get(),lbl_ll.get(),lbl_quilometro.get(), lbl_email.get(), lbl_senha.get()))
btn_salvar.place(relx = .20, rely = .800, anchor = "n",  width="80" , height="25")

btn_alterar = Button(ca, text="Alterar", bg="#F6AA1C", command=lambda: updateUsuario(lbl_nome.get(),lbl_sexo.get(),lbl_data.get(),lbl_rg.get(),lbl_cpf.get(),lbl_endereço.get(),lbl_numero.get(),lbl_bairro.get(),lbl_cidade.get(),lbl_estado.get(),lbl_complemento.get(),lbl_telefone.get(),lbl_celular.get(),lbl_nq.get(),lbl_cq.get(),lbl_ll.get(),lbl_quilometro.get(), lbl_email.get(), lbl_senha.get()))
btn_alterar.place(relx=.40, rely=.800, anchor="n", width="80", height="25")

btn_excluir=Button(ca,text="Excluir", bg="#F6AA1C", command=lambda:excluirUsuario(lbl_email.get()))
btn_excluir.place(relx = .60, rely = .800, anchor = "n",  width="80" , height="25")

def listar_dados():
    dados = collection.find()

    janela_dados = Toplevel(ca)

    treeview = ttk.Treeview(janela_dados)
    treeview.pack()

    treeview["columns"] = tuple(dados[0].keys())

    for column in treeview["columns"]:
        treeview.heading(column, text=column)

    for documento in dados:
        treeview.insert("", END, values=tuple(documento.values()))

# Botão para listar os dados
botao = Button(ca, text="Listar Dados",bg="#F6AA1C", command=lambda:listar_dados())
botao.place(relx = .80, rely = .800, anchor = "n",  width="80" , height="25")

ca.mainloop()