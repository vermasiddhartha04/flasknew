import mysql.connector
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="",database="............")
            self.cur=con.cursor(dictinory=true)
            print("successful")
            
        except:
            print("error")
    def user_signup_model(self):
        selfcur.execute("select * from users")
        return "this is user_signup_model"