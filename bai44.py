n = int(input("Nhập n: "))

# ===== TAM GIÁC CÂN ĐẶC =====
for i in range(1, n + 1):
    # in khoảng trắng
    for j in range(n - i):
        print(" ", end=" ")
    
    # in dấu *
    for j in range(2 * i - 1):
        print("*", end=" ")
    
    print()

print()  # xuống dòng

# ===== TAM GIÁC CÂN RỖNG =====
for i in range(1, n + 1):
    # khoảng trắng
    for j in range(n - i):
        print(" ", end=" ")
    
    # dấu *
    for j in range(2 * i - 1):
        if i == n or j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()
