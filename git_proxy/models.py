from django.db import models

# Create your models here.
class WebPage(models.Model):
    page_name = models.CharField(max_length=128)
    page_url = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.page_name
