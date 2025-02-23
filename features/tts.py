import pyttsx3

def text_to_speech(text):
    """Converts the given text to speech."""
    engine = pyttsx3.init()  # Initialize the TTS engine
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (default is ~200)
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
    
    engine.say(text)  # Speak the given text
    engine.runAndWait()  # Wait until speech is finished

if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")  # Get text input from the user
    text_to_speech(text)  # Call the TTS function
