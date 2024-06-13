from django.shortcuts import render
from .models import College

def search_view(request):
    # Get unique values from the College model for each field
    categories = College.objects.values_list('category', flat=True).distinct()
    genders = College.objects.values_list('gender', flat=True).distinct()
    unknowns = College.objects.values_list('unknown', flat=True).distinct()

    context = {
        'categories': categories,
        'genders': genders,
        'unknowns': unknowns,
    }
    return render(request, 'finder/index.html', context)

def index(request):
    categories = College.objects.values_list('category', flat=True).distinct()
    genders = College.objects.values_list('gender', flat=True).distinct()
    unknowns = College.objects.values_list('unknown', flat=True).distinct()
    return render(request, 'finder/index.html', {'categories': categories, 'genders': genders, 'unknowns': unknowns})

def search(request):
    if request.method == 'POST':
        rank = int(request.POST['rank'])
        category = request.POST['category']
        gender = request.POST['gender']
        unknown = request.POST['unknown']
        college_type = request.POST['college_type']
        
        # Base query
        results = College.objects.filter(
            category=category,
            gender=gender,
            unknown=unknown,
            opening_rank__lte=rank + 100,
            closing_rank__gte=rank - 100
        )

        # Filter based on college type
        if college_type == 'IITs':
            results = results.filter(college_name__startswith='Indian Institute of Technology')
        elif college_type == 'IIITs':
            results = results.filter(college_name__startswith='Indian Institute of Information Technology')
        elif college_type == 'Others':
            results = results.exclude(college_name__startswith='Indian Institute of Technology')
            results = results.exclude(college_name__startswith='Indian Institute of Information Technology')

        # Order the results by college name
        results = results.order_by('college_name')

        return render(request, 'finder/results.html', {'results': results})
    return render(request, 'finder/index.html')
