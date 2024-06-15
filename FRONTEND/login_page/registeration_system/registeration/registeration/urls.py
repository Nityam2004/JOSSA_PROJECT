from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.SignupPage, name='signup'),  # URL for signup page
    path('login/', views.LoginPage, name='login'),  # URL for login page
    path('home/', views.HomePage, name='home'),  # URL for home page
    path('logout/', views.LogoutPage, name='logout'),  # URL for logout page
    path('marks_vs_rank/', views.MarksVsRankPage, name='marks_vs_rank'),  # URL for marks vs rank page
    path('college_predictor/', views.CollegePredictor, name='college_predictor'),  # URL for college predictor page
    path('search/', views.search, name='search'),  # URL for search page
    path('faqs/', views.faqs, name='faqs'),  # URL for FAQs page
    path('about/', views.about, name='about'),  # URL for about page
    path('contact/', views.contact, name='contact'),  # URL for contact page
    path('help/', views.help, name='help'),  # URL for help page
    path('news/', views.news_and_notices_view, name='news_and_notices'),  # URL for news and notices page
]

# Serving static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
