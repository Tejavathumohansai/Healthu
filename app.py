import os
import MySQLdb
import smtplib
import random
import string
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, send_file
from database import db_connect, user_reg,inc_reg,admin_loginact,student_loginact,ins_loginact,bvu1,editact1,upload_act,upload_act1,dupact1
from database import db_connect, res1,rrequest,ins1,irequest,doc1,drequest,rvr1,user_verify,rpay_act,ivr1,user_verify1,ipay_act,user_verify2
from database import db_connect, dpay_act,dvr1,status1,upay_act,status2,status3,upay_act1,upay_act3,dvr4
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from werkzeug.utils import secure_filename
import io
import numpy as np


# def db_connect():
#     _conn = MySQLdb.connect(host="localhost", user="root",
#                             passwd="root", db="assigndb")
#     c = _conn.cursor()

#     return c, _conn


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route("/rup.html")
def rup():
    return render_template("rup.html")

@app.route("/iup.html")
def iup():
    return render_template("iup.html")

@app.route("/dup.html")
def dup():
    return render_template("dup.html")
    
@app.route("/user.html")
def admin():
    return render_template("user.html")


@app.route("/bcs.html")
def bcs():
    return render_template("bcs.html")

@app.route("/services.html")
def services():
    return render_template("services.html")

@app.route("/sreg.html")
def sreg():
    return render_template("sreg.html")

@app.route("/bvu.html")
def bvu():
    data = bvu1()
    return render_template("bvu.html", data= data)

@app.route("/status.html")
def status():
    username = session['username']
    data = status1(username)
    data1 = status2(username)
    data2 = status3(username)
    return render_template("status.html", data= data, data1 = data1, data2 = data2)



@app.route("/res.html")
def res():
    data = res1()
    return render_template("res.html", data= data)

@app.route("/rvr.html")
def rvr():
    username = session['username'] 
    branch =   session['branch']
    data = rvr1(username,branch)
    return render_template("rvr.html", data= data)


@app.route("/ivr.html")
def ivr():
    username = session['username'] 
    branch =   session['branch']
    data = ivr1(username,branch)
    return render_template("ivr.html", data= data)

@app.route("/dvr.html")
def dvr():
    username = session['username'] 
    branch =   session['branch']
    data = dvr1(username,branch)
    return render_template("dvr.html", data= data)


@app.route("/vi.html")
def vi():
    username = session['username'] 
    data = dvr4(username)
    return render_template("vi.html", data= data)


@app.route("/ins.html")
def ins():
    data = ins1()
    return render_template("ins.html", data= data)

@app.route("/doc.html")
def doc():
    data = doc1()
    return render_template("doc.html", data= data)

@app.route("/increg.html")
def increg():
    return render_template("increg.html")


@app.route("/index")
def index():
    return render_template("index.html") 


@app.route("/profile1", methods = ['GET','POST'])
def profile1():
    
    username = request.args.get('username')
    email = request.args.get('email')
    editact1(username,email)
    return render_template("bvu.html") 


@app.route("/userverify", methods = ['GET','POST'])
def userverify():
    
    username = request.args.get('username')
    data = user_verify(username)
    print(data[0][0])
    if data[0][0] != None:
       return render_template("rvr.html",m1="sucess")
    else:
       return render_template("rhome.html",m2="sucess")
    

@app.route("/userverify1", methods = ['GET','POST'])
def userverify1():
    
    username = request.args.get('username')
    data = user_verify1(username)
    print(data[0][0])
    if data[0][0] != None:
       return render_template("ivr.html",m1="sucess")
    else:
       return render_template("ihome.html",m2="sucess")
    


@app.route("/userverify2", methods = ['GET','POST'])
def userverify2():
    
    username = request.args.get('username')
    data = user_verify2(username)
    print(data[0][0])
    if data[0][0] != None:
       return render_template("dvr.html",m1="sucess")
    else:
       return render_template("dhome.html",m2="sucess")


@app.route("/raccept", methods = ['GET','POST'])
def raccept():
    
    username = request.args.get('username')
    researcher = session['username']
    return render_template("rpay.html",m1="sucess", username = username,researcher= researcher )


@app.route("/upay", methods = ['GET','POST'])
def upay():
    
    username = request.args.get('username')
    researcher = request.args.get('researcher')
    amount = request.args.get('amount')
    return render_template("upay.html",m1="sucess", username = username,researcher= researcher, amount = amount )


@app.route("/upay1", methods = ['GET','POST'])
def upay1():
    
    username = request.args.get('username')
    researcher = request.args.get('researcher')
    amount = request.args.get('amount')
    return render_template("upay1.html",m1="sucess", username = username,researcher= researcher, amount = amount )


@app.route("/upay2", methods = ['GET','POST'])
def upay2():
    
    username = request.args.get('username')
    researcher = request.args.get('researcher')
    amount = request.args.get('amount')
    return render_template("upay2.html",m1="sucess", username = username,researcher= researcher, amount = amount )
   

@app.route("/iaccept", methods = ['GET','POST'])
def iaccept():
    
    username = request.args.get('username')
    researcher = session['username']
    return render_template("ipay.html",m1="sucess", username = username,researcher= researcher )



@app.route("/daccept", methods = ['GET','POST'])
def daccept():
    
    username = request.args.get('username')
    researcher = session['username']
    return render_template("dpay.html",m1="sucess", username = username,researcher= researcher )


@app.route("/pd", methods = ['GET','POST'])
def pd():
    model_path = "covidmri.h5"
    classes = {0:"covid:-{ covid }",1:"nocovid:-{ nocovid} "}
    username = request.args.get('username')
    doctor = request.args.get('doctor')
    image1 = request.args.get('image')
    image = load_img(image1,target_size=(224,224))
    image = img_to_array(image)
    image = image/255
    image = np.expand_dims(image,axis=0)
    model = load_model(model_path)
    result = np.argmax(model.predict(image))
    prediction = classes[result]
    
    fres=""
    if result == 0:          
        fres="TB Detected"
    elif result == 1:
        fres="TB Not Detected"
    # predict code ------------------------
    predicted = 'skin dise'

    return render_template("vi1.html", pedicted = fres)


@app.route("/rreq", methods = ['GET','POST'])
def rreq():
    username = session['username']
    resercher = request.args.get('resercher')
    fname = request.args.get('fname')
    rrequest(username,resercher,fname)
    return render_template("res.html") 

@app.route("/ireq", methods = ['GET','POST'])
def ireq():
    username = session['username']
    resercher = request.args.get('resercher')
    fname = request.args.get('fname')
    irequest(username,resercher,fname)
    return render_template("ins.html") 

@app.route("/dreq", methods = ['GET','POST'])
def dreq():
    username = session['username']
    resercher = request.args.get('resercher')
    specialist = request.args.get('specialist')
    mobile = request.args.get('mobile')
    drequest(username,resercher,specialist,mobile)
    return render_template("doc.html") 

@app.route("/rdownload", methods = ['GET','POST'])
def rdownload():
    
    id = request.args.get('id')
    fname = request.args.get('fname')
    return send_file('C:/Users/Dell/Project/Healthu/static/'+fname , as_attachment=True, download_name=fname )


@app.route("/idownload", methods = ['GET','POST'])
def idownload():
    
    id = request.args.get('id')
    fname = request.args.get('fname')
    return send_file('C:/Users/Dell/Project/Healthu/static/'+fname , as_attachment=True, download_name=fname )
# -------------------------------Registration-----------------------------------------------------------------    
@app.route("/sregact", methods = ['GET','POST'])
def insreg():
   if request.method == 'POST':    
      
      status = user_reg(request.form['username'],request.form['password'],request.form['email'],request.form['mobile'],request.form['branch'])
      
      if status == 1:
       return render_template("services.html",m1="sucess")
      else:
       return render_template("sreg.html",m1="failed")


@app.route("/inceregact", methods = ['GET','POST'])
def inceregact():
   if request.method == 'POST':    
      
      status = inc_reg(request.form['username'],request.form['password'],request.form['email'],request.form['mobile'])
      
      if status == 1:
       return render_template("user.html",m1="sucess")
      else:
       return render_template("increg.html",m1="failed")
      

@app.route("/dupact", methods = ['GET','POST'])
def dupact():
   if request.method == 'POST':    
      username = session['username']
      status = dupact1(username,request.form['spe'],request.form['exp'],request.form['mobile'])
      
      if status == 1:
       return render_template("dup.html",m1="sucess")
      else:
       return render_template("dup.html",m1="failed")

@app.route("/rpayact", methods = ['GET','POST'])
def rpayact():
   if request.method == 'POST':
      status = rpay_act(request.form['username'],request.form['researcher'],request.form['amount'])
      
      if status == 1:
       return render_template("rvr.html")
      else:
       return render_template("rpay.html",m1="failed")

@app.route("/ipayact", methods = ['GET','POST'])
def ipayact():
   if request.method == 'POST':
      status = ipay_act(request.form['username'],request.form['researcher'],request.form['amount'])
      
      if status == 1:
       return render_template("ivr.html")
      else:
       return render_template("ipay.html",m1="failed")
      


@app.route("/dpayact", methods = ['GET','POST'])
def dpayact():
   if request.method == 'POST':
      status = dpay_act(request.form['username'],request.form['researcher'],request.form['amount'])
      
      if status == 1:
       return render_template("dvr.html")
      else:
       return render_template("dpay.html",m1="failed")
      


@app.route("/upayact", methods = ['GET','POST'])
def upayact():
   if request.method == 'POST':
      status = upay_act(request.form['username'],request.form['researcher'],request.form['amount'])
      
      if status == 1:
       return render_template("status.html")
      else:
       return render_template("upay.html",m1="failed")
      



@app.route("/upayact1", methods = ['GET','POST'])
def upayact1():
   if request.method == 'POST':
      status = upay_act1(request.form['username'],request.form['researcher'],request.form['amount'])
      
      if status == 1:
       return render_template("status.html")
      else:
       return render_template("upay1.html",m1="failed")
      

@app.route("/upayact2", methods = ['GET','POST'])
def upayact2():
   if request.method == 'POST':
      status = upay_act3(request.form['username'],request.form['researcher'],request.form['amount'],request.form['image'])
      
      if status == 1:
       return render_template("status.html")
      else:
       return render_template("upay2.html",m1="failed")


@app.route("/upload", methods = ['GET','POST'])
def upload():
   if request.method == 'POST':    
      
      username = session['username']
      about =request.form['about']
      file = request.files['pdf_file']
      fname = file.filename
      file_data =  file.read()
      paragraph_string = file_data[0]
      print("88888888888888888888888888888888888")
      print(paragraph_string)
      print("99999999999999999")
       
      status = upload_act(username,about,fname)
      
      if status == 1:
       return render_template("rup.html",m1="sucess")
      else:
       return render_template("rup.html",m1="failed")
      


@app.route("/upload1", methods = ['GET','POST'])
def upload1():
   if request.method == 'POST':    
      
      username = session['username']
      about =request.form['about']
      file = request.files['pdf_file']
      fname = file.filename
      file_data =  file.read()
      paragraph_string = file_data[0]
      print("88888888888888888888888888888888888")
      print(paragraph_string)
      print("9999999999999999")
     
      status = upload_act1(username,about,fname)
      
      if status == 1:
       return render_template("iup.html",m1="sucess")
      else:
       return render_template("iup.html",m1="failed")
      

# # -------------------------------Registration End-----------------------------------------------------------------
    
# #-------------------------------ADD_END---------------------------------------------------------------------------
# # -------------------------------Loginact-----------------------------------------------------------------
@app.route("/adminlogact", methods=['GET', 'POST'])       
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("bcshome.html", m1="sucess")
        else:
            return render_template("bcs.html", m1="Login Failed")





@app.route("/studentlogact", methods=['GET', 'POST'])       
def studentlogact():
        if request.method == 'POST':
           Researcher = "Researcher"
           Insurance = "Insurance"
           Doctor = "Doctor"
           branch = request.form['branch']
           status = student_loginact(request.form['username'], request.form['password'],branch )
           print(status)
           session['username'] = request.form['username']
           session['branch'] = request.form['branch']
        if status == 1 and branch == Researcher :
            
            return render_template("rhome.html", m1="sucess")
        elif status == 1 and branch == Insurance :
            session['username'] = request.form['username']
            return render_template("ihome.html", m1="sucess")
        
        elif status == 1 and branch == Doctor :
            session['username'] = request.form['username']
            return render_template("dhome.html", m1="sucess")

        else:
            return render_template("increg.html", m1="Login Failed")
            
       

@app.route("/inslogin", methods=['GET', 'POST'])       
def inslogin():
    if request.method == 'POST':
        status = ins_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("uhome.html", m1="sucess")
        else:
            return render_template("increg.html", m1="Login Failed")
        
# # -------------------------------Loginact End----------------------------------------------------------------- 
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
