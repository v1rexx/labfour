import random


def igrat():
    cumney = random.randint(4, 30)
    print(f"-----------\nВ кучке {cumney} камней\nВы можете брать 1, 2 или 3 камня\n"
          f"Победил тот, кто взял последний камень\n-----------")
    while cumney > 0:
        if cumney < 4:
            kompik_vibral = cumney
        else:
            kompik_vibral = random.randint(1, 3)
        cumney -= kompik_vibral
        print(f"Компьютер выбрал {kompik_vibral}. Осталось камней: {cumney}\n")
        if cumney <= 0:
            print("К сожалению, вы проиграли!\n")
            break
        while True:
            try:
                ya_vibral = int(input("Ваш ход: "))
            except ValueError:
                print('Необходимо ввести число от 1 до 3\n')
                continue
            if ya_vibral < 1 or ya_vibral > 3:
                print("Необходимо взять от 1 до 3 камней.\n")
            elif ya_vibral > cumney:
                print("В кучке недостаточно камней. Попробуйте ещё раз.\n")
            else:
                cumney -= ya_vibral
                print(f"Осталось камней: {cumney}\n")
                break
        if cumney <= 0:
            print("Вы выиграли\n")
            break
    igrat()


igrat()
