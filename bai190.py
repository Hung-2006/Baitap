import sys

def hex_dump(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Khong tim thay file: {filename}")
        return

    total = len(data)
    
    print(f"{'':8}  +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F  Contents")
    
    for i in range(0, total, 16):
        chunk = data[i:i+16]
        addr = f"{i:08X}"
        hex_part = ' '.join(f"{b:02X}" for b in chunk)
        hex_part = hex_part.ljust(47)
        content = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        print(f"{addr}  {hex_part}  {content}")
    
    print(f"{total} bytes")

if len(sys.argv) != 2:
    print("Cach dung: python hexdump.py <ten_file>")
else:
    hex_dump(sys.argv[1])
