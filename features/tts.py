import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import pyttsx3
import speech_recognition as sr
from kivy.clock import Clock

kivy.require('2.1.0')  # Replace with your installed Kivy version

# Initialize TTS engine
engine = pyttsx3.init()

class SpeechToTextAndTextToSpeechApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Label to display recognized text
        self.text_label = Label(
            text="Start speaking...", 
            font_size=24, 
            size_hint_y=0.8, 
            halign="center", 
            valign="middle"
        )
        self.layout.add_widget(self.text_label)

        # Start the voice prompt and speech recognition
        self.start_speech_recognition()

        return self.layout

    def start_speech_recognition(self):
        """Function to start listening for speech input"""
        engine.say("Start speaking")
        engine.runAndWait()
        self.text_label.text = "Start speaking..."
        Clock.schedule_once(self.listen_speech, 1)  # Start listening after a slight delay

    def listen_speech(self, dt):
        """Function to listen to speech and convert it to text"""
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")

            # Adjust recognizer sensitivity to ambient noise
            recognizer.adjust_for_ambient_noise(source)

            try:
                # Listen for audio and recognize it
                audio = recognizer.listen(source, timeout=5)  # Set a timeout for listening
                print("Recognizing...")

                # Convert speech to text
                recognized_text = recognizer.recognize_google(audio)
                self.text_label.text = f"Recognized: {recognized_text}"

                # Read the recognized speech aloud
                engine.say(f"Recognized speech: {recognized_text}")
                engine.runAndWait()

                # Call this function again to keep listening
                Clock.schedule_once(self.listen_speech, 1)

            except sr.UnknownValueError:
                self.show_error("Sorry, I could not understand the speech.")
                Clock.schedule_once(self.listen_speech, 1)  # Try again
            except sr.RequestError as e:
                self.show_error(f"Could not request results; {e}")
                Clock.schedule_once(self.listen_speech, 1)  # Try again
            except sr.WaitTimeoutError:
                self.show_error("Listening timed out. Please try again.")
                Clock.schedule_once(self.listen_speech, 1)  # Try again

    def show_error(self, message):
        """Function to show error messages"""
        engine.say(message)
        engine.runAndWait()
        self.text_label.text = message

# Run the app
if __name__ == "__main__":
    SpeechToTextAndTextToSpeechApp().run()
 
