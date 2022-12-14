#Tính tổng nghiệm của 2 phuương trình bậc 2
import math
i=2
s=0
while i>0:
    a=float(input("Nhập a :"))
    b=float(input("Nhập b :"))
    c=float(input("Nhập c :"))
    if a==0 :
        if b==0:
            print('Phương trình vô nghiệm')
        else:
            print(f"Phương trình có một nghiệm x= {-c/b}")
            s=s+(-c/b)
    delta = b**2-4*a*c
    if delta>0:
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        s=s+x1+x2
    elif delta==0:
        x1 = (-b/(2*a))
        print(x1)
        s=s+x1
    else:
        print("Phương trình vô nghiệm")
    i=i-1
print(f"Tổng các số nghiệm là {s}")


