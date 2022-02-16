from numpy import True_
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
        idu = self.data.generate_id()
        res = self.user.set_user(idu,name,lastname,age,email)
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
    def search(self,name=None,lastname=None,age=None,email=None,idu=None):
        res = self.data.search_user(name,lastname,age,email,idu)
        if len(res) > 0:
            self.messages.success("Se encontraron los siguientes resultados")
            for i in res:
                self.messages.simple_success(str(i))
        else:
            self.messages.error("No se encontraron Resultados")
        return res
    def update_field(self,idu,field,value):
        if field == 'name' or field == "lastname":
            self.data.update_item(idu=idu,field = field,value=value)
            return True
        if field == 'age':
            valid = self.user.valid_age(value)
            print(valid)
            print(type(valid))
            if valid:
                self.data.update_item(idu=idu,field = field,value=value)
                return True
            else:
                return "Error"
        if field == 'email':
            valid = self.user.valid_email(value)
            if valid:
                self.data.update_item(idu=idu,field = field,value=value)
                return True
            else:
                return "Error"
        

            