from flask import Flask,request,render_template,redirect,session
import os
import time
from DB_operation import Mysql
from utilities import replaceQuoteWithSpecialToken,checkSession


def user():

    print("#####IdNumber########")
    print(request.args.get('IdNumber'))
    db = Mysql()
    # get personal User table From Personal Info Edit Page
    if request.args.get('IdNumber') or request.args.get('IdNumber')=='0' or request.args.get('IdNumber')==0:
        Users = db.getUser(request.args.get('IdNumber'))
        candelete = 0
    # get whole User table
    else:
        Users = db.getUser(False)
        candelete = 1
    print(Users)

    userArray = []
    for user in Users:
        dict = {}
        dict["LastName"] = user[0]
        dict["FirstName"] = user[1]
        dict["IdNumber"] = user[2]
        dict["Address"] = user[3]
        dict["Email"] = user[4]
        dict["PhoneNumber"] = user[5]
        dict["DateJoined"] = user[6]
        dict["Status"] = user[7]
        dict["Username"] = user[8]
        dict["Passwd"] = user[9]
        dict["Authority"] = user[10]
        if user[10] == 0:
           dict["AuthorityDisplay"] = "admin"
        elif user[10] == 1:
            dict["AuthorityDisplay"] = "staff"
        else:
            dict["AuthorityDisplay"] = "user"
        userArray.append(dict)

    return render_template('User.html',userArray=userArray,Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"),candelete=candelete)

def editUser():
    
    #editTextual
    if request.method == 'POST':
        db = Mysql()
        db.updateUserTextual(request.form.get("LastName"),
                                request.form.get("FirstName"),
                                request.form.get("IdNumber"),
                                request.form.get("Address"),
                                request.form.get("Email"),
                                request.form.get("PhoneNumber"),
                                request.form.get("DateJoined"),
                                request.form.get("Status"),
                                request.form.get("Username"),
                                request.form.get("Passwd"),
                                request.form.get("Authority"),
                                request.args['IdNumber'].replace("'",""))
                                
        print("#############From Where###############")
        requstFromPersonalInfo = request.args['requstFromPersonalInfo']=='True'
        print(requstFromPersonalInfo)
        if requstFromPersonalInfo:
            return redirect('/user?IdNumber='+request.args['IdNumber'])
        else:
            return redirect('/user')
    
    #editPageDisplay
    db = Mysql()
    user = db.getUser(request.args['IdNumber'])
    user = user[0]
    dict = {}
    dict["LastName"] = user[0]
    dict["FirstName"] = user[1]
    dict["IdNumber"] = user[2]
    dict["Address"] = user[3]
    dict["Email"] = user[4]
    dict["PhoneNumber"] = user[5]
    dict["DateJoined"] = user[6]
    dict["Status"] = user[7]
    dict["Username"] = user[8]
    dict["Passwd"] = user[9]
    dict["Authority"] = user[10]
    if user[10] == 0:
        dict["AuthorityDisplay"] = "admin"
    elif user[10] == 1:
        dict["AuthorityDisplay"] = "staff"
    else:
        dict["AuthorityDisplay"] = "user"
    print("#############From Where###############")
    requstFromPersonalInfo = request.args['fromPersonalInfo']=='true'
    print(requstFromPersonalInfo)
    return render_template('editUser.html',dictForUser=dict,Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"),requstFromPersonalInfo=requstFromPersonalInfo)


def addUser():
    if request.form.get("Status"):

        

        
        db = Mysql()
        db.addUser(request.form.get("LastName"),
                    request.form.get("FirstName"),
                    request.form.get("IdNumber"),
                    request.form.get("Address"),
                    request.form.get("Email"),
                    request.form.get("PhoneNumber"),
                    request.form.get("DateJoined"),
                    request.form.get("Status"),
                    request.form.get("Username"),
                    request.form.get("Passwd"),
                    request.form.get("Authority"))

        return redirect('/user')



    requstFromDashBoard = request.args['fromDashBoard']=='true'
    return render_template('addUser.html',requstFromDashBoard=requstFromDashBoard)


def deleteUser():
    db = Mysql()
    db.deleteUser(request.args['IdNumber'])
    return redirect('/user')

def checkUsernameDuplication():

    db = Mysql()
    Usernames = db.checkUsernameDuplication()
    namesArray = []
    for namePair in Usernames:
        namesArray.append(namePair[0])
    return namesArray