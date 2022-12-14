#Tìm ước số chung lớn nhất của 2 số A B
def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

a = int(input("Nhập a = "))
b = int(input("Nhập b = "))

print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a,b))