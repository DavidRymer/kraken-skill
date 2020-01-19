from mycroft import MycroftSkill, intent_file_handler


class Kraken(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('kraken.intent')
    def handle_kraken(self, message):
        self.speak_dialog('kraken')


def create_skill():
    return Kraken()

