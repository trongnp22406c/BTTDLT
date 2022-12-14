#Viết chương trình tính tổng N số nguyên lẻ, N số nguyên chẳn

a = int(input("So phan tu nhap vao "))
s=0
for i in range(1,a+1):
    n = int(input("so can nhap "))
    if n%2==0:
        kq = 2
    else:
        kq=1
    if kq==2:
        s+=n
    print("Tong cac so la S=", s)



