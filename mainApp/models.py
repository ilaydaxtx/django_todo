from django.utils import timezone
from django.db import models
from django.conf import settings

# Create your models here.
class Task (models.Model):
    CATEGORIES = {
        "LEISURE" : "Leisure", # kucuk harflerle yazılmış taraf = how its displayed
        "WORK" : "Work",
    }
    category = models.CharField(max_length=20, choices=CATEGORIES, blank=True, null=True)
    user = models.CharField(max_length=200, blank=False)
    title = models.CharField(max_length = 200, primary_key= True, blank=False)
    description = models.CharField(max_length = 200, blank=True)
    complete = models.BooleanField(editable=True, verbose_name="progress of this project", default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return f"{self.title, self.complete,self.description}"
    
    class Meta:
        ordering = ['complete'] 