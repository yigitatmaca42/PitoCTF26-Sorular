# ============================================================
#  Tersine Checksum
# ============================================================
# Asagidaki "encode" fonksiyonu, gizli flag'i "data" listesine
# donusturdu. Gorevin: "data"dan orijinal flag'i geri elde etmek.
# ============================================================

def rotl8(x, r):
    return ((x << r) | (x >> (8 - r))) & 0xFF

def encode(flag: bytes):
    out = []
    prev = 0x5A
    for i, b in enumerate(flag):
        x = (b + (i * 7)) & 0xFF
        x ^= prev
        x = rotl8(x, (i % 7) + 1)
        out.append(x)
        prev = x
    return out

data = [84, 144, 144, 65, 199, 20, 66, 221, 25, 179, 145, 34, 100, 80, 61,
        207, 0, 190, 171, 23, 116, 17, 100, 19, 65, 171, 32, 130, 87, 185,
        124, 227, 22, 81, 3, 198, 254]

# flag = ?
