from django.urls import path
from . import views

app_name = 'citizen'

urlpatterns = [
    path('citizen_home/',views.citizen_home,name='citizen_home'),
    path('final_citizen/',views.final_citizens,name='final_citizen'),

]
