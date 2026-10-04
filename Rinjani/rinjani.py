import os
import sys
import time
import random
import textwrap


APP_NAME = "BIRTHDAY ADVENTURE"
VERSION = "2.0"

RESET = "\033[0m"
BOLD = "\033[1m"

CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
WHITE = "\033[97m"

USE_COLOR = True


def color(text, color_code):
    if USE_COLOR:
        return f"{color_code}{text}{RESET}"
    return text


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def type_text(text, delay=0.03, end="\n"):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(end=end)


def pause(seconds=1):
    time.sleep(seconds)


def show_header(title):
    print()
    print(color("╭────────────────────────────────────────────╮", CYAN))
    print(color(f"│  {title.center(40)}  │", CYAN))
    print(color("╰────────────────────────────────────────────╯", CYAN))
    print()


def loading_animation():
    clear_screen()

    print(color("""
    ██████╗ ██╗██████╗ ████████╗██╗  ██╗██████╗  █████╗ ██╗   ██╗
    ██╔══██╗██║██╔══██╗╚══██╔══╝██║  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██████╔╝██║██████╔╝   ██║   ███████║██║  ██║███████║ ╚████╔╝
    ██╔══██╗██║██╔══██╗   ██║   ██╔══██║██║  ██║██╔══██║  ╚██╔╝
    ██████╔╝██║██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║   ██║
    ╚═════╝ ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝
    """, MAGENTA))

    print()

    messages = [
        "BOOTING BIRTHDAY SYSTEM",
        "Loading celebration modules",
        "Connecting to happiness database",
        "Searching for today's special person"
    ]

    for message in messages:
        print(color(message, CYAN), end="")

        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)

        print(" " + color("[OK]", GREEN))

    pause(1)


def introduction():
    clear_screen()

    show_header("BIRTHDAY PROTOCOL v2.0")

    type_text(
        color("SYSTEM INITIALIZING...", CYAN),
        0.04
    )

    pause(0.5)

    type_text(
        color("Scanning today's calendar...", WHITE),
        0.03
    )

    pause(0.7)

    type_text(
        color("Searching for today's special person...", YELLOW),
        0.03
    )

    pause(1)

    print()

    print(color("      [████████████████████] 100%", GREEN))

    pause(0.7)

    print()

    type_text(
        color(">>> SPECIAL PERSON DETECTED <<<", MAGENTA),
        0.05
    )

    pause(1)

    print()

    type_text(
        "The Birthday Protocol requires one final piece of data."
    )

    print()


def get_name():
    while True:
        name = input(
            color("Enter the Birthday Person's name: ", CYAN)
        ).strip()

        if name:
            return name

        print(color(
            "Nama tidak boleh kosong. Bahkan robot ulang tahun punya standar.",
            RED
        ))


def birthday_cake():
    print(color(r"""
                 i i i i i
                |:H:a:p:p:y:|
             __ |___________| __
            |                 |
            |   BIRTHDAY!     |
            |_________________|
             \_______________/
              \_____________/
               |           |
               |___________|
    """, YELLOW))


def mission_lucky_number():
    clear_screen()

    show_header("MISSION 01 // LUCKY NUMBER")

    print(color("""
    ╔══════════════════════════════════════════╗
    ║        THE LUCKY NUMBER PROTOCOL        ║
    ╚══════════════════════════════════════════╝
    """, BLUE))

    print(
        "Sistem telah memilih angka keberuntungan rahasia "
        "antara 1 sampai 10."
    )

    print(
        color("Kamu punya 3 kesempatan untuk menemukannya.\n", YELLOW)
    )

    secret = random.randint(1, 10)
    attempts = 3

    for attempt in range(1, attempts + 1):

        while True:
            try:
                guess = int(input(
                    f"Attempt {attempt}/3 > Masukkan angka 1-10: "
                ))

                if 1 <= guess <= 10:
                    break

                print(color("Masukkan angka antara 1 dan 10.", RED))

            except ValueError:
                print(color("Input harus berupa angka.", RED))

        if guess == secret:
            points = 40 - ((attempt - 1) * 10)

            print()
            type_text(
                color(">>> JACKPOT! ANGKA BENAR! <<<", GREEN),
                0.04
            )

            print(
                color(f"+{points} BIRTHDAY POINTS", YELLOW)
            )

            pause(1)

            return points

        elif guess < secret:
            print(color("Terlalu kecil.", YELLOW))

        else:
            print(color("Terlalu besar.", YELLOW))

    print()
    print(color(f"Angka rahasianya adalah {secret}.", MAGENTA))
    print(color("+5 BIRTHDAY POINTS karena tetap berjuang.", YELLOW))

    pause(1)

    return 5


def mission_mystery_box():
    clear_screen()

    show_header("MISSION 02 // MYSTERY GIFT")

    print(color("""
       ┌────────┐     ┌────────┐     ┌────────┐
       │   ?    │     │   ?    │     │   ?    │
       │        │     │        │     │        │
       │ MYSTERY│     │ MYSTERY│     │ MYSTERY│
       └────────┘     └────────┘     └────────┘
          [1]            [2]            [3]
    """, MAGENTA))

    print("Tiga kotak misterius terdeteksi.")
    print("Satu berisi bonus besar.")
    print("Satu berisi bonus kecil.")
    print("Satu berisi kejutan...")

    print()

    while True:
        choice = input(
            color("Pilih kotak [1/2/3]: ", CYAN)
        ).strip()

        if choice in ["1", "2", "3"]:
            break

        print(color("Pilih 1, 2, atau 3.", RED))

    boxes = {
        "1": random.randint(10, 30),
        "2": random.randint(10, 30),
        "3": random.randint(10, 30)
    }

    jackpot_box = random.choice(["1", "2", "3"])
    boxes[jackpot_box] = 50

    print()
    type_text("Unlocking mystery box...", 0.04)

    pause(1)

    print()

    if choice == jackpot_box:

        print(color("""
        ✨✨✨ MYSTERY JACKPOT ✨✨✨
        """, YELLOW))

        print(
            color("Kamu menemukan Birthday Treasure!", GREEN)
        )

        points = 50

    else:

        points = boxes[choice]

        print(color(
            "Kotak terbuka... ternyata isinya hadiah kejutan!",
            MAGENTA
        ))

        print(
            color(f"Kamu mendapatkan +{points} poin.", YELLOW)
        )

    pause(1)

    return points


def mission_trivia(name):
    clear_screen()

    show_header("MISSION 03 // BIRTHDAY TRIVIA")

    print(
        color(
            f"Database trivia untuk {name} telah dibuka.",
            CYAN
        )
    )

    print()

    questions = [
        {
            "question": f"Apa yang paling cocok untuk menggambarkan {name}?",
            "options": [
                "A. Orang yang selalu punya ide random",
                "B. Orang yang suka membantu teman",
                "C. Orang yang selalu mengejar mimpi",
                "D. Semua jawaban bisa benar"
            ],
            "answer": "D"
        },

        {
            "question": "Apa hadiah terbaik untuk ulang tahun?",
            "options": [
                "A. Uang",
                "B. Makanan",
                "C. Jalan-jalan",
                "D. Momen bersama orang tersayang"
            ],
            "answer": "D"
        },

        {
            "question": "Apa yang harus dilakukan setelah bertambah umur?",
            "options": [
                "A. Menjadi lebih bijaksana",
                "B. Mengejar impian",
                "C. Tetap menikmati hidup",
                "D. Semuanya"
            ],
            "answer": "D"
        }
    ]

    score = 0

    for index, q in enumerate(questions, start=1):

        print(
            color(
                f"Question {index}/{len(questions)}",
                MAGENTA
            )
        )

        print(q["question"])

        for option in q["options"]:
            print(option)

        print()

        while True:
            answer = input(
                color("Jawaban [A/B/C/D]: ", CYAN)
            ).strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print(color("Masukkan A, B, C, atau D.", RED))

        if answer == q["answer"]:

            print(color("✓ Jawaban benar!", GREEN))
            score += 20

        else:

            print(
                color(
                    f"✗ Jawaban yang ditentukan sistem: {q['answer']}",
                    RED
                )
            )

        pause(0.7)
        print()

    print(
        color(
            f"Trivia selesai! Kamu mendapatkan {score} poin.",
            YELLOW
        )
    )

    pause(1)

    return score


def calculate_rank(score):

    if score >= 130:
        return (
            "LEGENDARY BIRTHDAY",
            "Birthday Legend",
            "Kamu berhasil menaklukkan Birthday Protocol."
        )

    elif score >= 90:
        return (
            "EPIC BIRTHDAY",
            "Birthday Explorer",
            "Petualangan ulang tahunmu berjalan sangat epik."
        )

    elif score >= 60:
        return (
            "AMAZING BIRTHDAY",
            "Birthday Adventurer",
            "Kamu berhasil melewati seluruh misi."
        )

    else:
        return (
            "BIRTHDAY ROOKIE",
            "Birthday Starter",
            "Perjalanan baru saja dimulai. Banyak petualangan menunggu."
        )


def surprise_one(name):
    clear_screen()

    show_header("SECRET EVENT UNLOCKED")

    print(color("""
       ╔══════════════════════════════════╗
       ║       HIDDEN MESSAGE FOUND      ║
       ╚══════════════════════════════════╝
    """, MAGENTA))

    pause(0.8)

    type_text(
        color(
            f"Sistem menemukan pesan tersembunyi untuk {name}.",
            CYAN
        ),
        0.04
    )

    pause(1)

    type_text(
        color(
            "Tidak semua hadiah harus berupa benda.",
            YELLOW
        ),
        0.05
    )

    pause(0.7)

    type_text(
        color(
            "Beberapa hadiah adalah momen yang akan diingat.",
            GREEN
        ),
        0.05
    )

    pause(1)


def surprise_two(name):
    clear_screen()

    show_header("FINAL BIRTHDAY SCAN")

    type_text(
        "Scanning birthday energy...",
        0.04
    )

    for i in range(1, 6):
        print(
            color(
                f"[{'█' * i}{'░' * (5-i)}]",
                CYAN
            )
        )
        pause(0.2)

    print()

    type_text(
        color(
            f"Birthday energy of {name}: 100%",
            YELLOW
        ),
        0.05
    )

    pause(1)

    type_text(
        color(
            "SYSTEM MESSAGE: Today is officially your day.",
            MAGENTA
        ),
        0.05
    )

    pause(1)


def countdown():
    clear_screen()

    print()
    print()

    type_text(
        color(
            "THE BIRTHDAY PROTOCOL IS READY...",
            CYAN
        ),
        0.05
    )

    pause(1)

    for number in ["3", "2", "1"]:

        print()
        print(
            color(
                number.center(50),
                YELLOW
            )
        )

        pause(1)

    clear_screen()

    print()
    print()

    print(
        color(
            "██████╗ ██╗   ██╗██████╗ ████████╗██╗  ██╗",
            MAGENTA
        )
    )

    print(
        color(
            "██╔══██╗██║   ██║██╔══██╗╚══██╔══╝██║  ██║",
            MAGENTA
        )
    )

    print(
        color(
            "██████╔╝██║   ██║██████╔╝   ██║   ███████║",
            MAGENTA
        )
    )

    print(
        color(
            "██╔══██╗██║   ██║██╔══██╗   ██║   ██╔══██║",
            MAGENTA
        )
    )

    print(
        color(
            "██████╔╝╚██████╔╝██║  ██║   ██║   ██║  ██║",
            MAGENTA
        )
    )

    print()

    print(
        color(
            "              HAPPY BIRTHDAY!",
            YELLOW
        )
    )

    print()


def confetti():

    symbols = ["*", "+", ".", "#", "✦"]

    for _ in range(18):

        line = ""

        for _ in range(70):
            line += random.choice(symbols + [" "] * 5)

        print(
            color(
                line,
                random.choice(
                    [CYAN, MAGENTA, YELLOW, GREEN, BLUE]
                )
            )
        )

        time.sleep(0.08)


def birthday_message(name, rank):

    clear_screen()

    show_header("PERSONAL BIRTHDAY MESSAGE")

    birthday_cake()

    print()

    type_text(
        color(
            f"Happy Birthday, {name}!",
            YELLOW
        ),
        0.07
    )

    print()

    messages = [
        f"Hari ini bukan cuma soal bertambahnya angka umur, {name}.",
        "Ini tentang semua cerita yang sudah kamu lewati.",
        "Tentang hal-hal yang berhasil kamu lakukan.",
        "Tentang kegagalan yang ternyata mengajarkan sesuatu.",
        "Dan tentang semua hal keren yang masih menunggu di depan."
    ]

    for message in messages:
        type_text(message, 0.025)

    print()

    type_text(
        color(
            "Semoga tahun berikutnya membawa lebih banyak alasan untuk tersenyum.",
            GREEN
        ),
        0.03
    )

    type_text(
        color(
            "Semoga mimpi-mimpi yang sekarang masih terasa jauh perlahan menjadi nyata.",
            CYAN
        ),
        0.03
    )

    type_text(
        color(
            "Dan semoga kamu tetap menjadi versi dirimu yang paling autentik.",
            MAGENTA
        ),
        0.03
    )

    print()

    type_text(
        color(
            f"Achievement Unlocked: {rank}",
            YELLOW
        ),
        0.04
    )

    print()


def birthday_certificate(name, score, rank, achievement):

    clear_screen()

    print(color("""
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║              BIRTHDAY CERTIFICATE                   ║
    ║                                                      ║
    ║                 THE BIRTHDAY                        ║
    ║                  PROTOCOL                            ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    """, CYAN))

    print()

    print(
        color(
            "This certificate is officially awarded to:",
            WHITE
        )
    )

    print()

    print(
        color(
            f"              ✦ {name.upper()} ✦",
            YELLOW
        )
    )

    print()

    print("┌──────────────────────────────────────────────────────┐")
    print(f"│ Birthday Score : {str(score).ljust(34)} │")
    print(f"│ Birthday Rank  : {rank.ljust(34)} │")
    print(f"│ Achievement    : {achievement.ljust(34)} │")
    print("└──────────────────────────────────────────────────────┘")

    print()

    type_text(
        color(
            "Official Birthday System Message:",
            MAGENTA
        ),
        0.04
    )

    print()

    message = (
        f"{name}, semoga perjalananmu di tahun baru kehidupan "
        "ini dipenuhi keberanian, kebahagiaan, pengalaman baru, "
        "dan banyak momen yang layak dikenang."
    )

    print(
        textwrap.fill(
            message,
            width=55
        )
    )

    print()

    print(
        color(
            "STATUS: BIRTHDAY MISSION COMPLETED ✓",
            GREEN
        )
    )

    print()

    print(
        color(
            "Certificate ID: BDAY-" +
            str(random.randint(10000, 99999)),
            CYAN
        )
    )

    print()


def show_message_again(name, rank):

    birthday_message(name, rank)

    input(
        color(
            "\nTekan ENTER untuk kembali...",
            CYAN
        )
    )


def play_birthday_adventure(name):

    total_score = 0

    total_score += mission_lucky_number()

    input(
        color(
            "\nTekan ENTER untuk lanjut ke misi berikutnya...",
            CYAN
        )
    )

    total_score += mission_mystery_box()

    input(
        color(
            "\nTekan ENTER untuk lanjut ke misi terakhir...",
            CYAN
        )
    )

    total_score += mission_trivia(name)

    rank, achievement, _ = calculate_rank(total_score)

    surprise_one(name)

    input(
        color(
            "\nTekan ENTER untuk membuka final surprise...",
            CYAN
        )
    )

    surprise_two(name)

    input(
        color(
            "\nTekan ENTER untuk memulai final celebration...",
            CYAN
        )
    )

    countdown()

    pause(1)

    confetti()

    pause(1)

    birthday_message(name, rank)

    input(
        color(
            "\nTekan ENTER untuk melihat Birthday Certificate...",
            CYAN
        )
    )

    birthday_certificate(
        name,
        total_score,
        rank,
        achievement
    )

    return total_score, rank, achievement


def main():

    loading_animation()

    introduction()

    name = get_name()

    clear_screen()

    print()

    type_text(
        color(
            f"Welcome to the Birthday Adventure, {name}.",
            YELLOW
        ),
        0.05
    )

    type_text(
        color(
            "Your birthday mission begins now...",
            CYAN
        ),
        0.04
    )

    pause(1)

    while True:

        score, rank, achievement = play_birthday_adventure(name)

        print()

        print(color("""
        ╭─────────────────────────────────────────────╮
        │              BIRTHDAY MENU                  │
        │                                             │
        │       [1] Mainkan lagi                     │
        │       [2] Lihat ucapan ulang tahun lagi    │
        │       [3] Keluar                           │
        ╰─────────────────────────────────────────────╯
        """, CYAN))

        while True:

            choice = input(
                color("Pilih menu [1/2/3]: ", YELLOW)
            ).strip()

            if choice in ["1", "2", "3"]:
                break

            print(
                color(
                    "Pilihan hanya 1, 2, atau 3.",
                    RED
                )
            )

        if choice == "1":

            clear_screen()

            print(
                color(
                    "Reinitializing Birthday Protocol...",
                    CYAN
                )
            )

            pause(1)

        elif choice == "2":

            show_message_again(name, rank)

        elif choice == "3":

            clear_screen()

            print()

            type_text(
                color(
                    "Birthday Protocol shutting down...",
                    CYAN
                ),
                0.04
            )

            pause(0.7)

            type_text(
                color(
                    f"Goodbye, {name}. Keep being awesome.",
                    MAGENTA
                ),
                0.04
            )

            print()

            print(
                color(
                    "SYSTEM OFFLINE.",
                    GREEN
                )
            )

            print()

            break


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n")
        print(
            color(
                "Birthday Protocol dihentikan oleh pengguna.",
                YELLOW
            )
        )
        sys.exit(0)