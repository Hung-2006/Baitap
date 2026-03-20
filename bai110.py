import random

# ===== Hàm đếm số âm =====
def sumNeg(a, m):
    count = 0
    for i in range(m):
        if a[i] < 0:
            count += 1
    return count

# ===== Nhập n, m =====
n, m = map(int, input("Nhap n, m: ").split())

# ===== Tạo ma trận ngẫu nhiên =====
A = []
for i in range(n):
    row = []
    for j in range(m):
        x = random.randint(-10, 10)
        row.append(x)
    A.append(row)

# ===== In ma trận =====
for row in A:
    for x in row:
        print(f"{x:3}", end=" ")
    print()

# ===== Nhập dòng k =====
k = int(input("Nhap dong k: "))

# ===== Kiểm tra hợp lệ =====
if 0 <= k < n:
    result = sumNeg(A[k], m)
    print(f"Dong {k} co {result} so am")
else:
    print("Dong k khong hop le")
