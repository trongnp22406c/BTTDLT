#Cho biết số đó có phải số hoàn hảo hay không
#Số hoàn hảo là số có tổng các ước (trừ chính nó) = số đó

n=int(input("Nhập n :"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print(f"{n} là số hoàn hảo")
else:
    print(f"{n} không phải là số hoàn hảo")