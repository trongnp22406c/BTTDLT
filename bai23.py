#Cho biết các ước số chung của 1 số
n=int(input("Nhập n :"))
for i in range (1,n+1):
    if n%i==0:
        print(i, end= " ")
