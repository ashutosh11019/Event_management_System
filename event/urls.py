from django.urls import path
from event import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bookevent/', views.bookevent, name='bookevent'),
    path('bookseat/', views.bookseat, name='bookseat'),
    path('viewevent/', views.viewevent, name='viewevent'),
    path('register/', views.register, name='register'),
    path('manage/', views.manage, name='manage'),
    path('updatetask/<str:pk>', views.UpdateTask, name='updatetask'),
    path('deletetask/<str:pk>', views.DeleteTask, name='deletetask'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
]
