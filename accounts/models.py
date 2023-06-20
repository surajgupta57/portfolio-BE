from datetime import timezone
import pytz
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token as AuthToken
from accounts.utils import user_profile_picture_upload_path
from analytics.utils import unique_slug_generator_using_name
from dateutil.relativedelta import relativedelta
import uuid


class User(AbstractUser):
    is_facebook_user = models.BooleanField(default=False)
    is_whatsapp_user = models.BooleanField(default=False)
    is_number_user = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    ad_source = models.CharField(max_length=100, blank=True, null=True)

    @property
    def get_parent_profile_count(self):
        count=ParentProfile.objects.filter(user=self).count()
        return count


class Token(AuthToken):
    key = models.CharField("Key", max_length=40, db_index=True, unique=True)
    user = models.ForeignKey(User,
        related_name="auth_token",
        on_delete=models.CASCADE,
        verbose_name="User",
    )

class OneTimeUsableToken(models.Model):
    mobile = models.CharField(max_length=25, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    token = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    used = models.BooleanField(default=False)
    via_whatsapp = models.BooleanField(default=False)
    via_number = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.mobile}"

    class Meta:
        verbose_name = "One Time Login/SignUp Token"
        verbose_name_plural = "One Time Login/SignUp Tokens"


class AnonymousUserSession(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}- {self.uuid}"

    class Meta:
        verbose_name = "Identification of Anonymous User"
        verbose_name_plural = "Identification of Anonymous Users"



