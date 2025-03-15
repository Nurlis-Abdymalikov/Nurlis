import configparser
import random


def load_config(file_path="settings.ini"):
    config = configp arser.ConfigParser()
    config.read(file_path)

    settings = config["Settings"]
    return {
        "min_number": int(settings["min_number"]),
        "max_number": int(settings["max_number"]),
        "attempts": int(settings["attempts"]),
        "capital": int(settings["capital"])
    }


def guess_the_number():
    config = load_config()
    min_num = config["min_number"]
    max_num = config["max_number"]
    attempts = config["attempts"]
    capital = config["capital"]

    secret_number = random.randint(min_num, max_num)
    print(f"Добро пожаловать в игру 'Угадай число'! Загадано число от {min_num} до {max_num}.")
    print(f"У вас {attempts} попыток и стартовый капитал {capital} монет.")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}. Ваш текущий капитал: {capital} монет.")
        try:
            bet = int(input("Сделайте ставку: "))
            if bet <= 0 or bet > capital:
                print("Некорректная ставка! Попробуйте снова.")
                continue

            guess = int(input(f"Введите число от {min_num} до {max_num}: "))

            if guess < min_num or guess > max_num:
                print("Число вне диапазона! Попробуйте снова.")
                continue

            if guess == secret_number:
                print(f"Поздравляем! Вы угадали число {secret_number} и выиграли {bet * 2} монет!")
                capital += bet * 2
                break
            else:
                print("Неверно! Вы потеряли свою ставку.")
                capital -= bet

            if capital <= 0:
                print("Вы проиграли весь капитал! Игра окончена.")
                break
        except ValueError:
            print("Ошибка ввода! Введите число.")

    print(f"Игра окончена! Загаданное число было: {secret_number}. Ваш итоговый капитал: {capital} монет.")
