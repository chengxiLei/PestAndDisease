import pymysql
from werkzeug.security import  generate_password_hash,check_password_hash
class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost',user='root',password='lcx6592183',database='biosecurity_guide',charset="utf8")
            self.cursor = self.conn.cursor()  # 游标对象
            print("连接数据库成功")
        except:
            print("连接失败")


    def getUser(self,id):
        sql = "select * from Users"
        if id :
            sql = sql + " WHERE IdNumber = " + id
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items

    def getGuide(self,id):
        sql = "select * from PestAndDisease"
        if id :
            sql = sql + " WHERE FreshwaterId = " + id
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items

    def updateGuideTextual(self,
                    FreshwaterId,
                    type,
                    present,
                    commonName,
                    scientificName,
                    keyCharacteristics,
                    biologyDescription,
                    impacts,
                    previousFreshwaterId):
        sql = '''UPDATE PestAndDisease SET FreshwaterItemtType = '{}', PresentInNZ = '{}', CommonName = '{}', ScientificName = '{}', KeyCharacteristics = '{}', BiologyDescription = '{}', Impacts = '{}' WHERE FreshwaterId = '{}';'''.format(type,present,commonName,scientificName,keyCharacteristics,biologyDescription,impacts,previousFreshwaterId)
        print("#########OLD ID##########")
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"


    def updateUserTextual(self,
                    LastName,
                    FirstName,
                    IdNumber,
                    Address,
                    Email,
                    PhoneNumber,
                    DateJoined,
                    Status,
                    Username,
                    Passwd,
                    Authority,
                    previousIdNumber):
        sql = '''UPDATE Users SET LastName = '{}', FirstName = '{}', Address = '{}', Email = '{}', PhoneNumber = '{}', DateJoined = '{}', Status = '{}', Username = '{}', Authority = '{}' WHERE IdNumber = '{}';'''.format(LastName, FirstName, Address, Email, PhoneNumber, DateJoined, Status, Username, Authority, previousIdNumber)
        if Passwd :
            print("#########new password detected##########")
            Passwd = generate_password_hash(Passwd)
            sql = '''UPDATE Users SET LastName = '{}', FirstName = '{}', Address = '{}', Email = '{}', PhoneNumber = '{}', DateJoined = '{}', Status = '{}', Username = '{}', Passwd = '{}', Authority = '{}' WHERE IdNumber = '{}';'''.format(LastName, FirstName, Address, Email, PhoneNumber, DateJoined, Status, Username, Passwd, Authority, previousIdNumber)
        print("#########OLD ID##########")
        print("#########OLD ID##########")
        print("#########OLD ID##########")
        print("#########password##########")
        print(Passwd)
        print(sql)
        print(previousIdNumber)
        print(IdNumber)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"


    def updateGuideImage(self,id,newImagePathString):
        sql = "UPDATE PestAndDisease SET Images = " + "'" + newImagePathString + "'"
        if id :
            sql = sql + " WHERE FreshwaterId = " + "'" + id + "'"
        try:
            print("#######ImageUpdateSQL############")
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"

    def changePrimary(self,id,newPrimaryImage):
        sql = "UPDATE PestAndDisease SET PrimaryImage = " + "'" + newPrimaryImage + "'"
        if id :
            sql = sql + " WHERE FreshwaterId = " + "'" + id + "'"
        try:
            print("#######ImageUpdateSQL############")
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"

    def deleteOneImage(self,id,newPrimaryImage):
        sql = "UPDATE PestAndDisease SET PrimaryImage = " + "'" + newPrimaryImage + "'"
        if id :
            sql = sql + " WHERE FreshwaterId = " + "'" + id + "'"
        try:
            print("#######ImageUpdateSQL############")
            print("#######ImageUpdateSQL############")
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"

    def Connect_db_select(self,username,passwd):
        sql="SELECT Passwd FROM Users WHERE Username='"+username+"'"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        if len(items) != 0 and check_password_hash(items[0][0], passwd):
            print("success")
            return True
        return False

    def Connect_db_check_authority(self,username):
        sql="SELECT Authority,IdNumber FROM Users WHERE Username='"+username+"'"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items[0]

    def addGuide(self,
                FreshwaterId,
                type,
                present,
                commonName,
                scientificName,
                keyCharacteristics,
                biologyDescription,
                impacts,
                images,
                primaryImage):
        sql = '''INSERT INTO PestAndDisease (FreshwaterItemtType,PresentInNZ,CommonName,ScientificName,KeyCharacteristics,BiologyDescription,Impacts,Images,PrimaryImage) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(type, present, commonName, scientificName, keyCharacteristics, biologyDescription, impacts, images, primaryImage)
        print("#########OLD ID##########")
        print(sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"
    

    def addUser(self,
                LastName,
                FirstName,
                IdNumber,
                Address,
                Email,
                PhoneNumber,
                DateJoined,
                Status,
                Username,
                Passwd,
                Authority):
        Passwd = generate_password_hash(Passwd)
        sql = '''INSERT INTO Users (LastName,FirstName,Address,Email,PhoneNumber,DateJoined,Status,Username,Passwd,Authority) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(LastName, FirstName, Address, Email, PhoneNumber, DateJoined, Status, Username, Passwd, Authority)
        print("#########OLD ID##########")
        print(sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"

    def deleteGuide(self, FreshwaterId):
        sql = '''DELETE FROM PestAndDisease WHERE FreshwaterId='{}'; '''.format(FreshwaterId)
        print("#########OLD ID##########")
        print(sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"

    def deleteUser(self, IdNumber):
        sql = '''DELETE FROM Users WHERE IdNumber='{}'; '''.format(IdNumber)
        print("#########OLD ID##########")
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("update successful")
            return "update successful"
        except:
            # 如果发生错误则回滚
            self.conn.rollback()
            print("update unsuccessful")
            return "update unsuccessful"

    def checkUsernameDuplication(self):
        sql = '''SELECT Username FROM Users '''
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items
