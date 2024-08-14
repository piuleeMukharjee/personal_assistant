import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def greet():
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            speak("Good Morning !")
        elif hour>= 12 and hour<18:
            speak("Good Afternoon !")
        else:
            speak("Good Evening !")
        speak("I am your Personal Assistant, what can i do for you today.. ")
#RECOGNITION
    def VoiceCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("Recognizing...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query= r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
        return query


    if __name__ == '__main__':
        greet()
        while True:
            work = VoiceCommand().lower()
            if 'hello' in work:
                speak('hi , how can i help you')
            elif 'hii how are you' in work:
                speak('i am fine ,glad you me that')    

            if "wikipedia" in work:
                speak("Searching wikipedia...")
                work = work.replace("wikipedia", "")
                results = wikipedia.summary(work,sentences =5)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open notepad' in work:
                speak('opening notepad for you.......')
                path = ("c:\\windows\\system32\\notepad.exe")
                os.startfile(path)
            elif 'close notepad' in work:
                speak('closing notepad wait.....')
                os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')

            elif 'open youtube' in work:
                speak("Here you go to Youtube\n")
                webbrowser.open("https://www.youtube.com/")

            elif "who made you" in work or "who created you" in work: 
                speak("I have been created by piulee.") 

            elif "who i am" in work:
                speak("If you talk then definitely your human.")                

            elif 'open google' in work:
                speak("Here you go to Google\n")
                webbrowser.open("https://www.google.co.in/")

            elif 'play music' in work :
                speak('opening music player....')
                webbrowser.open("https://spotify.com")

            elif 'open mail' in work:
                speak("Here you go to mail\n")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'open whatsapp' in work:
                speak("opening whatsaap for you\n")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'open netflix' in work:
                speak("opening netflix for you \n")
                webbrowser.open("https://netflix.com/")

            elif 'open our presentation' in work:
                speak('opening your presentation for you.......')
                path = ("C:\\Users\\piulee\\OneDrive\\Desktop\\Project work of Disruptive Technology-1.pptx")
                os.startfile(path)  
            elif 'the time' in work:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")    
                speak(f"Sir, the time is {strTime}") 
    
            elif 'exit' in work:
                speak("Thanks for giving me your time ..... have a nice day....")
                exit()

except BaseException as ex:
    print(f"error occured = {ex}")

finally:
    print("Thank you,have a nice day")
