print("Selamat datang di permainan Tebak Angka!")

def get_difficulty():
    while True:
        print("Pilih tingkat kesulitan:")
        print("1. Mudah (1-10)")
        print("2. Sedang (1-50)")
        print("3. Sulit (1-100)")
        choice = input("Masukkan pilihan (1-3): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 50
        elif choice == '3':
            return 100
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

def play_game():
    max_number = get_difficulty()
    import random
    number_to_guess = random.randint(1, max_number)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Tebak angka antara 1 dan {max_number}: "))
            attempts += 1
            if guess < number_to_guess:
                print("Terlalu rendah! Coba lagi.")
            elif guess > number_to_guess:
                print("Terlalu tinggi! Coba Lagi.")
            elif guess == number_to_guess:
                print(f"Selamat! Anda menebak angka {number_to_guess} dalam {attempts} percobaan.")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
           
while True:
    play_game()
    play_again = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
    if play_again == 'y':
        continue
    elif play_again == 'n':
        print("Terima kasih telah bermain! Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Keluar dari permainan.")
        break