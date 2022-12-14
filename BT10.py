#.  nhập vào một tháng năm và cho biết tháng đó có bao nhiêu ngày  biết
#tháng 1,3,5,6,8,10,12 có 31 ngày
#tháng 4 7 9 11 có 30
#tháng 2 có 28 ngày riêng năm nhuần  thì có 29 ngày
#•	năm nhuần là năm chia hết cho 4

t=int(input("nhập vào tháng"))

if t>1 and t<12 :
    if t==1 or t==3 or t==5 or t==6 or t==8 or t==10 or t==12:
        print("tháng đó có 31 ngày")
    elif t==4 or t==7 or t==9 or t==11:
        print("tháng đó có 30 ngày")
    else:
        n = int(input("nhập vào năm"))
        if n % 4 == 0:
            print(n,"là năm nhuần")
            print("Tháng 2 có 29 ngày")
        else:
            print("Tháng 2 có 28 ngày")
else:
    print("nhập liệu không hợp lệ, mời bạn nhập lại")
