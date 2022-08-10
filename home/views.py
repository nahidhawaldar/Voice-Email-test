from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr
import pyttsx3
import imaplib,email
from gtts import gTTS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.http import JsonResponse
import re
from .models import Details
# Create your views here.

email_address = ''
email_password = ''
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
imap_url = 'imap.gmail.com'
conn = imaplib.IMAP4_SSL(imap_url)
# this speaks the text sent as a parameter
def talk(text):
    engine = pyttsx3.init()  # text to speech initialized.Engine speaks the text out
    engine.say(text)
    engine.runAndWait()

# Speak Function Not Working Properly
def listen():
    print('INSIDE listen FNCTION')
    listener = sr.Recognizer()  # to understand what the user is saying.
    try:
        with sr.Microphone() as source:  # laptop's mic is the source for speech.
            print('Listening...')
            talk('Now Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)  # speech to text function
            print(info, '\n')
            return info
    except:
        pass

def login_view(request):
    global email_address, email_password

    if request.method == 'POST':
        text1 = "Welcome to our Voice Based Email. Login with your email account in order to continue. "
        talk(text1)
        flag = True
        while (flag):
            talk("Enter your Email")
            email_address = listen()
            if email_address != 'N':
                talk("You meant " + email_address + " say yes to confirm or no to enter again")
                say = listen()
                if say == 'yes' or say == 'Yes':
                    flag = False
            else:
                talk("could not understand what you meant:")
        email_address = email_address.strip()
        email_address = email_address.replace(' ', '')
        email_address = email_address.lower()
        print(email_address)
        request.email = email_address

        flag = True
        while (flag):
            talk("Enter your password")
            email_password = listen()
            if email_address != 'N':
                talk("You meant " + email_password + " say yes to confirm or no to enter again")
                say = listen()
                if say == 'yes' or say == 'Yes':
                    flag = False
            else:
                talk("could not understand what you meant:")
        email_password = email_password.strip()
        email_password = email_password.replace(' ', '')
        email_password = email_password.lower()
        print(email_password)

        imap_url = 'imap.gmail.com'
        conn = imaplib.IMAP4_SSL(imap_url)
        try:
            conn.login(email_address, email_password)
            s.login(email_address, email_password)
            talk("Congratulations. You have logged in successfully. You will now be redirected to the menu page.")
            return JsonResponse({'result' : 'success'})
        except Exception as e:
            print(e)
            talk("Invalid Login Details. Please try again.")
            return JsonResponse({'result': 'failure'})

    detail  = Details()
    detail.email = email_address
    detail.password = email_password
    return render(request, 'login.html', {'detail' : detail})


def menu_view(request):
    return render(request, 'options.html')