from flask import Flask,request,render_template,redirect,session
import os
import time
from DB_operation import Mysql
from utilities import replaceQuoteWithSpecialToken,checkSession

from guide_related import toDash,detail,editguide,setPrimaryImage,deleteImage,addGuide,deleteGuide

from user_related import  user,editUser,addUser,deleteUser,checkUsernameDuplication


app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route('/')
def indexFun():
    return checkSession(toDash)

@app.route('/detail')
def toDetail():
    return checkSession(detail)
    
@app.route('/editguide',methods=['GET', 'POST'])
def toeditguide():
    return checkSession(editguide)

@app.route('/setPrimaryImage')
def tosetPrimaryImage():
    return checkSession(setPrimaryImage)

@app.route('/deleteImage')
def todeleteImage():
    return checkSession(deleteImage)

@app.route('/user',methods=['GET', 'POST'])
def toUser():
    return checkSession(user)

@app.route('/editUser',methods=['GET', 'POST'])
def toeditUser():
    return checkSession(editUser)

@app.route('/addGuide',methods=['GET', 'POST'])
def toaddGuide():
    return checkSession(addGuide)

@app.route('/addUser',methods=['GET', 'POST'])
def toaddUser():
    #register doesn't need session
    if request.args.get("fromDashBoard")=='false':
        return addUser()
    return checkSession(addUser)

@app.route('/deleteGuide',methods=['GET', 'POST'])
def todeleteGuide():
    return checkSession(deleteGuide)

@app.route('/deleteUser',methods=['GET', 'POST'])
def todeleteUser():
    return checkSession(deleteUser)

@app.route('/checkUsernameDuplication',methods=['GET', 'POST'])
def tocheckUsernameDuplication():
    return checkSession(checkUsernameDuplication)

@app.route('/sign_in',methods=['GET', 'POST'])
def sign_in():
    if session.get("Username"):
        session.pop("Username",None)
        session.pop("Authority",None)
        session.pop("IdNumber",None)
    if request.args.get("wrongPwd"):
        return render_template('sign_in.html',wrongPwd=True)
    return render_template('sign_in.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    #get请求重定向要home页面
    if request.method=="GET":
        # 如果有直接进入主页
        if session.get("Username"):
            return redirect('/')
        #session没有就返回登录
        else:
            return redirect('/sign_in')
    #post请求处理form表单
    else:
        #输入的不是空的用户名或空的密码
        Username=request.form["Username"]
        Passwd=request.form["Passwd"]
        if Username!="" and Passwd!="":
            #进行用户名和数据的验证
            db = Mysql()
            if db.Connect_db_select(Username,Passwd):
                session["Username"] = Username
                session["Authority"] = db.Connect_db_check_authority(Username)[0]
                session["IdNumber"] = db.Connect_db_check_authority(Username)[1]
                return redirect('/')
            #否则进行注册
            else:
                return redirect('/sign_in?wrongPwd=True')
        #否则重新进行登录
        else:
            return redirect('/sign_in?wrongPwd=True')

@app.route("/logout")
def logout():
    session.pop("Username",None)
    session.pop("Authority",None)
    session.pop("IdNumber",None)
    return redirect('/sign_in')

if __name__ == '__main__':
    app.run(app.run(debug=True,port=5000,host='127.0.0.1'))
