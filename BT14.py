#Tính tổng nghiệm  của 2 phương trình bậc 2 nhập vào khi có 2 nghiệm
import math
i=2
s=0
while (i>0):
    a=float(input("nhap a"))
    b=float(input("nhap b"))
    c=float(input("nhap c"))

    if a == 0:
        if b==0:
            print ("Phương trình vô nghiệm!")
        else:
            print("phuong trinh co mot nghiem x=", + (-c / b))
            s=s+(-c/b)
    else:
        D = b * b - 4 * a * c
        if D==0:
            x1 = (-b / (2 * a))
            print(x1)
            s=s+x1
        if D>0:
            x1 = (float)((-b + math.sqrt(D)) / (2 * a))
            x2 = (float)((-b - math.sqrt(D)) / (2 * a))
            print(x1,x2)
            s=s+x1+x2
        if D<0:
            print("phuong trinh vo nghiem")
    i = i - 1
    print(s, "tong cac so nghiem")
