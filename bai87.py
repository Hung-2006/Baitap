n = int(input("Nhap bac ma tran: "))

# Nhập ma trận
a = []
for i in range(n):
    row = []
    for j in range(n):
        x = int(input(f"a[{i}][{j}] = "))
        row.append(x)
    a.append(row)

# In ma trận
print("Ma tran:")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()

# ===== Tính trace =====
trace = 0
for i in range(n):
    trace += a[i][i]

print("Trace =", trace)

# ===== Kiểm tra tam giác trên =====
tam_giac_tren = True
for i in range(n):
    for j in range(i):
        if a[i][j] != 0:
            tam_giac_tren = False
            break
    if not tam_giac_tren:
        break

# ===== Nếu là tam giác trên thì tính định thức =====
if tam_giac_tren:
    det = 1
    for i in range(n):
        det *= a[i][i]
    print("det(A) =", det)
else:
    print("Khong phai ma tran tam giac tren")
