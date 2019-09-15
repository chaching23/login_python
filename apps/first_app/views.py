from django.shortcuts import render, redirect   
from django.contrib.messages import error
from .models import data
import bcrypt

def index(request):
    if request.session:
        del request.session

    return render(request, 'first_app/login.html')

def register(request):
    if request.method == "POST":
        errors = data.objects.validate_registration(request.POST)
        if errors:
            for err in errors:
                error(request, err)
            print(errors)
            return redirect('/')
        else:
            new_id = data.objects.register_user(request.POST)

          
            return redirect('/success')
    
def login(request):
     if request.method == "POST":
        users = data.objects.filter(email=request.POST["email"])

        user = users[0]

        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['id']= user.id
            request.session['first_name']= user.first_name
            print(success)
            return redirect("/success")

        else:
        
            error(request, 'blah blah')
            return redirect("/")


def success(request):

    context={
            'user': data.objects.get(id=request.session["id"])
    }
    return render(request,'first_app/in.html',context)


