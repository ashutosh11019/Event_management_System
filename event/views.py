from django.shortcuts import render, redirect
from django.views import  View
from .forms import MyEvent, MyParticipant, MyRegistration
from .models import Event, Participant, registration
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home.html")

@login_required(login_url='loginPage')
def bookevent(request):
    form=MyEvent()
    if request.method == 'POST':
        form = MyEvent(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/viewevent/')
    return render(request,'createevent.html',{'form':form})

def bookseat(request):
    form=MyParticipant()
    if request.method == 'POST':
        form = MyParticipant(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'createevent.html',{'form':form})


def viewevent(request):
    data=Event.objects.all()
    return render(request,'viewevent.html',{'data':data})

def register(request):
    form = MyRegistration()
    if request.method == 'POST':
        username=request.POST['participant_name']
        print(username)
        user = MyRegistration(request.POST)
        if form.is_valid():
            user.save()
            messages.success(request, 'Accounts was created for ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='loginPage')
def UpdateTask(request,pk):
    task = Event.objects.get(id=pk)
    form = MyEvent(instance=task)
    if request.method == 'POST':
        form = MyEvent(request.POST,request.FILES,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/viewevent/')



    return render(request,'update.html',{'form':form})

@login_required(login_url='loginPage')
def DeleteTask(request,pk):
    item = Event.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/viewevent/')

    return render(request,'delete.html',{'item':item})

@login_required(login_url='loginPage')
def manage(request):
    data=Event.objects.all()
    return render(request,'manage.html',{'data':data})

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'Username OR password is incorrect')
			return render(request, 'login.html', {})
	return render(request, 'login.html', {})


def logoutUser(request):
	logout(request)
	return redirect('/')
