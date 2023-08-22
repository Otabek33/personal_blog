from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.

class JobTitle(models.Model):
    name = models.CharField("Должность", blank=True, max_length=55)
    code = models.CharField("Код", max_length=55)

    class Meta:
        verbose_name = "Job title"
        verbose_name_plural = "Job titles"

    def __str__(self) -> str:
        return self.name


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("Имя"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Фамилия"), max_length=50, blank=True, null=True)
    mid_name = models.CharField(_("Отчество"), max_length=50, blank=True, null=True)
    email = models.EmailField(_("Эл.почта"), blank=True, default="kebatotabek33@gmail.com")
    phone = models.CharField(max_length=13, blank=True, null=True)
    photo = models.ImageField(upload_to="avatar", default="avatars/user.png")
    cv = models.FileField(upload_to="cv", default="cv/my_cv.pdf")
    address = models.CharField(max_length=255, blank=True, null=False)
    birthdate = models.DateField(_("День рождение"), max_length=50, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    job_title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_absolute_url(self):
        return reverse("my_blog:user-detail", kwargs={"pk": self.id})
