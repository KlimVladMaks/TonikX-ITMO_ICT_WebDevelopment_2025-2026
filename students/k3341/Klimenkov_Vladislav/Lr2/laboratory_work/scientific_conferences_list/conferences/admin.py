from django.contrib import admin
from .models import Conference, Presentation, Review

admin.site.register(Conference)
admin.site.register(Presentation)
admin.site.register(Review)
