import uuid
from django.db import models
from django.forms import JSONField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from analytics.utils import unique_slug_generator_using_name
# Create your models here.



class PageVisited(models.Model):
    OBJECT_TYPE = (
        ("news", ("news")),
        ("experts", ("experts")),
        ("videos", ("videos")),
        ("discussions", ("discussions")),
    )

    path = models.CharField(max_length=1000, blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True
    # )
    client_ip = models.CharField(max_length=200, null=True, blank=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL, null=True, blank=True
    )
    identify_user = models.ForeignKey(
        "analytics.IdentifyUser", on_delete=models.SET_NULL, null=True, blank=True
    )
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    is_mobile = models.BooleanField(default=False, blank=True, null=True)
    is_tablet = models.BooleanField(default=False, blank=True, null=True)
    is_touch_capable = models.BooleanField(default=False, blank=True, null=True)
    is_pc = models.BooleanField(default=False, blank=True, null=True)
    is_bot = models.BooleanField(default=False, blank=True, null=True)

    browser_family = models.CharField(max_length=100, blank=True, null=True)
    browser_version = models.CharField(max_length=100, blank=True, null=True)
    browser_version_string = models.CharField(max_length=100, blank=True, null=True)

    os_family = models.CharField(max_length=100, blank=True, null=True)
    os_version = models.CharField(max_length=100, blank=True, null=True)
    os_version_string = models.CharField(max_length=100, blank=True, null=True)

    device_family = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "Page Visit"
        verbose_name_plural = "Pages Visits"


ADDITION = 1
CHANGE = 2
DELETION = 3
READ = 4

class ClickLogEntry(models.Model):

    ACTION_FLAG_CHOICES = (
        (ADDITION, ('Addition')),
        (CHANGE, ('Change')),
        (DELETION, ('Deletion')),
        (READ, ('Read')),
    )

    action_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        verbose_name=_('user'),
        blank=True, null=True,
    )
    content_type = models.ForeignKey(
        ContentType,
        models.SET_NULL,
        verbose_name=('content type'),
        blank=True, null=True,
    )
    object_id = models.TextField(('object id'), blank=True, null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    action_flag = models.PositiveSmallIntegerField(_('action flag'), choices=ACTION_FLAG_CHOICES)
    path = models.CharField(max_length=1000, blank=True, null=True)
    next_page_path = models.CharField(max_length=1000, blank=True, null=True)
    
    client_ip = models.CharField(max_length=200, null=True, blank=True)
    
    is_mobile = models.BooleanField(default=False, blank=True, null=True)
    is_tablet = models.BooleanField(default=False, blank=True, null=True)
    is_touch_capable = models.BooleanField(default=False, blank=True, null=True)
    is_pc = models.BooleanField(default=False, blank=True, null=True)
    is_bot = models.BooleanField(default=False, blank=True, null=True)

    browser_family = models.CharField(max_length=100, blank=True, null=True)
    browser_version = models.CharField(max_length=100, blank=True, null=True)
    browser_version_string = models.CharField(max_length=100, blank=True, null=True)

    os_family = models.CharField(max_length=100, blank=True, null=True)
    os_version = models.CharField(max_length=100, blank=True, null=True)
    os_version_string = models.CharField(max_length=100, blank=True, null=True)

    device_family = models.CharField(max_length=100, blank=True, null=True)
    
    action_message = models.TextField(('action message'), blank=True)

    class Meta:
        ordering = ['-action_time']
        
    def is_addition(self):
        return self.action_flag == ADDITION

    def is_change(self):
        return self.action_flag == CHANGE

    def is_deletion(self):
        return self.action_flag == DELETION

    def is_read(self):
        return self.action_flag == READ

class IdentifyUser(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    client_ip = models.CharField(max_length=200, null=True, blank=True)
    is_mobile = models.BooleanField(default=False, blank=True, null=True)
    is_tablet = models.BooleanField(default=False, blank=True, null=True)
    is_touch_capable = models.BooleanField(default=False, blank=True, null=True)
    is_pc = models.BooleanField(default=False, blank=True, null=True)
    is_bot = models.BooleanField(default=False, blank=True, null=True)
    browser_family = models.CharField(max_length=100, blank=True, null=True)
    browser_version = models.CharField(max_length=100, blank=True, null=True)
    browser_version_string = models.CharField(max_length=100, blank=True, null=True)
    os_family = models.CharField(max_length=100, blank=True, null=True)
    os_version = models.CharField(max_length=100, blank=True, null=True)
    os_version_string = models.CharField(max_length=100, blank=True, null=True)
    device_family = models.CharField(max_length=100, blank=True, null=True)
    uuid_version_4 = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    uuid_version_1 = models.UUIDField(unique=True, default=uuid.uuid1, editable=False)
    unique_id = models.CharField(max_length=100, blank=True, null=True)
    paths = JSONField(null=True, blank=True, default=dict)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name=" Identification of User"
        verbose_name_plural="Identification of User"



class CampaignType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, help_text="unique name to track particular campaign.")
    slug = models.CharField(max_length=100, null=True, blank=True, help_text="unique slug to track particular campaign.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Campaign Type"
        verbose_name_plural = "Campaign Type"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator_using_name(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

class ClickLinksInsideEmailCampaignActivity(models.Model):
    base_link = models.BooleanField(default=False, help_text="True only for the base redirect link")
    clicked_on = models.CharField(max_length=100, null=True, blank=True, help_text="unique slug to track particular link.")
    url = models.TextField(null=True, blank=True, help_text="url link to redirect.")
    is_clicked = models.BooleanField(default=False)
    count = models.PositiveIntegerField(default=0, help_text="Total number of clicks for same link per email.")
    clicked_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        verbose_name = "Click Links Inside Email Campaign"
        verbose_name_plural = "Click Links Inside Email Campaigns"

    def __str__(self):
        return str(self.id)

class EmailCampaignTrackingAnalytic(models.Model):
    tracking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    links = models.ManyToManyField(ClickLinksInsideEmailCampaignActivity,blank=True, related_name='clicked_links_inside_per_email')
    subject = models.CharField(max_length=200, null=True, blank=True)
    type = models.ForeignKey(CampaignType, on_delete=models.SET_NULL, blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Email Campaign Tracking Analytic"
        verbose_name_plural = "Email Campaign Tracking Analytics"

    def __str__(self):
        return str(self.tracking_id)
