from django.urls import path
from . import views

app_name='acont'
urlpatterns=[
    path('signup',views.signup_view,name='signupp'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
]