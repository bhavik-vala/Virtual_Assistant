import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>0 and hour <12:
        speak("Good Morning Sir")
    
    elif hour >=12 and hour <= 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")
    
    speak("My name is GoGO, Your personal Assistant. Memory 1 terabyte, processor 1 zeta hertz. How may i help you sir ?")

def takeCommand():
    '''
    it takes microphone input from the user and returns string as output
    '''
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening Sir....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f'User Said: {query}\n')

    except Exception as e:
        print(e)

        print('sorry, Say that again please...')
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com', 'emails password')
    server.sendmail('xyz@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia sir....')
            #query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        
        elif 'open twitter' in query:
            webbrowser.open('twitter.com')
        
        elif 'open prime' in query:
            webbrowser.open('primevideo.com')
        
        elif 'open stake' in query:
            webbrowser.open('stakeoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            currentTime = datetime.datetime.now().strftime("%H:%M%S")
            speak(f'sir, the time is {currentTime}')

        elif 'open code' in query:
            path = "C:\\Users\\bhavi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'open pycharm' in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\pycharm64.exe"
            os.startfile(path)
        
        elif 'open word' in query:
            path = "C:\\Program Files (x86)\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)

        elif 'open excel' in query:
            path = "C:\\Program Files (x86)\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path)

        elif 'open powerpoint' in query:
            path = "C:\\Program Files (x86)\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)
             
        elif 'send email to bhavik' in query:
            try:
                speak("what should i send sir?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent sir")

            except Exception as e:
                print(e)
                speak("Sorry sir, I could not sent an email at this moment")
