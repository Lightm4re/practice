import random

wins = 0
losses = 0
consecutive_losses = 0

while consecutive_losses < 3:
    guess = input("Введите 0 для выбора орла, 1 для выбора решки (любое другое число - выход): ")

    if guess == "0":
        user_choice = "орел"
    elif guess == "1":
        user_choice = "решка"
    else:
        break

    coin_flip = random.choice(["орел", "решка"])
    print("Вы выбрали:", user_choice)
    print("Монетка упала. Сверху:", coin_flip)

    if user_choice == coin_flip:
        print("Вы угадали!")
        wins += 1
        consecutive_losses = 0
    else:
        print("Вы не угадали.")
        losses += 1
        consecutive_losses += 1
    print()

print("Выигрыши:", wins)
print("Проигрыши:", losses)
print("Игра завершена.")
