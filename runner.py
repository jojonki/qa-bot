from dialog_mgr import DialogManager


def s_print(uttr):
    print('S:', uttr)


def run_console():
    dm = DialogManager()
    in_topic = False

    print("S: Hi! My name is AMA. Yo can ask me anything.")
    print("   What kind of topic do you want to talk about?")
    while True:
        u = input("U: ")
        u = u.lower()
        act = dm.get_action(u, in_topic)
        in_topic = not act['topic_end']
        s_print(act['sys_uttr'])
        if act['dlg_end']:
            break

run_console()
