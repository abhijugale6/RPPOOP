class Rectangle:
    def __init__(self,len,breadth):
        self.l = len
        self.b = breadth
    def area(self):
        return self.l * self.b
    def perimeter(self):
        return 2*(self.l+self.b)
    def setDimensions(self):
        self.l = int(input("Enter length:\n"))
        self.b = int(input("Enter breadth:\n"))
    def getDimensions(self):
        print("length:",self.l)
        print("breadth:",self.b)
r1=Rectangle(2,3)
print(r1.perimeter())
print(r1.area())
# r1.setDimensions(10,5)
r1.getDimensions()

print("Enter 1 to print area\nEnter 2 to print perimeter\nEnter 3 to set dimensions\nEnter 4 to print dimension\nEnter 5 to exit")
choice=int(input())
while(choice!=5):
    if(choice==1):
        print(r1.area())
    if(choice==2):
        print(r1.perimeter())
    if(choice==3):
        r1.setDimensions()
    if(choice==4):
        r1.getDimensions()
    print("Enter 1 to print area\nEnter 2 to print perimeter\nEnter 3 to set dimensions\nEnter 4 to print dimension\nEnter 5 to exit")
    choice=int(input())