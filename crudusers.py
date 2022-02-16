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
            option = self.messages.input("Ingrese Opcion ")
            print(option)
            if option == '1':
                self.create_section()
            if option == "2":
                self.update_section()
            if option == "4":
                self.read_section()
            if option == "5":
                cont_m = False
    def read_section(self):
        cont = True
        while cont:
            self.messages.tinfo("Consultar Registro")
            salir = self.messages.input("Salir al menu? Y/N:")
            if str(salir) == "Y":
                cont = False
            else:
                self.c.data.get_data()
                data = self.c.data.read_data()
                self.messages.tinfo("Datos")
                self.messages.warning("name | lastname | age | email")
                for i in data:
                    text = str(i['name'])+" | "+str(i['lastname'])+" | "+str(i['age'])+" | "+str(i['email'])
                    self.messages.info(text)

    def update_section(self):
        cont = True
        while cont:
            na = None
            l_na = None
            ag = None
            em = None
            self.messages.tinfo("Actualizar Registros")
            salir = self.messages.input("Salir al menu? Y/N ")
            if salir == "Y":
                cont = False
            name =self.messages.input("Filtrar por name: ")
            name = name.strip()
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
            c.update(name=na,lastname=l_na,age=ag,email=em)
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
                name = self.messages.input("Name: ").strip()
                print(len(name))
                if len(name) != 0:
                    na = name
                lastname = self.messages.input("lastname: ").strip()
                print(len(lastname))
                if len(lastname) != 0:
                    l_na = lastname
                age_error = True
                while age_error:
                    age = self.messages.input("age: ").strip()
                    print(len(age))
                    if len(age) != 0:
                        val = self.c.user.valid_age(age)
                        if val == False:
                            print(self.c.user.errors['age'])
                        else:
                            age_error = False
                    else:
                        age_error = False
                email = self.messages.input("email: ").strip()
                print(len(email))
                if len(email) != 0:
                    em = email
                if na != None and l_na != None and ag != None and em != None:
                    self.create(na,l_na,ag,em)
                else:
                    self.messages.error("Valores no validos")


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
                    print(i)
                    name = self.messages.input("Name: ")
                    name = name.strip()
                    print(len(name))
                    if len(name) != 0:
                        self.c.update_field(str(i['id']),field='name',value=name)
                    lastname = self.messages.input("Lastame: ")
                    lastname = lastname.strip()
                    print(len(lastname))
                    if len(lastname) != 0:
                        self.c.update_field(str(i['id']),field='lastname',value=lastname)
                    age_error = True
                    while age_error:
                        age = self.messages.input("Age: ")
                        age = age.strip()
                        print(age)
                        if len(age) != 0:
                            res = self.c.update_field(str(i['id']),field='age',value=age)
                            if res == "Error":
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
                            if res == "Error":
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
    