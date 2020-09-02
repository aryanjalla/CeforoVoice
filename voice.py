#importing all the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import wikipedia
import datetime
import random
import playsound
import requests

#not getting any warnings
warnings.filterwarnings('ignore')

#recording the audio from the user
def record():
    rec = sr.Recognizer() #creating a recognising object named rec
    #swtiching on the mic and start recording
    with sr.Microphone() as source:
        print ("Say something to me!")
        audio = rec.listen(source)
    #using the googles speech recognisition
    data = ''
    audiodata = rec.recognize_google(audio)
    print ("I heard : " + audiodata)
    return audiodata

#to get the laptop to speak
def speak(text):
    print(text)
    #convert text to speech
    voicespeak = gTTS(text= text, lang='en', slow=False)
    #save the audio as a file
    voicespeak.save('responsejk.mp3')
    #playsound.playsound('responsejk.mp3')
    os.system('start responsejk.mp3')
    #OR
    #os.remove('responsejk.mp3')

#to have a wake sentence
def wake(text):
    wakwords = ['hey bro', 'okay computer', 'hi computer', 'hi bro', 'hi there']
    text = text.lower() # to convert the text into lower text
    #to check if we said the wake word
    for phrase in wakwords:
        if phrase in text:
            return True
#if wake word is not found
    return False

#give us the current date
def givedate():
    now = datetime.datetime.now()
    datenow = datetime.datetime.today()
    weekday = calendar.day_name[datenow.weekday()]
    monthno = now.month
    dayno = now.day
    monthname = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
     'September', 'October', 'November', 'December']
    numvers = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th',
     '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
     '24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is ' +weekday+ '  ' + monthname[monthno-1] + ' the ' + numvers[dayno-1]

#to return a response
def greet(text):
    #the inputs that can be given by the user
    greets = ['hi', 'hey', 'hola', "what's up", 'yo','hi computer', 'hello', 'computer','who is','what', 'computer']
    #the outputs that can be given by the computer
    greetresponse =  ['howdy', 'whats up my boy', 'hello master', 'hey there','whats up dude']

    #if the user greets the voice
    for word in text.split():
        if word.lower() in greets:
            return random.choice(greetresponse) + '.'

    #if the user does not greet the voicespeak
    return ''

#a function to google search people
def person(text):
    wordlist = text.split() #splitting the words into  a list of words

    for i in range(0, len(wordlist)):
        if i+3 <= len(wordlist) - 1 and wordlist[i].lower() == 'who' and wordlist[i+1].lower() == 'is':
            return wordlist[i+2] + ' '+ wordlist[i+3]

def obj1(text):
    wordw = text.split() #splitting the words into  a list of words

    for i in range(0, len(wordw)):
        if wordw[i].lower() == 'is' and wordw[i].lower() == 'the':
            return ''
        if i+2 <= len(wordw) - 1 and wordw[i].lower() == 'what':
            return wordw[i+2]


while True:
#voicebolo = gTTS(text= "Ask me", lang='en', slow=False)
    #save the audio as a file
#    voicebolo.save('res.mp3')
#    os.system('start res.mp3')
    text=record()
    response=''
    if(wake(text)==True):
        response = response+' '+greet(text)

    if('date' in text):
        getdates = givedate()
        response = response +' '+getdates

    if('who is' in text):
        persona = person(text)
        wikis = wikipedia.summary(persona,  sentences=2)
        response =response+' '+wikis

    if('what is' in text):
        whats = obj1(text)
        andugondu = wikipedia.summary(whats,  sentences=2)
        response =response+' '+andugondu

    speak(response)
