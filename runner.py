from dialog_mgr import DialogManager

dm = DialogManager()


def s_print(uttr):
    print('S:', uttr)


def run_console():
    u = input("S: Hi! My name is AMA. Yo can ask me anything.\nU: ")
    u = u.lower()
    act, end = dm.get_action(u)
    s_print(act)
    while True:
        u = input("U: ")
        u = u.lower()
        act, end = dm.get_action(u)
        s_print(act)
        if end:
            break

run_console()
