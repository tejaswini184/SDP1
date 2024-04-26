from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .models import *
# Create your views here.
def festivals(request):
    return render(request,'usermodule/festivals.html')
def historical(request):
    return render(request,'usermodule/historicalplaces.html')
def artforms(request):
    return render(request,'usermodule/artforms.html')
def cultures(request):
    return render(request,'usermodule/cultures.html')
def login(request):
    return render(request,'usermodule/login.html')
def signup(request):
    return render(request,'usermodule/signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username) >= 5:
                return redirect('userhomepage')
            elif len(username) == 4:
                return redirect('homepage')
            else:
                return redirect('userhomepage')
            auth.login(request,user)
            return render(request,'userhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request, 'usermodule/login.html')
def signup1(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'usermodule/signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully')
                return render(request,'usermodule/login.html')
        else:
            messages.info(request,'password do not match')
            return render(request,'usermodule/signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'userhomepage.html')
from django.core.mail import mail_admins
def feedback(request):
    return render(request,'usermodule/feedback.html')
def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment + '---------------------------------------this is just the comment '
        data=contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)

        data.save()
        return HttpResponse("<h1><center>Thank you for giving feedback</center></h1>")


