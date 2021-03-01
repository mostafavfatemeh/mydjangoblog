
from django.urls import path
from . import views

app_name="dastan"
urlpatterns = [
    path('',views.articles_list,name="list"),
    path('create',views.create_dastan,name='create'),
    path('<slugg>',views.artic_detail,name="detail"),
]