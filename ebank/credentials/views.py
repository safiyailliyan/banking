from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    return render(request,"register.html")

def form(request):
    return render(request,"form.html")
def application(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']

        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        address = request.POST['address']
        District = request.POST['District']
        branch = request.POST['branch']
        Account = request.POST['Account']
        materials = request.POST['materials']

        user=User.objects.create_user(username=name,password='defaultpassword')
        user.save();
        messages.success(request,'Application accepted')




    return render(request,"application_form.html")
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return render(request,"form.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)

    return redirect('/')
def register1(request):
    if request.method== 'POST':

        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register1')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register1')
            else:


                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password, email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register1')
        return redirect('/')



    return render(request,"register1.html")