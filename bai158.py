def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0:
        return b
    return gcd(b % a, a)

a, b = map(int, input("Nhap hai so: ").split())

if a == 0 and b == 0:
    print(f"GCD ({a}, {b}): khong xac dinh")
else:
    print(f"GCD ({a}, {b}) = {gcd(a, b)}")
