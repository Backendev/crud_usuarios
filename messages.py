class Messages:
    terrors = "\x1b[31m\x1b[1m"
    errors = "\x1b[31m"
    tsucces = "\x1b[32m\x1b[1m"
    succes = "\x1b[32m"
    infot = "\x1b[34m"
    tinfot = "\x1b[34m\x1b[1m"
    warningt = "\x1b[33m"
    end = "\x1b[0m"

    def error(self,content,title=None):
        if title != None:
            print(self.terrors+"_"*5+"[ "+title+" ]"+"_"*5+self.end)
        else:
            print(self.terrors+"_"*5+"[ Error ]"+"_"*5+self.end)
        print(self.errors+content+self.end)
    def success(self,content,title=None):
        if title != None:
            print(self.tsucces+"_"*5+"[ "+title+" ]"+"_"*5+self.end)
        print(self.succes+content+self.end)
    def simple_success(self,content):
        print(self.succes+content+self.end)
    def input(self,content):
        inp = input(self.infot+content+self.end)
        return inp
    def info(self,content):
        print(self.infot+str(content)+self.end)
    def tinfo(self,content):
        print(self.tinfot+"_"*5+"[ "+str(content)+" ]"+"_"*5+self.end)
    def warning(self,content):
        print(self.warningt+str(content)+self.end)
