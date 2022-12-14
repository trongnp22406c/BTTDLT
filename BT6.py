#Nhập vào 3 cạnh của tam giác. Kiểm tra hợp lệ về tam giác và tính chu vi và diện tích
import math

print("3 canh cua tam giac")
a =float(input("a= "))
b =float(input("b= "))
c =float(input("c= "))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    C=a+b+c
    print("la 3 canh cua tam giac co chu vi la",C, "dien tich la",S)
else:
    print("khong la 3 canh cua tam giac")
