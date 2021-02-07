#Description : This is a virtual assistant program that gets the date,current time, responds back with
#     a random greeting and returns information on a person.

#install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia

# import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignore any warning messages
warnings.filterwarnings('ignore')

#record audio and return it as a string
def recordAudio():
    #Record audio
    r=sr.Recognizer() #Creating recognizer object

    #Open the microphone and start recording
    with sr.Microphone() as source:
        print("Say something:")
        audio=r.listen(source)

    #use Google speech recognition
    data =''
    try:
        data=r.recognize_google(audio)
        print("you said: "+ data)
    except sr.UnknownValueError: #check for unknown error
        print("Google Speech Recognition could not understand the audio,unknown errro")
    except sr.RequestError as e:
        print("Request results from Google Speech Recognition Service Error" + e)

    return data

#function to get the virtual assistant response
def assistantResponse(text):

    print(text)

    #convert the text to speech
    myobj = gTTS(text= text, lang='en',slow=False)

    #Save the converted audio
    myobj.save('assistant_response.mp3')

    #Play the converted file
    os.system('start assistant_response.mp3')

# text=("Hello Annita! Boris Borisov likes you very much and he wants you to be his girlfriend")
# assistantResponse(text)

    

# A function for wake words
def wakeword(text):
    WAKE_WORDS=['hey computer', 'okay computer'] # A list of wake words

    text=text.lower() #Converting the text to all lower case words

    #Check to see whether user commands contains a wake wors
    for  phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #If the wake word is not found in the text
    return False


# function to get the current date
def getDate():
    now = datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()] #e.g. Monday
    monthNum =now.month
    dayNum=now.day

    # A list of months
    month_names=['January', 'February', 'March','April', 'May','June','July',
                 'August', 'September','October', 'November', 'December']

    # A list of ordinal numbers
    ordinal_numbers=['1st','2nd','3rd','4rd','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th',
                     '25th','26th','27th','28th','29th','30th','31st']


    return 'Today is '+weekday+" "+month_names[monthNum-1]+' the '+ordinal_numbers[dayNum-1]

#print(getDate())

# A function to return random greeting response

def greeting(text):

    #Greetings inputs
    GREETING_INPUTS=['hey','hola', 'zdrasti','hi','wassup']

    #greeting responses
    GREETING_RESPONSES=['howdy', 'whats good','hello', 'I am okay']

    #if the user inpur a greeting then we return a random response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

    #If no greeting was detected then return an empty string
    return ''

# A FUNCTION TO GET A PERSON THE FIRST AND THE LAST NAME OF A TEXT
def getPerson(text):
    wordList=text.split()

    for i in range(0,len(wordList)):
        if i + 3<=len(wordList)-1 and wordList[i].lower()=='who' and wordList[i+1]=='is':
            return wordList[i+2]+' '+ wordList[i+3]

while True:
    #Record the audio
    text=recordAudio()
    response= ''

    #check for the wake word
    if(wakeword(text)==True):

    #check for the greetings
        response=response+greeting(text)

    #check to see if the user said anything having to do with a test
    if('date' in text):
        get_date=getDate()
        response=response+' '+ get_date
    #check whether the user said anything about the time
    if('time' in text):
        now=datetime.datetime.now()
        meridiem=''
        if now.hour>12:
            meridiem='p.m.'
            hour=now.hour-12
        else:
            meridiem='a.m'
            hour=now.hour
        #convert minute into a proper string
        if now.minute<10:
            minute='0'+str(now.minute)
        else:
            minute=str(now.minute)
        response=response+' '+ "It is "+str(hour)+":"+minute+" "+meridiem+'. and '



    #check to see if the user said who is
    if ('who is' in text):
        person = getPerson(text)
        wiki = wikipedia.summary(person, sentences=2)
        response = response+' ' + wiki

    #Have the assistant respond back using audio
    assistantResponse(response)











