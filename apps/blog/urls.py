from django.urls import path

from apps.blog import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_home, name="home"),
    path("create/", views.create_post, name="create_post"),
    path("<slug:slug>/update/", views.update_post, name="update_post"),
    path("<slug:slug>/details/", views.post_details, name="post_details"),
    path("<slug:slug>/delete/", views.delete_post, name="delete_post"),
    path("<slug:slug>/toggle/", views.toggle_like, name="toggle_like"),
    path("<slug:slug>/comment/", views.comment, name="comment"),
]
