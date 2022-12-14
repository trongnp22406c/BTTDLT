# Nhập vào 1 tam giác kiểm tra tính hợp lệ của nó và tính diện tích
import math
print("Nhập độ dài ba cạnh của tam giác")
a =float(input("Nhập độ dài cạnh a: "))
b =float(input("Nhập độ dài cạnh b: "))
c =float(input("Nhập độ dài cạnh c: "))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    print("Tam giác hợp lệ")
    print("Diện tích của tam giác là", math.sqrt(p*(p-a)*(p-b)*(p-c)),"đvdt")
else:
    print("khong la 3 canh cua tam giac")








