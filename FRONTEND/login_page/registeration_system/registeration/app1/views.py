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
    # Example news items (replace with actual data fetching logic)
    all_news_items = [
        {'title': 'Notice 1', 'link': '/static/pdf/notice1.pdf'},
        {'title': 'Notice 2', 'link': '/static/pdf/notice2.pdf'},
        {'title': 'Notice 3', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 4', 'link': '/static/pdf/notice1.pdf'},
        {'title': 'Notice 5', 'link': '/static/pdf/notice1.pdf'},
        {'title': 'Notice 6', 'link': '/static/pdf/notice2.pdf'},
        {'title': 'Notice 7', 'link': '/static/pdf/notice2.pdf'},
        {'title': 'Notice 8', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 9', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 10', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 11', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 12', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 13', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 14', 'link': '/static/pdf/notice3.pdf'},
        {'title': 'Notice 15', 'link': '/static/pdf/notice3.pdf'},
    ]

    if request.method == 'POST':
        if 'marks_vs_rank' in request.POST:
            return redirect('rank_vs_marks')
        elif 'college_predictor' in request.POST:
            return redirect('college_predictor')
        elif 'faqs' in request.POST:
            return redirect('faqs')
        elif 'about' in request.POST:
            return redirect('about')
        elif 'contact' in request.POST:
            return redirect('contact')
    
    context = {
        'all_news_items': all_news_items,
    }
    
    return render(request, 'home.html', context)

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
    # Get unique values from the College model for each field
    categories = College.objects.values_list('category', flat=True).distinct()
    genders = College.objects.values_list('gender', flat=True).distinct()
    unknowns = College.objects.values_list('unknown', flat=True).distinct()

    context = {
        'categories': categories,
        'genders': genders,
        'unknowns': unknowns,
    }
    return render(request, 'index1.html', context)

def signup(request):
    categories = College.objects.values_list('category', flat=True).distinct()
    genders = College.objects.values_list('gender', flat=True).distinct()
    unknowns = College.objects.values_list('unknown', flat=True).distinct()
    return render(request, 'index1.html', {'categories': categories, 'genders': genders, 'unknowns': unknowns})

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
        )

        results = results.order_by('college_name')

        return render(request, 'results.html', {'results': results})
    return render(request, 'index1.html')

def faqs(request):
    return render(request, 'faqs.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def help(request):
    return render(request, 'help.html')
def news_and_notices_view(request):
    # Example news items (replace with actual data fetching logic)
    news_items = [
        {'title': 'Notice 1', 'link': '#'},
        {'title': 'Notice 2', 'link': '#'},
        {'title': 'Notice 3', 'link': '#'},
    ]

    context = {
        'news_items': news_items,
    }

    return render(request, 'news_and_notices.html', context)

