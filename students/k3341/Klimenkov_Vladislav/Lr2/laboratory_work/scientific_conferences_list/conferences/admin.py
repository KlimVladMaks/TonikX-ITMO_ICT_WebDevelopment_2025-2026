from django.contrib import admin
from .models import Conference, Presentation, Review

admin.site.register(Conference)
admin.site.register(Review)

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'conference', 'recommendation']
