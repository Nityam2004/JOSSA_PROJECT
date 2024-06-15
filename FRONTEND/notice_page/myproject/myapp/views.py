# myapp/views.py

from django.shortcuts import render

def news_and_notices_view(request):
    # Replace this with fetching news from your database
    news_items = [
        {'title': 'Notice 1', 'link': '#'},
        {'title': 'Notice 2', 'link': '#'},
        {'title': 'Notice 3', 'link': '#'},
    ]

    context = {
        'news_items': news_items,
    }

    return render(request, 'news_and_notices.html', context)
