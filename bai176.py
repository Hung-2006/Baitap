import sys

def cipher(data):
    result = bytearray()
    for byte in data:
        if byte < 128:
            result.append(byte + 128)
        else:
            result.append(byte - 128)
    return result

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'rb') as f:
    data = f.read()

result = cipher(data)

with open(output_file, 'wb') as f:
    f.write(result)

print("Xu ly xong...")
