from singleton import Singleton
import re

class User(metaclass=Singleton):
    __id = None
    __name = None
    __lastname = None
    __age = None
    __email = None
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def lastname(self):
        return self.__lastname
    @property
    def age(self):
        return self.__age
    @property
    def email(self):
        return self.__email
    
    def get_user(self):
        user_d = {
            'id': self.__id,
            'name': self.__name,
            'lastname': self.__lastname,
            'age': self.__age,
            'email': self.__email,
        }
        return user_d
    def valid_items(function):
        def wrapper(self,name,lastname,age,email):
            patron_email = r'([a-zA-Z0-9\.\!\#\$\%\&\'\*\+\/\=\?\^\_\`\{\|\}\~\-]+@[a-z]+\.[a-z]{3}\.[a-z]{2}|[a-zA-Z0-9\.\!\#\$\%\&\'\*\+\/\=\?\^\_\`\{\|\}\~\-]+@[a-z]+\.[a-z]{3})'
            res_mail = ""
            valid_patron = re.findall(patron_email, email)
            if len(valid_patron) > 0:
                res_mail = valid_patron[0]
            errors = {
                'name': "El Nombre no puede esta vacio",
                'lastname':"El Apellido no puede esta vacio",
                'age': "La edad debe ser un ",
                'email': "El formato de email debe ser abcde@abcde.ab.abc o abcde@abcde.abc; caracteres aceptados .!#$%&'*+/=?^_`{|}~-"
            }
            validation = {
                'name' : True if len(name) > 0 else errors['name'],
                'lastname' : True if len(lastname) > 0 else errors['lastname'],
                'age' : True if isinstance(age, int) else errors['age'],
                'email' : True if res_mail == email else errors['email']
            }
            valid = True
            errors_v =[]
            for k,v in validation.items():
                val = v
                if val != True:
                    valid = False
                    errors_v.append(errors[k])
            if  valid:
                return function(self,name,lastname,age,email)
            else:
                return errors_v
        return wrapper
    @valid_items
    def set_user(self,name,lastname,age,email):
            self.__name = name
            self.__lastname = lastname
            self.__age = age
            self.__email = email
            return True
