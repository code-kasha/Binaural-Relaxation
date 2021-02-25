from django.urls import path

from apps.core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("info/", views.info, name="info"),
    path("update_user/", views.edit_user_details, name="user-edit"),
]
