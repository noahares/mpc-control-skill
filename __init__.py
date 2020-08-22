from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import subprocess


class MpcControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        play_music_intent = IntentBuilder('PlayIntent').require('play.music').build()
        self.register_intent(play_music_intent, self.handle_play_music_intent)

        stop_music_intent = IntentBuilder('StopIntent').require('stop.music').build()
        self.register_intent(stop_music_intent, self.handle_stop_music_intent)

        next_song_intent = IntentBuilder('nextIntent').require('next.song').build()
        self.register_intent(next_song_intent, self.handle_next_song_intent)

        previous_song_intent = IntentBuilder('previousIntent').require('previous.song').build()
        self.register_intent(previous_song_intent, self.handle_previous_song_intent)

    def handle_play_music_intent(self, message):
        self.speak_dialog('start.music')
        subprocess.run(['mpc', 'play'])

    def handle_stop_music_intent(self, message):
        self.speak_dialog('stop.music')
        subprocess.run(['mpc', 'pause'])

    def handle_next_song_intent(self, message):
        self.speak_dialog('next.song')
        subprocess.run(['mpc', 'next'])

    def handle_previous_song_intent(self, message):
        self.speak_dialog('previous.song')
        subprocess.run(['mpc', 'prev'])

    @intent_handler('play.song.intent')
    def handle_play_song_intent(self, message):
        song_title = message.data.get('title')
        subprocess.run(['mpc', 'searchplay', song_title])
        self.speak("This is what I found for %s" % song_title)

def stop(self):
    pass

def create_skill():
    return MpcControl()
