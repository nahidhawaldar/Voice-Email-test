from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import imaplib,email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.http import JsonResponse
import re
from .models import Details
from .TalkandListen import talk, listen
# Create your views here.

email_address = ''
email_password = ''
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
imap_url = 'imap.gmail.com'
conn = imaplib.IMAP4_SSL(imap_url)

def login_view(request):
    global email_address, email_password

    if request.method == 'POST':
        text1 = "Welcome to our Voice Based Email...... Login with your email account in order to continue. "
        talk(text1)
        flag = True
        while (flag):
            talk("Enter your Email")
            email_address = "voicebasedemailtest@gmail.com" #listen() function
            if email_address != 'N':
                talk("You meant " + email_address + " say yes to confirm or no to enter again")
                say = "yes" #listen() function
                if say == 'yes' or say == 'Yes':
                    flag = False
            else:
                talk("could not understand what you meant:")
        # email_address = email_address.strip()
        # email_address = email_address.replace(' ', '')
        # email_address = email_address.lower()
        print(email_address)
        request.email = email_address

        flag = True
        while (flag):
            talk("Enter your password")
            email_password = "voicebasedemailtest@123" #Listen() function
            if email_address != 'N':
                talk("You meant " + email_password + " say yes to confirm or no to enter again")
                say = "yes" #listen() function
                if say == 'yes' or say == 'Yes':
                    flag = False
            else:
                talk("could not understand what you meant:")
        # email_password = email_password.strip()
        # email_password = email_password.replace(' ', '')
        # email_password = email_password.lower()
        print(email_password)

        imap_url = 'imap.gmail.com'
        conn = imaplib.IMAP4_SSL(imap_url)
        try:
            # conn.login(email_address, email_password)
            # s.login(email_address, email_password)
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
    global email_address, email_password
    if request.method == "POST":
        text1 = "Welcome To The Email Menu " + email_address + ". What Would You Like To Do ?"
        talk(text1)
        flag = True
        while(flag):
            talk("To compose an email say compose. To open Inbox folder say Inbox. To open Trash folder say Trash. To Logout say Logout. Do you want me to repeat?")
            say = "No" #listen() function
            if say == "No" or say == "no":
                flag = False
            talk("What Do You Want To Do ?")
            action = "compose" #listen() function
            action = action.lower()
            if action == 'compose':
                return JsonResponse({'result' : 'compose'})
            elif action == 'inbox':
                return JsonResponse({'result' : 'inbox'})
            elif action == 'trash':
                return JsonResponse({'result' : 'trash'})
            elif action == 'log out':
                email_address = ""
                email_password = ""
                talk("You have been logged out of your account and now will be redirected back to the login page.")
                return JsonResponse({'result': 'logout'})
            else:
                talk("Invalid action. Please try again.")
                return JsonResponse({'result': 'failure'})
    return render(request, 'menu.html')

def compose_view(request):
    return render(request, 'compose.html')

def inbox_view(request):
    return render(request, 'inbox.html')

def trash_view(request):
    return render(request, 'trash.html')