from log_config import log


@log
def drink_vodka():
    print("Выпьешь с нами водочки? yes/no")
    a = input()
    if a == "yes":
        print("Тебя спалили, получай штраф 50% зарплаты")
    elif a == "no":
        print("Теперь ты нам не товарищ!")
    else:
        print("Чо ты несешь? Он и так пьяный!")




