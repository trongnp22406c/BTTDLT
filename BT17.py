#Cho biết 1 số có phải là số chẳn hay lẻ
def KTchanle(n):
    x = 1
    if n % 2 == 0 :
        x = 0
    return x
n = int(input("Nhập số cần kiểm tra "))
KT = KTchanle(n)
if KT == 1:
    print(n,"là số lẻ")
else:
    print(n, "là số chẵn")

