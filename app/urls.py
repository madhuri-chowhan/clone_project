from django.urls import path
from . import views
app_name="app_two"

urlpatterns=[
   
    path('', views.about.as_view(), name="about"),
    path('contact/', views.contact.as_view(), name="contact"),
    
    path('signup/', views.signupView, name="signup"),
   
]