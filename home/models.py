from django.db import models

# Create your models here.

class Details:
    email : str
    password : str

class Compose:
    recipient : str
    subject : str
    body : str