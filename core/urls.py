from django.urls import path
from core import views as core_views

urlpatterns = [
    path(route="", view=core_views.index, name="index"),
]