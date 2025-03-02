import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import os
import platform
import time
import sys  # For exiting the program and closing the editor window

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Sorry, the service is down. Error: {e}")
            speak("Sorry, the service is busy. Please try again later.")
            return None

def open_browser():
    webbrowser.open('http://www.google.com')
    speak("Opening your browser.")

def open_cmd():
    if platform.system() == "Windows":
        subprocess.Popen("start cmd", shell=True)
    else:
        subprocess.Popen("gnome-terminal")  # Modify for your OS
    speak("Opening command prompt.")

def open_calculator():
    if platform.system() == "Windows":
        subprocess.Popen("calc")
    else:
        subprocess.Popen("gnome-calculator")  # Modify for your OS
    speak("Opening calculator.")

def open_whatsapp():
    webbrowser.open('https://web.whatsapp.com')
    speak("Opening WhatsApp.")

def open_file_manager():
    if platform.system() == "Windows":
        subprocess.Popen("explorer")
    else:
        subprocess.Popen("nautilus")  # Modify for your OS
    speak("Opening file manager.")

def open_notepad():
    if platform.system() == "Windows":
        subprocess.Popen("notepad")
    else:
        speak("Notepad is not available on this operating system.")

def open_word():
    if platform.system() == "Windows":
        subprocess.Popen("start winword", shell=True)
    else:
        speak("Microsoft Word is not available on this operating system.")

def open_excel():
    if platform.system() == "Windows":
        subprocess.Popen("start excel", shell=True)
    else:
        speak("Microsoft Excel is not available on this operating system.")

def open_powerpoint():
    if platform.system() == "Windows":
        subprocess.Popen("start powerpnt", shell=True)
    else:
        speak("Microsoft PowerPoint is not available on this operating system.")

def open_photos():
    if platform.system() == "Windows":
        subprocess.Popen("start ms-photos:", shell=True)
    else:
        speak("Photos application is not available on this operating system.")

def open_mail():
    if platform.system() == "Windows":
        subprocess.Popen("start outlook", shell=True)
    else:
        speak("Mail application is not available on this operating system.")

def open_settings():
    if platform.system() == "Windows":
        subprocess.Popen("start ms-settings:", shell=True)
    else:
        speak("Settings application is not available on this operating system.")

def search_in_browser(query):
    webbrowser.open(f"http://www.google.com/search?q={query}")
    speak(f"Searching for {query}.")

def close_editor():
    speak("Closing editor window.")
    # Close VS Code or any editor using sys.exit()
    sys.exit()  # This will close the script and the editor window where it's running

def main():
    speak("Hello! I am Jarvis, your virtual assistant.")

    while True:
        command = listen()

        if command is None:
            continue

        if "shiva" in command:
            speak("Welcome back, Shiva!")

        elif "open browser" in command:
            open_browser()

        elif "open command prompt" in command:
            open_cmd()

        elif "open calculator" in command:
            open_calculator()

        elif "open whatsapp" in command:
            open_whatsapp()

        elif "open file manager" in command:
            open_file_manager()

        elif "open notepad" in command:
            open_notepad()

        elif "open word" in command:
            open_word()

        elif "open excel" in command:
            open_excel()

        elif "open powerpoint" in command:
            open_powerpoint()

        elif "open photos" in command:
            open_photos()

        elif "open mail" in command:
            open_mail()

        elif "open settings" in command:
            open_settings()

        elif "search" in command:
            query = command.replace("search", "").strip()
            search_in_browser(query)

        elif "369" in command:
            speak("You can start speaking, and I will write it in Notepad.")
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio)
                    with open("speech_to_text.txt", "a") as f:  # Using "a" for appending
                        f.write(text + "\n")  # Writing speech-to-text in the file
                    speak("I have written your speech in Notepad.")
                except Exception as e:
                    speak("Sorry, I could not understand that.")
                    print(f"Error: {e}")

        elif "exit" in command or "shut up" in command:
            speak("Goodbye, Shiva!")
            close_editor()  # Close the editor window when saying "exit"

if __name__ == "__main__":
    main()
