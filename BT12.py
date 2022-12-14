#viết chương trình đổi số thập phân sang nhị phân
n = -1
while (n <= 0):
    n = int(input("Nhập vào n>0: "))

x = n
kq = ""
while (n > 0):
    kq= str(n % 2) + kq
    print("n%2 = ", n % 2)
    n //= 2
    print("n = ", n)

print("Kết quả: ", kq)
