from django.db import models

# Create your models here.
class Insight(models.Model):
    end_year = models.CharField(max_length=10, blank=True)
    intensity = models.IntegerField(blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True)
    topic = models.CharField(max_length=100, blank=True)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=10, blank=True)
    impact = models.CharField(max_length=100, blank=True)
    added = models.DateTimeField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    relevance = models.IntegerField(blank=True, null=True)
    pestle = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
