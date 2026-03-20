print("Celsius   Fahrenheit")
for c in range(0, 11):
    f = c * 9/5 + 32
    print(c, "      ", format(f, ".2f"))

print("\nFahrenheit   Celsius")
for f in range(32, 43):
    c = (f - 32) * 5/9
    print(f, "        ", format(c, ".2f"))
