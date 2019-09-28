import pyttsx3                     
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import sys
import random
import wolframalpha
import pyjokes
from datetime import date
from googlesearch import search
from PyDictionary import PyDictionary

print("###########INSTRUCTIONS############")
print("#just speak what you want when the Assistant starts listening.")
print("#You can Use Specific Keywords for specific functions:-")
print("-------KEYWORDS--------|---------FUNCTION-------|")
print("1)    WIKIPEDIA        |         WIKIPEDIA      |")
print("2)     SEARCH          |       GOOGLE SEARCH    |")
print("3)     ALPHA           |      WOLFRAM SEARCH    |")
print("4)   TIME/DATE         |        TIME/DATE       |")
print("5) ACTIVATE DICTIONARY |     DICTIONARY MODE    |")
print("6)****I AM BORED*******|RANDOM programming JOKES|")
print("-----------------------|------------------------|")
print("**you can also open some common websites LIKE:")
print("->google; youtube; google_drive; facebook; instagram; twitter; Stack_Overflow; Git_Hub;")
print("->IITR MAIN WEBSITE ; CHANNEL I ;")
print("***YOU! CAN ALSO OPEN SOME COMMON APPS ON YOUR PC LIKE:")
print("@->CODE_BLOCKS  @->SPOTIFY  @->PLAY MUSIC")

client = wolframalpha.Client('TUXL5R-5WYA3T7LVP')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("how can I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 420
        r.pause_threshold = 0.7
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'search' in query:
            query=query.replace("search","")
            chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                 webbrowser.open("https://google.com/search?q=%s" % query)
        elif 'alpha' in query:
            query=query.replace("alpha","")
            try:
              res=client.query(query)
              output=next(res.results).text
              print(output)
              speak(output)
            except StopIteration:
              print('speak again')
            except :
              print("can't find this in library")
            
        elif 'open youtube' in query or 'open you tube' in query:
            webbrowser.get(chrome_path).open_new_tab("youtube.com")
        elif 'open google' in query:
            webbrowser.get(chrome_path).open_new_tab("google.com")
        elif 'open google drive' in query:
            webbrowser.get(chrome_path).open("drive.google.com")   
        elif 'open facebook' in query:
            webbrowser.get(chrome_path).open("www.facebook.com")
        elif 'open instagram' in query:
            webbrowser.get(chrome_path).open("www.instagram.com")
        elif 'activate dictionary' in query:
            dictionary=PyDictionary()
            print('you can say commands like:')
            speak('you can say commands like these,')
            print('what is the meaning of "..."')
            print('what is the synonym of "..."')
            print('what is the antonym of "..."')
            print('translate "YOURword" into "language"')
            speak('So, what do you want to ask')
            while True:
             if 'exit dictionary' in query:
                 break
             query=takeCommand();
             if 'meaning' in query:
                 query=query.replace("what is the meaning of ","")
                 print(dictionary.meaning(query))
                 speak(dictionary.meaning(query))
             elif 'synonym' in query:
                 query=query.replace(("what is the synonym of ",""))
                 speak(dictionary.synonym(query))
             elif 'antonym' in query:
                 query=query.replace("what is the antonym of ","")
                 speak(dictionary.antonym(query))
             elif 'translate' in query:
                 query=query.replace('translate ','')
                 query=query.replace(' into ','')
                 key=query.split();
                 word=key[0]
                 lang=key[1]
                 if 'hindi' in lang:
                    code='hi'
                 elif 'tamil' in lang:
                     code='ta'
                 elif 'japanese' in lang:
                     code='ja'
                 elif 'chinese' in lang:
                     code='zh'
                 elif 'telugu' in lang:
                     code='te'
                 elif 'marathi' in lang:
                     code='mr'
                 elif 'bengali' in lang:
                     code='bn'
                 elif 'russian' in lang:
                     code='ru'
                 else: 
                  speak('sorry, we cannot convert in this language')
                 speak('here you go')
                 print('translated word is: ')
                 print(dictionary.translate("word",'code'))
                    
        elif 'open main website' in query:
            webbrowser.get(chrome_path).open("www.iitr.ac.in")
        elif 'open channel i' in query:
            webbrowser.get(chrome_path).open("www.channeli.in")
        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            webbrowser.get(chrome_path).open_new_tab("stackoverflow.com")
        elif 'open github' in query or 'open git hub' in query:
            webbrowser.get(chrome_path).open("www.github.com")
        elif 'open twitter' in query:
            webbrowser.get(chrome_path).open("www.twitter.com")
        elif 'open learncpp' in query:
            webbrowser.get(chrome_path).open("www.learncpp.com")
        elif 'open movies' in query:
            webbrowser.get(chrome_path).open("yts.lt")
        elif 'open coursera' in query:
            webbrowser.get(chrome_path).open("www.coursera.org")
        elif 'open udemy' in query:
            webbrowser.get(chrome_path).open("www.udemy.com")
        elif 'open photoshop' in query:
            webbrowser.get(chrome_path).open("www.photoshop.com")
        elif 'open e library' in query:
            webbrowser.get(chrome_path).open("https://ndl.iitkgp.ac.in/")
        elif 'open photoshop' in query:
            webbrowser.get(chrome_path).open("www.photoshop.com")
        elif 'open geeksforgeeks' in query:
            webbrowser.get(chrome_path).open("https://www.geeksforgeeks.org/")
        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            y=random.randrange(0,50,1)
            print(songs[y])
            os.startfile(os.path.join(music_dir, songs[y]))
        elif 'open image' in query:
            try:  
              img  = Image.open('F:\\HONOR pics\\img.jpg')  
            except IOError: 
              pass
        elif 'open code blocks' in query:
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\CodeBlocks.exe"
            os.startfile(codePath)
        elif 'open codeblocks' in query:
             codePath = "C:\\Program Files (x86)\\CodeBlocks\\CodeBlocks.exe"
             os.startfile(codePath)
        elif'exit code blocks' in query or 'exit codeblocks' in query:
            os.system("taskkill /f /im codeblocks.exe")
        elif 'exit' in query:
            speak("good bye sir, have a nice day")
            sys.exit()
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print("The Time is : "+strTime)   
            speak(f"Sir, the time is {strTime}") 
        
        elif 'date' in query:                   
            print("Present date is : ",end="")   
            print(date.today())                  
            speak(date.today())
        elif'spotify' in query:
            os.startfile("C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe")
        elif 'exit spotify' in query:
            os.system("taskkill /f /im spotify.exe")
        elif 'i am bored' in query:
            speak('maybe this programmer joke could make you smile.')
            speak(pyjokes.get_joke())
        elif 'shut down' in query:
            os.system("shutdown /s /t 1")