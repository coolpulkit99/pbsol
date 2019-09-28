import random
import re
import os
import speech_to_text
import tts2 as text_to_speech
import webbrowser
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import youtubesearch as ytplay
import translate
import symptomspecificdiagnosis
l=''
language='en-US'
while(1):
    query=speech_to_text.main(language)
    if(language=="hi-IN"):
        query=translate.translate(query)
    query=query.lower()
    #query=input("Enter:")
    print(query)
    if re.search(r'\b(jarv|jarvis|jar)\b',query, re.I):
        if re.search(r'\b(up|awake)\b',query, re.I):
            l=text_to_speech.speak("For you sir,always",l)
            print("For you sir! always!")
        if re.search(r'\b(where is)\b',query, re.I):
            #data=query
            #data = data[re.search(r'\b(where is)\b',query, re.I).span()[1]:]#.split(" ")
            data=query[re.search(r'\b(where is)\b',query, re.I).span()[1]:].strip()
            location = data[2]
            location=data
            l=text_to_speech.speak("Hold on Apoorv, I will show you where " + location + " is.",l)
            webbrowser.open("https://www.google.nl/maps/place/" + location )#+ "/&amp;")
        if re.search(r'\b(play)\b',query, re.I):
            if re.search(r'\b(youtube)\b',query, re.I):
                newquer=query.split(" ")
                valxxxx1=newquer.index("play")
                valxxxy1=newquer.index("youtube")
                searchquer=""
                for i in range(valxxxx1+1,valxxxy1-1):
                    searchquer=searchquer+" "+newquer[i]
                searchquer.strip()
                l=text_to_speech.speak("Opening youtube",l)
                ytplay.playyt(searchquer)
            elif re.search(r'\b(my queue|some music|a song|a beat)\b',query, re.I):
                urls="https://www.youtube.com/watch?v=29a6o5vRKVM&list=RDmt1mXwBLsSE&index=2"
                webbrowser.open(urls)
            else:
                newquer=query.split(" ")
                valxxxx1=newquer.index("play")
                searchquer=""
                for i in range(valxxxx1+1,len(newquer)):
                    searchquer=searchquer+" "+newquer[i]
                searchquer.strip()
                l=text_to_speech.speak("Playing on youtube",l)
                ytplay.playyt(searchquer)
        if re.search(r'\b(queue some music|queue music|drop the music|drop the beat|drop a beat)\b',query, re.I):
                urls="https://www.youtube.com/watch?v=29a6o5vRKVM&list=RDmt1mXwBLsSE&index=2"
                webbrowser.open(urls)
            
                
        if re.search(r'\b(repeat this|repeat after me)\b',query, re.I):
            mystrss=query.split()
            if re.search(r'\b(repeat after me)\b',query, re.I):
                indx1=mystrss.index("me")
            if re.search(r'\b(repeat this)\b',query, re.I):
                indx1=mystrss.index("this")
            strnewxxy=""
            for i in range(indx1,len(mystrss)):
                strnewxxy=strnewxxy+" "+mystrss[i]
            l=text_to_speech.speak(strnewxxy,l)
            
            
        if re.search(r'\b(meaning|mean)\b',query, re.I):
            if("meaning" in query):
                valxx1=query.split("of")
                word=valxx1[1].strip()
                print("-"+str(word)+"-")
            elif("mean" in query):
                valxx1=query.split(" ")
                xxxx1=valxx1.index("does")+1
                yyyy1=valxx1.index("mean")-1
                if(xxxx1==yyyy1):
                    word=valxx1[xxxx1]
                else:
                    l=text_to_speech.speak("Sorry try again",l)
                    continue
                
                
            try:
                my_url = "https://www.dictionary.com/browse/%s?s=t" %(word)
                uClient = uReq(my_url)
                page_html = uClient.read()
                uClient.close()
                page_soup = soup(page_html, "html.parser")
                container = page_soup.findAll("div",{"class":"css-1o58fj8 e1hk9ate4"})
                container = container[0]
                meanings = container.text.split(".")
                speakthis11="It means "
                if(len(meanings)>1):
                    for i in range(0,len(meanings)-1):
                        speakthis11=speakthis11+meanings[i]+" or, it might also mean "
                    speakthis11=speakthis11+meanings[len(meanings)-1]
                else:
                    speakthis11=speakthis11+meanings[0]
                l=text_to_speech.speak(speakthis11,l)
            except:
                l=text_to_speech.speak("Sorry I dont know the meaning of this",l)
                continue
        if re.search(r'\b(doctor|medicines)\b',query, re.I):
            #nakx=["Yes sir,Can i recommend some medicines?","Indeed sir, how can i help you?"]
            #l=text_to_speech.speak(nakx[random.randint(0,1)],l)
            l=text_to_speech.speak("Starting Oversmart Doctor",l)
            symptomspecificdiagnosis.oversmartdoctor(language)
            
        if re.search(r'\b(do you speak hindi|talk in hindi|in hindi)\b',query, re.I):
            language='hi-IN'
            l=text_to_speech.speak("Language Changed to hindi",l)
            
            

            
                
            

