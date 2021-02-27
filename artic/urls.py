
from django.urls import path
from . import views

app_name="dastan"
urlpatterns = [
    path('',views.articles_list,name="list"),
    path('<slugg>',views.artic_detail,name="detail"),
]