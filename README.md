# 🔐 Caesar Cipher — Enkripsi & Dekripsi Klasik

Implementasi **Caesar Cipher** dalam Python — salah satu teknik kriptografi tertua yang digunakan oleh Julius Caesar untuk komunikasi militer rahasia.

---

## 📖 Apa itu Caesar Cipher?

Caesar Cipher bekerja dengan **menggeser** setiap huruf dalam alfabet sejumlah posisi tertentu (disebut **shift** atau **kunci**).

```
Contoh shift = 10:
  Plaintext : A B C D E F ... X Y Z
  Ciphertext: K L M N O P ... A B C

Pesan    : Nurul Hidayah
Terenkripsi: Xebev Rsnkikr
```

---

## 📁 Struktur File

```
caesar_cipher.py   ← File utama program
README.md          ← Dokumentasi ini
```

---

## ⚙️ Cara Menjalankan

**Persyaratan:** Python 3.x (tidak ada library eksternal yang dibutuhkan)

```bash
python3 caesar_cipher.py
```

---

## 🧩 Fitur

| Fitur | Deskripsi |
|---|---|
| **Enkripsi** | Mengubah plaintext menjadi ciphertext dengan kunci shift |
| **Dekripsi** | Mengembalikan ciphertext ke plaintext menggunakan kunci yang sama |
| **Brute Force** | Mencoba semua 25 kemungkinan shift tanpa mengetahui kunci |
| **Tabel Alfabet** | Menampilkan pemetaan huruf asli → huruf terenkripsi |
| **Mode Interaktif** | Input teks dan kunci sendiri langsung di terminal |

---

## 📦 Fungsi Utama

### `enkripsi(teks, shift)`
Mengenkripsi teks dengan menggeser setiap huruf sebanyak `shift` posisi ke depan.

```python
enkripsi("Nurul Hidayah", 10)
# Output: "Xebev Rsnkikr"
```

### `dekripsi(teks, shift)`
Mendekripsi ciphertext dengan menggeser huruf ke arah sebaliknya.

```python
dekripsi("Xebev Rsnkikr", 10)
# Output: "Nurul Hidayah"
```

### `brute_force(ciphertext)`
Mencoba semua kemungkinan shift (1–25) dan menampilkan seluruh hasilnya.

```python
brute_force("Wkh txlfn eurzq ira")
# Shift  3 : The quick brown fox  ← kunci ditemukan!
```

---

## 📝 Catatan Penting

- **Huruf besar/kecil** dipertahankan (A tetap A, a tetap a)
- **Angka, spasi, dan simbol** tidak dienkripsi — dibiarkan apa adanya
- **Shift valid:** 1–25 (shift 0 atau 26 tidak mengubah apapun)
- **ROT13** adalah Caesar Cipher dengan `shift = 13` (paling umum digunakan)

---

## 🔓 Kelemahan Caesar Cipher

Caesar Cipher termasuk enkripsi **sangat lemah** karena:
- Hanya ada **25 kemungkinan kunci** → mudah di-brute force
- Rentan terhadap **analisis frekuensi** huruf
- **Tidak cocok** untuk keamanan modern — hanya untuk edukasi

---

## 💡 Contoh Penggunaan

```python
from caesar_cipher import enkripsi, dekripsi, brute_force

# Enkripsi
pesan = "Belajar Kriptografi"
kunci = 5
cipher = enkripsi(pesan, kunci)
print(cipher)   # Gjqfofs Pwnuytlwfkn

# Dekripsi
asli = dekripsi(cipher, kunci)
print(asli)     # Belajar Kriptografi

# Brute force
brute_force("Mjqqt")   # Akan menampilkan "Hello" di Shift 5
```

---

## 📚 Referensi

- [Wikipedia — Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Kriptografi Klasik — Britannica](https://www.britannica.com/topic/cryptology)