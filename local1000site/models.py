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


class ShipRepertory(models.Model):
    ship_name = models.CharField(max_length=256)
    dir_name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.ship_name


class ShipPic(models.Model):
    pic_name = models.CharField(max_length=128)
    pic_type = models.CharField(max_length=8, blank=True)
    pic_url = models.CharField(max_length=1024)
    pic_description = models.CharField(max_length=8192)
    pic_copyright = models.CharField(max_length=1024)
    ship = models.ForeignKey(ShipRepertory)

    def __unicode__(self):
        return self.pic_name
