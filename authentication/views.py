from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import user

# Create your views here.
#loginpage
def LoginPage(request):

    if request.user.is_authenticated:

         return redirect('/Inventory/home/')
    
    context={
        'error':" "
    }

    if request.method == "POST":
        print(request.POST)
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user)

        if user is not None:
            login(request,user)

         #sometimes namaku role ah poruthu page redirect pannanum aodtha ethula if condition kudukanum
            return redirect('/Inventory/home/')
        
        else:
            context={
                'error':'*Invalid Username or Password'
            }

        return render(request,'login.html',context)
    
    return render(request,'login.html',context)


#logoutpage
def LogoutUser(request):
    logout(request)
    return redirect('/')

#signupPage
def Signup(request):
    if request.method=="POST":

        context={
            "error":""
        }

        user_check=user.objects.filter(username=request.POST['username'])

        if len(user_check)>0:

            context={
                "error":"*Username already exits!"
            }
            return render(request,'signup.html',context)
        else:
            new_user=user(username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],
                            email=request.POST['email_address'],user_age=request.POST['user_age'],role=int(request.POST['role']))
                
            new_user.set_password(request.POST['password'])

            new_user.save()
            return redirect('/')

    return render(request,'signup.html')