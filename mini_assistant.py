import speech_recognition as sr
import os
import webbrowser as wb
import subprocess as sb
from googlesearch import search

def mini_assist(audio):
    
    if 'youtube' in audio.lower():
        url = 'https://www.youtube.com/'   # Adding URL of the website.
        print('Opening youtube....')
        wb.get().open_new_tab(url)
        
    elif 'gmail' in audio.lower():
        url = 'https://mail.google.com/'
        print('Opening gmail....')
        wb.get().open_new_tab(url)
        
    elif 'notepad' in audio.lower():
        path = 'notepad'
        print('Opening notepad....')
        os.system(path)
        
    elif 'calculator' in audio.lower():
        path = 'calc'
        print('Opening calculator....')
        os.system(path)
        
    elif 'wordpad' in audio.lower():
        path = 'write'
        print('Opening wordpad....')
        os.system(path)
        
    elif 'vlc' in audio.lower():
        path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe" # Adding destination of the Programme.
        print('Opening VLC Player....')
        sb.call(path)
        
    elif 'search' in audio.lower():
        r1 = sr.Recognizer()
        with sr.Microphone() as source:
            print('Search?? ')
            audio = r1.listen(source)            
            get = r1.recognize_google(audio)
            print('Google Searching....', get)
            for j in search(get, tld='co.in', lang='en', num=1, start = 0, stop=1, pause=2):
                wb.get().open_new_tab(j)
    
    elif 'facebook' in audio.lower():
        url = 'https://www.facebook.com/'
        print('Opening Facebook...')
        wb.get().open_new_tab(url)
    
    elif 'google' in audio.lower():
        url = 'https://www.google.co.in/'
        print('Opening Google...')
        wb.get().open_new_tab(url)
        
    elif 'linkedin' in audio.lower():
        path = "C:\\Users\\Pushpinder\\Desktop\\LinkedIn.lnk"
        print('Opening LinkedIn....')
        sb.call(path, shell = True)
        
    elif 'twitter' in audio.lower():
        url = 'https://twitter.com/'
        print('Opening Twitter...')
        wb.get().open_new_tab(url)
        
    elif 'reddit' in audio.lower():
        url = 'https://www.reddit.com/'
        print('Opening Reddit...')
        wb.get().open_new_tab(url)
        
    elif 'yahoo' in audio.lower():
        url = 'https://in.yahoo.com/'
        print('Opening Yahoo...')
        wb.get().open_new_tab(url)
        
    elif 'msn' in audio.lower():
        url = 'https://www.msn.com/'
        print('Opening MSN...')
        wb.get().open_new_tab(url)
        
    elif 'bing' in audio.lower():
        url = 'https://www.bing.com/'
        print('Opening Bing...')
        wb.get().open_new_tab(url)
        
    elif 'duckduckgo' in audio.lower():
        url = 'https://duckduckgo.com/'
        print('Opening Duck Duck Go...')
        wb.get().open_new_tab(url)
        

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Please say something...\n')
    pre_audio = r.listen(source)
    try:
        audio = r.recognize_google(pre_audio)
        print('>> ', audio)
        mini_assist(audio)
    except sr.UnknownValueError:
        print('Not Searched')
    except sr.RequestError as e:
        print('Failed'.format(e))
    
    