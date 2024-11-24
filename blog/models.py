from django.db import models
from django.utils.timezone import now
from accounts.models import User
from django.utils.text import slugify


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=now)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(unique=True)
    content = models.CharField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        else:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)
