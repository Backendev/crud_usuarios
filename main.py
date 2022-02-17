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
        self.messages.tinfo("Datos")
        data = self.c.data.read_data()
        self.messages.warning(data)
        

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
                lastname =self.messages.input("Filtrar por lastlastname: ").strip()
                if len(lastname) > 0:
                    l_na = lastname
                age =self.messages.input("Filtrar por age: ").strip()
                if len(age) > 0:
                    ag = age
                email =self.messages.input("Filtrar por email: ").strip()
                if len(email) > 0:
                    em = email
                self.c.update(idu=idd, name=na,lastname=l_na,age=ag,email=em)
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
                    if len(lastname) != 0:
                        l_na = lastname
                        lastname_error = False
                    else:
                        self.messages.error("El valor no puede estar vacio")
                        lastname_error = True
                age_error = True
                while age_error:
                    age = self.messages.input("age: ").strip()
                    if len(age) != 0:
                        try:
                            age = int(age)
                        except:
                            pass
                        val = self.c.user.valid_age(age)
                        if val == False:
                            self.messages.error(str(self.c.user.errors['age']))
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
                            self.messages.error(str(self.c.user.errors['email']))
                        else:
                            em = email
                            email_error = False
                if na != None and l_na != None and ag != None and em != None:
                    self.c.create(na,l_na,ag,em)
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
                    idu = self.messages.input("Filtrar por id: ").strip()
                    if len(idu) != 0:
                        try:
                            idu = int(idu)
                        except:
                            pass
                        val = self.c.user.valid_age(idu)
                        if val == False:
                            self.messages.error("El Id debe ser un valor numerico")
                        else:
                            idd = idu
                            idu_error = False
                    else:
                        idu_error = False
                name = self.messages.input("Filtrar por name: ").strip()
                if len(name) != 0:
                    na = name
                lastname = self.messages.input("Filtrar por lastname: ").strip()
                if len(lastname) != 0:
                    l_na = lastname
                age_error = True
                while age_error:
                    age = self.messages.input("Filtrar por age: ").strip()
                    if len(age) != 0:
                        try:
                            age = int(age)
                        except:
                            pass
                        val = self.c.user.valid_age(age)
                        if val == False:
                            self.messages.error(str(self.c.user.errors['age']))
                        else:
                            ag = age
                            age_error = False
                    else:
                        age_error = False
                email_error = True
                while email_error:
                    email = self.messages.input("Filtrar por email: ").strip()
                    if len(email) != 0:
                        val = self.c.user.valid_email(email)
                        if val == False:
                            self.messages.error(str(self.c.user.errors['email']))
                        else:
                            em = email
                            email_error = False
                    else:
                        email_error = False
                l_items = self.c.search(name=na,lastname=l_na,age=ag,email=em,idu=idd)
                self.c.delete(l_items)

if __name__ == "__main__":
    c = Process()
    c.menu()
    