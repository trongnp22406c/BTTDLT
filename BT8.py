#8.Viết chương trình nhập vào một con số ứng với con số đó là
#•	1 thì in ra màn hình dòng “tôi là người việt nam”
#•	2 in ra màn hình dòng “tôi là người hàn quốc”
#•	3.  in ra      “tôi là người  campuchia “
#•	Khác 1,2,3 “toi khong phai la nguoi”
#(viết bằng if, select case )

n=int(input("Nhập vào một con số"))

if n==1 :
    print("tôi là người việt nam")
if n==2 :
    print("tôi là người hàn quốc")
if n==3 :
    print("tôi là người campuchia")
if n!=1 and n!= 2 and n!= 3 :
    print("toi khong phai la nguoi")