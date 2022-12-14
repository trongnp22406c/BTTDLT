# Tính số hạng N của dãy fibonaci
n = int(input("Nhập số thứ n: "))
if n == 0 or n == 1:
    print(" Số hạng thứ n trong dãy Fibonaci là: ", n)
else:
    f0 = 0
    f1 = 1
    for i in range(1, n):
        fn= f0 + f1
        f0 = f1
        f1 = fn
    print('Số hạng thứ n trong dãy Fibonaci là: ', fn)
