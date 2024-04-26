from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')
def userhomepage(request):
    return render(request,'userhomepage.html')
def contactus(request):
    return render(request,'contactus.html')
def changes(request):
    return render(request,'app1 ')

