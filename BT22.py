#Tính tổng các số chẵn nhập vào
a=int(input('Số phần tử nhập vào : '))
s=0
for i in range(1,a+1):
    n=int(input('Số cần nhập : '))
    if n%2==0:
        s=s+n
    else:
        print('Không phải số chẵn')
print(f"Tổng các số chãn là {s}")
