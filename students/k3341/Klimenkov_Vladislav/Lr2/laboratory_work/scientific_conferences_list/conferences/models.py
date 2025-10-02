from django.db import models


class Conference(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    topics = models.CharField(max_length=255, blank=True)
    participation_conditions = models.TextField(blank=True)
    venue_name = models.CharField(max_length=255)
    venue_description = models.TextField(blank=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return f'{self.name} ({self.start_date} - {self.end_date})'
