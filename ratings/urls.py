from django.urls import path
from . import views
app_name = 'rating'

urlpatterns = [
    path('ratings/',views.ratings, name='ratings'),
    path('thanks/',views.thanks,name='thanks'),
    
]