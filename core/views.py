from django.shortcuts import render
from blog.models import Post


def index(request):
    return render(
        request=request,
        template_name="core/index.html",
        context={
            "title": "Home",
            "posts": Post.objects.all(),
        }
    )
