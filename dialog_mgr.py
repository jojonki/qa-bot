bye_words = ['bye', 'good bye', 'see you']


class DialogManager():
    def __init__(self):
        pass

    def get_action(self, u):
        if u in bye_words:
            return 'Bye', True
        else:
            return "I'm sorry. I cannot understand what you said", False
