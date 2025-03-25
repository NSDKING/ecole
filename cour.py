class Nombre:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, autre):
        a = self.x + autre.x
        b = self.y + autre.y
        return(a,b)

    def __call__(self, e):
        self.x=self.x + e
    
    def __del__(self):
        self.x=0
        self.y=0

    def __mul__(self, other):
        a = self.x*other.x
        b = self.y*other.y
        return Nombre(a,b)
    
    def __print__(self):
        print(self.x)
        print(self.y)
    
a =Nombre(4,5)
a.__print__()
print(a.__mul__())

a.__del__()
a.__print__()

print(a.__mul__())

