#Cho biết số đó có phải là số chính phương hay không
import math

n=int(input('Nhập vào một số nguyên dương : '))
def check(k):
    m=int(math.sqrt(k))
    if m*m==k:
        return True
    else:
        return False

if check(n)==True:
    print('Đây là số chính phương')
else:
    print('Đây không phải là số chính phương')

