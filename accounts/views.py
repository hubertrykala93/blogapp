from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


@user_passes_test(test_func=lambda user: not user.is_authenticated, login_url="index")
def log_in(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(
            data=request.POST,
        )

        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get("username"))

            authenticated_user = authenticate(
                request=request,
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )

            if authenticated_user is not None:
                if "remember_me" in request.POST and request.POST.get("remember_me") == "on":
                    request.session.set_expiry(60 * 60 * 24 * 30)

                else:
                    request.session.set_expiry(0)

                login(
                    request=request,
                    user=user
                )

                messages.success(
                    request=request,
                    message="The login was successfully completed.",
                )

                return redirect(to="index")

    return render(
        request=request,
        template_name="accounts/login.html",
        context={
            "title": "Login",
            "form": form,
        },
    )


@user_passes_test(test_func=lambda user: not user.is_authenticated, login_url="index")
def register(request):
    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(
            data=request.POST,
        )

        if form.is_valid():
            user = User(
                username=form.cleaned_data.get("username"),
                email=form.cleaned_data.get("email")
            )
            user.set_password(
                raw_password=form.cleaned_data.get("password"),
            )
            user.save()

            messages.success(
                request=request,
                message="Your account has been created successfully. You can now log in.",
            )

            return redirect(to="login")

    return render(
        request=request,
        template_name="accounts/register.html",
        context={
            "title": "Register",
            "form": form,
        },
    )


@user_passes_test(test_func=lambda user: user.is_authenticated, login_url="login")
def log_out(request):
    request.session.flush()

    logout(request=request)

    messages.success(
        request=request,
        message="You have been successfully logged out.",
    )

    return redirect(to="login")


@login_required(login_url="login")
def create_author(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(
            data=request.POST,
        )

        if form.is_valid():
            author = User(
                username=form.cleaned_data.get("username"),
                email=form.cleaned_data.get("email"),
            )
            author.set_password(raw_password=form.cleaned_data.get("password"))
            author.save()

            messages.success(
                request=request,
                message="The new author has been successfully created.",
            )

            return redirect(to="index")

    return render(
        request=request,
        template_name="accounts/create-author.html",
        context={
            "title": "Create Author",
            "form": form,
        }
    )
