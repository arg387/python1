import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak a response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen to the user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    return ""

# Main loop for the voice assistant
while True:
    command = listen().lower()

    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "goodbye" in command:
        speak("Goodbye!")
        break
    else:
        speak("I'm not sure how to respond to that.")

# Close the text-to-speech engine
engine.stop()
