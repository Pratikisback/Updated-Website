from musics.views import addMusic, homePage, aboutus, contactus
from django.urls import path
from . import views

app_name='musics'

urlpatterns = [
    path('',homePage,name='home_page'), 
    path('add/',addMusic,name='add_music'),  
    path('aboutus/',contactus,name='about_us'),
    path('contactus/',views.contactus,name='contact_us')
    
]
