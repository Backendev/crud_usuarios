from singleton import Singleton
import pandas as pd
class Data(metaclass=Singleton):
    __data = None
    def __init__(self):
        self.__data = pd.read_json('users.json',orient="index")
        self.__data.reset_index(inplace=True)
        self.__data = self.__data.rename(columns = {'index':'id'})
    @property
    def data(self):
        return self.__data
    def read_data(self):
        l_data = []
        print(self.__data)
        for index,i in self.__data.iterrows():
            user = {}
            user['id'] = i['id']
            user['name'] = i['name']
            user['lastname'] = i['lastname']
            user['age'] = i['age']
            user['email'] = i['email']
            l_data.append(user)
        return l_data
    def get_data(self):
        self.__data = None
        self.__data = pd.read_json('users.json',orient ='index')
        self.__data.reset_index(inplace=True)
        self.__data = self.__data.rename(columns = {'index':'id'})
        
    def get_users(self):
        return self.__data
    def generate_id(self):
        print(self.__data)
        last_item = self.__data.iloc[-1,:].id
        print("___")
        print(last_item)
        new_id = int(last_item) +1
        return new_id
    def new_user(self,user):
        new_user = {
            'id':user.id,
            'name':user.name,
            'lastname':user.lastname,
            'age':user.age,
            'email':user.email
        }
        return new_user
    def save(self):
        self.__data = self.__data.set_index('id')
        self.__data.to_json('users.json',orient="index",indent=4)
        self.get_data()
    def create_user(self,user):
        search_email = self.__data.query("email == '"+str(user.email)+"'")
        if len(search_email) == 0:
            new_user = self.new_user(user)
            self.__data = self.__data.append(
                new_user,ignore_index=True)
            
            self.save()
            return new_user
        else:
            return False
    
    def create_query(self,name=None,lastname=None,age=None,email=None,idu=None):
        query = ""
        search = {}
        if name != None:
            search['name'] = name
        if lastname != None:
            search['lastname'] = lastname
        if age != None:
            search['age'] = age
        if email != None:
            search['email'] = email
        if idu != None:
            search['id'] = idu
        print(search)
        print(len(search))
        count = 0
        inter = ""
        if len(search) > 0:
            for k,v in search.items():
                if count >= 1 and count < len(search):
                    inter = " & "
                query += inter+str(k) + "=='"+str(v)+"'"
                count += 1
                print(query)
            return query
        else:
            return False

        

    def search_user(self,name=None,lastname=None,age=None,email=None,idu=None):
        query = self.create_query(name,lastname,age,email,idu)
        print(query)
        if query != None:
            l_users = []
            result = self.__data.query(query)
            for index,i in result.iterrows():
                print(i['email'])
                user = {}
                user['id'] = i['id']
                user['name'] = i['name']
                user['lastname'] = i['lastname']
                user['age'] = i['age']
                user['email'] = i['email']
                l_users.append(user)
            print(l_users)
            return l_users
        else:
            return []

    def update_item(self,idu,field,value):
        if field == 'name':
            self.__data.loc[self.__data['id'] == idu,'name'] = value
        if field == 'lastname':
            self.__data.loc[self.__data['id'] == int(idu),'lastname'] = value
        if field == 'age':
            self.__data.loc[self.__data['id'] == int(idu),'age'] = value
        if field == 'email':
            self.__data.loc[self.__data['id'] == int(idu),'email'] = value
        print(self.__data.loc[self.__data['id'] == int(idu)])
    def filter_delete_item(self,name=None,lastname=None,age=None,email=None,idu=None):
        query = self.create_query(name,lastname,age,email,idu)
        l_ids = self.__data.query(query).index.tolist
        return l_ids
    def delete(self,idu):
        result = self.__data.query("id == '"+str(idu)+"'")
        self.__data.drop(result.index,inplace=True)
        self.save()


        

