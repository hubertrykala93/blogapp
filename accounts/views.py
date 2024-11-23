from django.shortcuts import render
from django.conf import settings


def login(request):
    print(settings.STATIC_URL)
    print(settings.STATIC_ROOT)
    return render(
        request=request,
        template_name="accounts/login.html",
        context={
            "title": "Login",
        },
    )


def register(request):
    return render(
        request=request,
        template_name="accounts/register.html",
        context={
            "title": "Register",
        },
    )
