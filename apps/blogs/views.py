from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from apps.blogs.models import Blog


# Create your views here.

class BlogListView(TemplateView):
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_list"] = Blog.objects.filter(delete_status=False).order_by("-created_at")
        return context


blogList = BlogListView.as_view()


class BlogView(DetailView):
    model = Blog
    template_name = "blog/blog.html"


blog = BlogView.as_view()
