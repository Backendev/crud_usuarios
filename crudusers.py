import pandas as pd
from crud import Crud


class Process:
    def __init__(self):
        self.c = Crud()
        self.start = ""
        self.last = ""


if __name__ == "__main__":
    c = Process()
    c2 = Process()
    if id(c.c) == id(c2.c):
        print("Mismo Id")
    else:
        print("Diferente Id")
    c.c.create("edward","gonzales",22,"edrr@mail.com.co")
    c.c.update()
    
