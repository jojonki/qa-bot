bye_words = ['bye', 'good bye', 'see you']


class DBRetriever():
    def __init__(self):
        pass

    def search_topic_by_uttr(self, user_uttr):
        return "iPod"

    def search_topic_by_title(self, topic_title):
        pass


class DialogManager():
    def __init__(self):
        self.db_retr = DBRetriever()

    def get_action(self, uttr, in_topic):
        sys_uttr = "I'm sorry. I cannot understand what you said"
        topic_end = False
        dlg_end = False
        if uttr in bye_words:
            return 'Bye', True
        else:
            if in_topic:
                pass
            else:
                # try to retrieve a topic what user said
                topic = self.db_retr.search_topic_by_uttr(uttr)
                if topic is None:
                    sys_uttr = "I cannot find a topic what you want to ask"
                else:
                    sys_uttr = "OK. I know a lot about \"{}\". Ask Me Anything!".format(topic)

        return {'sys_uttr': sys_uttr,
                'topic_end': topic_end,
                'dlg_end': dlg_end}
