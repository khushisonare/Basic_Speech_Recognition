import speech_recognition as sr
import pyttsx3
import datetime
import pytz
import webbrowser
import sys

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice rate (optional)
engine.setProperty('rate', 150)

# Set IST time zone
ist = pytz.timezone('Asia/Kolkata')

def speak(text):
    print("🤖 Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("🧠 Recognizing...")
            command = recognizer.recognize_google(audio)
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Could not connect to the recognition service.")
        return ""

def respond(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "time" in command:
        now = datetime.datetime.now(ist).strftime("%H:%M:%S")
        speak(f"The current time is {now}")
    elif "browser" in command or "open browser" in command:
        speak("Opening Google in your browser.")
        webbrowser.open("https://www.google.com")
    elif "exit" in command:
        speak("Goodbye!")
        sys.exit()
    else:
        speak("Sorry, I don't recognize that command.")

# 🔁 Main loop
if __name__ == "__main__":
    speak("Voice assistant started. Say something!")
    while True:
        command = listen()
        if command:
            respond(command)
