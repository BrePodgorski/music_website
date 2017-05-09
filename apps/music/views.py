from django.shortcuts import render, redirect

def index(request):
    return render(request, 'music/index.html')

def shop(request):
    return redirect('/')

def home(request):
    return redirect('/')

def shows(request):
    return redirect('/')

def bio(request):
    return redirect('/')
