from audioop import reverse
import http
import re
from app.forms import loginForm
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
class index(TemplateView):
    template_name = "index.html" 
    
class about(TemplateView):
    template_name= 'about.html'

class contact(TemplateView):
    template_name= 'contact.html'



def signupView(request):
    registered = False
    if request.method == 'POST':
        userform = loginForm(data=request.POST)

        if userform.is_valid():
            user = userform.save()
            user.save()
        else:
            print(userform.errors)

    else:
        userform= loginForm()          
    return render(request, 'signup.html',{'userform':userform, 'registered':registered})

@login_required
def special(request):
    return HttpResponse("already logged in")


@login_required
def logoutview(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))


def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password= password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("not logged in")
        else:
            return HttpResponse("invalid user")

    else:
        
     return render(request, 'login.html',{})
     


