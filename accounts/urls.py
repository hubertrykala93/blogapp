from django.urls import path
from accounts import views as accounts_views

urlpatterns = [
    path(route="login", view=accounts_views.login, name="login"),
    path(route="register", view=accounts_views.register, name="register"),
]
