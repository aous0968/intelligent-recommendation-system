from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.all_users, name="all_users"),
    path("recommend/<int:user_id>/", views.recommend),
]