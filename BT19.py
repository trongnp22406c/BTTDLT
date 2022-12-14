# Giải phương trình bậc 2 và cho biết nó có mấy nghiệm. Nếu nó 2 nghiệm thì tính tổng nghiệm của chúng
import math
print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a khác 0)")

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
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta)) / (2 * a))
    print("x1 = ", (-(b) - math.sqrt(delta)) / (2 * a))
    print("Tổng của hai nghiệm x1, x2 là: ", (-b/a))