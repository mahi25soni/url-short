from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('login/', views.LogIn , name='login'),
    path('signup/', views.SignUp , name='signup'),
    path('logout/', views.LogOut , name='logout'),
    path('showurls/', views.showurls , name='showurls'),
    path('removeurl/<int:pk>', views.removeurl , name='removeurl'),
    path('<slug:para>', views.redirecting , name='redirecting'),
]