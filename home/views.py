from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact, Video, Image
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.


def index(request):
    # return HttpResponse("hey hey hey")
    # print(request.user)
    # if request.user.is_anonymous:
    #     return redirect("/login")
    image = Image.objects.all()
    return render(request, 'index.html', {"image": image})


def signup(request):
    if request.method == "POST":
        # gettinng parameter
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Cn_password = request.POST['Cn_password']

        # checking error inputs
        if len(username) > 10:
            messages.error(request, "Username must be less than 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(
                request, "Username must conatins only letters and numbers")
            return redirect('/')

        if password != Cn_password:
            messages.error(request, "Username must be less than 10 characters")
            return redirect('/')

        # ceate thee user
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        messages.success(request, " your account has been succesfully creted")
    else:
        return HttpResponse('404-Not Found')

    return redirect('/')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, "Successfully logged in !!")
            return redirect("/")
        else:
            # No backend authenticated the credentials
            messages.warning(request, "Invalid login,Please try again !!")
            return redirect('/')

    return HttpResponse('login')


def service(request):

    if request.user.is_anonymous:
        messages.warning(
            request, "you are not authorized to use this part of this website!!")
        return redirect('/')

    video = Video.objects.all()
    return render(request, 'service.html', {"video": video})


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!!')

    return render(request, 'contact.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'You are logged out !!')
    return redirect("/")
