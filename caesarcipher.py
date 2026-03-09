"""
╔══════════════════════════════════════════════════════════╗
║           CAESAR CIPHER - Enkripsi & Dekripsi Klasik     ║
╚══════════════════════════════════════════════════════════╝

Caesar Cipher adalah salah satu teknik enkripsi paling kuno,
digunakan oleh Julius Caesar untuk komunikasi rahasia militer.
Prinsipnya: setiap huruf digeser sejumlah posisi tertentu
dalam alfabet.

Contoh shift=3:
  A → D, B → E, C → F, ..., X → A, Y → B, Z → C
"""


def enkripsi(teks: str, shift: int) -> str:
    """
    Mengenkripsi teks menggunakan Caesar Cipher.

    Args:
        teks  : Teks asli (plaintext) yang ingin dienkripsi
        shift : Jumlah pergeseran huruf (1–25)

    Returns:
        Teks terenkripsi (ciphertext)
    """
    hasil = []

    for karakter in teks:
        if karakter.isalpha():                  # Hanya proses huruf
            # Tentukan basis: 'A' untuk huruf besar, 'a' untuk huruf kecil
            basis = ord('A') if karakter.isupper() else ord('a')

            # Geser huruf dan wrap menggunakan modulo 26
            huruf_baru = chr((ord(karakter) - basis + shift) % 26 + basis)
            hasil.append(huruf_baru)
        else:
            hasil.append(karakter)              # Karakter non-huruf tetap

    return ''.join(hasil)


def dekripsi(teks: str, shift: int) -> str:
    """
    Mendekripsi teks yang dienkripsi dengan Caesar Cipher.

    Args:
        teks  : Teks terenkripsi (ciphertext)
        shift : Jumlah pergeseran yang digunakan saat enkripsi

    Returns:
        Teks asli (plaintext)
    """
    # Dekripsi = enkripsi dengan shift berlawanan arah
    return enkripsi(teks, -shift)


def brute_force(ciphertext: str) -> None:
    """
    Mencoba semua kemungkinan shift (1–25) untuk memecahkan enkripsi
    tanpa mengetahui kunci (brute force attack).

    Args:
        ciphertext : Teks terenkripsi yang ingin dipecahkan
    """
    print("\n" + "=" * 55)
    print("  BRUTE FORCE - Semua Kemungkinan Kunci")
    print("=" * 55)

    for shift in range(1, 26):
        hasil = dekripsi(ciphertext, shift)
        print(f"  Shift {shift:>2} : {hasil}")

    print("=" * 55)


def tampilkan_tabel_alfabet(shift: int) -> None:
    """
    Menampilkan tabel pemetaan huruf asli → huruf terenkripsi.

    Args:
        shift : Jumlah pergeseran
    """
    print(f"\n  Tabel Enkripsi (Shift = {shift})")
    print("  " + "-" * 44)

    # Baris huruf asli
    asli = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    enkr = [chr((i + shift) % 26 + ord('A')) for i in range(26)]

    print("  Asli  : " + " ".join(asli))
    print("  Cipher: " + " ".join(enkr))
    print("  " + "-" * 44)


# ─────────────────────────────────────────────────────────
#  DEMO INTERAKTIF
# ─────────────────────────────────────────────────────────

def demo():
    """Demonstrasi lengkap Caesar Cipher."""

    print("╔══════════════════════════════════════════════════════╗")
    print("║          CAESAR CIPHER — Demo Interaktif             ║")
    print("╚══════════════════════════════════════════════════════╝")

    # ── Contoh 1: Enkripsi & Dekripsi Dasar ──────────────────
    print("\n📌 CONTOH 1 — Enkripsi & Dekripsi Dasar")
    print("─" * 45)

    plaintext = "Hello World"
    shift = 13                                 # ROT13 adalah shift=13

    ciphertext = enkripsi(plaintext, shift)
    hasil_dekripsi = dekripsi(ciphertext, shift)

    print(f"  Plaintext  : {plaintext}")
    print(f"  Shift      : {shift}")
    print(f"  Ciphertext : {ciphertext}")
    print(f"  Dekripsi   : {hasil_dekripsi}")

    # ── Contoh 2: Teks dengan angka & simbol ─────────────────
    print("\n📌 CONTOH 2 — Teks Campuran (angka & simbol diabaikan)")
    print("─" * 45)

    plaintext2 = "Belajar Python 101! Seru banget :)"
    shift2 = 7

    cipher2 = enkripsi(plaintext2, shift2)
    dekripsi2 = dekripsi(cipher2, shift2)

    print(f"  Plaintext  : {plaintext2}")
    print(f"  Shift      : {shift2}")
    print(f"  Ciphertext : {cipher2}")
    print(f"  Dekripsi   : {dekripsi2}")

    # ── Tabel Alfabet ─────────────────────────────────────────
    tampilkan_tabel_alfabet(shift2)

    # ── Contoh 3: Brute Force ─────────────────────────────────
    print("\n📌 CONTOH 3 — Brute Force Attack")
    print("─" * 45)
    pesan_rahasia = "Wkh txlfn eurzq ira"   # shift=3 dari "The quick brown fox"
    print(f"  Ciphertext misterius: \"{pesan_rahasia}\"")
    print("  Kita tidak tahu kuncinya — coba semua kemungkinan!")

    brute_force(pesan_rahasia)

    # ── Mode Interaktif ───────────────────────────────────────
    print("\n" + "═" * 55)
    print("  MODE INTERAKTIF — Coba Sendiri!")
    print("═" * 55)

    while True:
        print("\n  Pilihan:")
        print("  [1] Enkripsi teks")
        print("  [2] Dekripsi teks")
        print("  [3] Brute force ciphertext")
        print("  [0] Keluar")

        pilihan = input("\n  Masukkan pilihan: ").strip()

        if pilihan == "0":
            print("\n  👋 Terima kasih! Program selesai.")
            break

        elif pilihan in ("1", "2"):
            teks = input("  Masukkan teks   : ")
            try:
                shift_input = int(input("  Masukkan shift  : "))
                shift_input = shift_input % 26   # Normalisasi

                if pilihan == "1":
                    hasil = enkripsi(teks, shift_input)
                    print(f"  ✅ Ciphertext   : {hasil}")
                else:
                    hasil = dekripsi(teks, shift_input)
                    print(f"  ✅ Plaintext    : {hasil}")

            except ValueError:
                print("  ❌ Shift harus berupa angka!")

        elif pilihan == "3":
            ct = input("  Masukkan ciphertext: ")
            brute_force(ct)

        else:
            print("  ❌ Pilihan tidak valid!")


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    demo()