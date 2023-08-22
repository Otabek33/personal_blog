from django.urls import path

from apps.accounts.views import mainPage

app_name = "my_blog"

urlpatterns = [

    path("", mainPage, name="main_page"),


]