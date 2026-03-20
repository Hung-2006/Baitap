# Test logic cipher
def cipher(data):
    result = bytearray()
    for byte in data:
        if byte < 128:
            result.append(byte + 128)
        else:
            result.append(byte - 128)
    return result

# Test với chuỗi "Hello"
original = b"Hello World"
encoded = cipher(original)
decoded = cipher(encoded)  # Giải mã = mã hóa lại

print("Original: ", original)
print("Encoded:  ", encoded)
print("Decoded:  ", decoded)
print("Khop nhau:", original == bytes(decoded))
