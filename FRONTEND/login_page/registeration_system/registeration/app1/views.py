from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if(password1!=password2):return HttpResponse("Enter same confirm password")
        else:
            my_user = User.objects.create_user(uname,email,password1)
            my_user.save()
        return redirect('login')
        

        # Add any additional logic here, like saving the user to the database
    return render(request, 'registeration.html')



def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        # Check for empty email or password
        if not username or not password:
            return HttpResponse("Please provide both email and password.")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        # Debugging: Print email and password to console
        print("Username:", username)
        print("Password:", password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("USERNAME OR PASSWORD IS INCORRECT!")

    return render(request, 'login.html')

def Logoutpage(request):
       logout(request)
       return redirect('login')