from django.urls import path
from . import views
app_name = 'middleman'

urlpatterns = [
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('panel/',views.panel,name="panel"),
    path('proceed/<int:citizen_id>/', views.proceed, name='proceed'),
    path('workman_registration/',views.add_workman,name="add_workman"),
    path('workman_panel/',views.workman_panel,name="workman_panel"),
    path('completed/<int:citizen_id>/',views.completed,name="completed"),
    path('deleting/<int:id>/', views.deleting, name='deleting'),
]
