# Nhập vào điểm của các môn học 1 sinh viên và cho biết  bạn này có bao nhiêu môn cần phải thi lại .
name = input("Nhap ten sinh vien: ")
s=0
a=int(input("So mon can nhap: "))
for i in range (1,a+1):
    n=float(input(f"Mon {i} "))
    if n<5:
        s+=1
print("So mon can thi lai: ",s)
