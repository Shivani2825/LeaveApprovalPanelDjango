from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from . models import Employee, Mail, AdminResponse

from django.contrib import messages

def index(request):
    return render(request,'index.html')

def userlogin(request):
    return render(request,'login.html')

def email(request):
    return render(request,'email.html')

def table(request):
    data=AdminResponse.objects.all()
    return render(request,'table.html',{'data':data})

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request,'Superuser Does not exists')
            return render(request, 'adminlogin.html')
    return render(request, 'adminlogin.html')

@login_required
def dashbaord(request):
    data=Mail.objects.all()
    return render(request,'dashboard.html',{'data':data})


def register(request):
    if request.method=="POST":
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        if Employee.objects.filter(email=email).exists():
            messages.error(request,'Employee already exists')
            return redirect("/")
        else:
            emp=Employee.objects.create(firstname=fname,lastname=lname,email=email,password=password)
            emp.save()
            messages.success(request,'Employee Added Successfully')
            return render(request,'login.html')


def loginemp(request):
    if request.method=="POST":
        email=request.POST['email']
        userpassword=request.POST['password']
        if Employee.objects.filter(email=email).exists():
            empobj=Employee.objects.get(email=email)
            password=empobj.password
            if check_password(userpassword,password):
                messages.success(request,'Logged In Successfully')
                return redirect("/email/")
            else:
                messages.error(request,'Password Incorrect')
                return render(request,'login.html')
        else:
            messages.error(request,'Employee does not exists')
            return render(request,'login.html')
    else:
        return redirect("/login")
        
def addmail(request):
    if request.method=="POST":
        name=request.POST['name']
        to=request.POST['mail']
        subject=request.POST['subject']
        body=request.POST['body']
        data=Mail.objects.create(name=name,to=to,subject=subject,body=body)
        data.save()
        messages.success(request,'Email Sent Successfully')
        return render(request,'email.html')


def action(request,eid):
    data=Mail.objects.get(id=eid)
    return render(request,'action.html',{'data':data})


def actiontaken(request):
    if request.method=="POST":
        name=request.POST['name']
        to=request.POST['mail']
        subject=request.POST['subject']
        body=request.POST['body']
        response=request.POST['response']
        data=AdminResponse.objects.create(name=name,to=to,subject=subject,body=body,response=response)
        data.save()
        messages.success(request,'Status Updated Successfully')
        data=AdminResponse.objects.all()
        return render(request,'table.html',{'data':data})


