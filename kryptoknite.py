import os
import sys
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser
import smtplib
import random

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('WXUQYQ-7A5665H6P4')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 2].id)


def talk(audio):
    print('KryptoKnite: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    CurrentHour = int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
        talk('Good Morning!')

    if CurrentHour >= 12 and CurrentHour < 18:
        talk('Good Afternoon!')

    if CurrentHour >= 18 and CurrentHour != 0:
        talk('Good Evening!')


greetMe()

talk('Hey Buddy, It\'s  your assistant KryptoKnite!')
talk('tell me about today?')


def GivenCommand():
    k = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        k.pause_threshold = 1
        audio = k.listen(source)
    try:
        query = k.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        talk('Sorry! I didn\'t get that! Try typing it here!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = GivenCommand()
        query = query.lower()

        if 'open google' in query:
            talk('sure')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            talk('sure')
            webbrowser.open('www.gmail.com')
            
        elif 'open youtube' in query:
            talk('sure')
            webbrowser.open('www.youtube.com')

        elif "what\'s up" in query or 'how are you' in query:
            setReplies = ['Just doing some stuff!', 'I am good!', 'Nice!', 'I am amazing and full of power']
            talk(random.choice(setReplies))
       
        elif "who are you" in query or 'where are you' in query or 'what are you' in query:
            setReplies = [' I am KryptoKnite', 'In your system', 'I am an example of AI']
            talk(random.choice(setReplies))

        elif 'email' in query:
            talk('Who is the recipient? ')
            recipient = GivenCommand()

            if 'me' in recipient:
                try:
                    talk('What should I say? ')
                    content = GivenCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    talk('Email sent!')

                except:
                    talk('Sorry ! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            talk('okay')
            talk('Bye, have a good day.')
            sys.exit()

        elif 'hello' in query:
            talk('hey')

        elif 'bye' in query:
            talk('Bye, have a great day.')
            sys.exit()

        elif 'play music' in query:
            music_folder = 'C:\\Users\\Public\\Music\\'
            music = ['friends']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            talk('Okay, here is your music! Enjoy!')

        elif 'show images' in query:
            images_folder = 'C:\\Users\\Public\\Pictures\\'
            images = ['kunal']
            random_images = images_folder + random.choice(images) + '.jpeg'
            os.system(random_images)

            talk('Okay, here are your images! Have Fun!')


        else:
            query = query
            talk('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    talk('Alpha says')
                    talk('Gotcha')
                    talk(results)

                except:
                    results = wikipedia.summary(query, sentences=3)
                    talk('Got it.')
                    talk('Wikipedia says')
                    talk(results)

            except:
                webbrowser.open('www.google.com')

        talk('Next Command! Please!')

