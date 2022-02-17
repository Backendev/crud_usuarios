import pandas as pd
from crud import Crud
import json
from messages import Messages

class Process:
    def __init__(self):
        self.c = Crud()
        self.start = ""
        self.last = ""
        self.messages = Messages()
    def menu(self):
        cont_m = True
        while cont_m:
            self.messages.tinfo("Menu")
            self.messages.tinfo("Opciones")
            self.messages.info("1 - Crear registro")
            self.messages.info("2 - Actualizar registro")
            self.messages.info("3 - Eliminar registro")
            self.messages.info("4 - Consultar Registros")
            self.messages.info("5 - Salir")
            option = self.messages.input("Ingrese Opcion: >>")
            print(option)
            if option == '1':
                self.create_section()
            if option == "2":
                self.update_section()
            if option == "3":
                self.delete_section()
            if option == "4":
                self.read_section()
            if option == "5":
                cont_m = False
    def read_section(self):
        self.messages.tinfo("Consultar Registro")
        self.c.data.get_data()
        data = self.c.data.read_data()
        self.messages.tinfo("Datos")
        self.messages.warning("| id | name | lastname | age | email |")
        for i in data:
            text = str(i['id'])+" | "+str(i['name'])+" | "+str(i['lastname'])+" | "+str(i['age'])+" | "+str(i['email'])
            self.messages.info(text)

    def update_section(self):
        cont = True
        while cont:
            na = None
            l_na = None
            ag = None
            em = None
            idd = None
            self.messages.tinfo("Actualizar Registros")
            salir = self.messages.input("Salir al menu? Y/N ")
            if str(salir) == "Y":
                cont = False
            else:
                idu =self.messages.input("Filtrar por id: ").strip()
                if len(idu) > 0:
                    idd = idu
                name =self.messages.input("Filtrar por name: ").strip()
                if len(name) > 0:
                    na = name
                
                lastname =self.messages.input("Filtrar por lastlastname: ")
                lastname = lastname.strip()
                if len(lastname) > 0:
                    l_na = lastname
                age =self.messages.input("Filtrar por age: ")
                age = age.strip()
                if len(age) > 0:
                    ag = age
                email =self.messages.input("Filtrar por email: ")
                email = email.strip()
                if len(email) > 0:
                    em = email
                c.update(idu=idd, name=na,lastname=l_na,age=ag,email=em)
    def create_section(self):
        cont = True
        while cont:
            na = None
            l_na = None
            ag = None
            em = None
            self.messages.tinfo("Crear Registro")
            salir = self.messages.input("Salir al menu? Y/N:")
            if str(salir) == "Y":
                cont = False
            else:
                name_error = True
                while name_error:
                    name = self.messages.input("Name: ").strip()
                    if len(name) != 0:
                        na = name
                        name_error = False
                    else:
                        self.messages.error("El valor no puede estar vacio")
                        name_error = True
                lastname_error = True
                while lastname_error:
                    lastname = self.messages.input("lastname: ").strip()
                    print(len(lastname))
                    if len(lastname) != 0:
                        l_na = lastname
                        lastname_error = False
                    else:
                        self.messages.error("El valor no puede estar vacio")
                        lastname_error = True
                age_error = True
                while age_error:
                    age = self.messages.input("age: ").strip()
                    print(len(age))
                    if len(age) != 0:
                        try:
                            age = int(age)
                        except:
                            pass
                        val = self.c.user.valid_age(age)
                        if val == False:
                            print(self.c.user.errors['age'])
                        else:
                            ag = age
                            age_error = False
                    else:
                        age_error = True
                email_error = True
                while email_error:
                    email = self.messages.input("email: ").strip()
                    if len(email) != 0:
                        val = self.c.user.valid_email(email)
                        if val == False:
                            print(self.c.user.errors['email'])
                        else:
                            em = email
                            email_error = False
                if na != None and l_na != None and ag != None and em != None:
                    self.create(na,l_na,ag,em)
                else:
                    self.messages.error("Valores no validos")

    def delete_section(self):
        cont = True
        while cont:
            na = None
            l_na = None
            ag = None
            em = None
            idd = None
            self.messages.tinfo("Borrar Registro")
            salir = self.messages.input("Salir al menu? Y/N:")
            if str(salir) == "Y":
                cont = False
            else:
                idu_error = True
                while idu_error:
                    idu = self.messages.input("id: ").strip()
                    print(len(idu))
                    if len(idu) != 0:
                        try:
                            idu = int(idu)
                        except:
                            pass
                        val = self.c.user.valid_age(idu)
                        if val == False:
                            print("El Id debe ser un valor numerico")
                        else:
                            idd = idu
                            idu_error = False
                    else:
                        idu_error = False
                name = self.messages.input("Name: ").strip()
                if len(name) != 0:
                    na = name
                lastname = self.messages.input("lastname: ").strip()
                if len(lastname) != 0:
                    l_na = lastname
                age_error = True
                while age_error:
                    age = self.messages.input("age: ").strip()
                    print(len(age))
                    if len(age) != 0:
                        try:
                            age = int(age)
                        except:
                            pass
                        val = self.c.user.valid_age(age)
                        if val == False:
                            print(self.c.user.errors['age'])
                        else:
                            ag = age
                            age_error = False
                    else:
                        age_error = False
                email_error = True
                while email_error:
                    email = self.messages.input("email: ").strip()
                    if len(email) != 0:
                        val = self.c.user.valid_email(email)
                        if val == False:
                            print(self.c.user.errors['email'])
                        else:
                            em = email
                            email_error = False
                    else:
                        email_error = False
                l_items = self.c.search(name=na,lastname=l_na,age=ag,email=em,idu=idd)
                self.delete(l_items)
    def delete(self,l_items):
        if len(l_items) > 0:
            if len(l_items) > 1:
                self.messages.warning("Se encontraron varios resultados:")
                self.messages.warning("\tPuede probar adicionando mas filtros")
                self.messages.warning("\t\tEl campo email es unico!!")
                self.messages.warning("Desea actualizarlos todos?")
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
                        self.c.data.delete(i['id'])
                        self.messages.success(str(i),title="Eliminado")

    def create(self,name,lastname,age,email):
        self.c.create(name,lastname,age,email)
    def update(self,name=None,lastname=None,age=None,email=None,idu=None):
        search = self.c.search(name,lastname,age,email,idu)
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
                    name = self.messages.input("Name: ")
                    name = name.strip()

                    if len(name) != 0:
                        self.c.update_field(int(i['id']),field='name',value=str(name))
                    lastname = self.messages.input("Lastame: ")
                    lastname = lastname.strip()
                    print(len(lastname))
                    if len(lastname) != 0:
                        self.c.update_field(str(i['id']),field='lastname',value=lastname)
                    age_error = True
                    while age_error:
                        age = self.messages.input("Age: ")
                        age = age.strip()
                        if len(age) != 0:
                            try:
                                age = int(age)
                            except:
                                pass
                            res = self.c.update_field(str(i['id']),field='age',value=age)
                            if res:
                                age_error = False
                            else:
                                print(self.c.user.errors['age'])
                        else:
                            age_error = False
                    email_error = True
                    while email_error:
                        email = self.messages.input("Email: ")
                        email = email.strip()
                        print(len(email))
                        if len(email) != 0:
                            res = self.c.update_field(str(i['id']),field='email',value=email)
                            if res:
                                email_error = False
                            else:
                                print(self.c.user.errors['email'])
                        else:
                            email_error = False
                    self.messages.warning("desea guardar los cambios? ")
                    save_ch = self.messages.input("Y/N ")
                    if save_ch == "Y":
                        self.c.data.save()

                        
                

if __name__ == "__main__":
    c = Process()
    c2 = Process()
    c.menu()
    