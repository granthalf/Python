import sys

def detect_encoding(filename):
    # Try UTF-8 first
    try:
        with open(filename, "r", encoding="utf-8") as f:
            f.read()
        return "utf-8"
    except:
        pass

    # Try ISO-8859-1 (Latin-1)
    try:
        with open(filename, "r", encoding="iso-8859-1") as f:
            f.read()
        return "iso-8859-1"
    except:
        pass

    # Try CP1252 (Windows encoding)
    try:
        with open(filename, "r", encoding="cp1252") as f:
            f.read()
        return "cp1252"
    except:
        pass

    # Fallback
    return "utf-8"


if len(sys.argv) != 2:
    print("Usage: python count_lines.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Detect encoding
encoding = detect_encoding(filename)
print(f"Detected encoding: {encoding}")

# Count lines
count = 0
with open(filename, "r", encoding=encoding, errors="replace") as f:
    for count, _ in enumerate(f, start=1):
        pass

print("Total lines:", count)
