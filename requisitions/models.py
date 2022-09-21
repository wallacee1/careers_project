from django.db import models
from datetime import datetime
from hiringsupervisors.models import Hiringsupervisors

class Requisition(models.Model):
    hiringsupervisors = models.ForeignKey(Hiringsupervisors, on_delete=models.DO_NOTHING)
    department = models.CharField(max_length=200)
    positiontitle = models.CharField(max_length=200)
    wagerange = models.FloatField(max_length=200)
    essentialfunctions = models.TextField()
    skillsrequired = models.TextField()
    education_knowledgerequired = models.TextField()
    experiencerequired = models.IntegerField()
    physicalrequirements = models.TextField()
    is_published = models.BooleanField(default=True)
    dateofrequisition = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.title
