class vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print("vehicle brand is:",self.brand)
        print("vehicle speed is :",self.speed)
class car(vehicle):
    def __init__(self,brand,speed,wheelno,color,typeN_O):
        super().__init__(brand,speed)
        self.wn=wheelno
        self.color=color
        self.tno=typeN_O        
    def display(self):
        super().display()
        print("wheelno is :",self.wn)
        print("vehicle color is :",self.color)
        print("type of vehicle:",self.tno)
        print("--"*30)

class bike(vehicle):
    def __init__(self,brand,speed,wheelno,color,typeN_O):
        super().__init__(brand,speed)
        self.wn=wheelno
        self.color=color
        self.tno=typeN_O
    def display(self):
        super().display()
        print("wheelno is :",self.wn)
        print("vehicle color is :",self.color)
        print("type of vehicle:",self.tno)
        print("--"*30)
        
class truck(vehicle):
    def __init__(self,brand,speed,wheelno,color,typeN_O):
        super().__init__(brand,speed)
        self.wn=wheelno
        self.color=color
        self.tno=typeN_O
    def display(self):
        super().display()
        print("wheelno is :",self.wn)
        print("vehicle color is :",self.color)
        print("type of vehicle:",self.tno)
        print("--"*30)

liss1=[]
liss2=[]
liss3=[]

# def add():
#     n=int(input("enter the how many vehicle want to add"))
#     for i in range(n):
#         brand=input("enter the vehicle brand name :")
#         speed=int(input("enter the speed of the vehicle:"))
#         wn=int(input("enter the wheel no of the vehicle:"))
#         color=input("enter the color of the vehicle:")
#         tno=input("enter the type of vehicle Old or New:")
#         print("--"*30)

#         if wn == 2:
#             b=bike(brand,speed,wn,color,tno)
#             liss1.append(b)
#         elif wn==4:
#             c=car(brand,speed,wn,color,tno)
#             liss2.append(c)
#         else:
#             t=truck(brand,speed,wn,color,tno)
#             liss3.append(t)
# add()
def display():
    vn=input("which vehicle do you want to print:")
    if vn == 'Car':
        for i in range(len(liss2)):
            liss2[i].display()
    elif vn == 'bike':
        for i in range(len(liss1)):
            liss1[i].display()
    elif vn == 'truck':
        for i in range(len(liss3)):
            liss3[i].display()
    else:
        print("your not entering the wrong vehicle")
display()

def display_color():
    vc=input("which color do you want to print:")
    if vc=="red":
        for i in range(len(liss1)):
            if liss1[i].color=='red':
                liss1[i].display()
        for i in range(len(liss2)):
            if liss2[i].color=='red':
                liss2[i].display()
        for i in range(len(liss3)):
            if liss3[i].color=='red':
                liss3[i].display()
    if vc=="blue":
        for i in range(len(liss1)):
            if liss1[i].color=='blue':
                liss1[i].display()
        for i in range(len(liss2)):
            if liss2[i].color=='blue':
                liss2[i].display()
        for i in range(len(liss3)):
            if liss3[i].color=='blue':
                liss3[i].display()
    if vc=="white":
        for i in range(len(liss1)):
            if liss1[i].color=='white':
                liss1[i].display()
        for i in range(len(liss2)):
            if liss2[i].color=='white':
                liss2[i].display()
        for i in range(len(liss3)):
            if liss3[i].color=='white':
                liss3[i].display()

display_color()