n = int(input("Nhap n [1, 99]: "))

a = list(map(int, input(f"Nhap {n} phan tu: ").split()))

count = {}

for x in a:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

for k in count:
    print(f"{k}[{count[k]}]", end=" ")
