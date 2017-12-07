bye_words = ['bye', 'good bye', 'see you']
chg_topic = ['change topic', 'other topic', 'do you know anything else']


class QAModel():
    # dummy
    def __init__(self):
        pass

    def get_answer(self, paragraph, question):
        answer = 'Apple Inc.' # dummy
        return answer


class DBRetriever():
    def __init__(self):
        self.crnt_topic = None

    def search_topic_by_uttr(self, user_uttr):
        # find articles with user uttr from SQuAD...
        title = 'iPod' # dummy
        self.crnt_topic = title
        return title

    def search_paragraph(self, user_uttr):
        # find a specific paragraph which may be related to a user question
        # ex) 'who made iPod touch?'
        paragraph = 'iPod was invented by Apple inc in 1998. For two years ago, they...' # dummy
        return paragraph


class DialogManager():
    def __init__(self):
        self.db_retr = DBRetriever()
        self.model = QAModel()

    def get_action(self, uttr, in_topic):
        sys_uttr = "I'm sorry. I cannot understand what you said"
        topic_end = False
        dlg_end = False
        if uttr in bye_words:
            sys_uttr = "Bye. Have a nice day!"
            dlg_end = True
        elif uttr in chg_topic:
            sys_uttr = "Sure. What kind of topic do you want to talk about?"
            topic_end = True
        else:
            if in_topic:
                paragraph = self.db_retr.search_topic_by_uttr(uttr)
                if paragraph is None:
                    sys_uttr = "Hmmm... I don't know that. I will check it later.\nDo you have other questions?"
                else:
                    answer = self.model.get_answer(paragraph, question=uttr)
                    sys_uttr = "I'd say \"{}\"".format(answer)
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
