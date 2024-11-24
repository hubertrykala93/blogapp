from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path(route="create-post", view=blog_views.create_post, name="create-post"),
    path(route="update-post/<str:slug>", view=blog_views.update_post, name="update-post"),
    path(route="delete-post/<int:pk>", view=blog_views.delete_post, name="delete-post"),
]
