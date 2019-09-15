#system
import os
import subprocess
import re

#date and time
import time
import datetime
from datetime import date

#utilitize
import playsound
import speech_recognition as sr
from gtts import gTTS
import random
#web
import webbrowser

def speak(text):
    print(f'Momo: {text}\n')
    tts = gTTS(text=text, lang="en")
    filename = ("voice.mp3")
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#listen for commands

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print(f"\nYou said: {command}")

#loop back to continue to listen for commands
        except sr.UnknownValueError:
            print('....')
            command = myCommand()
        return command

#if statements for commands
def functions():
    text = myCommand()
#Interaction
    #hello
    if 'hello' in text:
        random_list = []
        random_list.append(random.randint(1, 4))
        num = random_list[0]
        if num == 1:
            speak("Hello there.")
        elif num == 2:
            speak("Hi!")
        elif num == 3:
            speak('Whatsup!')
        elif num == 4:
            speak('Nice to meet you')
        random_list.clear()
    if 'hi' in text:
        random_list = []
        random_list.append(random.randint(1, 4))
        num = random_list[0]
        if num == 1:
            speak("Hello there.")
        elif num == 2:
            speak("Hi!")
        elif num == 3:
            speak('Whatsup!')
        elif num == 4:
            speak('Nice to meet you')
        random_list.clear()

    #how are you?
    elif "how are you" in text:
        random_list = []
        random_list.append(random.randint(1, 4))
        num = random_list[0]
        if num == 1:
            speak("I'm fine. How about you?")
        elif num == 2:
            speak("I'm fine. Thanks for asking")
        elif num == 3:
            speak("I'm doing fine")
        elif num == 4:
            speak("I'm well. How about you?")
        random_list.clear()

    #Im fine
    elif "fine" in text:
        random_list = []
        random_list.append(random.randint(1, 3))
        num = random_list[0]
        if num == 1:
            speak("Glad to know!")
        elif num == 2:
            speak("Alright then")
        elif num == 3:
            speak("Good to know!")
        random_list.clear()
    elif "alright" in text:
        random_list = []
        random_list.append(random.randint(1, 3))
        num = random_list[0]
        if num == 1:
            speak("Glad to know!")
        elif num == 2:
            speak("Alright then")
        elif num == 3:
            speak("Good to know!")
        random_list.clear()

    #what is your name
    elif "your name" in text:
        random_list = []
        random_list.append(random.randint(1, 3))
        num = random_list[0]
        if num == 1:
            speak("My name is Momo")
        elif num == 2:
            speak("You can call me Momo")
        elif num == 3:
            speak("I am Momo")
        random_list.clear()
    elif "who are you" in text:
        random_list = []
        random_list.append(random.randint(1, 3))
        num = random_list[0]
        if num == 1:
            speak("My name is Momo")
        elif num == 2:
            speak("You can call me Momo")
        elif num == 3:
            speak("I am Momo")
        random_list.clear()

# Jokes
    # tell me a joke
    elif "joke" in text:
        random_list = []
        random_list.append(random.randint(1, 7))
        num = random_list[0]
        if num == 1:
            speak("Why should you sit in a corner when you get cold?")
            time.sleep(1)
            speak("Because most corners are 90 degrees")
        elif num == 2:
            speak("I asked my French friend if she likes to play video games. She said, Wii.")
        elif num == 3:
            speak(
                "I was going to make myself a belt made out of watches, but then I realized it would be a waist of time.")
        elif num == 4:
            speak("What do you call a bee that can’t make up its mind? A Maybe")
        elif num == 5:
            speak("What do you call a pig that does karate?")
            time.sleep(1)
            speak("Pork Chop")
        elif num == 6:
            speak("What do you call a crocodile investigator")
            time.sleep(1)
            speak("An Alligator")
        elif num == 7:
            speak("The past, the present, and the future walk into a bar")
            time.sleep(1)
            speak("It was tense")
        random_list.clear()

    elif "knock knock joke" in text:
        speak("knock knock")
        time.sleep(1)
        speak("Tank")
        time.sleep(1)
        speak("You're Welcome")

#Web Browser
    #Open YouTube
    elif 'youtube' in text:
        speak("Opening YouTube")
        webbrowser.open('https://www.youtube.com')

    elif "videos on" in text:
        reg_ex = re.search("videos on (.*)", text)
        if reg_ex:
            topic = reg_ex.group(1)
            speak(f"Looking up video about {topic} on YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={topic}")

    #Open Google
    elif 'open google' in text:
        speak("Opening Google")
        webbrowser.open('https://www.google.com')
    elif "close google chrome" in text:
        speak("Closing Google Chrome")
        os.system("TASKKILL /F /IM chrome.exe")


    elif 'open' in text:
        reg_ex = re.search('open (.+)', text)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = ('https://www.' + domain)
            speak(f"Opening {domain}")
            webbrowser.open(url)
        else:
            pass

    #location
    elif "where is" in text:
        reg_ex = re.search("where is (.*)", text)
        if reg_ex:
            location = reg_ex.group(1)
            speak(f"This is the location of {location}")
            webbrowser.open(f"https://www.google.com/maps/place/{location}")

    #news
    elif "news" in text:
        speak("This is the news by straitstimes")
        webbrowser.open("https://www.straitstimes.com/")

#Applications
    elif 'launch' in text:
        reg_ex = re.search("launch (.*)", text)
        if reg_ex:
            app = reg_ex.group(1).title()
            paths = []
            try:
                for (root, dir, files) in os.walk("c:\\"):
                    for file in files:
                        if file == app + '.lnk':
                            app_paths = (os.path.join(root, file))
                            paths.append(app_paths)
                speak(f"Launching {app}")
                os.startfile(paths[0])
            except IndexError:
                speak(f"Could not find {app}")

    elif "close" in text:
        reg_ex = re.search("close (.*)", text)
        if reg_ex:
            close_app = reg_ex.group(1).title()
            speak(f"Closing {close_app}")
            os.system(f"TASKKILL /F /IM {close_app}.exe")

    #time
    elif "time" in text:
        now = datetime.datetime.now()
        speak('The time now is %d hours %d minutes' % (now.hour, now.minute))

    #date
    elif "date" in text:
        today = date.today()
        months = ['blank', 'January', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month = months[today.month]
        speak(f"The date is {today.day} {month} {today.year}")

    #day of the week
    elif 'day' in text:
        x = date.today()
        day = x.strftime('%A')
        speak(f"Today is {day}")

    #wikipedia
    elif "what is" in text:
        reg_ex = re.search("what is (.*)", text)
        if reg_ex:
            topic = reg_ex.group(1)
            webbrowser.open(f"https://en.wikipedia.org/wiki/{topic}")
            speak(f"This is what I have found about {topic}")
    elif "tell me about" in text:
        reg_ex = re.search("tell me about (.*)", text)
        if reg_ex:
            topic = reg_ex.group(1)
            webbrowser.open(f"https://en.wikipedia.org/wiki/{topic}")
            speak(f"This is what I have found about {topic}")
    elif "search for" in text:
        reg_ex = re.search("search for (.*)", text)
        if reg_ex:
            topic = reg_ex.group(1)
            webbrowser.open(f"https://en.wikipedia.org/wiki/{topic}")
            speak(f"This is what I have found about {topic}")


    elif "game" in text:
        speak("Let's play Rock Paper Scissors!")
        play_game()

    #stop
    elif "goodbye" in text:
        speak("Goodbye!")
        exit()
    elif "stop" in text:
        speak("Goodbye!")
        exit()
    elif "shut down" in text:
        speak("Shutting down.")
        exit()

    elif "list commands" in text:
        speak("This is the list of commands")
        print("___________________________________________________")
        print("List of Commands")
        print("___________________________________________________")
        print("Hello")
        print("Open (any website)")
        print("What is/Search for/Tell me about (anything)")
        print("Time/Day/Date")
        print("joke")
        print("game")
        print("Where is (any location)")
        print("Goodbye/Shutdown/Bye")
        print("___________________________________________________\n")

print("How may I assist you?")
while True:
    functions()
