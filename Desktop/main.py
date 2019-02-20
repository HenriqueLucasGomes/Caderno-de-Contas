#coding: utf-8
#author Henrique Lucas Gomes Rezende
import sqlite3
#------------------------QUANDO VC TERMINA ISSO FAZ UM DOCUMENTAÇÃO DE GENTE DECENTE OUVIU!!!------------
import time

import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import  Window
conn=sqlite3.connect(r"C:\dev\eXcript\kivy\source\projetos\Caderno de Contas\Desktop\log.db")

u=None
s=None
class Principal(FloatLayout):
    def entrar(self):
        self.ids.sErro.color = 0, 0, 0, 0
        self.ids.sErro.color = 0, 0, 0, 0
        u = self.ids.u.text
        s = self.ids.s.text

        if(u=="USUARIO"):
            self.ids.uErro.color=1,0,0,1
        if(s=="SENHA"):
            self.ids.sErro.color=1,0,0,1
        cursor = conn.execute("select USUARIO from LOGIN")
        rows = cursor.fetchall()
        if(True):
            self.ids.uErro.color = 1, 0, 0, 1
            for i in rows:
                if(str(i[0])==u):
                    self.ids.uErro.color = 0, 0, 0, 0
        cursor = conn.execute("select SENHA from LOGIN where USUARIO='"+u+"'")
        rows = cursor.fetchall()
        if (self.ids.uErro.color==0,0,0,0):
            self.ids.sErro.color = 1, 0, 0, 1
            for i in rows:
                if (str(i[0]) == s):
                    self.ids.sErro.color = 0, 0, 0, 0
        l = str(self.ids.uErro.color), str(self.ids.sErro.color)
        chc = 1
        for i in l:
            if (str(i) != '[0, 0, 0, 0]'):
                chc = 0
    def cadastrar(self):
        tela.root_window.remove_widget(tela.root)
        tela.root_window.remove_widget(p)
        global c
        c = Cadastro()
        tela.root_window.add_widget(c)

class Cadastro(FloatLayout):
    def voltar(self):
        tela.root_window.remove_widget(tela.root)
        tela.root_window.remove_widget(c)
        global p
        p = Principal()
        tela.root_window.add_widget(p)
    def confirmar(self):
        u = self.ids.u.text
        s = self.ids.s.text
        n = self.ids.n.text
        d = self.ids.d.text
        sx = self.ids.sx.text
        c = self.ids.c.text
        self.ids.uErro.color = 0, 0, 0, 0
        self.ids.sErro.color = 0, 0, 0, 0
        self.ids.nErro.color = 0, 0, 0, 0
        self.ids.sxErro.color = 0, 0, 0, 0
        self.ids.cErro.color = 0, 0, 0, 0
        self.ids.dErro.color = 0, 0, 0, 0
        if (u == "USUARIO"):
            self.ids.uErro.color = 1, 0, 0, 1
        if (s == "SENHA"):
            self.ids.sErro.color = 1, 0, 0, 1
        if (n == "NOME COMPLETO"):
            self.ids.nErro.color = 1, 0, 0, 1
        if (d == "DD/MM/AA"):
            self.ids.dErro.color = 1, 0, 0, 1
        if (sx == "SEXO F/M"):
            self.ids.sxErro.color = 1, 0, 0, 1
        if (c == "CONFIRMAR SENHA"):
            self.ids.cErro.color = 1, 0, 0, 1
        cursor = conn.execute("select USUARIO from LOGIN")
        rows = cursor.fetchall()
        if (True):
            for i in rows:
                if (str(i[0]) == u):
                    self.ids.uErro.color = 1, 0, 0, 1
        if(sx!="M" and sx != "F"):
            self.ids.sxErro.color = 1, 0, 0, 1
        if(s!=c):
            self.ids.cErro.color = 1, 0, 0, 1
        try:
            if (True):
                if(len(d)!=8 or d[2]!='/' or d[5]!='/'
                    or int(d[0])>3 or int(d[0])<0 or int(d[1])<=0
                    or int(d[1]) < 0 or int(d[4])<0 or int(d[3])>1
                    or int(d[3])<0 or int(d[6])<0 or int(d[7])<0
                ):
                    self.ids.dErro.color = 1, 0, 0, 1
                if (int(d[0]) == 3 and int(d[1]) > 1):
                    self.ids.dErro.color = 1, 0, 0, 1
                if(int(d[3])==1 and int(d[4])>2):
                    self.ids.dErro.color = 1, 0, 0, 1
        except:
            self.ids.dErro.color,
        l=str(self.ids.uErro.color),str(self.ids.sErro.color),str(self.ids.nErro.color),str(self.ids.sxErro.color),str(self.ids.cErro.color),str(self.ids.dErro.color)
        chc=1
        for i in l:
            if(str(i)!='[0, 0, 0, 0]'):
                chc=0
        if(chc==1):
            conn.execute("insert into LOGIN (USUARIO,SENHA,NOME,NASCIMENTO,SEXO) "
                                 "values('"+u+"','"+s+"','"+n+"','"+d+"','"+sx+"')")
            conn.commit()
            self.ids.gam.color=1,1,1,1
            self.ids.gam.opacity=1
            self.ids.gam.disabled=False
            self.ids.con.color=0,0,0,0
            self.ids.con.opacity=.0
            self.ids.con.disabled=True
            self.ids.vol.color=0,0,0,0
            self.ids.vol.opacity=.0
            self.ids.vol.disabled=True
            self.ids.suc.color = 1, 0, 0, 1


class CadApp(App):
    global p
    p=Principal()

#Window.size= 1280,800
tela=CadApp()
tela.title="Caderno de Contas"
tela.run()



















# conn=sqlite3.connect(r"C:\dev\eXcript\kivy\source\projetos\Caderno de Contas\log.db")
# conn.execute("insert into LOGIN (USUARIO,SENHA) values ('Arnaldo','123')")
# cursor=conn.execute("select * from LOGIN")
# rows=cursor.fetchall()
# print(rows)