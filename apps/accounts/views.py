from django.views.generic import TemplateView
from apps.accounts.models import CustomUser
from apps.blogs.models import Blog


# Create your views here.
class MainDashboard(TemplateView):
    template_name = "dashboard/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["otabek"] = CustomUser.objects.first()
        context["blog_list"] = Blog.objects.filter(delete_status=False).order_by("-id")[:3]
        return context


mainPage = MainDashboard.as_view()
