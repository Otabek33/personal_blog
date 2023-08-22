from django.urls import path
from apps.blogs.views import (blogList,blog)

app_name = "blogs"

urlpatterns = [

    path("", blogList, name="blogList"),
    path("<uuid:pk>", blog, name="blog"),
]
