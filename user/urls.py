from django.urls import path
from user import views

urlpatterns=[
    path('login/', views.login, name='login'),
    path('signup/', views.register, name='signup'),
    path('logout/', views.logout_view,   name='logout'),
   
]
