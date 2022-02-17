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
    
    def delete(self,l_items):
        if len(l_items) > 0:
            if len(l_items) > 1:
                self.messages.warning("Se encontraron varios resultados:")
                self.messages.warning("\tPuede probar adicionando mas filtros")
                self.messages.warning("\t\tEl campo email es unico!!")
                self.messages.warning("Desea borrarlos todos?")
                act = self.messages.input("Y/N: ")
                if act == "Y":
                    cont = True
            if len(l_items) == 1:
                cont = True
            if cont:
                for i in l_items:
                    self.messages.error(str(i),title="Eliminar")
                    eli = self.messages.input("Y/N: ")
                    if eli == "Y":
                        self.data.delete_item(i['id'])
                        self.messages.success(str(i),title="Eliminado")
    
    def update(self,name=None,lastname=None,age=None,email=None,idu=None):
        search = self.search(name,lastname,age,email,idu)
        cont = False
        if len(search) > 0:
            if len(search) > 1:
                self.messages.warning("Se encontraron varios resultados:")
                self.messages.warning("\tPuede probar adicionando mas filtros")
                self.messages.warning("\t\tEl campo email es unico!!")
                self.messages.warning("Desea actualizarlos todos?")
                act = self.messages.input("Y/N: ")
                if act == "Y":
                    cont = True
            if len(search) == 1:
                cont = True
            if cont:
                for i in search:
                    self.messages.warning("Usuario: "+str(i))
                    name = self.messages.input("Nuevo name: ")
                    name = name.strip()
                    if len(name) != 0:
                        self.update_field(int(i['id']),field='name',value=str(name))
                    lastname = self.messages.input("Nuevo lastame: ")
                    lastname = lastname.strip()
                    if len(lastname) != 0:
                        self.update_field(str(i['id']),field='lastname',value=lastname)
                    age_error = True
                    while age_error:
                        age = self.messages.input("Nuevo age: ")
                        age = age.strip()
                        if len(age) != 0:
                            try:
                                age = int(age)
                            except:
                                pass
                            res = self.update_field(str(i['id']),field='age',value=age)
                            if res:
                                age_error = False
                            else:
                                print(self.user.errors['age'])
                        else:
                            age_error = False
                    email_error = True
                    while email_error:
                        email = self.messages.input("Nuevo email: ")
                        email = email.strip()
                        if len(email) != 0:
                            res = self.update_field(str(i['id']),field='email',value=email)
                            if res:
                                email_error = False
                            else:
                                print(self.user.errors['email'])
                        else:
                            email_error = False
                    self.messages.warning("desea guardar los cambios? ")
                    save_ch = self.messages.input("Y/N ")
                    if save_ch == "Y":
                        self.data.save()
                        self.messages.success("Antes -> "+str(i),title="Actualizado")
                        self.messages.success(str(self.data.get_users()))
    
    def search(self,name=None,lastname=None,age=None,email=None,idu=None):
        res = self.data.search_user(name,lastname,age,email,idu)
        if len(res) > 0:
            self.messages.success("Se encontraron los siguientes resultados")
            for i in res:
                self.messages.simple_success(str(i))
        else:
            self.messages.error("No se encontraron Resultados h")
        return res

    def update_field(self,idu,field,value):
        if field == 'name' or field == "lastname":
            self.data.update_item(idu=idu,field = field,value=value)
            return True
        if field == 'age':
            valid = self.user.valid_age(value)
            if valid:
                self.data.update_item(idu=idu,field = field,value=value)
                return True
            else:
                return False
        if field == 'email':
            valid = self.user.valid_email(value)
            if valid:
                self.data.update_item(idu=idu,field = field,value=value)
                return True
            else:
                return False