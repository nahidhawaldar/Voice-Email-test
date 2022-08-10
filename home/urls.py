# Import The Django Path
from django.urls import path, re_path

# Import Views - Views is a function or method that takes http requests as arguments,
# imports the relevant models and finds out what data to send to the template
# and return final result.
from . import views

# To provide mapping we use urlpatterns list
urlpatterns = [
    path('', views.login_view, name="login"),
    re_path(r'^options/$', views.menu_view, name="options")
]