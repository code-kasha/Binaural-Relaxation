from django.urls import path

from apps.blog import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_home, name="home"),
    path("create/", views.create_post, name="create_post"),
    path("<int:pk>/update/", views.update_post, name="update_post"),
    path("<int:pk>/details/", views.post_details, name="post_details"),
    path("<int:pk>/delete/", views.delete_post, name="delete_post"),
    path("<int:pk>/toggle/", views.toggle_like, name="toggle_like"),
    path("<int:pk>/comment/", views.comment, name="comment"),
]
