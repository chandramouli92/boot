from django.urls import path
from myapp2 import views
app_name="myapp2"
urlpatterns = [
    path('trail/',views.trail,name='trail'),
    path('profile/',views.profile,name='profile'),
    
]
