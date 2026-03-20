import re

chuoi = input("Nhap chuoi: ")

chuan = re.sub(r'[^a-zA-Z0-9]', '', chuoi).lower()
if chuan == chuan[::-1]:
    print("Chuoi doi xung")
else:
    print("Chuoi khong doi xung")

ky_tu = input("Xoa ky tu nao? ")
ket_qua = ""
for ch in chuoi:
    if ch.lower() != ky_tu.lower():
        ket_qua += ch
print(ket_qua)
