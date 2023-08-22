from django.db import models
import uuid
from apps.accounts.models import CustomUser


# Create your models here.
class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to="blog",default="blog/blog.jpg")
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    delete_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")
