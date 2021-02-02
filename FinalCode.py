import threading
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
from functools import partial
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd


loop = True
window = tk.Tk()
window.geometry("800x545")
window.resizable(0,0)
musicPath = tk.StringVar()
cust_1_path = tk.StringVar()
cust_2_path = tk.StringVar()
cust_3_path = tk.StringVar()
window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=700, weight=1)

buttons = tk.Frame(window)
texts   = tk.Frame(window)
text = st.ScrolledText(texts, height = 18)
texts.grid(row=0, column=1, sticky="nsew")
text2 = st.ScrolledText(texts, width=87, height=15)
text2.grid(row=1, column=0, padx=0,pady=2)




 
wlcmNote ="""                    ############INSTRUCTIONS############
           just speak what you want when the Assistant starts listening.
              You can Use Specific Keywords for specific functions:-
              -------KEYWORDS--------|---------FUNCTION-------|
              1)    WIKIPEDIA        |         WIKIPEDIA      |
              2)      SEARCH         |       GOOGLE SEARCH    |
              3)     ALPHA           |      WOLFRAM SEARCH    |
              4)   TIME/DATE         |        TIME/DATE       |
              5) MEANING OF <WORD>   |        DICTIONARY      |
              6)*I AM BORED**|RANDOM programming JOKES        |
              7) OPEN <SOMETHING>    |OPEN VARIOUS SITES/APPS |
              8)    SHUT DOWN        |  SHUTS YOUR LAPPY DOWN |
              -----------------------|------------------------|
              **you can also open some common websites LIKE:
 google; youtube; google_drive; facebook; instagram; twitter; Stack_Overflow; Git_Hub;
           ***YOU! CAN ALSO OPEN SOME COMMON APPS ON YOUR PC LIKE:
                  CODE_BLOCKS  ||  SPOTIFY  ||   PLAY MUSIC
"""

client = wolframalpha.Client('TUXL5R-5WYA3T7LVP')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

with open("new.txt", "w") as f:                #this code's folder must contain a new.txt file
    f.write("1stc"+"\n"+"2ndc"+"\n"+"3rdc")
f.close()
def cust_Getpath(x):
    x.set(fd.askopenfilename())
    if x == cust_1_path:
        fin = open("new.txt", "rt")
        data = fin.read()
        data = data.replace('1stc', x.get())
        fin.close()
        fin = open("new.txt", "wt")
        fin.write(data)
        fin.close()

    elif x == cust_2_path:
        fin = open("new.txt", "rt")
        data = fin.read()
        data = data.replace('2ndc', x.get())
        fin.close()
        fin = open("new.txt", "wt")
        fin.write(data)
        fin.close()
    elif x == cust_3_path:
        fin = open("new.txt", "rt")
        data = fin.read()
        data = data.replace('3rdc', x.get())
        fin.close()
        fin = open("new.txt", "wt")
        fin.write(data)
        fin.close()
            
        



def browseMusic():
    global musicPath
    filename = fd.askdirectory()
    musicPath.set(filename)
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("how can I help you")


def takeCommand():
    global loop
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        if loop:
            text2.insert(tk.END, f"Listening...\n")
            r.energy_threshold = 400
            r.pause_threshold = 0.8
            r.pause_threshold = 1
            audio = r.listen(source)

    try:
        print("Recognizing...")
        if loop:
            text2.insert(tk.END, f"Recognizing...\n")
        if loop:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        if loop:
            text2.insert(tk.END, f"User said:\n {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
 
    return query


def mainloop():
    global loop
    while loop:
        query = takeCommand().lower()
       # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    
       # group of "open" keyword related programmes
        if 'what' in query:
            for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                try:
                    webbrowser.open("https://google.com/search?q=%s" % query)
                except webbrowser.Error:
                    print("unexpected error happened in webbrower")
                    text2.insert(tk.END, "unexpected error happened in webbrower\n")
        
        if 'open' in query:
            if 'open youtube' in query or 'open you tube' in query:
                webbrowser.open("youtube.com")
        
            elif 'open google scholar' in query:
                webbrowser.open("https://scholar.google.com/")
        
            elif 'open google' in query:
                webbrowser.open("google.com")
        
            elif 'open reddit' in query:
                webbrowser.open("reddit.com")
        
            elif 'open google drive' in query:
                webbrowser.open("drive.google.com")
        
            elif 'open facebook' in query:
                webbrowser.open("www.facebook.com")
        
            elif 'open instagram' in query:
                webbrowser.open("www.instagram.com")
        
            elif 'open geeksforgeeks' in query:
                webbrowser.open("https://www.geeksforgeeks.org")
        
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")
        
            elif 'open codechef' in query:
                webbrowser.open("www.codechef.com")
            elif 'open code chef' in query:
                webbrowser.open("www.codechef.com")
        
            elif 'open udemy' in query:
                webbrowser.open("www.udemy.com")
        
            elif 'open learncpp' in query:
                webbrowser.open("www.learncpp.com")
            elif 'open learn cpp' in query:
                webbrowser.open("www.learncpp.com")
        
            elif 'open main website' in query:
                webbrowser.open("www.iitr.ac.in")
        
            elif 'open channel i' in query:
                webbrowser.open("www.channeli.in")
        
            elif 'open github' in query or 'open git hub' in query:
                webbrowser.open("www.github.com")
        
            elif 'open twitter' in query:
                webbrowser.open("www.twitter.com")
        
            elif 'open movies' in query:
                webbrowser.open("yts.lt")
        
            elif 'open course' in query:
                webbrowser.open("www.coursera.org")
            elif 'open coursera' in query:
                webbrowser.open("www.coursera.org")
        
            elif 'open e library' in query:
                webbrowser.open("https://ndl.iitkgp.ac.in/")
        
            elif 'open photoshop' in query:
                webbrowser.open("www.photoshop.com")
        
            elif 'open glassdoor' in query:
                webbrowser.open("https://www.glassdoor.co.in/index.htm")
        
            elif 'open linkedin' in query:
                webbrowser.open("https://in.linkedin.com/")
        
            elif 'open ted talks' in query:
                webbrowser.open("https://www.ted.com/#/")
    
            elif 'open custom 1' in query:
                f=open('new.txt')                #this code's folder must contain a empty new.txt file
                lines=f.readlines()
                codePath = lines[0]
                prtln=''
                for letters in lines[0]:
                    if letters != '\n':
                        prtln += letters
                if codePath != '1stc\n':
                    text2.insert(tk.END, prtln +'\n')
                    os.startfile(prtln)
                else:
                    text2.insert(tk.END, "First Enter custom1 you idiot\n")
                f.close()
                
            elif 'open custom 2' in query:
                f=open('new.txt')             #this code's folder must contain a empty new.txt file
                lines=f.readlines()
                codePath = lines[1]
                prtln=''
                for letters in lines[1]:
                    if letters != '\n':
                        prtln += letters
                if codePath != '2ndc\n':
                    text2.insert(tk.END, prtln+'\n')
                    os.startfile(prtln)
                else:
                    text2.insert(tk.END, "First Enter custom2 you idiot\n")
                f.close()

            elif 'open custom 3' in query:
                f=open('new.txt')          #this code's folder must contain a empty new.txt file
                lines=f.readlines()
                codePath = lines[2]
                prtln=''
                for letters in lines[2]:
                    if letters != '\n':
                        prtln += letters
                if codePath != '3rdc' :
                    text2.insert(tk.END, prtln+'\n')
                    os.startfile(prtln)
                else:
                    text2.insert(tk.END, "First Enter custom3 you idiot\n")
                f.close()
        
        elif 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                if "in" in query:
                    query = query.replace("in", "")
                if "search" in query:
                    query = query.replace("search", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                text2.insert(tk.END, results+"\n")
                speak(results)
            except:
                print("sorry, could not find a result")
                text2.insert(tk.END, "sorry, could not find a result\n")
                speak("sorry, could not find a result")
        elif 'activate alpha' in query or 'wolfram alpha' in query or 'wolfram' in query:
        
            while True:
                print('do you want to ask oral question or a math expression?')
                text2.insert(tk.END,'do you want to ask oral question or a math expression?\n')
                speak('do you want to ask oral question or a math expression?')
                print('speak oral/mathematics/exit')
                text2.insert(tk.END, 'speak oral/mathematics/exit\n')
                inp = takeCommand()
                if 'oral' in inp:
                    speak("ask question")
                    print("ask question: ")
                    text2.insert(tk.END, "ask question: \n")
                    query = takeCommand()
                elif 'mathematics' in inp:
                    print('Please type the question: ')
                    text2.insert(tk.END, 'Please type the question: \n')
                    query = input()
                elif 'exit' in inp:
                    break
                try:
                    res = client.query(query)
                    output = next(res.results).text
                    print(output)
                    speak(output)
                except StopIteration:
                    print('speak again')
                    text2.insert(tk.END, 'speak again\n')
                except:
                    print("can't find this in library")
                    text2.insert(tk.END, "can't find this in library\n")
                inp = ''
                query = ''
        elif 'google search' in query:
            query = query.replace("google search", "")
            # you have to update this path for your machine for now
            # chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            for url in search(query, tld="co.in", num=1, stop=1, pause=2):
                try:
                    webbrowser.open("https://google.com/search?q=%s" % query)
                except webbrowser.Error:
                    print("unexpected error happened in webbrower")
                    text2.insert(tk.END, "unexpected error happened in webbrower\n")
        elif 'meaning of ' in query:
            query = query.replace("meaning of ", "")
            dictionary = PyDictionary()
            try:
                query = query.replace("what is the meaning of ", "")
                b = 'here is the meaning of the word'
                c = b+query
                speak(c)
                test_dict = dictionary.meaning(query)
                res = [value[i] for key, value in test_dict.items()
                       for i in range(1)]
                # shows most relevent meaning
                print(str(res[0]))
                text2.insert(tk.END, str(res[0])+"\n")
                speak(str(res[0]))
            except:
                print("sorry! word not found...")
                text2.insert(tk.END, "sorry! word not found...\n")
        
        elif 'play music' in query:
            music_dir = musicPath.get()
            songs = os.listdir(music_dir)
            y = random.randrange(0, 50, 1)
            print(songs[y])
            os.startfile(os.path.join(music_dir, songs[y]))
        
        elif'exit code blocks' in query or 'exit codeblocks' in query:
            os.system("taskkill /f /im codeblocks.exe")
        
        elif 'exit' in query:
            speak("good bye sir, have a nice day")
            loop = False
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The Time is : "+strTime)
            speak(f"Sir, the time is {strTime}")
        
        elif 'date' in query:
            print("Present date is : ", end="")
            print(date.today())
            speak(date.today())
        
        elif'spotify' in query:
            os.startfile(
                "C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe")
        
        elif 'exit spotify' in query:
            os.system("taskkill /f /im spotify.exe")
        
        elif'visual studio' in query:
            os.startfile(
                "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        elif'code' in query:
            os.startfile(
                "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        elif 'downloads' in query:
            os.startfile("C:\\Users\\hp\\Downloads")
        elif 'download' in query:
            os.startfile("C:\\Users\\hp\\Downloads")
        
        elif 'exit spotify' in query:
            os.system("taskkill /f /im spotify.exe")
        
        elif 'i am bored' in query:
            speak('maybe this programmer joke could make you smile.')
            speak(pyjokes.get_joke())
        
        elif 'shut down' in query:
            os.system("shutdown /s /t 1")
        elif 'shutdown' in query:
            print("Do you really want to ShutDown?[y/n]")
            response = input()
            if response == 'y':
                os.system("shutdown /s /t 1")

def kill(x):
    global loop 
    loop = False
    #if x.is_alive():
        #x.join()
    sys.exit()

    
if __name__ == "__main__":
    x = threading.Thread(target=mainloop)
    #wishMe()
    text.insert(tk.END, wlcmNote)
    button = tk.Button(buttons, text= "Start Query", command = x.start)
    button2 = tk.Button(buttons, text= "Kill Query", command = partial(kill, x))
    button3 = tk.Button(buttons, text= "music folder", command = browseMusic)
    button4 = tk.Button(buttons, text= "custom 1", command = partial(cust_Getpath, cust_1_path))
    button5 = tk.Button(buttons, text= "custom 2", command = partial(cust_Getpath, cust_2_path))
    button6 = tk.Button(buttons, text= "custom 3", command = partial(cust_Getpath, cust_3_path))

    button.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
    button2.grid(row = 1, column = 0, sticky = "ew", padx = 5, pady = 5)
    button3.grid(row = 2, column = 0, sticky = "ew", padx = 5, pady = 5)
    button4.grid(row = 3, column = 0, sticky = "ew", padx = 5, pady = 5)
    button5.grid(row = 4, column = 0, sticky = "ew", padx = 5, pady = 5)
    button6.grid(row = 5, column = 0, sticky = "ew", padx = 5, pady = 5)
    buttons.grid(row=0, column=0, sticky="ns")
    
    text.grid(row=0, column=0, sticky="ew", padx=0,pady=2)
    
    window.mainloop()
