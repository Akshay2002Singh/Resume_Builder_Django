from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from home.models import contact,users_data
from .fetchdata import api_call
import json
import threading
# Create your views here.
def show_resume(request):
    user=users_data.objects.get(f_key=request.user)
    user_details=json.loads(user.data)
    print(user_details["skills"]["library_and_framework"])
    return render(request,'resume_template.html',{"user":user,"intro":user_details["Summary"],
    "languages":user_details["skills"]["language"],
    "education":user_details["Education"],
    "laf":user_details["skills"]["library_and_framework"],
    "others":user_details["skills"]["other"],
    "exp":user_details["Experience"],
    "projects":user_details["Projects"],
    })
def index(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,'index.html',context)

def login_user(request):
    return render(request,'login.html')

def login_form(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect ("/")
        else:
            return redirect("/login")

def create_user(request):
    return render(request,"sign_up.html")

def create_user_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        user.first_name=name
        user.save()
        return render(request,'login.html')

def log_out(request):
    logout(request)
    return redirect("/")

def contact_us(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,"contact_us.html",context)

def submit_contact_form(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        temp_contact = contact(name=name,email=email,phone=phone,message=message)
        temp_contact.save()

        return render(request,'contact_us.html',context)

def generate_data(request):
    return render(request,'generate.html')

def generate_data_form(request):
    if request.method == 'POST':
        git = request.POST.get('Github')
        linked = request.POST.get('LinkedIn')
        data_entry = users_data(f_key=request.user,fetch_done = 0)
        data_entry.save()
        # print(git)
        # print(linked)
        thread = threading.Thread(target=api_call,args=(git,linked,request))
        thread.start()
        # api_call(git,linked,request)
        return render(request,"generate.html")
