
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from musics import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('musics.urls',namespace='music')),
    path('aboutus/',views.aboutus,name='about_us'),
    path('contactus/',views.contactus,name='contact_us')
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)