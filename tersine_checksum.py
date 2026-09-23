# ============================================================
#  Tersine Checksum
# ============================================================
# Asagidaki "encode" fonksiyonu, gizli flag'i geri
# donusturulebilir bir zincirle kodlayarak "data" listesini uretti.
#
# Gorevin: bu algoritmayi TERSINE cevirip "data"dan flag'i geri cikarmak.
#
# Ipucu: her adim geri alinabilir (toplama -> cikarma,
#        XOR -> ayni XOR, sola dondurme -> saga dondurme).
#        Zincirde her bayt bir ONCEKI *kodlanmis* bayta baglidir.
# ============================================================

def rotl8(x, r):
    return ((x << r) | (x >> (8 - r))) & 0xFF

def encode(flag: bytes):
    out = []
    prev = 0x5A  # sabit baslangic (IV)
    for i, b in enumerate(flag):
        x = (b + (i * 7)) & 0xFF     # 1) pozisyona bagli toplama
        x ^= prev                    # 2) onceki cikti baytiyla XOR (zincir)
        x = rotl8(x, (i % 7) + 1)    # 3) pozisyona bagli sola bit dondurme
        out.append(x)
        prev = x                     # zincir: bir sonraki bayt bunu kullanir
    return out

# Gizli flag bu sekilde kodlandi:
data = [84, 144, 144, 65, 199, 20, 66, 221, 25, 179, 145, 34, 100, 80, 61,
        207, 0, 190, 171, 23, 116, 17, 100, 19, 65, 171, 32, 130, 87, 185,
        124, 227, 22, 81, 3, 198, 254]

# flag = ?
