from django.shortcuts import render, redirect
from .forms import PostForm, UpdatePostForm
from .models import Post
from django.contrib import messages


def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(
            data=request.POST,
        )

        if form.is_valid():
            post = Post(
                user=request.user,
                title=form.cleaned_data.get("title"),
                content=form.cleaned_data.get("content"),
            )

            post.save()

            messages.success(
                request=request,
                message="The post has been created successfully.",
            )

            return redirect(to="index")

    return render(
        request=request,
        template_name="blog/create-post.html",
        context={
            "title": "Add Post",
            "form": form,
        }
    )


def update_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)

        if request.method == "POST":
            form = UpdatePostForm(
                data=request.POST,
                instance=post,
            )

            if form.is_valid():
                fields_to_update = {}

                if post.title != form.cleaned_data.get("title"):
                    fields_to_update["title"] = form.cleaned_data.get("title")

                if post.content != form.cleaned_data.get("content"):
                    fields_to_update["content"] = form.cleaned_data.get("content")

                if fields_to_update:
                    for key, value in fields_to_update.items():
                        setattr(post, key, value)

                    post.save()

                messages.success(
                    request=request,
                    message="The post has been updated successfully.",
                )

                return redirect(to="index")

        else:
            form = PostForm()

    except Post.DoesNotExist:
        messages.info(
            request=request,
            message="This post does not exists.",
        )

        return redirect(to="index")

    return render(
        request=request,
        template_name="blog/update-post.html",
        context={
            "title": "Update Post",
            "post": post,
            "form": form,
        },
    )


def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)

        post.delete()

    except Post.DoesNotExist:
        messages.info(
            request=request,
            message="This post does not exists.",
        )
        return redirect(to="index")

    return redirect(to="index")
