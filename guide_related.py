from flask import Flask,request,render_template,redirect,session
import os
import time
from DB_operation import Mysql
from utilities import replaceQuoteWithSpecialToken,checkSession

def toDash():
   # get whole Guide table
    db = Mysql()
    #explain the parameter
    guides = db.getGuide(False)
    print(guides)

    guideArray = []
    for guide in guides:
        dict = {}
        dict["FreshwaterId"] = guide[0]
        dict["FreshwaterItemtType"] = guide[1]
        dict["PresentInNZ"] = guide[2]
        dict["CommonName"] = guide[3]
        dict["ScientificName"] = guide[4]
        dict["KeyCharacteristics"] = guide[5]
        dict["BiologyDescription"] = guide[6]
        dict["Impacts"] = guide[7]

        dict["Images"] = guide[8].split(",")
        dict["PrimaryImage"] = guide[9]
        guideArray.append(dict)
    return render_template('Guide.html',guideArray=guideArray, Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"))

def detail():



    # get specific one row of Guide table
    
    # get whole Guide table
    db = Mysql()
    guide = db.getGuide(request.args['FreshwaterId'])
    guide = guide[0]
    dictForGuide = {}
    dictForGuide["FreshwaterId"] = guide[0]
    dictForGuide["FreshwaterItemtType"] = guide[1]
    dictForGuide["PresentInNZ"] = guide[2]
    dictForGuide["CommonName"] = guide[3]
    dictForGuide["ScientificName"] = guide[4]
    dictForGuide["KeyCharacteristics"] = guide[5]
    dictForGuide["BiologyDescription"] = guide[6]
    dictForGuide["Impacts"] = guide[7]
    dictForGuide["Images"] = guide[8].split(",")
    dictForGuide["PrimaryImage"] = guide[9]

    return render_template('Detail.html',dictForGuide=dictForGuide,Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"))

def editguide():
    
    #add image
    if request.method == 'POST' and request.files.get('addPic'):

        file = request.files.get('addPic') # 从请求中获取文件
        timestamp = time.time()
        filename = os.path.join(os.getcwd(),'static/img', str(timestamp).replace(".","") + file.filename)  # 拼接文件绝对路径
        file.save(filename)

        db = Mysql()
        guide = db.getGuide(request.args['FreshwaterId'].replace("'",""))
        guide = guide[0]

        newImagePathString = guide[8] + "," + str(timestamp).replace(".","") + file.filename



        db.updateGuideImage(request.args['FreshwaterId'].replace("'",""),newImagePathString)


        guide = db.getGuide(request.args['FreshwaterId'].replace("'",""))
        guide = guide[0]
        dictForGuide = {}
        dictForGuide["FreshwaterId"] = guide[0]
        dictForGuide["FreshwaterItemtType"] = guide[1]
        dictForGuide["PresentInNZ"] = guide[2]
        dictForGuide["CommonName"] = guide[3]
        dictForGuide["ScientificName"] = guide[4]
        dictForGuide["KeyCharacteristics"] = guide[5]
        dictForGuide["BiologyDescription"] = guide[6]
        dictForGuide["Impacts"] = guide[7]
        dictForGuide["Images"] = guide[8].split(",")
        dictForGuide["PrimaryImage"] = guide[9]

        return render_template('editGuide.html',dictForGuide=dictForGuide,Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"))

    #editTextual
    if request.method == 'POST' and request.form.get("present"): 
        db = Mysql()
        db.updateGuideTextual(request.form.get("FreshwaterId"),
                                request.form.get("type"),
                                request.form.get("present"),
                                replaceQuoteWithSpecialToken(request.form.get("commonName")),
                                replaceQuoteWithSpecialToken(request.form.get("scientificName")),
                                replaceQuoteWithSpecialToken(request.form.get("keyCharacteristics")),
                                replaceQuoteWithSpecialToken(request.form.get("biologyDescription")),
                                replaceQuoteWithSpecialToken(request.form.get("impacts")),
                                request.args['FreshwaterId'].replace("'",""))


        guide = db.getGuide(request.form.get("FreshwaterId"))
        guide = guide[0]
        dictForGuide = {}
        dictForGuide["FreshwaterId"] = guide[0]
        dictForGuide["FreshwaterItemtType"] = guide[1]
        dictForGuide["PresentInNZ"] = guide[2]
        dictForGuide["CommonName"] = guide[3]
        dictForGuide["ScientificName"] = guide[4]
        dictForGuide["KeyCharacteristics"] = guide[5]
        dictForGuide["BiologyDescription"] = guide[6]
        dictForGuide["Impacts"] = guide[7]
        dictForGuide["Images"] = guide[8].split(",")
        dictForGuide["PrimaryImage"] = guide[9]
        
        return render_template('editGuide.html',dictForGuide=dictForGuide,Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"))
    
    #editPage
    db = Mysql()
    guide = db.getGuide(request.args['FreshwaterId'])
    guide = guide[0]
    dictForGuide = {}
    dictForGuide["FreshwaterId"] = guide[0]
    dictForGuide["FreshwaterItemtType"] = guide[1]
    dictForGuide["PresentInNZ"] = guide[2]
    dictForGuide["CommonName"] = guide[3]
    dictForGuide["ScientificName"] = guide[4]
    dictForGuide["KeyCharacteristics"] = guide[5]
    dictForGuide["BiologyDescription"] = guide[6]
    dictForGuide["Impacts"] = guide[7]
    dictForGuide["Images"] = guide[8].split(",")
    dictForGuide["PrimaryImage"] = guide[9]

    return render_template('editGuide.html',dictForGuide=dictForGuide,Username=session.get("Username"), Authority=session.get("Authority"))

def setPrimaryImage():

    db = Mysql()
    guide = db.changePrimary(request.args['FreshwaterId'],request.args['image'])
    # get specific one row of Guide table
    
    guide = db.getGuide(request.args['FreshwaterId'].replace("'",""))
    guide = guide[0]
    dictForGuide = {}
    dictForGuide["FreshwaterId"] = guide[0]
    dictForGuide["FreshwaterItemtType"] = guide[1]
    dictForGuide["PresentInNZ"] = guide[2]
    dictForGuide["CommonName"] = guide[3]
    dictForGuide["ScientificName"] = guide[4]
    dictForGuide["KeyCharacteristics"] = guide[5]
    dictForGuide["BiologyDescription"] = guide[6]
    dictForGuide["Impacts"] = guide[7]
    dictForGuide["Images"] = guide[8].split(",")
    dictForGuide["PrimaryImage"] = guide[9]

    return render_template('editGuide.html',dictForGuide=dictForGuide,Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"))

def deleteImage():


    #delete file
    print("########DeleteIMAGE##########")
    filename = os.path.join(os.getcwd(),'static/img',request.args['imageTodelete'])
    print(filename)
    os.remove(filename)
    #change DB
    db = Mysql()
    guide = db.updateGuideImage(request.args['FreshwaterId'],request.args['newImageArrayString'])

    # get specific one row of Guide table
    #reload page
    guide = db.getGuide(request.args['FreshwaterId'].replace("'",""))
    guide = guide[0]
    dictForGuide = {}
    dictForGuide["FreshwaterId"] = guide[0]
    dictForGuide["FreshwaterItemtType"] = guide[1]
    dictForGuide["PresentInNZ"] = guide[2]
    dictForGuide["CommonName"] = guide[3]
    dictForGuide["ScientificName"] = guide[4]
    dictForGuide["KeyCharacteristics"] = guide[5]
    dictForGuide["BiologyDescription"] = guide[6]
    dictForGuide["Impacts"] = guide[7]
    dictForGuide["Images"] = guide[8].split(",")
    dictForGuide["PrimaryImage"] = guide[9]

    return render_template('editGuide.html',dictForGuide=dictForGuide,Username=session.get("Username"), Authority=session.get("Authority"), IdNumber=session.get("IdNumber"))

def addGuide():
    
    if request.files.get('addPrimary'):

        arrayForImages = []

        files = request.files.getlist('addPics')
        files.append(request.files.get('addPrimary'))
        for file in files:
            timestamp = time.time()
            filename = os.path.join(os.getcwd(),'static/img', str(timestamp).replace(".","") + file.filename)  # 拼接文件绝对路径
            file.save(filename)
            arrayForImages.append(str(timestamp).replace(".","") + file.filename)
        print(len(files))

        print(','.join(arrayForImages))
        print(arrayForImages[len(arrayForImages) - 1])

        
        db = Mysql()
        db.addGuide(request.form.get("FreshwaterId"),
                                request.form.get("type"),
                                request.form.get("present"),
                                replaceQuoteWithSpecialToken(request.form.get("commonName")),
                                replaceQuoteWithSpecialToken(request.form.get("scientificName")),
                                replaceQuoteWithSpecialToken(request.form.get("keyCharacteristics")),
                                replaceQuoteWithSpecialToken(request.form.get("biologyDescription")),
                                replaceQuoteWithSpecialToken(request.form.get("impacts")),
                                ','.join(arrayForImages),
                                arrayForImages[len(arrayForImages) - 1])

        return redirect('/')


    return render_template('addGuide.html')

def deleteGuide():
    
    #delete image files
    db = Mysql()
    guide = db.getGuide(request.args['FreshwaterId'].replace("'",""))
    guide = guide[0]
    imageArray = guide[8].split(",")
    print("########DeleteIMAGE##########")
    print(imageArray)
    for image in imageArray:
      filename = os.path.join(os.getcwd(),'static/img',image)
      print(filename)  
      os.remove(filename)


    db.deleteGuide(request.args['FreshwaterId'])
    return redirect('/')
