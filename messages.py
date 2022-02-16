class Messages:
    terrors = "\x1b[41m\x1b[37m\x1b[1m"
    errors = "\x1b[31m\x1b[40m"
    tsucces = "\x1b[42m\x1b[37m\x1b[1m"
    succes = "\x1b[32m\x1b[40m"
    end = "\x1b[0m"

    def error(self,content,title=None):
        if title != None:
            print(self.terrors+"_"*80+self.end)
            print(self.terrors+title+self.end)
            print(self.terrors+"_"*80+self.end)
        else:
            print(self.terrors+"_"*80+self.end)
            print(self.terrors+"Error"+self.end)
            print(self.terrors+"_"*80+self.end)
        print(self.errors+content+self.end)
        print(self.terrors+"_"*80+self.end)
    def success(self,content,title=None):
        print(self.tsucces+"_"*80+self.end)
        if tittle != None:
            print(self.tsucces+title+self.end)
        print(self.tsucces+"_"*80+self.end)
        print(self.succes+content+self.end)
        print(self.tsucces+"_"*80+self.end)