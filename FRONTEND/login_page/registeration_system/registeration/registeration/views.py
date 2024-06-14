import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import College
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    if request.method == 'POST':
        if 'marks_vs_rank' in request.POST:
            return redirect('rank_vs_marks')
        if 'college_predictor' in request.POST:
            return redirect('college_predictor')
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if password1 != password2:
            return HttpResponse("Passwords do not match.")
        else:
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Username already taken.")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already registered.")
            else:
                my_user = User.objects.create_user(uname, email, password1)
                my_user.save()
                return redirect('login')
    return render(request, 'registeration.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        if not username or not password:
            return HttpResponse("Please provide both username and password.")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect.")
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def predict_ranks(file_name, marks_to_predict):
    data = pd.read_csv(file_name)
    ranks = data['Rank']
    marks = data['Marks'].apply(lambda x: float(str(x).replace(',', '')))
    sorted_indices = np.argsort(marks)
    ranks = ranks.iloc[sorted_indices]
    marks = marks.iloc[sorted_indices]
    extrapolate = interp1d(marks, ranks, fill_value="extrapolate")
    predicted_ranks = extrapolate(marks_to_predict)
    predicted_ranks = np.round(predicted_ranks).astype(int)
    return predicted_ranks

def get_file_name(category):
    file_names = {
        'crl': 'data/crl.csv',
        'ews': 'data/ews.csv',
        'sc': 'data/sc.csv',
        'st': 'data/st.csv',
        'obc': 'data/obc.csv'
    }
    return file_names.get(category.lower())

def MarksVsRankPage(request):
    predicted_ranks = []
    if request.method == 'POST':
        category = request.POST['category']
        marks_input = request.POST['marks']
        marks_to_predict = [float(mark.replace(',', '')) for mark in marks_input.split(',')]
        file_name = get_file_name(category)
        if file_name:
            predicted_ranks = predict_ranks(file_name, marks_to_predict)
        return render(request, 'index.html', {'predicted_ranks': predicted_ranks})
    return render(request, 'index.html')




def CollegePredictor(request):
    if request.method == 'POST':
        college_name = request.POST['college_name']
        branch = request.POST['branch']
        unknown = request.POST['unknown']
        category = request.POST['category']
        gender = request.POST['gender']
        opening_rank = int(request.POST['opening_rank'])
        closing_rank = int(request.POST['closing_rank'])
        
        College.objects.create(
            college_name=college_name,
            branch=branch,
            unknown=unknown,
            category=category,
            gender=gender,
            opening_rank=opening_rank,
            closing_rank=closing_rank
        )
        return redirect('college_predictor')  # Redirect to the same page after creating a new College instance
    
    # Retrieve distinct values for categories, genders, and unknowns
    categories = College.objects.values_list('category', flat=True).distinct()
    genders = College.objects.values_list('gender', flat=True).distinct()
    unknowns = College.objects.values_list('unknown', flat=True).distinct()
    
    context = {
        'categories': categories,
        'genders': genders,
        'unknowns': unknowns,
    }
    return render(request, 'index1.html', context)

def search(request):
    if request.method == 'POST':
        rank = int(request.POST['rank'])
        category = request.POST['category']
        gender = request.POST['gender']
        unknown = request.POST['unknown']
        
        results = College.objects.filter(
            category=category,
            gender=gender,
            unknown=unknown,
            opening_rank__lte=rank + 100,
            closing_rank__gte=rank - 100
        ).order_by('college_name')

        return render(request, 'results.html', {'results': results})
    
    # If not a POST request or form submission, render the search form again
    categories = College.objects.values_list('category', flat=True).distinct()
    genders = College.objects.values_list('gender', flat=True).distinct()
    unknowns = College.objects.values_list('unknown', flat=True).distinct()
    
    context = {
        'categories': categories,
        'genders': genders,
        'unknowns': unknowns,
    }
    return render(request, 'index1.html', context)
