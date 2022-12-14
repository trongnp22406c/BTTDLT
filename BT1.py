#1.	Solve to quadratic equation 2 ax^2+bx+c=0
import math

print("ax**2 + b*x + c = 0")
a =float(input("a= "))
b =float(input("b= "))
c =float(input("c= "))
if a == 0:
     if b == 0:
          if c == 0:
               print("phuong trinh vo so nghiem")
          else:
               print("phuong trinh vo nghiem")
     else:
          print("phuong trinh co 1 nghiem x1=x2=",-c/b)
else:
  D=b*b - 4*a*c
  if D>0:
    x1 = float((-b + math.sqrt(D)) / (2 * a))
    x2 = float((-b - math.sqrt(D)) / (2 * a))
    print("phuong trinh co 2 nghiem x1=",x1,"va x2=",x2)
  else:
     if D==0:
          print("phuong trinh co 1 nghiem kep x1=x2=",-b/(2*a))
     else:
          print("phuong trinh vo nghiem")

