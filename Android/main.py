#coding: utf-8
#author Henrique Lucas Gomes Rezende
import sqlite3
#------------------------QUANDO VC TERMINA ISSO FAZ UM DOCUMENTAÇÃO DE GENTE DECENTE OUVIU!!!------------
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import  Window
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.clock import Clock
from time import sleep, time

#conn=sqlite3.connect(r"/storage/emulated/0/kivy/Caderno de Contas/log.db")
conn=sqlite3.connect(r"C:\dev\eXcript\kivy\source\projetos\Caderno de Contas\Android\log.db")

def remove(s):
    global cls
    cls = {'h': h, 'log': log, 'cad': cad, 'jh': jh, 'at': at,
           'ja': ja}
    # print(self.ids)
    for i in list(s.ids.keys()):
        # print(i)
        if (i == "h" or i == "jh" or i == "cad"
                or i == "log" or i == "at" or
                i == "ja" or i=="sa"):
            global rem
            global ant
            rem = cls[i]
            if (i != "ja" and i != "at"):
                ant = rem
    # print(rem)
    # print("-----"+str(ant))
    if (rem==log):
        tela.root_window.remove_widget(tela.root)
    tela.root_window.remove_widget(rem)

class Login(FloatLayout):
    def entrar(self):
        global u
        global s
        self.ids.sErro.color = 0, 0, 0, 0
        self.ids.sErro.color = 0, 0, 0, 0
        u = self.ids.u.text
        s = self.ids.s.text
        global sav
        sav=self
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
        if(chc==1):
            anim=Animation(x=100)
            anim.start(log)
            #Clock.schedule_once(remove(self),5)
            #sleep(3)
            #remove(self)
            global h
            h=Home()    #MANO, CARA TENHA UM BOM DIA E PENSA NO QUE SE VAI FAZER NESSE TREM AQUI
            #anim.start(h)
            #Clock.schedule_once(tela.root_window.add_widget(h),5)
            tela.root_window.add_widget(h)
    def cadastrar(self):
        remove(self)
        global cad
        cad = Cadastro()
        tela.root_window.add_widget(cad)

class Cadastro(FloatLayout):
    def voltar(self):
        remove(self)
        global log
        log = Login()
        tela.root_window.add_widget(log)
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

class Home(FloatLayout):
    def voltar(self):
        remove(self)
        global log
        log = Login()
        tela.root_window.add_widget(log)
    def ajuda(self):
        remove(self)
        global jh
        jh = AjudaHome()
        tela.root_window.add_widget(jh)
        jh.ids.x1.text="Acessar[color=#ffffff]->Acesso aos cadernos de contas[/color]"
        jh.ids.x1.markup=True
        jh.ids.x2.text="Registrar[color=#ffffff]->Registro de um gasto/ganho[/color]"
        jh.ids.x2.markup=True
        jh.ids.x3.text="Saldo[color=#ffffff]->Saldo atual ou anual/mensal[/color]"
        jh.ids.x3.markup=True
        jh.ids.x4.text="Graficos[color=#ffffff]->Graficos dos gastos[/color]"
        jh.ids.x4.markup=True
        jh.ids.x5.text="Tipos[color=#ffffff]->Criacao ou exclusao de algum tipo de gasto[/color]"
        jh.ids.x5.markup=True
    def atalhos(self):
        remove(self)
        global at
        at=Atalhos()
        tela.root_window.add_widget(at)

class Atalhos(FloatLayout):
    def voltar(self):
        tela.root_window.add_widget(ant)
        remove(self)
    def ajuda(self):
        remove(self)
        global ja
        ja=AjudaAtalhos()
        tela.root_window.add_widget(ja)
        ja.ids.x1.text = "Deletar[color=#ffffff]->Deleta um gasto/ganho[/color]"
        ja.ids.x1.markup = True
        ja.ids.x2.text = "Registrar[color=#ffffff]->Registro de um gasto/ganho[/color]"
        ja.ids.x2.markup = True
        ja.ids.x3.text = "Tipos[color=#ffffff]->Criacao ou exclusao de algum tipo de gasto[/color]"
        ja.ids.x3.markup = True
        ja.ids.x4.text = "Saldo[color=#ffffff]->Saldo atual ou anual/mensal[/color]"
        ja.ids.x4.markup = True
        ja.ids.x5.text = "Graficos[color=#ffffff]->Graficos dos gastos[/color]"
        ja.ids.x5.markup = True
        ja.ids.x6.text = "Acessar[color=#ffffff]->Acesso aos cadernos de contas[/color]"
        ja.ids.x6.markup = True

class AjudaHome(FloatLayout):
    def voltar(self):
        remove(self)
        tela.root_window.add_widget(h)

class AjudaAtalhos(FloatLayout):
    def voltar(self):
        remove(self)
        tela.root_window.add_widget(at)


class CadApp(App):
    global log
    global cad
    global h
    global jh
    global at
    global ja
    at=Atalhos()
    log=Login()
    cad=Cadastro
    jh=AjudaHome()
    h=Home()
    ja=AjudaAtalhos()



Window.size= 325,650
tela=CadApp()
tela.title="Caderno de Contas"
tela.run()



















# conn=sqlite3.connect(r"C:\dev\eXcript\kivy\source\projetos\Caderno de Contas\log.db")
# conn.execute("insert into LOGIN (USUARIO,SENHA) values ('Arnaldo','123')")
# cursor=conn.execute("select * from LOGIN")
# rows=cursor.fetchall()
# print(rows)

# def atalhos(self):
#     global cls
#     cls={'h': Home(),'l':Login(),'cad':Cadastro(),'jh':AjudaHome(),'at':Atalhos}
#     print(self.ids)
#     for i in list(self.ids.keys()):
#         print(i)
#         if (i == "h" or i == "jh" or i == "cad" or i == "log"):
#             global rem
#             rem=cls[i]
#             break
#
#     #x = "tela.root_window.remove_widget(" + wid + ")"
#     print(rem)
#     tela.root_window.remove_widget(rem)
#     tela.root_window.remove_widget(jh)
#     global at
#     at = Atalhos()
#     tela.root_window.add_widget(at)

# class Salvar(FloatLayout):
#     def salvar(self,r):
#         if(r==True):
#             log=sav
#             sav.ids.u.text = u
#             sav.ids.s.text = s
#         remove(self)
#         global h
#         h = Home()
#         tela.root_window.add_widget(h)
