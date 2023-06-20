from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportModelAdmin
from rangefilter.filter import DateTimeRangeFilter
from analytics.models import *

# Register your models here.

@admin.register(CampaignType)
class CampaignTypeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'slug', 'is_active']
    search_fields = ['id', 'name', 'slug', 'is_active', ]
    list_filter = ["is_active"]


@admin.register(EmailCampaignTrackingAnalytic)
class EmailCampaignTrackingAnalyticAdmin(ImportExportModelAdmin):
    list_display = ['tracking_id', 'subject', 'type', 'sent_at', 'opened_at']
    filter_horizontal = ["links",]

@admin.register(ClickLinksInsideEmailCampaignActivity)
class ClickLinksInsideEmailCampaignActivityAdmin(ImportExportModelAdmin):
    list_display = ['id', 'url', 'base_link', 'clicked_on', 'count', 'clicked_at']
    list_filter = ["base_link", "clicked_on", ('clicked_at', DateTimeRangeFilter)]
