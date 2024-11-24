from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    title = forms.CharField(
        error_messages={
            "required": "Title is required.",
        },
    )
    content = forms.CharField(
        error_messages={
            "required": "Content is required.",
        },
    )

    class Meta:
        model = Post
        exclude = [
            "created_at",
            "updated_at",
            "user",
            "slug",
        ]

    def clean_title(self):
        title = self.cleaned_data.get("title").strip()

        if len(title) < 5:
            raise ValidationError(
                message="The title should consist of at least 5 characters long.",
            )

        if len(title) > 50:
            raise ValidationError(
                message="The title cannot be longer than 50 characters.",
            )

        return title

    def clean_content(self):
        content = self.cleaned_data.get("content").strip()

        if len(content) < 10:
            raise ValidationError(
                message="The content should consist of at least 10 characters long.",
            )

        if len(content) > 255:
            raise ValidationError(
                message="The content cannot be longer than 255 characters.",
            )

        return content


class UpdatePostForm(forms.Form):
    title = forms.CharField(
        error_messages={
            "required": "Title is required.",
        }
    )
    content = forms.CharField(
        error_messages={
            "required": "Content is required.",
        },
    )

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop("instance", None)

        super(UpdatePostForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get("title").strip()

        if len(title) < 5:
            raise ValidationError(
                message="The title should consist of at least 5 characters long.",
            )

        if len(title) > 50:
            raise ValidationError(
                message="The title cannot be longer than 50 characters.",
            )

        return title

    def clean_content(self):
        content = self.cleaned_data.get("content").strip()

        if len(content) < 10:
            raise ValidationError(
                message="The content should consist of at least 10 characters long.",
            )

        if len(content) > 255:
            raise ValidationError(
                message="The content cannot be longer than 255 characters.",
            )

        return content
