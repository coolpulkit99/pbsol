import PriaidDiagnosisClient
import config
import re
import speech_to_text
import tts2 as text_to_speech
import translate
import time
import pygame
language2="en-US"
#def oversmartjarvis(language2):
#if(1):
    #'''initialise config parameters'''
def oversmartdoctor(language2):

    username = config.username
    password = config.password
    authUrl = config.priaid_authservice_url
    healthUrl = config.priaid_healthservice_url
    language = config.language
    apicall = PriaidDiagnosisClient.DiagnosisClient(username, password, authUrl, language, healthUrl)

    #'''initialize paramenters'''
    ldel=''
    #apicall=PriaidDiagnosisClient.DiagnosisClient()
    l=(apicall.loadSymptoms())
    symplist=[]
    #print(apicall.loadIssues())
    gender=PriaidDiagnosisClient.Gender.Male
    year=1999
    #query=input("Enter your gender:")

    #'''Prompt user for gender'''

    #ldel=text_to_speech.speak("Tell me your gender",ldel)
    if(language2=="en-US"):
        ldel=text_to_speech.speak("Tell me your gender",ldel)
    elif(language2=="hi-IN"):
        ldel=text_to_speech.speakhindi(translate.translate_hindi("Tell me your gender"),ldel)
    time.sleep(3)
    print("speak now")
    
    query=speech_to_text.main(language2)
    if(language2=="hi-IN"):
        query=translate.translate(query)
    if(re.search(r'\b(jarvis)\b', query, re.I)):
        if(re.search(r'\b(male|boy|man|gentleman)\b', query, re.I)):
            gender=PriaidDiagnosisClient.Gender.Male
        if(re.search(r'\b(woman|girl|female|lady)\b', query, re.I)):
            gender=PriaidDiagnosisClient.Gender.Female

    #'''Prompt user for year of birth'''

    #query=input("Enter your year of birth:")
    #ldel=text_to_speech.speak("Tell me when you were born",ldel)
    if(language2=="en-US"):
        ldel=text_to_speech.speak("Tell me when you were born",ldel)
    elif(language2=="hi-IN"):
        ldel=text_to_speech.speakhindi(translate.translate_hindi("Tell me when you were born"),ldel)
    
    time.sleep(4)
    print("speak now")
    query=speech_to_text.main(language2)
    if(language2=="hi-IN"):
        query=translate.translate(query)
    if(re.search(r'\b(jarvis)\b', query, re.I)):
        year=int(query.strip().split(" ")[1])

        
    counter=0


#'''Prompt user for symptoms'''
    while(1):
        counter=counter+1
        if counter<2:
            if(language2=="en-US"):
                ldel=text_to_speech.speak("Tell me any symptoms you are having",ldel)
            elif(language2=="hi-IN"):
                ldel=text_to_speech.speakhindi(translate.translate_hindi("Tell me any symptoms you are having"),ldel)
        #query=input("Enter the symptom:")
        else:
            if(language2=="en-US"):
                ldel=text_to_speech.speak("Tell me any other symptoms you are having",ldel)
            elif(language2=="hi-IN"):
                ldel=text_to_speech.speakhindi(translate.translate_hindi("Tell me any othersymptoms you are having"),ldel)
                #ldel=text_to_speech.speak("Tell me any other symptoms you are having",ldel)
        time.sleep(4)
        
        print("speak now")
    
        query=speech_to_text.main(language2)
        if(language2=="hi-IN"):
            query=translate.translate(query)
        if(re.search(r'\b(jarvis)\b', query, re.I)):
            if(re.search(r'\b(no|none|bye|that is it|is it)\b', query, re.I)):
                   break
        else:
            continue
        strlis=(query).split()
        probid2=[]
        for j in strlis:
           for i in l:
               #liss=re.split("&|,",i["Name"].lower())
               #liss=list(map(str.strip,liss))
               patt=r'\b('+re.escape(j)+r')'
               if(re.search(patt, i["Name"], re.I)):
                   probid2.append(i)
                   print(i,j,probid2)
        print(probid2)
        if(len(probid2)>0):
            symplist.append(probid2[0])
    idlist=[]
    for i in symplist:
        idlist.append(i["ID"])
        
#'''draw conclusion based on collected symptoms'''
    finalres=apicall.loadDiagnosis(idlist,gender,year)[0]
    issuex=apicall.loadIssueInfo(finalres["Issue"]["ID"])
    if(language2=="en-US"):
        ldel=text_to_speech.speak(str("You might have "+str(issuex["Name"])+str(issuex["DescriptionShort"])+str(issuex["TreatmentDescription"])),ldel)
    elif(language2=="hi-IN"):
        ldel=text_to_speech.speakhindi(translate.translate_hindi("You might have "+str(issuex["Name"])+str(issuex["DescriptionShort"])+str(issuex["TreatmentDescription"])),ldel)
    #a = pygame.mixer.Sound(ldel)
    #print("length",a.get_length())

    time.sleep(10)
    print(finalres)
