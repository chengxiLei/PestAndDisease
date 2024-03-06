from flask import Flask,request,render_template,redirect,session
import os
import time
from DB_operation import Mysql

def replaceQuoteWithSpecialToken(strinWithQuotes):
    print('##############')
    print(request.form.get("impacts"))
    replacedString = strinWithQuotes.replace("'","_tokeForSingleQuote_")
    replacedString = replacedString.replace('"',"_tokeForDoubleQuote_")
    return replacedString

def checkSession(FuncToRun):
    if session.get("Username"):
        return FuncToRun()
    else:
        return redirect('/sign_in')
