import kivy
from kivy.app import App
from kivy.uix.button import Button
import pyttsx3

class VisionGuideApp(App):
    def build(self):
        btn = Button(text="Speak", on_press=self.speak_text)
        return btn

    def speak_text(self, instance):
        engine = pyttsx3.init()
        engine.say("Hello, welcome to Vision Guide!")
        engine.runAndWait()

if __name__ == "__main__":
    VisionGuideApp().run()

