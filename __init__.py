from mycroft import MycroftSkill, intent_file_handler


class MpcControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.mpc.intent')
    def handle_control_mpc(self, message):
        self.speak_dialog('control.mpc')


def create_skill():
    return MpcControl()

