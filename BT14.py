#Tính tổng nghiệm  của 2 phương trình bậc 2 nhập vào khi có 2 nghiệm
import math

n=int(input("nhap so phuong trinh"))
s=0
for i in range (1,n+1):
    a=float(input("nhap a"))
    b=float(input("nhap b"))
    c=float(input("nhap c"))

    if a == 0:
        if b==0:
            if c==0:
                print("phuong trinh co vo so nghiem")
            else:
                print("phuong trinh vo nghiem")
        else:
            print("phuong trinh co mot nghiem x=", + (-c / b))
            s=s+(-c/b)
    else:
        D= b*b-4*a*c
        if D==0:
            x1=x2=x= (-b)/(2 * a)
            s=x1+x2
        if D>0:
            x1=((-b+math.sqrt(D))/(2*a))
            x2=((-b-math.sqrt(D))/(2*a))
            s=x1+x2
        if D<0:
            print("phuong trinh vo nghiem")
print("Tổng nghiệm của",n," phương trình là",s)

