gio = int(input("Nhap so gio: "))

tuan = gio // (24 * 7)
gio_du = gio % (24 * 7)

ngay = gio_du // 24
gio_con = gio_du % 24

print(tuan, "tuan,", ngay, "ngay,", gio_con, "gio")
