from django.urls import path

from apps.profiles import views

urlpatterns = [
    path("profile/", views.my_profile, name="profile"),
]
