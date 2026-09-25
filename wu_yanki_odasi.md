# 🎯 Yankı Odası - Network

🔍 Çözüm

1) pcap'i aç
`trafik.pcap` dosyasını Wireshark ile aç. Çoğu paket DNS gürültüsü; bir de 80 portuna HTTP trafiği var.

2) HTTP akışını takip et
Bir HTTP GET isteği görünür: `GET /rapor.txt`. Sağ tık → Follow → HTTP Stream (ya da TCP Stream).

3) Aktarılan dosyayı oku
Sunucunun cevabında düz metin bir rapor gelir; içinde flag yazılı.

Komut satırıyla:
```bash
tshark -r trafik.pcap -q -z follow,tcp,ascii,0
# veya
strings trafik.pcap | grep pitoctf
```

🚩 FLAG: pitoctf{pc4p_1c1nd3_g1zl1_d0sy4}

Öğretici not: Şifresiz protokoller (HTTP, FTP, Telnet) ağı dinleyen herkese açıktır. Hassas veri her zaman TLS ile taşınmalı.

**~yigit.atmacaaa**
