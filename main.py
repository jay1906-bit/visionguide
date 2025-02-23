from kivy.app import App
from kivy.uix.label import Label

class VisionGuideApp(App):
    def build(self):
        return Label(text="Hello, VisionGuide!", font_size=24)

if __name__ == "__main__":
    VisionGuideApp().run()
