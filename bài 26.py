#tính tổng các số chính phương từ 1-n
import math

n=int(input('Nhập n : '))
s=0
for i in range(1,n+1):
    for j in range(1,int(math.sqrt(i)+1)):
        if j**j==i:
            s=s+i
print(s)