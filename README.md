# rinjani

# 🎂 Birthday Adventure

**Birthday Adventure** adalah program Python interaktif bertema **Birthday Mission** yang dirancang sebagai mini game di terminal. Program ini bukan sekadar menampilkan ucapan ulang tahun, tetapi mengajak pengguna menyelesaikan beberapa misi untuk mendapatkan **Birthday Score**, membuka **surprise event**, dan memperoleh **Birthday Certificate**.

Program menggunakan konsep **futuristic terminal / cyber birthday** dengan animasi teks, ASCII art, countdown, confetti, sistem skor, ranking, dan pesan ulang tahun yang dipersonalisasi.

---

## ✨ Features

- Loading animation dengan efek terminal
- Birthday System initialization
- Input nama orang yang berulang tahun
- 3 Birthday Mission interaktif
- Sistem perhitungan skor
- Birthday Rank berdasarkan skor
- Surprise Event
- Final Birthday Scan
- Countdown `3... 2... 1...`
- ASCII Birthday Cake
- Efek confetti
- Typewriter text animation
- Personal birthday message
- Birthday Certificate
- Certificate ID otomatis
- Menu untuk memainkan kembali program
- Menu untuk melihat kembali ucapan ulang tahun
- Validasi input agar program tidak mudah crash
- Dukungan terminal Windows, Linux, dan macOS
- Tidak membutuhkan library eksternal

---

## 🎮 Birthday Missions

### 1. Lucky Number Protocol

Pengguna harus menebak angka rahasia antara **1 sampai 10**.

Pengguna memiliki 3 kesempatan.

Semakin cepat angka berhasil ditebak, semakin besar poin yang diperoleh.

Contoh:

```text
MISSION 01 // LUCKY NUMBER

Sistem telah memilih angka keberuntungan rahasia
antara 1 sampai 10.

Kamu punya 3 kesempatan untuk menemukannya.

Attempt 1/3 > Masukkan angka 1-10:
```

---

### 2. Mystery Gift Protocol

Pengguna diberikan tiga kotak misterius.

```text
       ┌────────┐     ┌────────┐     ┌────────┐
       │   ?    │     │   ?    │     │   ?    │
       │        │     │        │     │        │
       │ MYSTERY│     │ MYSTERY│     │ MYSTERY│
       └────────┘     └────────┘     └────────┘
          [1]            [2]            [3]
```

Salah satu kotak memiliki **Mystery Jackpot** dengan bonus poin lebih besar.

Pilihan pengguna menentukan hadiah yang diperoleh.

---

### 3. Birthday Trivia

Pengguna harus menjawab beberapa pertanyaan trivia.

Setiap jawaban benar akan memberikan tambahan **Birthday Points**.

Pertanyaan dapat dimodifikasi agar lebih personal sesuai dengan orang yang berulang tahun.

---

## 🏆 Birthday Rank

Total skor dari seluruh misi digunakan untuk menentukan ranking.

| Score | Birthday Rank |
|---:|---|
| 130+ | LEGENDARY BIRTHDAY |
| 90–129 | EPIC BIRTHDAY |
| 60–89 | AMAZING BIRTHDAY |
| < 60 | BIRTHDAY ROOKIE |

Setiap rank memiliki achievement dan pesan khusus.

---

## 🎁 Surprise System

Setelah semua mission selesai, program akan menjalankan beberapa event tersembunyi.

### Secret Event

Program menampilkan:

```text
SECRET EVENT UNLOCKED
```

Kemudian sistem memberikan pesan khusus kepada birthday person.

### Final Birthday Scan

Program melakukan simulasi scanning birthday energy.

```text
Birthday energy of [NAME]: 100%

SYSTEM MESSAGE:
Today is officially your day.
```

### Final Countdown

Sebelum perayaan utama dimulai:

```text
3...

2...

1...

HAPPY BIRTHDAY!
```

Kemudian program menampilkan confetti dan pesan ulang tahun.

---

## 📜 Birthday Certificate

Di akhir permainan, pengguna mendapatkan sertifikat digital melalui terminal.

Informasi yang ditampilkan:

```text
BIRTHDAY CERTIFICATE

Name
Birthday Score
Birthday Rank
Achievement
Personal Message
Certificate ID
```

Contoh:

```text
┌──────────────────────────────────────────────────────┐
│ Birthday Score : 125                                │
│ Birthday Rank  : EPIC BIRTHDAY                      │
│ Achievement    : Birthday Explorer                  │
└──────────────────────────────────────────────────────┘

STATUS: BIRTHDAY MISSION COMPLETED ✓

Certificate ID: BDAY-48392
```

---

## 🛠️ Technologies

Project ini dibuat menggunakan:

- **Python 3**
- `os`
- `sys`
- `time`
- `random`
- `textwrap`
- ANSI Escape Code

Tidak menggunakan:

- GUI
- Tkinter
- API
- Internet
- Database
- Library eksternal
- File eksternal

---

## 📂 Project Structure

Struktur sederhana project:

```text
birthday-adventure/
│
├── birthday_adventure.py
└── README.md
```

File utama:

```text
birthday_adventure.py
```

berisi seluruh sistem Birthday Adventure.

---

## 💻 Requirements

Pastikan Python sudah terinstall.

Cek versi Python:

```bash
python --version
```

atau pada beberapa sistem:

```bash
python3 --version
```

Program disarankan dijalankan menggunakan **Python 3.x**.

Tidak diperlukan instalasi package tambahan.

---

## 🚀 How to Run

Clone repository:

```bash
git clone https://github.com/USERNAME/birthday-adventure.git
```

Masuk ke folder:

```bash
cd birthday-adventure
```

Jalankan program:

```bash
python birthday_adventure.py
```

Jika menggunakan Linux/macOS:

```bash
python3 birthday_adventure.py
```

Pada Windows, alternatifnya:

```bash
py birthday_adventure.py
```

---

## 🎨 Customization

Program dibuat supaya mudah dimodifikasi.

### Mengubah Warna

Warna terminal terdapat pada bagian awal program:

```python
CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
WHITE = "\033[97m"
```

Jika terminal tidak mendukung warna ANSI:

```python
USE_COLOR = False
```

---

### Mengubah Pertanyaan Trivia

Pertanyaan terdapat pada function:

```python
def mission_trivia(name):
```

Kemudian edit bagian:

```python
questions = [
    {
        "question": "...",
        "options": [
            "A. ...",
            "B. ...",
            "C. ...",
            "D. ..."
        ],
        "answer": "D"
    }
]
```

Bagian `answer` menentukan jawaban yang benar.

---

### Mengubah Pesan Ulang Tahun

Pesan personal terdapat pada:

```python
def birthday_message(name, rank):
```

Kalimat dapat disesuaikan dengan karakter, hubungan, atau cerita orang yang sedang berulang tahun.

---

### Mengubah Sistem Ranking

Ranking dapat diubah pada:

```python
def calculate_rank(score):
```

Contohnya:

```python
if score >= 130:
    return (
        "LEGENDARY BIRTHDAY",
        "Birthday Legend",
        "Kamu berhasil menaklukkan Birthday Protocol."
    )
```

Nilai threshold dan nama rank dapat disesuaikan.

---

## 🧠 Program Flow

Secara sederhana, alur program adalah:

```text
START
  │
  ▼
Loading Animation
  │
  ▼
Birthday System Initialization
  │
  ▼
Input Birthday Person
  │
  ▼
Mission 01
Lucky Number
  │
  ▼
Mission 02
Mystery Gift
  │
  ▼
Mission 03
Birthday Trivia
  │
  ▼
Calculate Score
  │
  ▼
Determine Birthday Rank
  │
  ▼
Secret Event
  │
  ▼
Final Birthday Scan
  │
  ▼
Countdown
  │
  ▼
Happy Birthday
  │
  ▼
Confetti
  │
  ▼
Personal Message
  │
  ▼
Birthday Certificate
  │
  ▼
Birthday Menu
