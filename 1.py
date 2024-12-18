import random


def get_user_move():
    while True:
        try:
            move = int(input("Возьмите 1, 2 или 3 камня: "))
        except ValueError:
            print("Введите число.")
        else:
            if move in [1, 2, 3]:
                return move
            else:
                print("Некорректный ввод.")


def get_computer_move(st):
    return random.choice([1, 2, 3])


stones = random.randint(4, 30)
print(f"Начальное кол-во камней: {stones}")

while stones > 0:
    user_move = get_user_move()
    stones -= user_move
    if stones <= 0:
        print("Вы одержали победу!")
        break
    print(f"Осталось камней: {stones}")

    computer_move = get_computer_move(stones)
    print(f"Компьютер берет {computer_move} камня(ей).")
    stones -= computer_move
    if stones <= 0:
        print("Компьютер одержал победу!")
        break
    print(f"Осталось камней: {stones}")
