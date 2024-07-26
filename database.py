import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from flask import Flask, request, send_file
import io
import plotly.graph_objs as go
from main import generateblockchain


#data base connection
def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="healthdb")
    c = _conn.cursor()

    return c, _conn

# -------------------------------Registration-----------------------------------------------------------------

def user_reg(username,password,email,mobile,branch):
    try:
        c, conn = db_connect()
        print(username,password,email,mobile,branch)
        id="0"
        
        j = c.execute("insert into services (id,username,password,email,mobile,branch) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+mobile+"','"+branch+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    

#user reg
def inc_reg(username,password,email,mobile):
    try:
        c, conn = db_connect()
        print(username,password,email,mobile)
        id="0"
        key = "pending"
        j = c.execute("insert into user (id,username,password,email,mobile,skey) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+mobile+"','"+key+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
#uploading doctor data
def dupact1(username,spe,exp,mobile):
    try:
        c, conn = db_connect()
        print(username,spe,exp,mobile)
        id="0"
        key = "pending"
        j = c.execute("insert into dupload (id,username,spe,exp,mobile) values ('"+id +
                      "','"+username+"','"+spe+"','"+exp+"','"+mobile+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

   #doctor upload the amount to the user to pay
def rpay_act(username,researcher,amount):
    try:
        c, conn = db_connect()
        print(username,researcher,amount)
        id="0"
        status = "pending"
        j = c.execute("insert into rpay (id,username,resercher,amount,status) values ('"+id +
                      "','"+username+"','"+researcher+"','"+amount+"','"+status+"')")
        
        k = c.execute("update rrequest set status='accepted' where username='"+username+"' and resercher='"+researcher+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

    
def ipay_act(username,researcher,amount):
    try:
        c, conn = db_connect()
        print(username,researcher,amount)
        id="0"
        status = "pending"
        j = c.execute("insert into ipay (id,username,insurancer,amount,status) values ('"+id +
                      "','"+username+"','"+researcher+"','"+amount+"','"+status+"')")
        
        k = c.execute("update irequest set status='accepted' where username='"+username+"' and insurancer='"+researcher+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def dpay_act(username,researcher,amount):
    try:
        c, conn = db_connect()
        print(username,researcher,amount)
        id="0"
        status = "pending"
        status1 = 'pending'
        status2 = 'pending'
        j = c.execute("insert into dpay (id,username,doctor,amount,status,status1,status2) values ('"+id +
                      "','"+username+"','"+researcher+"','"+amount+"','"+status+"','"+status1+"','"+status2+"')")
        
        k = c.execute("update drequest set status='accepted' where username='"+username+"' and doctor='"+researcher+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def upay_act(username,researcher,amount):
    try:
        c, conn = db_connect()
        print(username,researcher,amount)
        id="0"
        status = "pending"

        j = c.execute("update rpay set status='paid' where username='"+username+"' and resercher='"+researcher+"'")
        
        
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def upay_act1(username,researcher,amount):
    try:
        c, conn = db_connect()
        print(username,researcher,amount)
        id="0"
        status = "pending"

        j = c.execute("update ipay set status='paid' where username='"+username+"' and insurancer='"+researcher+"'")
        
        
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def upay_act3(username,researcher,amount,image):
    try:
        c, conn = db_connect()
        print(username,researcher,amount)
        id="0"
        status = "pending"

        j = c.execute("update dpay set status='paid',status1='"+image+"' where username='"+username+"' and doctor='"+researcher+"'")
        
        
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    

def bvu1():
    c, conn = db_connect()
    c.execute("select * from user  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def status1(username):
    c, conn = db_connect()
    c.execute("select * from rpay where username = '"+username+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def status2(username):
    c, conn = db_connect()
    c.execute("select * from ipay where username = '"+username+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def status3(username):
    c, conn = db_connect()
    c.execute("select * from dpay where username = '"+username+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def doc1():
    c, conn = db_connect()
    c.execute("select * from dupload  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def res1():
    c, conn = db_connect()
    c.execute("select * from rupload  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def rvr1(username,branch):
    c, conn = db_connect()
    c.execute("select * from rrequest  where resercher='"+username+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def ivr1(username,branch):
    c, conn = db_connect()
    c.execute("select * from irequest  where insurancer='"+username+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def dvr1(username,branch):
    c, conn = db_connect()
    c.execute("select * from drequest  where doctor='"+username+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def dvr4(username):
    c, conn = db_connect()
    c.execute("select * from dpay  where doctor='"+username+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_verify(username):
    c, conn = db_connect()
    c.execute("select skey from user  where username='"+username+"'   ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def user_verify1(username):
    c, conn = db_connect()
    c.execute("select skey from user  where username='"+username+"'   ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def user_verify2(username):
    c, conn = db_connect()
    c.execute("select skey from user  where username='"+username+"'   ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def ins1():
    c, conn = db_connect()
    c.execute("select * from iupload  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result


def editact1(username,email):
    try:
        c, conn = db_connect()
        print(username,email)
        id="0"
        
        datas,key=generateblockchain('firstblock',username)
        print("blockchain")
        print(datas)
        print(key)
        
        j = c.execute("update user set skey='"+key+"' where username='"+username+"' and email='"+email+"'")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def rrequest(username,resercher,fname):
    try:
        c, conn = db_connect()
        print(username,resercher,fname)
        id="0"

        j = c.execute("insert into rrequest (id,username,resercher,fname,status,status1) values ('"+id +
                      "','"+username+"','"+resercher+"','"+fname+"','pending' , 'pending')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def irequest(username,resercher,fname):
    try:
        c, conn = db_connect()
        print(username,resercher,fname)
        id="0"

        j = c.execute("insert into irequest (id,username,insurancer,fname,status,status1) values ('"+id +
                      "','"+username+"','"+resercher+"','"+fname+"','pending' , 'pending')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def drequest(username,resercher,specialist,mobile):
    try:
        c, conn = db_connect()
        print(username,resercher,specialist,mobile)
        id="0"

        j = c.execute("insert into drequest (id,username,doctor,specialist,status,status1) values ('"+id +
                      "','"+username+"','"+resercher+"','"+specialist+"','pending' , 'pending')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def upload_act(username,about,fname):
    try:
        c, conn = db_connect()
        print(username,about,fname)
        id="0"
       
        j = c.execute("insert into rupload (id,username,about,fname) values ('"+id +
                      "','"+username+"','"+about+"','"+fname+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def upload_act1(username,about,fname):
    try:
        c, conn = db_connect()
        print(username,about,fname)
        id="0"
       
        j = c.execute("insert into iupload (id,username,about,fname) values ('"+id +
                      "','"+username+"','"+about+"','"+fname+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
# # -------------------------------Registration End-----------------------------------------------------------------
# # -------------------------------Loginact Start-----------------------------------------------------------------

def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from bcs where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))


def student_loginact(username, password , branch):
    try:
        c, conn = db_connect()
        print(username, password , branch)
        j = c.execute("select * from services where username='" +
                      username+"' and password='"+password+"' and branch = '"+branch+"'   ")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def ins_loginact(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from user where username='" +
                      username+"' and password='"+password+"' "  )
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())
