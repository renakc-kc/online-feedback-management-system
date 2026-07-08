from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('sendfeedback/', views.sendfeedback, name='sendfeedback'),
    path('myfeedback/', views.myfeedback, name='myfeedback'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('allfeedback/', views.allfeedback, name='allfeedback'),
    path('reply/<int:id>/', views.replyfeedback, name='replyfeedback'),
    path('viewstudents/', views.viewstudents, name='viewstudents'),
    path('deletefeedback/<int:id>/', views.deletefeedback, name='deletefeedback'),
]