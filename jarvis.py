import pyttsx3 #FOR VOICE
import datetime #FOR TIME
import wikipedia #READING FROM WIKI
import webbrowser #ACCESSING WEB APP
import speech_recognition as sr
import smtplib #FOR MAIL
from googletrans import Translator
from pygame import mixer #FOR MUSIC
mixer.init()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',b'\x02en-gb')

#FUN FOR SPEAK
def speak_jarvis(audio):
    engine.say(audio)
    engine.runAndWait()

#FUN FOR WISHING USER GM GA GE
def Wishme():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak_jarvis("Good Morning")
    elif time>=12 and time<15:
        speak_jarvis("Good AfterNoon")
    else:
        speak_jarvis("Good Evening")
    speak_jarvis("I am Jarvis. How Can I Help You Sir")
    print("I am Jarvis. Big Fan. How Can I Help You Sir")

#TAKING VOICE INPUT FROM USER TO PERFORM FUNCTION
def get_task():
    speech=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        speech.pause_threshold=1
        audio=speech.listen(source)
    try:
        print("Recognizing.........")
        query=speech.recognize_google(audio,language='en-in')
        print("user Said",query)
    except Exception as e:
        speak_jarvis("Sorry I can't Understand. Please Try Again")
        print("Try Again")
        return "None"
    return query

#FUNCTION TO SEND EMAIL
def send_email(to,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Youremail.com','your_password')
    server.sendmail('Youremail.com',to,message)
    server.close()

 #MAIN FUNCTION
if __name__ == '__main__':
    Wishme()
    counter=0
    query = get_task().lower()
    if 'jarvis' in query:
        speak_jarvis("Yes Boss")
        while True:
                query=get_task().lower()
                if 'wikipedia' in query:
                    speak_jarvis("Searching in Wikipedia")
                    print("Seaching in Wikipedia.......")
                    query=query.replace("wikipedia","")
                    result=wikipedia.summary(query,sentences=2)
                    speak_jarvis("According to Wikipedia")
                    print(result)
                    speak_jarvis(result)
                elif 'play a song' in query:
                    counter += 1
                    mixer.music.load("/home/akshay/Desktop/Music/Koi Vi Nahi - (amlijatt.in).mp3")
                    mixer.music.play()
                elif 'youtube' in query:
                    speak_jarvis("Opening YouTube!")
                    webbrowser.open('http://youtube.com')
                elif 'google' in query:
                    speak_jarvis("Opening Google!")
                    webbrowser.open('http://google.co.kr')
                elif 'open stackoverflow' in query:
                    speak_jarvis("Opening StackOverflow!")
                    webbrowser.open('http://stackoverflow.com')
                elif 'open facebook' in query:
                    speak_jarvis("Opening FaceBook!")
                    webbrowser.open('http://facebook.com')
                elif 'open whatapp' in query:
                    speak_jarvis("Opening Whatapp!")
                    webbrowser.open('http://whatapp.com')
                elif 'time' in query:
                    speak_jarvis("Current Time is ")
                    time=datetime.datetime.now().strftime("%H:%M:%S")
                    speak_jarvis(time)
                    print(time)
                elif 'stop 'in query:
                    mixer.music.stop()
                elif 'thank ' in query:
                    speak_jarvis("Your Welcome. I am always available For You my Boss")
                elif 'email' in query:
                    try:
                        speak_jarvis("To whom You want to send Email")
                        name=get_task()
                        speak_jarvis("What Should I Say")
                        message=get_task()
                        to="receiveremail.com"
                        speak_jarvis("Sending Email to RecieverName ")
                        send_email(to,message)
                        speak_jarvis("Email Sent Successfully")
                    except Exception as e:
                        speak_jarvis("Sorry Brother Some Problem Occur While Sending Email")
                elif 'translate' in query:
                    speak_jarvis("Tell Me a Sentence to Translate")
                    sentence=get_task()
                    from_lang='en'
                    to_lang='hi'
                    speak_jarvis("Translating Please Wait")
                    translator=Translator()
                    try:
                        text_to_trans=translator.translate(sentence,src=from_lang,dest=to_lang)
                        hind_text=text_to_trans.text
                        speak_jarvis(hind_text)
                    except Exception as E:
                        speak_jarvis("problem")