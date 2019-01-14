#coding: utf-8
#author Henrique Lucas Gomes Rezende
import sqlite3
#conn=sqlite3.connect(r"/storage/emulated/0/kivy/Caderno de Contas/log.db")
conn=sqlite3.connect(r"C:\dev\eXcript\kivy\source\projetos\Caderno de Contas\Android\log.db")

global b
def newAge(age):
    age+=2000
    if(age<2000):
        return False
    if(age%100==0):
        b = False
        if(age%400==0):
            b=True
    else:
        if(age%4==0):
            b = True
        else:
            b = False
    return b

def date(dat):
    r=0
    try:
        if (True):
            if (len(dat) != 8 or dat[2] != '/' or dat[5] != '/'
                    or int(dat[0]) > 3 or int(dat[0]) < 0 or int(dat[1]) <= 0
                    or int(dat[1]) < 0 or int(dat[4]) < 0 or int(dat[3]) > 1
                    or int(dat[3]) < 0 or int(dat[6]) < 0 or int(dat[7]) < 0
                    or int(dat[6]) > 3 # limite 2020
            ):
                print("DATA INVALIDA")
                return 1
            if(int(dat[6]==2) and int(dat[7]>0)):# limite 2020
                print("DATA INVALIDA")
                return 1
            if (int(dat[0]) == 3 and int(dat[1]) > 1):
                print("DATA INVALIDA")
                return 1
            if (int(dat[3]) == 1 and int(dat[4]) > 2):
                print("DATA INVALIDA")
                return 1
    except:
        print("DATA INVALIDA")
    # qual ano/caderno ele se encaixa
    cursor = conn.execute("select ANO from ANOS")
    rows = cursor.fetchall()
    if(True):
        for i in rows:
            if (str(i[0]) == str(dat[6:8])):
                r=2
    if(r==2):
        print("DATA JA OCUPADA")
        return r
    else:
        # verifica se a data existe data existente
        me = {"01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril", "05": "Maio", "06": "Junho",
          "07": "Julho", "08": "Agosto", "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"}
        sem={0:"seg",1:"ter",2:"qua",3:"qui",4:"sex",5:"sab",6:"dom"}
        cursor = conn.execute("select "+me.pop(dat[3:5])+" from Calendario_base where Dia="+dat[0:2])
        rows = cursor.fetchall()
        if( (newAge(int(dat[6:8])) and int(dat[0:2])>29 and dat[3:5]=="02") or (not(newAge(int(dat[6:8]))) and int(dat[0:2])>28 and dat[3:5]=="02")):
            print("DATA INEXISTENTE")
            return 3
        if(rows[0]=="INVL"):
            print("DATA INEXISTENTE")
            return 3
        # qual dia da semana ele pertence
        s=int((int(dat[6:8])/4)+int(dat[6:8])-1)
        print(s)
        d=int(s/7)
        s-=d*7
        #print(sem.pop(s))
        return sem.pop(s)


date(str(input()))
#newAge(int(input()))

