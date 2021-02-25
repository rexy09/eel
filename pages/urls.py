from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
]