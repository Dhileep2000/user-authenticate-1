from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *


def loginpage(request):

    context={
        "error":""
    }

    if request.method == "POST":
        print(request.POST)
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user)
        
        if user != None:
            login(request,user)
            return redirect("/blog/home/")
        
        else:
            context={
                "error":"*invaild username and password"
            }

            return render(request,"login.html",context)

    return render(request,"login.html",context)




def logoutpage(request):

    logout(request)
    return redirect("/")



def signuppage(request):

    if request.method == "POST":
        
        new_user=user_forms.objects.filter(username=request.POST['username'])
        
        if len(new_user)>0:

            context={
                "error":"*invalid username"
            }

            return render(request,"signup.html",context)



        else:

            user=user_forms(username=request.POST['username'],email=request.POST['email'])
            user.set_password(request.POST['password'])
            user.save()
            return redirect("/")

   
    


    return render(request,"signup.html")

