#Giải phương trình bậc nhất ax+b=0

a=int(input("Nhập a"))
b=int(input("Nhập b"))

if a==0:
    if b==0:
        kq=1
    else:
        kq=2
else:
    kq=3
if kq==1:
    print("Phương trình có vô số nghiệm")
if kq==2:
    print("Phương trình vô nghiệm")
if kq==3:
    print("Phương trình có 1 nghiệm x=",-b/a)