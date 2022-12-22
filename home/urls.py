# Import The Django Path
from django.urls import path, re_path

# Import Views - Views is a function or method that takes http requests as arguments,
# imports the relevant models and finds out what data to send to the template
# and return final result.
from . import views

# To provide mapping we use urlpatterns list
urlpatterns = [
    path('', views.login_view, name="login"),
    re_path(r'^menu/$', views.menu_view, name="menu"),
    re_path(r'^compose/$', views.compose_view, name="compose"),
    re_path(r'^inbox/$', views.inbox_view, name="inbox"),
    re_path(r'^sent/$', views.sent_view, name="sent"),
    re_path(r'^trash/$', views.trash_view, name="trash")

]