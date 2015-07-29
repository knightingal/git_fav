from django.db import models

# Create your models here.
class PicRepertory(models.Model):
    rep_name = models.CharField(max_length=256)
    pub_date = models.DateTimeField()

    def __unicode__(self):
        return self.rep_name


class PicInstance(models.Model):
    pic_name = models.CharField(max_length=64)
    repertory = models.ForeignKey(PicRepertory)

    def __unicode__(self):
        return self.pic_name
