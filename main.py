import os
os.environ['KIVY_AUDIO'] = 'sdl2'

from kivy.app import App
from kivy.core.audio import SoundLoader
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Point, GraphicException
from kivy.uix.boxlayout import BoxLayout
from random import random
from note_list import note_list
from kivy.core.window import Window
import signal
import sys
import RPi.GPIO as GPIO

BUTTON_GPIO = 16

class FretBoard(FloatLayout):

    Window.size = (480, 320)
    Window.fullscreen = True
    NOTE_NAME = ''

    def on_touch_down(self, touch):
        #win = self.get_parent_window()
        ud = touch.ud
        ud['group'] = g = str(touch.uid)
        pointsize = 5
        if 'pressure' in touch.profile:
            ud['pressure'] = touch.pressure
            pointsize = (touch.pressure * 100000) * 2
        ud['color'] = random()
        """
        with self.canvas:
            Color(ud['color'], 1, 1, mode='hsv', group=g)
            ud['lines'] = [
                Rectangle(pos=(touch.x, 0), size=(1, win.height), group=g),
                Rectangle(pos=(0, touch.y), size=(win.width, 1), group=g),
                Point(points=(touch.x, touch.y), source='particle.png',
                      pointsize=pointsize, group=g)]
        """
        ud['label'] = Label(size_hint=(None, None))

        touch.grab(self)

        #begin screen 4 note assignment
        sound = SoundLoader.load(note_list.E1.file_name())
        # Section 5 (if needed)
        if touch.x > 430 and touch.y > 254 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.E1.file_name())
            NOTE_NAME = '1E'
            sound.play()
        if touch.x > 430 and 254 > touch.y > 161 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.A1.file_name())
            NOTE_NAME = '1A'
            sound.play()
        if touch.x > 430 and 161 > touch.y > 73 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.D2.file_name())
            NOTE_NAME = '2D'
            sound.play()
        if touch.x > 430 and 73 > touch.y and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.G2.file_name())
            NOTE_NAME = 'G2'
            sound.play()

        #Section 4
        if 430 > touch.x > 330 and touch.y > 254 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.F1.file_name())
            NOTE_NAME = '1F'
            sound.play()
        if 430 > touch.x > 330 and 254 > touch.y > 161 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.A1_sharp.file_name())
            NOTE_NAME = '1A#'
            sound.play()
        if 430 > touch.x > 330 and 161 > touch.y > 73 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.D2_sharp.file_name())
            NOTE_NAME = '2D#'
            sound.play()
        if 430 > touch.x > 330 and 73 > touch.y and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.G2_sharp.file_name())
            NOTE_NAME = '2G#'
            sound.play()

        #Section 3
        if 330 > touch.x > 230 and touch.y > 254 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.F1_sharp.file_name())
            NOTE_NAME = '1F#'
            sound.play()
        if 330 > touch.x > 230 and 254 > touch.y > 161 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.B1.file_name())
            NOTE_NAME = '1B'
            sound.play()
        if 330 > touch.x > 230 and 161 > touch.y > 73 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.E2.file_name())
            NOTE_NAME = '2E'
            sound.play()
        if 330 > touch.x > 230 and 73 > touch.y and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.A2.file_name())
            NOTE_NAME = '2A'
            sound.play()

        #Section 2
        if 230 > touch.x > 125 and touch.y > 254 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.G1.file_name())
            NOTE_NAME = '1G'
            sound.play()
        if 230 > touch.x > 125 and 254 > touch.y > 161 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.C2.file_name())
            NOTE_NAME = '2C'
            sound.play()
        if 230 > touch.x > 125 and 161 > touch.y > 73 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.F2.file_name())
            NOTE_NAME = '2F'
            sound.play()
        if 230 > touch.x > 125 and 73 > touch.y and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.A2_sharp.file_name())
            NOTE_NAME = '2A#'
            sound.play()

        #Section 1
        if 125 > touch.x > 25 and touch.y > 254 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.G1_sharp.file_name())
            NOTE_NAME = '1G#'
            sound.play()
        if 125 > touch.x > 25 and 254 > touch.y > 161 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.C2_sharp.file_name())
            NOTE_NAME = '2C#'
            sound.play()
        if 125 > touch.x > 25 and 161 > touch.y > 73 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.F2_sharp.file_name())
            NOTE_NAME = '2F#'
            sound.play()
        if 125 > touch.x > 25 and 73 > touch.y and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.B2.file_name())
            NOTE_NAME = '2B'
            sound.play()

        #Section 0 (if needed)
        if 25 > touch.x and touch.y > 254 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.A1.file_name())
            NOTE_NAME = '1A'
            sound.play()
        if 25 > touch.x and 254 > touch.y > 161 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.D2.file_name())
            NOTE_NAME = '2D'
            sound.play()
        if 25 > touch.x and 161 > touch.y > 73 and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.G2.file_name())
            NOTE_NAME = '2G'
            sound.play()
        if 25 > touch.x and 73 > touch.y and GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING):
            sound.unload()
            sound = SoundLoader.load(note_list.C3.file_name())
            NOTE_NAME = '3C'
            sound.play()

        self.update_touch_label(ud['label'], NOTE_NAME, touch)

        self.add_widget(ud['label'])

        return True

    def on_touch_up(self, touch):
        if touch.grab_current is not self:
            touch.ungrab(self)
            ud = touch.ud
            self.canvas.remove_group(ud['group'])
            self.remove_widget(ud['label'])
            return True
        touch.ungrab(self)
        #ud = touch.ud
        #self.canvas.remove_group(ud['group'])
        #self.remove_widget(ud['label'])

    def update_touch_label(self, label, note_name, touch):
        label.text = 'Note:%s\nPos: (%d, %d)' % (note_name, touch.x, touch.y)
        label.texture_update()
        label.pos = touch.pos
        label.size = label.texture_size[0] + 20, label.texture_size[1] + 20

    def signal_handler(sig, frame):
        GPIO.cleanup()
        sys.exit(0)


class FretApp(App):
    def build(self):
        return FretBoard()

    def on_pause(self):
        return True


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    FretApp().run()
