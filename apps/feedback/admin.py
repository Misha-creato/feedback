from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_resolved',
        'created_at',
    )
    exclude = (
        'id',
    )
