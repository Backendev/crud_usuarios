from data import Data
from user import User
from singleton import Singleton

class Crud(metaclass=Singleton):
    terrors = "\x1b[41m\x1b[37m\x1b[1m"
    errors = "\x1b[31m\x1b[40m"
    tsucces = "\x1b[42m\x1b[37m\x1b[1m"
    succes = "\x1b[32m\x1b[40m"
    end = "\x1b[0m"
    "\x1b[31m"
    def __init__(self):
        self.user = User()
        self.data = Data()
    def create(self,name,lastname,age,email):
        res = self.user.set_user(name,lastname,age,email)
        if res == True:
            ret = self.data.create_user(self.user)
            if ret != False:
                print(self.tsucces+"Creado"+self.end)
                print(self.succes+str(ret)+self.end)
                print(self.tsucces+"_"*80+self.end)
                print(self.succes+str(self.data.get_users())+self.end)
            else:
                print(self.terrors+"Error"+self.end)
                print(self.errors+"Ya existe un usuario con este email"+self.end)
        else:
            print(self.terrors+"Error"+self.end)
            for i in res:
                print(self.errors+str(i)+self.end)
    def update(self):
        self.data.search_user(idu=300)
    