# Viết chương trình nhập vào một con số ứng với con số đó là
# 1 thì in ra màn hình dòng “tôi là người việt nam”
# 2 in ra màn hình dòng “tôi là người hàn quốc”
# 3.  in ra      “tôi là người  campuchia “
# Khác 1,2,3 “toi khong phai la nguoi ”
# (viết bằng if, select case )
n=int(input("Nhap so: "))
if n==1:
    print("Toi la nguoi Viet Nam")
elif n==2:
    print("Toi la nguoi Han Quoc")
elif n==3:
    print("Toi la nguoi Campuchia")
else:
    print("Toi khong phai la nguoi")
