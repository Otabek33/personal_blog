from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import CustomUser, JobTitle


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "id",
        "first_name",
        "last_name",
        "mid_name",
        "email",
        "phone",

    ]
    list_editable = ['email']
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "mid_name",
                    "email",
                    "job_title",
                    "phone",
                    "photo",
                    "cv",
                    "address",
                    "birthdate",
                    "zip_code",

                )
            },
        ),
    )


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    model = JobTitle
    list_display = [
        "name",
        "code",
    ]
