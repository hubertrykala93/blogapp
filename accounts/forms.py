from django import forms
from .models import User
from django.core.exceptions import ValidationError
import re


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        error_messages={
            "required": "Username is required.",
        },
    )
    email = forms.CharField(
        error_messages={
            "required": "E-mail is required.",
        },
    )
    password = forms.CharField(
        error_messages={
            "required": "Password is required.",
        },
    )
    repassword = forms.CharField(
        error_messages={
            "required": "Confirm Password is required.",
        },
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]

    def clean_username(self):
        username = self.cleaned_data.get("username").strip()

        if not username.isalpha():
            raise ValidationError(
                message="The username must consist of letters only.",
            )

        if len(username) < 8:
            raise ValidationError(
                message="The username must be at least 8 characters long.",
            )

        if len(username) > 255:
            raise ValidationError(
                message="The username must be no more than 255 characters long.",
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email").strip()

        if len(email) > 255:
            raise ValidationError(
                message="The e-mail address cannot be longer than 255 characters.",
            )

        if not re.match(pattern=r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                        string=email):
            raise ValidationError(
                message="The e-mail address format is invalid.",
            )

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                message=f"The user with the e-mail address '{email}' already exists.",
            )

        return email

    def clean_password(self):
        password = self.cleaned_data.get("password").strip()

        if len(password) < 8:
            raise ValidationError(
                message="The password should consist of at least 8 characters.",
            )

        if len(password) > 255:
            raise ValidationError(
                message="The password cannot be longer than 255 characters.",
            )

        if not re.match(pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", string=password):
            raise ValidationError(
                message="The password should contain at least one uppercase letter, one lowercase letter, one number, "
                        "and one special character."
            )

        return password

    def clean_repassword(self):
        password = self.data.get("password")
        repassword = self.cleaned_data.get("repassword").strip()

        if repassword != password:
            raise ValidationError(
                message="Confirm Password does not match the password.",
            )

        return repassword


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            "required": "Username is required.",
        },
    )
    password = forms.CharField(
        error_messages={
            "required": "Password is required.",
        },
    )

    def clean_username(self):
        username = self.cleaned_data.get("username").strip()

        if not User.objects.filter(username=username).exists():
            raise ValidationError(
                message="The user with provided username does not exists."
            )

        return username

    def clean_password(self):
        username = self.cleaned_data.get("username").strip() if "username" in self.cleaned_data else None
        password = self.cleaned_data.get("password").strip()

        try:
            user = User.objects.get(username=username)

            if user:
                if not user.check_password(raw_password=password):
                    raise ValidationError(
                        message=f"Invalid password for user '{user.username}'."
                    )

        except User.DoesNotExist:
            pass

        return password
