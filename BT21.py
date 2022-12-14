# Lập trình cho việc ‘cho phép rút tiền tại một cây ATM’ của ngân hàng
# ▫	Tiền còn đủ
# ▫	Không quá hạn mức 1 ngày
# ▫	Số tiền 1 lần rút
tienRut=float(input(f"nhập số tiền cần rút:"))
tienKhadung=100000000
hanMuc=50000000
tienRuthomnay=0
rutToida=5000000
if tienRut<tienKhadung:
    print("có thể rút tiền")
else:
    print("không đủ tiền")
if tienRut<rutToida:
    print("có thể rút tiền")
else:
    print("rút quá nhiều")
if tienRuthomnay<hanMuc:
    tienKhadung=tienKhadung-tienRut
    tienRuthomnay+=tienRut
    print(f"rút thành công-số tiền khả dụng là:{tienKhadung}")
else:
    print("hôm nay đã rút quá hạn mức")