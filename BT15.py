# Cho n phương trình bậc 2 tính tổng của nghiệm khi có 1 nghiệm
import math
n = int(input("Nhập số phương trình bậc hai dạng ax^2 + bx +c( a khác 0) : "))
s = 0
for i in range(1, n +1):
    print(f"Phương trình thứ {i} ")
    a = float(input("Mời bạn nhập hệ số a: "))
    b = float(input("Mời bạn nhập hệ số b: "))
    while True:
        if a == 0 :
            print("Hệ số a phải khác 0: ")
            a = float(input("Mời nhập lại số a: "))
        else:
            break
    c = float(input("Mời bạn nhập hệ số c: "))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)))
        s += (-b/(2*a))
    else:
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 = ", (-(b) + math.sqrt(delta)) / (2 * a))
        print("x1 = ", (-(b) - math.sqrt(delta)) / (2 * a))
    print("Tổng các nghiệm khi phương trình có 1 nghiệm là: ", s)
