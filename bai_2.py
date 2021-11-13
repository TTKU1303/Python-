import math
a = int(input("Nhap so a"))
b = int(input("Nhap so b"))
c = int(input("Nhap so c"))
if (a==0):
    if (b==0):
        if (c==0):
            print ("Luon dung")
        else:
            print ("Vo nghiem")
    else:
        x = -c / b
        print ("Nghiem cua phuong trinh la:", x)
else:
    delta = b*b - 4*a*c
    if (delta < 0):
        print ("Phuong trinh vo nghiem")
    elif (delta == 0):
        x = -b/(2*a)
        print ("Nghiem cua phuong trinh la:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print ("Nghiem cua phuong trinh la:", x1, "va", x2)