from data import Data
from user import User
from singleton import Singleton
from messages import Messages


class Crud(metaclass=Singleton):
    
    def __init__(self):
        self.user = User()
        self.data = Data()
        self.messages = Messages()
    def create(self,name,lastname,age,email):
        res = self.user.set_user(name,lastname,age,email)
        if res == True:
            ret = self.data.create_user(self.user)
            if ret != False:
                self.messages.success(str(ret),title="Creado")
                self.messages.success(str(self.data.get_users()))
            else:
                self.messages.error("Ya existe un usuario con este email")
        else:
            for i in res:
                self.messages.error(str(i))
    def update(self):
        self.data.search_user(idu=300)
    